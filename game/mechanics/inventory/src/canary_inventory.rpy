init 999 python:
    import json

    class InventoryItem(DragItem):
        def __init__(self, group, title, description=None, image_path=None, init_xpos=500, init_ypos=500, default_scale=1.0):
            super().__init__(group, title, description, image_path, init_xpos, init_ypos, default_scale=default_scale)
            self.hover_trans = glow_outline(12, "#cfb760", num_passes=30, power=0.8)
            
        def create_drag_widget(self):
            """Creates a draggable widget for InventoryItem."""
            # Auto-scaling transform
            self.img_idle =  self.img
            self.img_hover = At(self.img, self.hover_trans)
            self.drag_widget = Drag(
                d=self.img, \
                drag_name="item_"+str(self.index), \
                idle_child=self.img_idle, \
                hover_child=self.img_hover, \
                draggable=True, \
                droppable=False, \
                dragging=self.on_dragging_start, \
                dragged=self.drag_placed, \
                pos=(self.x, self.y)
            )
        
        def show_description(self):
            """Displays the description of the item."""
            return self.description
    
    # Group class for inventory logic
    class InventoryGroup(DragItemsGroup):
        def assign_item_to_slot(self, item, slot):
            """Assigns an item to a slot."""
            super().assign_item_to_slot(item, slot)

    # Slot class for inventory
    class InventorySlot(DragSlot):
        def __init__(self, group, init_xpos, init_ypos, image_path='./images/inventory/default/slot1.png', default_scale=1.0):
            super().__init__(group, init_xpos, init_ypos, image_path, default_scale=default_scale)

        def create_drag_widget(self):
            self.img = At(Image(self.image_path), Transform(Null(), zoom=self.default_scale))
            self.drag_widget = Drag(d=self.img, drag_name="inventorySlot_" + str(self.index), \
                                droppable=True, draggable=False, pos=(self.x, self.y))

    # Inventory management class
    class InventoryManager:
        def __init__(self, total_events=3, slot_info=None, data_path=None):
            """Initialize the inventory manager and prepare for events."""
            self.group = InventoryGroup(identical_overlap=True)
            self.current_event = 0  # Track current event number
            self.total_events = total_events  # Total number of events
            self.data_path = data_path
            self.slot_info = slot_info

        def run_events(self):
            """Load the next event's inventory and start the session."""
            if self.current_event < self.total_events:
                path = self.data_path
                json_file = f"{path}/inventory_event_{self.current_event + 1}.json"
                self.load_inventory_slots()
                self.load_inventory_from_json(json_file)
                print(f"Running event {self.current_event + 1}")
                self.current_event += 1
            else:
                print("All events have been completed.")

        def end_events(self):
            """Ends the current event and clears the inventory."""
            print(f"Ending event {self.current_event}")
            self.clear_inventory()

        def load_inventory_slots(self):
            # Initialize slots based on slot_info
            for slot_data in self.slot_info:
                new_slot = InventorySlot(self.group, slot_data['pos'][0], slot_data['pos'][1], slot_data['image_path'])
                self.group.add_slot(new_slot)
        
        def load_inventory_from_json(self, json_file_path):
            """Loads inventory data from a JSON file using renpy's loader."""
            try:
                # Use renpy loader to access the file inside the project directory
                with renpy.loader.load(json_file_path) as f:
                    # Read binary data and decode to string
                    json_data = f.read().decode("utf-8")
                    data = json.loads(json_data)
                    # Debugging: Print loaded data to see what is in the JSON
                    print(f"Loaded JSON data: {data}")
                    item_data = data.get("items", [])
                    self.initialize_inventory(item_data)
            except Exception as e:
                print(f"Error loading JSON file {json_file_path}: {e}")
    
        def initialize_inventory(self, item_data):
            """Initializes inventory based on external item data (list of dicts)."""
            quantity = 0
            for data in item_data:
                title = data.get("title")
                description = data.get("description", "No description available")  # Default description
                image_path = data.get("image_path")
                quantity = data.get("quantity", 1)  # Default quantity is 1
                init_xpos = data.get("xpos", 0)
                init_ypos = data.get("ypos", 0)
                self.add_items_to_inventory(title, description, image_path, init_xpos, init_ypos, quantity)
                
        def add_items_to_inventory(self, title, description, image_path, init_xpos, init_ypos, quantity):
            """Adds multiple items to the inventory."""
            for i in range(quantity):
                new_item = InventoryItem(self.group, title, description, image_path, init_xpos + (i * 50), init_ypos)
                self.group.add_item(new_item)
                
        def remove_item(self, item):
            """Removes a specific item from the inventory."""
            if item in self.items:
                item.remove()  # Implement a remove method inside the InventoryItem class
                self.items.remove(item)
                self.group.shift_items_left()

        def get_inventory_state(self):
            """Returns a summary of current inventory status."""
            return self.group.get_items_and_quantity()

        def get_inventory_summary(self):
            state_report = ""
            state = self.get_inventory_state()
            for item, quantity in state.items():
                state_report += f"{item}: {quantity} item(s)\n"
            if state_report == "":
                state_report = "Inventory is empty."
            return state_report
    
        def clear_inventory(self):
            """Clears the entire inventory by setting items and slots to None."""
            self.items = []
            self.slots = []
            self.group = InventoryGroup(identical_overlap=True)

            