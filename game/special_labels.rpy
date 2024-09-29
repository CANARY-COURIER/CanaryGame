## Special Labels ##############################################################
##
## These are special labels that Ren'Py automatically recognizes if they
## are included with the game. Read more here:
## https://www.renpy.org/doc/html/label.html#special-labels
##

image White = "White.png"
define dissolve1 = Dissolve(1.0)
define dissolve2 = Dissolve(2.0)
define dissolve3 = Dissolve(3.0)
define fade = Fade(2.0)

label splashscreen:

    $_dismiss_pause = False

    scene White
    show spooktober at truecenter:
        xsize 1200 ysize 461
    with dissolve1

    $ renpy.pause(1.0)

    play music "music/CC Title Screen Theme Jingle.wav" noloop

    scene White
    show qnl logo at truecenter
    with dissolve1

    $ renpy.pause(1.0)

    scene White
    show avane studios logo at truecenter:
        xsize 400 ysize 513
    with Dissolve(1.5)

    $ renpy.pause(1.5)

    return

screen contentwarning:

    modal True

    frame:
        xsize 1920
        ysize 1080
        xpos 0
        ypos 0
        padding (0, 0) # Manually reset padding
        background color("#000")

        vbox:
            text "{size=33}Content Warning{/size}":
                pos (370, 40)
                xsize 540 # sets line length
                text_align 0.5 # align center

        imagebutton:
            auto "gui/button_%s.png"
            # YES button
            focus_mask True
            pos (370,440)
            action Return(), With(dissolve)

        imagebutton:
            auto "gui/button_%s.png"
            # NO button
            focus_mask True
            pos (650,440)
            action Quit()

        text "{size=35}Yes{/size}":
            pos (380, 455)
            min_width 240 # sets line length
            text_align 0.5 # align center

        text "{size=35}No{/size}":
            pos (660, 455)
            min_width 240 # sets line length
            text_align 0.5 # align center

screen tape:
    imagebutton:
            auto "gui/tape_argument_%s.png"
            focus_mask True
            action Return()

screen bennynewspaper:
    imagebutton:
            auto "gui/benny_newspaper_clipping_%s.png"
            focus_mask True
            action Return()

## After Load ##################################################################
##
## Adjust any variables etc in the after_load label
## Also consider: define config.after_load_callbacks = [ ... ]
##
label after_load():
    return
