
"""This is the inventory screen. It will show all the items the player has collected so far."""

init python:
    # All Items and their description
    item_book = {
        # Items
        "Camping equipment": "Contains a tent and a sleeping bag. Good night.",
        "Rope": "Can be quite useful here and there. Can be VERY useful if you are creative.",
        "Rations2": "Pack of long-lasting food. Not really tasty but like already said, long-lasting.",
        "Map and compass": "A map of Bear Jarldim and Cat Kingdom.",
        "Tinderbox": "Why make fire the hard way if there is an easier way?",
        # Weapons (Rogue)
        "Dagger": "Your standard weapon.",
        "Leather armor": "Your standard armor.",
        # Weapons (Warrior)
        "Great axe": "Your standard weapon.",
        "Heavy armor": "Your standard armor.",
        # Weapons (Wizard)
        "Spellbook": "You can keep track of your spell slots.",
        "Staff": "Your standard weapon. You are nothing without your staff, be careful."
    }
    
    class Inventory:
        def __init__(self):
            self.itemList = []
        
        def addItem(self, item_name, amount=1):
            if len(self.itemList) > 0:
                for item in self.itemList:
                    if item['name'] == item_name:
                        item['amount'] += amount
                        return
            self.itemList.append({'name': item_name, 'amount': amount})

        def deleteItem(self, item_name, amount=1):
            if self.isItem(item_name):
                for item in self.itemList:
                    if item['name'] == item_name:
                        if item['amount'] == amount:
                            self.itemList.remove(item)
                        elif item['amount'] > amount:
                            item['amount'] -= amount
                        else:
                            narrator("You don't have enough of this item!")
                        return
        
        def isItem(self, item_name):
            for item in self.itemList:
                if item['name'] == item_name:
                    return True
            return False
    
    def get_item_description(item_name):
        if item_name in item_book.keys():
            return item_book[item_name]
        return "No description available."

init:
    default my_inventory = Inventory()
    
    screen Inventory_Window:
        frame:
            background "#00000044"
            padding (50, 20)
            xminimum 600
            ymaximum 1000
            align (0.5, 0.5)
            vbox:
                spacing 15
                text "{b}INVENTORY{/b}" size 30 line_spacing 10 color "#ffffff"
                $ max_rows = 10
                $ columns = 8
                for row in range(max_rows):
                    hbox:
                        spacing 10
                        $ index_start = (row-1) * columns
                        $ index_end = index_start + columns
                        for item in my_inventory.itemList[index_start:index_end]:
                            $ item_image = "./libs/inventory_module/images/items/" + item['name'] + ".png"
                            $ item_description = get_item_description(item['name'])
                            imagebutton idle [item_image]:
                                action Function(my_inventory.deleteItem, item['name'], 1)
                                tooltip "{b}" + item['name'] + "{/b}\n" + item_description
                            if item['amount'] > 1:
                                text str(item['amount']) color "#cacaca" size 20 xoffset -7 yoffset 10
                textbutton "close" action Hide('Inventory_Window')
    
    image inventory_button = './libs/inventory_module/images/main_ui/backpack.png'
    screen inventory_main_interface:
        frame:
            align(1.0, 0.0)
            margin (20, 20)
            background "#00000000"
            imagebutton idle 'inventory_button' action ToggleScreen("Inventory_Window")
        
