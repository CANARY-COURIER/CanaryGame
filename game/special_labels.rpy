## Special Labels ##############################################################
##
## These are special labels that Ren'Py automatically recognizes if they
## are included with the game. Read more here:
## https://www.renpy.org/doc/html/label.html#special-labels
##

define introPlay = True
define dissolve = Dissolve(2.0)
define fade = Fade(2.0)

label splashscreen:
    
    scene white
    show BlackBars
    show avane studios logo at truecenter
    with dissolve

    $ renpy.pause(2.0)

    show black with dissolve

    return

## After Load ##################################################################
##
## Adjust any variables etc in the after_load label
## Also consider: define config.after_load_callbacks = [ ... ]
##
label after_load():
    return
