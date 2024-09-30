# characters.rpy

define l = Character('Louis', callback = name_callback, cb_name = "louis")
define nl = Character ('Narrator Louis')
define a = Character('Aven', callback = name_callback, cb_name='aven')
define e = Character('Elio', callback = name_callback, cb_name='elio')
define c = Character('Catcher', callback = name_callback, cb_name='catcher')
define i = Character('Ivory', callback = name_callback, cb_name='ivory')
define az = Character('Aziel', callback = name_callback, cb_name='aziel')
define li = Character('Lily', callback = name_callback, cb_name='lily')
define m = Character('Maverick', callback = name_callback, cb_name='maverick')

define no = Character('', what_font="/fonts/AveriaSerifLibre-Regular.ttf")
define ca = Character('Catcher', callback = name_callback, cb_name='catcher', \
                            what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff")
define iv = Character('Ivory', callback = name_callback, cb_name='ivory', \
                            what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff")
define cro = Character('???',  callback = name_callback, cb_name='crow', \
                            what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff")
define b = Character('Benny',  callback = name_callback, cb_name='crow',
                            what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff")


define av = Character('Aven', callback = name_callback, cb_name='aven', \
                                what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff")
define p = Character('Pieter', what_font="/fonts/AveriaSerifLibre-Regular.ttf", who_font="/fonts/AveriaSerifLibre-Regular.ttf", color="#ffffff")