# Example usage
define inv_data_path = './mechanics/inventory/data'
define my_inv_slots = [
    {'pos' : (400, 900), 'image_path' : './images/inventory/default/slot1.png'},
    {'pos' : (550, 900), 'image_path' : './images/inventory/default/slot2.png'},
    {'pos' : (700, 900), 'image_path' : './images/inventory/default/slot3.png'},
    {'pos' : (850, 900), 'image_path' : './images/inventory/default/slot4.png'},
    {'pos' : (1000, 900), 'image_path' : './images/inventory/default/slot5.png'}
]
default my_inventory = InventoryManager(total_events=3, slot_info=my_inv_slots, data_path=inv_data_path)
default inv_state = None

# Screen for displaying drag-and-drop functionality
init:
    screen drag_and_drop_inventory():
        tag menu
        modal True
        fixed:
            draggroup:
                # Display inventory slots
                for slot in my_inventory.group.slots:
                    add slot.drag_widget
                # Display shop items
                for item in my_inventory.group.items:
                    add item.drag_widget