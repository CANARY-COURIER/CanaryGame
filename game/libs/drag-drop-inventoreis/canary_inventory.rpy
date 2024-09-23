init 999 python:
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
            self.img = Image('./images/inventory/'+str(image_path)+'.png', Transform(Null(), zoom=0.5))
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
            # self.slot_spacing = 300  # Spacing between items
            # self.allow_overlap = allow_overlap
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
    
    # Slot class: Represents a slot for placing items
    class DragSlot:
        def __init__(self, group, init_xpos, init_ypos, image_path="empty"):
            self.group = group
            self.index = len(group.slots)
            self.x = init_xpos
            self.y = init_ypos
            self.cards = []
            self.quantity = 0
            self.item_title = None
            self.group.add_slot(self)
            self.image_path = image_path
            self.img = At(Image('./images/inventory/'+str(image_path)+'.png'), Transform(Null(), zoom=0.5))
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
            # if self.card and self.card.quantity > 1:
            #     self.quantity_display = Text(f"Qty: {self.card.quantity}", size=20, xpos=self.x, ypos=self.y + 100)
    
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

    # Base class: Draggable items are abstracted and managed
    class InventoryItem(DragItem):
        def __init__(self, group, title, description=None, image_path=None, init_xpos=500, init_ypos=500):
            super().__init__(group, title, description, image_path, init_xpos, init_ypos)
            self.index = len(group.items)  # Unique index for the item
            self.in_slot = False  # Track if the item is in inventory or not
            self.create_drag_widget()

        def create_drag_widget(self):
            """Creates a draggable widget for InventoryItem."""
            trans = glow_outline(12, "#cfb760", num_passes=30, power=0.8)
            self.img_idle = At(Image('./images/inventory/' + str(self.image_path) + ".png"), Transform(Null(), zoom=0.5))
            self.img_hover = At(self.img_idle, trans)
            self.drag_widget = Drag(
                d=self.img_idle, \
                drag_name="item_"+str(self.index), \
                idle_child=self.img_idle, \
                hover_child=self.img_hover, \
                draggable=True, \
                droppable=False, \
                dragged=self.drag_placed, \
                pos=(self.x, self.y)
            )
    
    # Group class for inventory logic
    class InventoryGroup(DragItemsGroup):
        def assign_item_to_slot(self, item, slot):
            """Assigns an item to a slot."""
            super().assign_item_to_slot(item, slot)

    # Slot class for inventory
    class InventorySlot(DragSlot):
        def __init__(self, group, init_xpos, init_ypos, image_path='empty'):
            super().__init__(group, init_xpos, init_ypos, image_path)
            self.drag_widget = Drag(d=self.img, drag_name="inventorySlot_" + str(self.index), \
                                droppable=True, draggable=False, pos=(self.x, self.y))
        # def on_hover(self):
        #     """Shift items right on hover."""
        #     print(f"Hovering over slot {self.index}")
        #     self.group.shift_items(self, direction="right")

        # def on_unhover(self):
        #     """Pull items back after hover ends."""
        #     print(f"Hover ended for slot {self.index}")
        #     self.group.pull_items_back(self)

    # Inventory class that manages both shop and inventory items
    class InventoryNew:
        def __init__(self):
            self.slots = []
            self.items = []
            self.inventory_group = InventoryGroup(self.items, self.slots, vertical_align=False, identical_overlap=True)

            # Create slots for inventory
            self.slots.append(InventorySlot(self.inventory_group, init_xpos=200, init_ypos=200))
            self.slots.append(InventorySlot(self.inventory_group, init_xpos=400, init_ypos=200))
            self.slots.append(InventorySlot(self.inventory_group, init_xpos=600, init_ypos=200))
            self.slots.append(InventorySlot(self.inventory_group, init_xpos=800, init_ypos=200))
            # Add individual items based on quantity for each type of product
            self.add_items_to_shop("Apple", "item1", 200, 600, 3)
            self.add_items_to_shop("Orange", "item2", 400, 600, 2)
            self.add_items_to_shop("Banana", "item3", 600, 600, 4)
            
        def add_items_to_shop(self, title, image_path, init_xpos, init_ypos, quantity):
            """Adds individual items based on quantity to the shop."""
            for i in range(quantity):
                # Spread items vertically to avoid overlap (increment y position for each item)
                new_xpos = init_xpos + (i * 100)  # Adjust 50 based on your desired spacing
                item = InventoryItem(self.inventory_group, title, image_path=image_path, init_xpos=new_xpos, init_ypos=init_ypos)
                self.items.append(item)
                # self.shop_items.append(item)

# Initialization for creating inventory and shop slots
init 1000 python:
    renpy.store.inventory = InventoryNew()

# Screen for displaying drag-and-drop functionality
init:
    screen drag_and_drop_inventory():
        modal True
        vbox:
            frame:
                hbox:
                    xfill True
                    align (0.0, 0.5)
                    draggroup:
                        # Display inventory slots
                        for slot in renpy.store.inventory.slots:
                            add slot.drag_widget
                        # Display shop items
                        for item in renpy.store.inventory.items:
                            add item.drag_widget