default persistent.turn_on_switch = False 

image animated_button:
    './gui/BlankButton_hover.png'
    parallel:
        yalign 0.0
        linear 2.0 yalign 1.0
        repeat
    parallel:
        xalign 0.0
        linear 2.0 xalign 1.0

screen sample_screen(): # main_menu??
    ## This ensures that any other menu screen is replaced.
    tag menu
    
    image 'animated_button'
    if persistent.turn_on_switch == False:
        frame align(0.5, 0.5):
            background "#000000ff"
            # xmaximum 1200
            padding (500, 300)
            vbox:
                spacing 50
                xmaximum 1000
                textbutton "{b}START{/b}" text_size 100 action SetVariable('persistent.turn_on_switch', True) xalign 0.5 # OFF -> ON

    else: # start_main_menu == True
        add gui.main_menu_background
        # use animated_main_menu
        ## This empty frame darkens the main menu.
