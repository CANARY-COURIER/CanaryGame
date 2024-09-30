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
        xalign 0.5
        yalign 1
        padding (0, 0) # Manually reset padding
        background color("#000")
        add "/gui/ContentWarning.png"
        # vbox:
        #     text "{size=60}Content Warning{/size}":
        #         pos (700, 200)
        #         xsize 540 # sets line length
        #         text_align 0.5 # align center
        #     text "{size=40}This game contains{/size}":

        imagebutton:
            auto "gui/Iunderstand_%s.png"
            # YES button
            focus_mask True
            #pos (370,440)
            action Return(), With(dissolve)

        imagebutton:
            auto "gui/quit_%s.png"
            # NO button
            focus_mask True
            #pos (650,440)
            action Quit()
        

        # text "{size=35}Yes{/size}":
        #     pos (380, 455)
        #     min_width 240 # sets line length
        #     text_align 0.5 # align center

        # text "{size=35}No{/size}":
        #     pos (660, 455)
        #     min_width 240 # sets line length
        #     text_align 0.5 # align center

screen dailydelightspick:
    imagebutton:
            auto "images/items/bun_%s.png"
            focus_mask True
            action Return()
    imagebutton:
            auto "images/items/donut_%s.png"
            focus_mask True
            action Return()
    imagebutton:
            auto "images/items/donut2_%s.png"
            focus_mask True
            action Return()
    imagebutton:
            auto "images/items/pie_%s.png"
            focus_mask True
            action Return()

screen hardwarepick:
    imagebutton:
            auto "images/items/glue_%s.png"
            focus_mask True
            action Return("glue")
    imagebutton:
            auto "images/items/screwdriver_%s.png"
            focus_mask True
            action Return("screwdriver")
    imagebutton:
            auto "images/items/toothpick_%s.png"
            focus_mask True
            action Return("toothpick")
    imagebutton:
            auto "images/items/wrench_%s.png"
            focus_mask True
            action Return("wrench")

screen itchpage:
    imagebutton:
            auto "gui/itch button_%s.png"
            focus_mask True
            action Return()

screen tape:
    imagebutton:
            auto "gui/tape_arguement_%s.png"
            focus_mask True
            action Return()

screen bennynewspaper:
    imagebutton:
            auto "gui/benny_newspaper_clipping_%s.png"
            focus_mask True
            action Return()

screen pills:
    imagebutton:
            auto "gui/pills_bottle_%s.png"
            focus_mask True
            action Return()

screen pills2:
    imagebutton:
            auto "gui/pills_bottle2_%s.png"
            focus_mask True
            action Return()

## After Load ##################################################################
##
## Adjust any variables etc in the after_load label
## Also consider: define config.after_load_callbacks = [ ... ]
##
label after_load():
    return
