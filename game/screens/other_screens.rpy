
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
Director, Writers, Character Designers, and Video Editors\n
Quack & Loaf Co.\n
GUI & Programmers\n
{a=https://sites.google.com/view/alessandro-brillo/}Alessandro{/a} - {a=https://x.com/panino_dev}@panino_dev{/a}\n
{a=https://itch.io/profile/seo-a-nam}SAN{/a}\n
{a=https://samehawke.itch.io/}samehawke{/a}\n
Sprites & CG Artists\n
shibakiba - {a=https://twitter.com/shiba_kiba}@shiba_kiba{/a}\n
CRRN - {a=https://x.com/_crrn_}@_crrn_{/a}\n
Helper Artists\n
smuisers - {a=https://www.instagram.com/smuisers?igsh=c21oOGNqZHZrbmEx&utm_source=qr}@smuisers{/a}\n
{a=https://weissily.carrd.co/}Weissily{/a}\n
Background & Item Artists\n
{a=https://ajihaew.com/}ajihaew{/a} - {a=https://twitter.com/ajihaew}@ajihaew{/a}\n
Fiona - {a=https://www.instagram.com/unenthusedcrayon/}@unenthusedcrayon{/a}\n
Composers\n
Lilith "Lilithpad" Scarlet - {a=https://x.com/lilithpads}@lilithpads{/a}\n
{a=https://composerapogio.com/}Apogio{/a}\n
Voice Actors\n
Samuel Hagg as Avel Leto - {a=https://x.com/aseattorney}@aseattorney{/a}
Luminaryyxx as Evangeline Leto - {a=https://x.com/Luminaryyxx}@Luminaryyxx{/a}
Keedo as Kane Cozbi\n
Pluto as Elise Shaw\n
Miscellanous\n
beta tester - {a=https://altairdelirio.carrd.co/}AltairDeLirio{/a} & Lily Wisteria\n
senstivity reader - I Specialize in Sad - {a=https://www.instagram.com/i_specialize_in_sad?igsh=MTN6eHUxMDM4NGxybA%3D%3D&utm_source=qr}@i_specialize_in_sad{/a}\n
proofreaders - sieerrraaa & helio.wyrm\n
manager - Lily Wisteria\n
itch.io designer - https://mishantics.itch.io/
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():

    tag menu

    add "#21212db2" # The background; can be whatever

    use game_menu(_("About"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

            style_prefix "about"
            style "about_label_text" 

style about_label_text:
    xsize 900
    size 36


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"
    style_prefix 'game_menu'
    #add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Help"))

    fixed:
        xoffset 1000
        yoffset 200
        hbox:
            spacing 50
            style_prefix 'help'
            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")

            if GamepadExists():
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
    fixed:
        xsize 900 ysize 5
        yoffset 260
        xoffset 650
        add "#ffffff": # white
            alpha 0.3

    null height 10

    viewport:
        style_prefix 'help'
        mousewheel True draggable True pagekeys True
        yinitial 1.0
        scrollbars "vertical" 
        xalign 0.6
        yalign 0.7
        xmaximum 800
        ymaximum 700 

        has vbox
        style_prefix "help"
        spacing 23
    
        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button:
    xmargin 12

style help_label:
    xpos 120
    right_padding 140

style help_label_text:
    #xpos 200
    right_padding 100
    xalign 1.0
    textalign 1.0

style help_vscrollbar:
    base_bar Frame("gui/slider/vertical_idle_bar.png")
    thumb "gui/slider/vertical_idle_thumb.png"
    thumb_offset 0
    top_gutter 0
    bottom_gutter 0
    xmaximum 25
    ymaximum 600
    yoffset 50

style help_viewport:
    xsize 920
    ysize config.screen_height-450
    yoffset 30
    # align (0.9, 0.8)

style help_side:
    yfill True
    align (1.3, 1)