# characters.rpy

# make all sprites unfocused on narration
define narrator = Character(callback=name_callback, cb_name=None)

# Character definitions
define l = Character('Louis', callback=name_callback, cb_name="louis")
define nl = Character('Narrator Louis')
define a = Character('Aven', callback=name_callback, cb_name="aven")
define e = Character('Elio', callback=name_callback, cb_name="elio")
define c = Character('Catcher', callback=name_callback, cb_name="catcher")
define i = Character('Ivory', callback=name_callback, cb_name="ivory")
define az = Character('Aziel', callback=name_callback, cb_name="aziel")
define li = Character('Lily', callback=name_callback, cb_name="lily")
define m = Character('Maverick', callback=name_callback, cb_name="maverick")

# Character with no name (empty label)
define no = Character('', what_font="/fonts/AveriaSerifLibre-Regular.ttf", callback=name_callback, cb_name=None)

# Specific style characters with cb_name in lowercase and callback
define ca = Character('Catcher', what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff", callback=name_callback, cb_name="catcher")
define iv = Character('Ivory', what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff", callback=name_callback, cb_name="ivory")
define cro = Character('???', what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff", callback=name_callback, cb_name="crow")
define b = Character('Benny', what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff", callback=name_callback, cb_name="crow")

# Additional characters with cb_name in lowercase and callback
define av = Character('Aven', what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff", callback=name_callback, cb_name="aven")
define p = Character('Pieter', what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff", callback=name_callback, cb_name="aven")


########################################################################

# l = Louis - louis normal
# nl = Narrator Louis - no sprite
# a = Aven - aven neutral
# e = Elio - elio neutral
# c = Catcher - catcher neutral
# i = Ivory - ivory neutral
# az = Aziel - aziel neutral
# li = Lily - lily neutral
# m = Maverick - maverick neutral

# no = NO CHARACTER (but still with font of second half) - no sprite
# ca = Catcher - catcher normal 2
# iv = Ivory - ivory normal 2
# cro = ??? - crow default 2
# b = Benny - crow default 2
# av = Aven - aven neutral 2
# p = Pieter - aven neutral 2

########################################################################


init:
    image louis glitch_1:
        glitch("./images/Sprites_FirstHalf/louis normal.png") 
        pause 1.0
        glitch("./images/Sprites_FirstHalf/louis scared.png", \
                offset=60, randomkey=100) # bigger and always-random slicing
        pause 0.1
        repeat

    image louis glitch_2:
        animated_glitch('louis glitch_1', timeout_base=1.0, timeout_vanilla=0.2, randomkey=30) 
    
    image louis glitch_3:
        squares_glitch("./images/Sprites_FirstHalf/louis normal.png", squareside=40, chroma=1.4, permutes=0.2, randomkey=40)
        pause 0.02
        squares_glitch("./images/Sprites_FirstHalf/louis scared.png", squareside=20, chroma=0.8, permutes=0.3, randomkey=100) 
        pause 0.05
        repeat

    layeredimage louis:
        at sprite_highlight('louis') 
        zoom 0.8
        align (0.5, 1.0)
        group body:
            attribute normal default:
                "./images/Sprites_FirstHalf/louis normal.png"
            attribute anxious:
                "./images/Sprites_FirstHalf/louis anxious.png"
            attribute happy:
                "./images/Sprites_FirstHalf/louis happy.png"
            attribute scared:
                "./images/Sprites_FirstHalf/louis scared.png"
            attribute angry_2:
                "./images/Sprites_SecondHalf/louis angry 2.png"
            attribute happy_2:
                "./images/Sprites_SecondHalf/louis happy 2.png"
            attribute normal_2:
                "./images/Sprites_SecondHalf/louis normal 2.png"
            attribute sad_2:
                "./images/Sprites_SecondHalf/louis sad 2.png"
            attribute glitch_1:
                'louis glitch_1'
            attribute glitch_2:
                'louis glitch_2'
            attribute glicth_3:
                'louis glitch_3'

    layeredimage aven:
        at sprite_highlight('aven') 
        zoom 0.8
        align (0.5, 1.0)
        
        group body:
            attribute neutral default:
                "./images/Sprites_FirstHalf/aven neutral.png"
            attribute angry:
                "./images/Sprites_FirstHalf/aven angry.png"
            attribute questioning:
                "./images/Sprites_FirstHalf/aven questioning.png"
            attribute thinking:
                "./images/Sprites_FirstHalf/aven thinking.png"
            attribute angry_2:
                "./images/Sprites_SecondHalf/aven angry 2.png"
            attribute confused_2:
                "./images/Sprites_SecondHalf/aven confused 2.png"
            attribute happy_2:
                "./images/Sprites_SecondHalf/aven happy 2.png"
            attribute neutral_2:
                "./images/Sprites_SecondHalf/aven neutral 2.png"
            attribute sad_2:
                "./images/Sprites_SecondHalf/aven sad 2.png"

    layeredimage elio:
        at sprite_highlight('elio') 
        zoom 0.8
        align (0.5, 1.0)
        
        group body:
            attribute anxious:
                "./images/Sprites_FirstHalf/elio anxious.png"
            attribute confused:
                "./images/Sprites_FirstHalf/elio confused.png"
            attribute happy:
                "./images/Sprites_FirstHalf/elio happy.png"
            attribute neutral default:
                "./images/Sprites_FirstHalf/elio neutral.png"

    layeredimage catcher:
        at sprite_highlight('catcher') 
        zoom 0.8
        align (0.5, 1.0)
        
        group body:
            attribute angry:
                "./images/Sprites_FirstHalf/catcher angry.png"
            attribute anxious:
                "./images/Sprites_FirstHalf/catcher anxious.png"
            attribute confused:
                "./images/Sprites_FirstHalf/catcher confused.png"
            attribute neutral default:
                "./images/Sprites_FirstHalf/catcher neutral.png"
            attribute angry_2:
                "./images/Sprites_SecondHalf/catcher angry 2.png"
            attribute happy_2:
                "./images/Sprites_SecondHalf/catcher happy 2.png"
            attribute normal_2:
                "./images/Sprites_SecondHalf/catcher normal 2.png"
            attribute sad_2:
                "./images/Sprites_SecondHalf/catcher sad 2.png"

    layeredimage ivory:
        at sprite_highlight('ivory') 
        zoom 0.8
        align (0.5, 1.0)
        
        group body:
            attribute anxious:
                "./images/Sprites_FirstHalf/ivory anxious.png"
            attribute happy:
                "./images/Sprites_FirstHalf/ivory happy.png"
            attribute neutral default:
                "./images/Sprites_FirstHalf/ivory neutral.png"
            attribute sad:
                "./images/Sprites_FirstHalf/ivory sad.png"
            attribute angry_2:
                "./images/Sprites_SecondHalf/ivory angry 2.png"
            attribute happy_2:
                "./images/Sprites_SecondHalf/ivory happy 2.png"
            attribute normal_2:
                "./images/Sprites_SecondHalf/ivory normal 2.png"
            attribute sad_2:
                "./images/Sprites_SecondHalf/ivory sad 2.png"
            attribute sad_sad:
                "./images/Sprites_SecondHalf/ivory sad sad.png"
            attribute sad_sad_sad:
                "./images/Sprites_SecondHalf/ivory sad sad sad.png"

    layeredimage aziel:
        at sprite_highlight('aziel') 
        zoom 0.8
        align (0.5, 1.0)
        
        group body:
            attribute alarmed:
                "./images/Sprites_FirstHalf/aziel alarmed.png"
            attribute confused:
                "./images/Sprites_FirstHalf/aziel confused.png"
            attribute neutral default:
                "./images/Sprites_FirstHalf/aziel neutral.png"
            attribute think:
                "./images/Sprites_FirstHalf/aziel think.png"

    layeredimage lily:
        at sprite_highlight('lily') 
        zoom 0.8
        align (0.5, 1.0)
        
        group body:
            attribute neutral default:
                "./images/Sprites_FirstHalf/lily neutral.png"
            attribute anxious:
                "./images/Sprites_FirstHalf/lily anxious.png"
            attribute confused:
                "./images/Sprites_FirstHalf/lily confused.png"
            attribute happy:
                "./images/Sprites_FirstHalf/lily happy.png"

    layeredimage maverick:
        at sprite_highlight('maverick') 
        zoom 0.8
        align (0.5, 1.0)
        
        group body:
            attribute neutral default:
                "./images/Sprites_FirstHalf/maverick neutral.png"
            attribute angry:
                "./images/Sprites_FirstHalf/maverick angry.png"
            attribute confused:
                "./images/Sprites_FirstHalf/maverick confused.png"
            attribute smile:
                "./images/Sprites_FirstHalf/maverick smile.png"

    layeredimage crow:
        at sprite_highlight('crow') 
        zoom 0.8
        align (0.5, 1.0)
        group body:
            attribute default_2 default:
                "./images/Sprites_SecondHalf/crow default 2.png"
            attribute snapped_neck:
                "./images/Sprites_SecondHalf/crow snapped neck.png"


