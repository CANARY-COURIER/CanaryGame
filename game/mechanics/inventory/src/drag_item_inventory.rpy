init 998 python:
        # Base class: Draggable items are abstracted and managed
    class DragItem:
        def __init__(self, group, title, description=None, image_path=None, init_xpos=400, init_ypos=400):
            self.group = group
            self.index = len(group.items)
            self.title = title
            self.description = description
            self.image_path = image_path
            self.x = init_xpos
            self.y = init_ypos
            self.in_slot = False
            self.slot_index = None
            self.drag_widget = None
            self.group.add_item(self)

        def update_position(self, x, y):
            """Updates the position of the item."""
            self.x = x
            self.y = y
            self.drag_widget.pos = (x, y)

        def create_drag_widget(self):
            """Creates a draggable widget."""
            self.img = Image(image_path, Transform(Null(), zoom=0.5))
            self.drag_widget = Drag(d=self.img, drag_name="dragged_" + str(self.index), draggable=True, dragged=self.drag_placed, pos=(self.x, self.y))

        def drag_placed(self, drags, drop):
            """Handles drag placement for the item."""
            dragged_idx = int(drags[0].drag_name.split("_")[1])
            dragged_item = self.group.items[dragged_idx]
            if drop is None and dragged_item.in_slot == True:
                self.draggable_to_origin()
                return
            if drop:
                drop_slot_idx = int(drop.drag_name.split("_")[1])
                drop_slot = self.group.slots[drop_slot_idx]
                self.group.assign_item_to_slot(dragged_item, drop_slot)
            else:
                self.draggable_to_origin()

        def draggable_to_origin(self):
            """Return the item to its original position if not dropped into a slot."""
            if self.slot_index is not None: # if dropped out of slot
                previous_slot = self.group.slots[self.slot_index]
                previous_slot.remove_card(self)
                self.drag_widget.snap(self.x, self.y, 0.2)
                self.group.shift_items_left()
            else: 
                self.drag_widget.snap(self.x, self.y, 0.2)

    # Group class to manage draggable items and slots
    class DragItemsGroup:
        def __init__(self, items, slots, vertical_align=False, allow_overlap=False, identical_overlap=False):
            """Manages items and slots with simplified options."""
            self.items = items  # List of all items in the group
            self.slots = slots  # List of slots in the group
            self.vertical_align = vertical_align  # Whether to align vertically
            self.identical_overlap = identical_overlap
            self.slot_eject_behavior = 'bounce'  # Default behavior

        def add_item(self, item):
            """Adds an item to the group."""
            self.items.append(item)

        def add_slot(self, slot):
            """Adds a slot to the group."""
            self.slots.append(slot)

        def get_slot_for_indentical_item(self, item):
            # First, check all other slots for a match
            for s in self.slots:
                if s.cards is not []:
                    for c in s.cards:
                        if c.image_path == item.image_path:
                            return s
            return None
        
        # Assign item to a slot with overlap/replace/shift logic
        def assign_item_to_slot(self, item, slot):
            """Assigns an item to a slot with optional overlap/replace/shift logic."""
            # If no matching slot, handle the drop into the current slot
            if self.identical_overlap:
                if slot.cards and slot.cards[0].image_path is not item.image_path:
                    item.draggable_to_origin()
                    return
                s = self.get_slot_for_indentical_item(item)
                if s is not None:
                    s.assign_card(item, True)
                    return
            if slot.cards:
                # Identical Overlap + Replace -> handled in card drop callbacks
                # Bounce: Return to original position if the slot is occupied and cannot be replaced
                if slot.cards[0].image_path and slot.cards[0].image_path is not item.image_path:
                    if self.slot_eject_behavior == 'bounce':
                        item.draggable_to_origin()
                        # # Replace: Remove the existing card and place the new one
                        # elif self.slot_eject_behavior == 'replace':
                        #     slot.remove_card(item)
                        #     slot.assign_card(item)
            slot.assign_card(item)
            # Shift the items to the left to fill any gaps in the inventory
            self.shift_items_left()

        def shift_items_left(self):
            """Shift all items in the inventory to the left to fill empty slots."""
            last_filled_slot = 0
            # Iterate through all slots
            for i, slot in enumerate(self.slots):
                if slot.cards:
                    # If the slot is filled and not in the correct position, move its cards
                    if i != last_filled_slot:
                        self.slots[last_filled_slot].cards = slot.cards
                        slot.cards = []  # Clear the current slot
                        # Update the position of the cards to the new slot
                        for card in self.slots[last_filled_slot].cards:
                            card.slot_index = last_filled_slot
                            card.drag_widget.snap(self.slots[last_filled_slot].x, self.slots[last_filled_slot].y, 0.2)
                    last_filled_slot += 1
            # Redraw to reflect the updated arrangement
            renpy.redraw(self.slots, 0)

        def get_items_and_quantity(self):
            """Returns a list of item titles and their quantities."""
            item_quantities = {}
            for slot in self.slots:
                if slot.item_title and (slot.item_title not in item_quantities):
                    item_quantities[slot.item_title] = slot.quantity
            return item_quantities

    
    # Slot class: Represents a slot for placing items
    class DragSlot:
        def __init__(self, group, init_xpos, init_ypos, image_path="./images/inventory/default/slot1.png"):
            self.group = group
            self.index = len(group.slots)
            self.x = init_xpos
            self.y = init_ypos
            self.cards = []
            self.quantity = 0
            self.item_title = None
            self.group.add_slot(self)
            self.image_path = image_path
            self.img = At(Image(image_path), Transform(Null(), zoom=0.5))
            self.drag_widget = Drag(d=self.img, drag_name="slot_" + str(self.index), \
                                droppable=True, draggable=False, pos=(self.x, self.y))

        def assign_card(self, card, is_identical=False):
            """Assigns a card to the slot."""
            if is_identical:
                self.quantity += 1
            self.item_title = card.title
            self.cards.append(card)
            card.in_slot = True
            card.slot_index = self.index
            card.drag_widget.snap(self.x, self.y, 0.2)
            
        def remove_card(self, card):
            """Removes the card from the slot."""
            if card in self.cards:
                card.in_slot = False
                card.slot_index = None
                card.drag_widget.snap(card.x, card.y, 0.2)
                self.cards.remove(card)
            self.update_quantity_display()

        def update_quantity_display(self):
            """Updates the quantity display for stacked items."""
            if self.cards == []:
                self.quantity = 0
                self.item_title = None

        # def on_hover(self):
        #     """Function triggered when hovering over the slot."""
        #     print(f"Hovering over slot {self.index}")
        #     # Shift items when hovering over this slot
        #     self.group.shift_items(self, direction="right")

        # def on_unhover(self):
        #     """Function triggered when hover ends."""
        #     print(f"Hover ended for slot {self.index}")
        #     # Pull items back when unhovered
        #     self.group.pull_items_back(self)
