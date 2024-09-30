# devider.rpy

label itch:

    scene itch
    with dissolve1
    call screen itchpage

    jump transitioning

label transitioning:

    scene black
    call screen contentwarning

    $ half = 1.5

    scene black
    with dissolve3
    no "The sound of rustling leaves from outside fills the silence that consumed the void. A deep humming mixes in with the creaking of an open door, the clamor of a distant murder echoes to nowhere."

    no "Breathing heavily as the prattling sound of birds is in earshot, focusing on nothing yet it induces a sinking, anxious feeling inside."

    no "{color=#f00}Wake up.{/color}"
    jump catcher_day_one
