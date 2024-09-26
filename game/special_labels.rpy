## Special Labels ##############################################################
##
## These are special labels that Ren'Py automatically recognizes if they
## are included with the game. Read more here:
## https://www.renpy.org/doc/html/label.html#special-labels
##

define dissolve2 = Dissolve(2.0)
define fade = Fade(2.0)

label splashscreen:
    $_dismiss_pause = False

    scene white
    show BlackBars
    show avane studios logo at truecenter
    with dissolve2

    $ renpy.pause(2.0)

    scene white
    show BlackBars
    show spooktober at truecenter:
        xsize 1200 ysize 461
    with dissolve2

    $ renpy.pause(2.0)

    return

## After Load ##################################################################
##
## Adjust any variables etc in the after_load label
## Also consider: define config.after_load_callbacks = [ ... ]
##
label after_load():
    return
