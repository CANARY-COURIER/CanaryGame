## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##

image BlackBars = "BlackBars.png"

screen game_menu(title):

    style_prefix "game_menu"
    fixed:
        fixed:
            image 'gui/MenuBackground.png' align (0.5, 0.5)
        fixed:
            image 'BlackBars.png'
        
    vbox:
        xpos 250 yalign 0.5
        spacing -8

        if main_menu:

            ## LOAD ##
            imagebutton auto "gui/BlankButton_%s.png" focus_mask True action ShowMenu("load")
            text _("Load") xpos 95 ypos -55

            ## SETTINGS ##
            imagebutton auto "gui/BlankButton_%s.png" focus_mask True action ShowMenu("preferences")
            text _("Settings") xpos 70 ypos -55

            ## CREDITS ##
            imagebutton auto "gui/BlankButton_%s.png" focus_mask True action ShowMenu("about")
            text _("Credits") xpos 70 ypos -55

            # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            #     imagebutton auto "gui/BlankButton_%s.png" focus_mask True action ShowMenu("help")
            #     text _("Help") xpos 95 ypos -55

            # textbutton _("Start") action Start()
            # textbutton _("Load") action ShowMenu("load")
            # textbutton _("Preferences") action ShowMenu("preferences")
            # textbutton _("About") action ShowMenu("about")

            # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            #     textbutton _("Help") action ShowMenu("help")

        else:

            ## HISTORY ##
            #textbutton _("History") action ShowMenu("history")
            imagebutton auto "gui/BlankButton_%s.png" focus_mask True action ShowMenu("history")
            text _("History") xpos 80 ypos -55

            ## SAVE ##
            #textbutton _("Save") action ShowMenu("save")
            imagebutton auto "gui/BlankButton_%s.png" focus_mask True action ShowMenu("save")
            text _("Save") xpos 95 ypos -55

            ## LOAD ##
            imagebutton auto "gui/BlankButton_%s.png" focus_mask True action ShowMenu("load")
            text _("Load") xpos 95 ypos -55

            ## SETTINGS ##
            imagebutton auto "gui/BlankButton_%s.png" focus_mask True action ShowMenu("preferences")
            text _("Settings") xpos 70 ypos -55

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                imagebutton auto "gui/BlankButton_%s.png" focus_mask True action ShowMenu("help")
                text _("Help") xpos 95 ypos -55


        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            ## MAIN MENU ##
            #textbutton _("Main Menu") action MainMenu()
            imagebutton auto "gui/BlankButton_%s.png" focus_mask True action MainMenu()
            text _("Main Menu") xpos 50 ypos -55

        if renpy.variant("pc"):

            #textbutton _("Quit") action Quit(confirm=not main_menu)
            imagebutton auto "gui/BlankButton_%s.png" focus_mask True action Quit(confirm=not main_menu)
            text _("Quit") xpos 95 ypos -55

    imagebutton auto "gui/BlankButton_%s.png" action Return() xpos 250 ypos 960
    #     focus_mask True
    #     style "return_button"
    #     action Return()
    text _("Return") xpos 335 ypos 975
    #textbutton _("Return") style "return_button" action Return()

    ## Remove this line if you don't want to show the screen
    ## title text as a label (for example, if it's baked into
    ## the background image.)
    label title xpos 400 ypos 100

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style return_button:
    idle_color "#332221"
    hover_color "#a5a5a5"
    xpos 320
    yalign 1.0
    yoffset -55

style game_menu_viewport:
    xsize config.screen_width-420
    ysize config.screen_height-150
    align (0.9, 0.8)

style game_menu_side:
    yfill True
    align (1.3, 1)

style game_menu_vscrollbar:
    unscrollable "hide"

style game_menu_label:
    padding (300, 10)
style game_menu_label_text:
    size 30
