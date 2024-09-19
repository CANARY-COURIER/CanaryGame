
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

image main_menu_background = "Backgrounds/key art background.png"
image BlackBars = "BlackBars.png"
image Louis = "louis key art.png"

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"
    add "BlackBars"
    add "Louis"

    vbox:
        xpos 250
        yalign 0.5
        spacing 6

        textbutton _("Start") action Start()

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Settings") action ShowMenu("preferences")

        #textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

