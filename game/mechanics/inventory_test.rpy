
# The game starts here.
init python:
    def add_default_items():
        # Add the default items to the inventory.
        my_inventory.addItem('Camping equipment')
        my_inventory.addItem('Rope')
        my_inventory.addItem('Tinderbox')
        my_inventory.addItem('Rations2', amount = 10)
        my_inventory.addItem('Map and compass')

    def remove_existing_armors():
        # Clear the armor and weapon items in the inventory, if any. (Since the player is choosing a new class.)
        my_inventory.deleteItem('Dagger')
        my_inventory.deleteItem('Leather armor')
        my_inventory.deleteItem('Great axe')
        my_inventory.deleteItem('Heavy armor')
        my_inventory.deleteItem('Staff')
        my_inventory.deleteItem('Spellbook')
    
    def add_armor_and_weapon(clas):
        # Add the armor and weapon items to the inventory.
        if clas == "rogue":
            my_inventory.addItem('Dagger', amount = 2)
            my_inventory.addItem('Leather armor')
        elif clas == "warrior":
            my_inventory.addItem('Great axe')
            my_inventory.addItem('Heavy armor')
        elif clas == "wizard":
            my_inventory.addItem('Staff')
            my_inventory.addItem('Spellbook')

label inventory_test_script:
    show screen inventory_main_interface
    $ add_default_items()
    "tessting1"
    "tessting2"
    "tessting3"
    "tessting4"
    "tessting5"
    "tessting1"
    "tessting2"
    "tessting3"
    "tessting4"
    "tessting5"