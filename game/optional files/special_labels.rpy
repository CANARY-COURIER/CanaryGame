## Special Labels ##############################################################
##
## These are special labels that Ren'Py automatically recognizes if they
## are included with the game. Read more here:
## https://www.renpy.org/doc/html/label.html#special-labels
##

define introPlay = True

label splashscreen:
    if introPlay:
        #call screen sample_screen
        #############################################
        #FUNCTIONALITY HERE
        "{color=#f00}The game opens with the AVANE STUDIOS logo cutscene, transitioning to the main menu screen.{/color}"
        "{color=#f00}Upon starting the game, the screen transitions into a white screen, wherein a short introduction is introduced in the form of scribbled drawings with a short voice over.{/color}"
        #############################################
        # splash screens?
    
        nl "Welcome! This is Narrator Louis, pleasure to be guiding you in Avane Studio's first ever- Canary Courier! Alpha Build- of course!"
    
        nl "Now, to catch you up to speed if you weren't present for our forum dev logs- here's a quick rundown!"
    
        nl "You, the player, will be controlling me- Louis, the canary bird- throughout the whole game and in my stead- deliver and fulfill customer orders to get me that sweet 3 star rating!"
        nl "That's the gist of it- the name of the game basically!"
    
        nl "You must be wondering, now what's all this for, right? All of this is with cause, of course, but I'll tell you that a bit later on, let's first proceed- to your first task of the day!"
    
        #############################################
        #FUNCTIONALITY HERE
        "{color=#f00}The game transitions into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Aves Courier Center{/color}"
        #############################################
        $introPlay = False
    return

## After Load ##################################################################
##
## Adjust any variables etc in the after_load label
## Also consider: define config.after_load_callbacks = [ ... ]
##
label after_load():
    return
