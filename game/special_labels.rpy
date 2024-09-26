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

## After Load ##################################################################
##
## Adjust any variables etc in the after_load label
## Also consider: define config.after_load_callbacks = [ ... ]
##
label after_load():
    return
