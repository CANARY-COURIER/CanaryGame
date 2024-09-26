init 998 python:
    # Base class: Draggable items are abstracted and managed
    class DragItem:
        def __init__(self, group, title, description=None, image_path=None, init_xpos=400, init_ypos=400, default_scale=0.5):
            self.group = group
            self.index = None
            self.title = title
            self.description = description
            # draggable properties
            self.x = init_xpos
            self.y = init_ypos
            self.in_slot = False
            self.slot_index = None
            self.drag_widget = None
            self.is_dragging = False
            self.should_resize_to_origin = False
            # Images
            self.image_path = image_path
            self.default_scale = default_scale
            self.width, self.height = renpy.image_size(self.image_path)
            self.width *= self.default_scale
            self.height *= self.default_scale
            # Auto-scaling transform
            self.auto_scaling = Transform(function=self.apply_distance_scaling, delay=0.1)
            self.img = At(Image(self.image_path), self.auto_scaling)
            self.auto_scaled_value = 1.0
        
        def create_drag_widget(self):
            """Creates a draggable widget."""
            self.drag_widget = Drag(d=self.img, drag_name="dragged_" + str(self.index), draggable=True, \
                dragging=self.on_dragging_start, dragged=self.drag_placed, dropped=self.on_drop, \
                 pos=(self.x, self.y))
            
        def on_dragging_start(self, drags):
            """Sets the item as being dragged."""
            self.is_dragging = True
            self.should_resize_to_origin = False  # not turning back to original scale on drag
        
        def drag_placed(self, drags, drop):
            """Handles drag placement for the item."""
            self.is_dragging = False
            dragged_idx = int(drags[0].drag_name.split("_")[1])
            dragged_item = self.group.items[dragged_idx]
            # Case: Dropped outside a slot
            if drop is None and dragged_item.in_slot == True:
                self.draggable_to_origin()
                return
            # Case: Dropped inside a slot
            if drop:
                drop_slot_idx = int(drop.drag_name.split("_")[1])
                drop_slot = self.group.slots[drop_slot_idx]
                # Snap to the slot position
                self.group.assign_item_to_slot(dragged_item, drop_slot)
            else:
                self.draggable_to_origin()  
    
        def draggable_to_origin(self):
            """Return the item to its original position if not dropped into a slot."""
            if self.slot_index is not None: # if dropped out of slot
                previous_slot = self.group.slots[self.slot_index]
                previous_slot.remove_card(self)
                self.drag_widget.snap(self.x, self.y, 0.2)
            else: 
                self.drag_widget.snap(self.x, self.y, 0.2)
            self.should_resize_to_origin = True  # Mark to resize the item back to its original scale
        
        def apply_distance_scaling(self, trans, st, at):
            """Applies dynamic scaling based on distance to the closest slot and adjusts for size."""
            if self.is_dragging:
                # Rescaling on drag
                distance, origin_dist, closest_slot = self.get_closest_slot_distance()
                print("closest slot : " + str(closest_slot.index))
                if distance is not None and closest_slot is not None:
                    zoom_factor = distance_zoom_with_size(
                        distance,
                        self,
                        closest_slot,
                        min_scale=0.5, max_scale=1.0,
                        max_distance=origin_dist
                    )
                    trans.zoom = zoom_factor
                    self.auto_scaled_value = zoom_factor
            elif self.should_resize_to_origin:
                # Smoothly turn back to the original size using smooth_resize
                self.auto_scaled_value = smooth_resize(current_scale=trans.zoom, target_scale=self.default_scale)
                trans.zoom = self.auto_scaled_value
                if trans.zoom == self.default_scale:
                    self.should_resize_to_origin = False  # Stop resizing when original scale is reached
            else:
                trans.zoom = self.auto_scaled_value
            return None
        
        def get_closest_slot_distance(self):
            """Finds the closest slot to the current mouse position."""
            closest_slot = None
            closest_distance = float('inf')
            origin_distance = None
            distance = None
            xpos, ypos = self.drag_widget.last_x or self.x, self.drag_widget.last_y or self.y
            # print("Position value:", xpos, ypos)
            for slot in self.group.slots:
                distance = ((xpos - slot.x) ** 2 + (ypos - slot.y) ** 2) ** 0.5
                if distance < closest_distance:
                    closest_distance = distance
                    closest_slot = slot
            # Calculate origin distance between slot and item
            if closest_slot:
                origin_distance = ((self.x - closest_slot.x) ** 2 + (self.y - closest_slot.y) ** 2) ** 0.5
                return closest_distance, origin_distance, closest_slot
            return None
        
        def resize_to_slot(self, slot):
            """Resizes the item to fit within the slot's dimensions and retains the auto-scaling."""
            self.auto_scaled_value = calculate_scale_factor(slot, self)
        
        def resize_to_origin(self):
            self.auto_scaled_value = self.default_scale
            
    # Group class to manage draggable items and slots
    class DragItemsGroup:
        def __init__(self, vertical_align=False, identical_overlap=False):
            """Manages items and slots with simplified options."""
            self.items = []  # List of all items in the group
            self.slots = []  # List of slots in the group
            self.vertical_align = vertical_align  # Whether to align vertically
            self.identical_overlap = identical_overlap
            self.slot_eject_behavior = 'bounce'  # Default behavior

        def add_item(self, item):
            """Adds an item to the group."""
            item.index = len(self.items)
            item.create_drag_widget()
            self.items.append(item)
        
        def add_slot(self, slot):
            """Adds a slot to the group."""
            slot.index = len(self.slots)
            slot.create_drag_widget()
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
        def __init__(self, group, init_xpos, init_ypos, image_path="./images/inventory/default/slot1.png", default_scale=0.5):
            self.group = group
            self.index = None
            self.x = init_xpos
            self.y = init_ypos
            # Item information in the slot
            self.cards = []
            self.quantity = 0
            self.item_title = None
            # Images 
            self.image_path = image_path
            self.default_scale = default_scale
            self.width, self.height = renpy.image_size(self.image_path)
            self.width *= self.default_scale
            self.height *= self.default_scale

        def create_drag_widget(self):
            scaled_img = Transform(Image(self.image_path), zoom=self.default_scale) 
            self.img = scaled_img
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
            card.resize_to_slot(self)
            self.group.shift_items_left()
            
        def remove_card(self, card):
            """Removes the card from the slot."""
            if card in self.cards:
                card.in_slot = False
                card.slot_index = None
                card.drag_widget.snap(card.x, card.y, 0.2)
                card.resize_to_slot(self)
                self.cards.remove(card)
                self.group.shift_items_left()
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

    def calculate_scale_factor(slot, item, padding_factor=0.9):
        """
        Calculates the scale factor to resize the item to fit within the slot,
        while maintaining the aspect ratio. Optionally applies padding.
        """
        # Get the size of the slot image considering slot's scale factor
        slot_width, slot_height = renpy.image_size(slot.image_path)
        slot_width *= slot.default_scale
        slot_height *= slot.default_scale
        # Get the size of the item image considering the item's scale factor
        item_width, item_height = renpy.image_size(item.image_path)
        item_width *= item.default_scale
        item_height *= item.default_scale
        # Calculate the scaling factors to fit the item into the slot while preserving aspect ratio
        scale_x = slot_width / item_width
        scale_y = slot_height / item_height
        scale_factor = min(scale_x, scale_y)  # Ensure aspect ratio is maintained
        # Apply padding factor to create a "loose fit" effect
        scale_factor *= padding_factor
        return scale_factor

    def distance_zoom_with_size(distance, item, slot, min_scale=0.5, max_scale=1.0, max_distance=300):
        """Calculates zoom factor based on the distance and size comparison between the card and the slot."""
        # scale benchmark is the one with smaller scale (item or slot)
        new_scale = calculate_scale_factor(slot, item)
        if distance >= max_distance:
            return 1.0
        else:
            return 1.0 + (new_scale - 1.0) * (1 - (distance / max_distance))
        
    def smooth_resize(current_scale=0.5, target_scale=1.0, step=0.05):
        """Smoothly transitions from current_scale to target_scale."""
        step_size = (target_scale - current_scale) * step  # Adjust step for smooth transition
        new_scale = current_scale + step_size
        # Prevent overshooting the target scale
        if abs(new_scale - target_scale) < 10:
            return target_scale
        return new_scale