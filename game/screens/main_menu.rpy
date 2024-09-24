
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

image main_menu_background = "Backgrounds/key art background.png"
image main_menu_logo = "logos/menu logo.png"
image BlackBars = "BlackBars.png"
image Louis = "louis key art.png"

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"
    add "main_menu_logo"
    add "BlackBars"
    add "Louis"

    vbox:
        xpos 520
        ypos 632
        spacing 6

        ## START ##
        # textbutton _("Start") action Start()
        imagebutton auto "gui/menu start button_%s.png" focus_mask True action Dissolve(Start())
        
        ## OPTIONS ##
        # textbutton _("Settings") action ShowMenu("preferences")
        imagebutton auto "gui/menu options button_%s.png" focus_mask True action ShowMenu("preferences")
        
        ## LOAD ##
        #textbutton _("Load") action ShowMenu("load")

        ## ABOUT ##
        #textbutton _("About") action ShowMenu("about")

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        #     ## Help isn't necessary or relevant to mobile devices.
        #     textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## QUIT ##
            # textbutton _("Quit") action Quit(confirm=not main_menu)
            imagebutton auto "gui/menu quit button_%s.png" focus_mask True action Quit(confirm=not main_menu)

