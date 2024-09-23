label inventory_test:
    "This is an inventory test script -- 1st event"
    $ my_inventory.run_events() # start event
    "Collect the itmes in the inventory!"
    "Collect the itmes in the inventory!!"
    "Collect the itmes in the inventory!!!"
    $ inv_state = my_inventory.get_inventory_summary() # get summary (string)
    "Inventory Status (1):\n[inv_state]"
    $ my_inventory.end_events()
    "Event 1 ended."

    ###############################################

    "This is an inventory test script -- 2nd event"
    $ my_inventory.run_events() # start event
    "Collect the itmes in the inventory!"
    "Collect the itmes in the inventory!!"
    "Collect the itmes in the inventory!!!"
    $ inv_state = my_inventory.get_inventory_summary() # get summary (string)
    "Inventory Status (2):\n[inv_state]"
    $ my_inventory.end_events()
    "Event 2 ended."

    ###############################################

    "This is an inventory test script -- 3rd event"
    $ my_inventory.run_events() # start event
    "Collect the itmes in the inventory!"
    "Collect the itmes in the inventory!!"
    "Collect the itmes in the inventory!!!"
    $ inv_state = my_inventory.get_inventory_summary() # get summary (string)
    "Inventory Status (3):\n[inv_state]"
    $ my_inventory.end_events()
    "Event 3 ended."