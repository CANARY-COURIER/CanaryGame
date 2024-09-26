init 998 python:

    # Group class to manage draggable items and slots
    class DragItemsGroup:
        # Class variables 
        default_sort_option = "left"
        default_eject_behavior = 'bounce'

        # Class initialization
        def __init__(self, identical_overlap=False, sort_option=None):
            """Manages items and slots with simplified options."""
            self.items = []  # List of all items in the group
            self.slots = []  # List of slots in the group
            self.sort_option = sort_option or DragItemsGroup.default_sort_option
            self.identical_overlap = identical_overlap
            self.slot_eject_behavior = DragItemsGroup.default_eject_behavior

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
            # Check all other slots for a match
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
                if slot.cards and (slot.cards[0].image_path is not item.image_path):
                    item.draggable_to_origin()
                    return
                s = self.get_slot_for_indentical_item(item)
                if s is not None:
                    s.assign_card(item, True)
                    return
            if slot.cards:
                # When overalapped to different cards (not identical)
                if slot.cards[0] and (slot.cards[0].image_path is not item.image_path):
                    if self.slot_eject_behavior == 'bounce':
                        item.draggable_to_origin()
                    # elif self.slot_eject_behavior == 'replace':
                    #     slot.remove_card(item)
                    #     slot.assign_card(item)
            slot.assign_card(item)
            
        def arrange_items(self):
            """Shift items according to the defined sort_option."""
            if self.sort_option == 'left':
                self.arrange_items_left()
                
        def arrange_items_left(self):
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
                            card.drag_widget.snap(self.slots[last_filled_slot].origin_x, self.slots[last_filled_slot].origin_y, card.snap_arr_dur)
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
        # Class variables 
        name_tag = "slot_"
        # Class initialization
        def __init__(self, group, init_xpos=200, init_ypos=200, image_path=None, default_scale=0.5):
            self.group = group
            self.index = None
            self.origin_x = init_xpos
            self.origin_y = init_ypos
            # Item information in the slot
            self.cards = []
            self.quantity = 0
            self.item_title = None
            # Images 
            self.image_path = image_path
            self.default_scale = default_scale
            self.width, self.height = renpy.image_size(self.image_path)

        def create_drag_widget(self):
            self.img = Transform(Image(self.image_path), zoom=self.default_scale) 
            self.drag_widget = Drag(d=self.img, drag_name=(self.name_tag + str(self.index)), \
                                droppable=True, draggable=False, pos=(self.origin_x, self.origin_y))

        def assign_card(self, card, is_identical=False):
            """Assigns a card to the slot."""
            if is_identical:
                self.quantity += 1
            self.item_title = card.title
            card.assign_to_slot(self)
            self.cards.append(card)
            self.group.arrange_items()
            
        def remove_card(self, card):
            """Removes the card from the slot."""
            if card in self.cards:
                card.remove_from_slot(self) 
                self.cards.remove(card)
                self.group.arrange_items()
            self.update_quantity_display()

        def update_quantity_display(self):
            """Updates the quantity display for stacked items."""
            if self.cards == []:
                self.quantity = 0
                self.item_title = None
    
    # Base class: Draggable items are abstracted and managed
    class DragItem:
        # Class variables 
        name_tag="dragged_"
        scale_intervals = 0.001
        snap_ret_dur = 10.0  # snap_return_duration
        snap_assign_dur = 0.15  # snap_assign_duration
        snap_arr_dur = 0.05  # snap_arrange_duration
        origin_threshold = 1
        hover_trans = glow_outline(12, "#cfb760", num_passes=30, power=0.8) 
        padding_factor = 0.9
        # Class initialization
        def __init__(self, group, title, description=None, image_path=None, \
                    init_xpos=400, init_ypos=400, \
                    default_scale=0.5, rescale_enabled=True):
            self.group = group
            self.index = None
            self.title = title
            self.description = description
            # draggable properties
            self.origin_x, self.origin_y = init_xpos, init_ypos
            self.in_slot = False
            self.slot_index = None
            self.drag_widget = None
            self.is_dragging = False
            self.should_resize_to_origin = False
            self.rescale_enabled = rescale_enabled
            # Images properties
            self.image_path = image_path
            self.default_scale = default_scale
            self.width, self.height = renpy.image_size(self.image_path)
            # Auto-scaling transform
            self.auto_scaled_value = default_scale
            if self.rescale_enabled:
                self.auto_scaling = Transform(function=self.apply_distance_scaling, delay=self.scale_intervals)
                self.img = At(Image(self.image_path), self.auto_scaling)
            else:
                self.img = At(Image(self.image_path), self.default_scale)  # No scaling if rescale is disabled
            self.img_idle = self.img
            self.img_hover = At(self.img, self.hover_trans) # Hover effects
        
        ################ DRAG BEHAVIORS ######################

        def create_drag_widget(self):
            """Creates a draggable widget."""
            self.drag_widget = Drag(d=self.img, drag_name=(self.name_tag + str(self.index)), \
                idle_child=self.img_idle, hover_child=self.img_hover, pos=(self.origin_x, self.origin_y), \
                draggable=True, droppable=False, \
                dragging=self.on_dragging_start, dragged=self.drag_placed)
        
        def show_description(self):
            """Displays the description of the item."""
            return self.description
            
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
                # Add resizing logic here: fit the item into the slot
                if self.rescale_enabled:
                    self.resize_to_slot(drop_slot)
            else:
                self.draggable_to_origin()  
    
        def draggable_to_origin(self):
            """Return the item to its original position if not dropped into a slot."""
            if self.rescale_enabled:
                self.should_resize_to_origin = True  # Mark to resize the item back to its original scale
            if self.slot_index is not None: # if dropped out of slot
                previous_slot = self.group.slots[self.slot_index]
                previous_slot.remove_card(self)
            self.group.arrange_items_left()
            self.snap_to_origin()
                
        def assign_to_slot(self, slot):
            self.in_slot = True
            self.slot_index = slot.index
            self.resize_to_slot(slot)
            self.snap_to_slot(slot)
            self.should_resize_to_origin = False
            
        def remove_from_slot(self, slot):
            self.in_slot = False
            self.slot_index = None
            self.removal_slot_scale = self.auto_scaled_value
            self.removal_slot_x = slot.origin_x
            self.removal_slot_y = slot.origin_y
            self.should_resize_to_origin = True
            self.resize_to_origin()
        
        def snap_to_slot(self, slot):
            """Snaps the item to the center of the slot, resizing if enabled."""
            if self.rescale_enabled:
                self.resize_to_slot(slot)
            # Scaled sizing of item and slot
            scaled_item_width = self.width * self.auto_scaled_value
            scaled_item_height = self.height * self.auto_scaled_value
            scaled_slot_width = slot.width * self.default_scale
            scaled_slot_height = slot.height * self.default_scale
            # Center the item within the slot, with padding if necessary
            pad_x = (scaled_slot_width - scaled_item_width) / 2 if scaled_slot_width > scaled_item_width else 0
            pad_y = (scaled_slot_height - scaled_item_height) / 2 if scaled_slot_height > scaled_item_height else 0
            centered_x = slot.origin_x + pad_x
            centered_y = slot.origin_y + pad_y
            # Snap to the center of the slot
            self.drag_widget.snap(int(centered_x), int(centered_y), self.snap_assign_dur)

        def snap_to_origin(self):
            self.drag_widget.snap(self.origin_x, self.origin_y, self.snap_ret_dur)
        
        ########### RESCALE TO FIT IN THE SLOT #################

        def apply_distance_scaling(self, trans, st, at):
            """Applies dynamic scaling based on the current state: dragging, resizing, or maintaining current scale."""
            if self.is_dragging:
                # Handle rescaling when dragging
                self.handle_dragging_scale()
            elif self.should_resize_to_origin:
                self.resize_to_origin()
                print("Resizing : " + str(trans.zoom))
            trans.zoom = self.auto_scaled_value
            return None
            
        def handle_dragging_scale(self):
            """Adjusts the item's scale based on its distance to the closest slot while dragging."""
            # Find the closest slot and distances
            distance, origin_dist, closest_slot = self.get_closest_slot_distance()
            if distance is not None and closest_slot is not None:
                # Calculate zoom factor based on the distance and slot properties
                zoom_factor = distance_zoom_with_size(
                    distance=distance,
                    item=self,
                    slot=closest_slot,
                    max_distance=origin_dist,
                    padding_factor=self.padding_factor
                )
                # Apply the zoom factor and update the auto-scaled value
                self.auto_scaled_value = zoom_factor

        def get_closest_slot_distance(self):
            """Finds the closest slot to the current mouse position."""
            closest_slot = None
            closest_distance = float('inf')
            origin_distance = None
            distance = None
            xpos, ypos = self.drag_widget.last_x or self.origin_x, self.drag_widget.last_y or self.origin_y
            # print("Position value:", xpos, ypos)
            for slot in self.group.slots:
                distance = ((xpos - slot.origin_x) ** 2 + (ypos - slot.origin_y) ** 2) ** 0.5
                if distance < closest_distance:
                    closest_distance = distance
                    closest_slot = slot
            # Calculate origin distance between slot and item
            if closest_slot:
                origin_distance = ((self.origin_x - closest_slot.origin_x) ** 2 + (self.origin_y - closest_slot.origin_y) ** 2) ** 0.5
                return closest_distance, origin_distance, closest_slot
            return None
        
        def resize_to_slot(self, slot):
            """Resizes the item to fit within the slot's dimensions and applies the scale."""
            self.scale_factor = compute_scale_factor(slot, self, self.padding_factor)
            self.auto_scaled_value = self.scale_factor * self.default_scale
            
        def resize_to_origin(self):
            """Smoothly resizes the item based on distance to original position and adjusts scaling accordingly."""
            current_x = self.drag_widget.last_x or self.origin_x
            current_y = self.drag_widget.last_y or self.origin_y
            current_distance = ((current_x - self.origin_x) ** 2 + (current_y - self.origin_y) ** 2) ** 0.5
            # if self.removal_slot_x and self.removal_slot_y:
            #     total_distance = ((self.removal_slot_x - self.origin_x) ** 2 + (self.removal_slot_y - self.origin_y) ** 2) ** 0.5
            # self.auto_scaled_value = (1.0 + (self.scale_factor - 1.0) * (1 - (current_distance / total_distance))) * self.default_scale     
            if abs(total_distance - current_distance) < self.origin_threshold:
                self.auto_scaled_value = self.default_scale
                self.should_resize_to_origin = False
                return None
            return None

    ############### UTIL FUNCTIONS USED IN RESCLAING ###############

    def compute_scale_factor(slot, item, padding_factor=0.9):
        """
        Computes the scale factor needed to fit the item within the slot,
        maintaining the aspect ratio and applying an optional padding factor.
        """
        # Get the dimensions of the slot and the item
        slot_width, slot_height = slot.width * slot.default_scale, slot.height * slot.default_scale
        item_width, item_height = item.width * item.default_scale, item.height * item.default_scale
        # Calculate the scaling factors to fit the item into the slot while preserving aspect ratio
        scale_x = slot_width / item_width
        scale_y = slot_height / item_height
        scale_factor = min(scale_x, scale_y)  # Choose the smaller scale to maintain the aspect ratio
        # Apply optional padding factor
        return scale_factor * padding_factor

    def distance_zoom_with_size(distance, item, slot, max_distance=300, padding_factor=0.9):
        """Calculates zoom factor based on the distance and size comparison between the card and the slot."""
        # scale benchmark is the one with smaller scale (item or slot)
        new_scale = compute_scale_factor(slot, item, padding_factor)
        if distance >= max_distance:
            return item.default_scale
        else:
            return (1.0 + (new_scale - 1.0) * (1 - (distance / max_distance))) * item.default_scale