# louis_day1.rpy

#######################################################
#                   STORY LABELS                     #
#######################################################


# ===== Start Scene: Introduction and Tutorial =====
label start_scene:
    #""" Intro to the tutorial """
    $ half = 0.5

    # Scene starts, and we introduce the player to the world
    scene tutorial 1
    with dissolve1

    voice "voice/nl1.wav"    
    nl "Welcome! This is Narrator Louis, and it's my pleasure to be guiding you in Avane Studio's first ever- {i}Canary Courier{/i}! Alpha Build- of course!"
    
    # Transition: Move to next tutorial section 
    scene tutorial 2
    with dissolve1

    voice "voice/nl2.wav"
    nl "Now, to catch you up to speed if you weren't present for our forum dev logs- here's a quick rundown!"
    
    scene tutorial 3
    with dissolve1

    voice "voice/nl3.wav"
    nl "You, the player, will be controlling me- Louis, the canary bird!"

    scene tutorial 4
    with dissolve1
    scene tutorial 5
    with dissolve1

    voice "voice/nl4.wav"
    nl "Throughout the whole game, you'll deliver and fulfill customer orders in my stead, to get me that sweet 3 star rating!"

    scene tutorial 6
    with dissolve1

    voice "voice/nl5.wav"
    nl "That's the gist of it- the name of the game!"

    scene acorn street
    with dissolve3

    voice "voice/nl6.wav"
    nl "You must be wondering, now what's all this for, right?"

    voice "voice/nl7.wav"
    nl "All of this is with cause, of course, but I'll explain that a bit later."
    
    voice "voice/nl8.wav"
    nl "For now, let's proceed to your first task of the day!"
    
    # Moving to the next part of the tutorial
    jump opening_sequence
    with dissolve3


# ===== Label: Opening Sequence (Day 1 Task Start) =====
label opening_sequence:
    """ Start of Day 1 """
    $ half = 1
    # Environment setup, music, and player intro to Aves Courier Center
    play music "music/CC Main Story Dialogue Theme.wav" fadein 3 fadeout 3

    $quick_menu = True

    scene aves courier center inside
    with dissolve2
    #show lightoverlay
    
    show louis happy at tint1
    with dissolve2
    l "Aves Courier Center, this is where all the magic happens..."
    
    #"Louis speaks of his work fondly."
    
    "Louis enters Aves Courier Center with a big smile on his face, looking forward to whatever the day may bring..."
    
    "Wandering further into the building, a shrill voice draws his attention towards the center of the room."
    
    "All eyes on a familiar, yet still loud, Bearded Bellbird with a built-in megaphone device strapped around its neck."
    
    # Jump to a decision point (choices are coming next!)
    jump bellbird_decision


label day_1_concluded:
    
    "Louis rummages through his bag, sorting out other stuff out of the way as he pulls out the paper bag containing the contents of Ivory's orders, handing it over gently with a small smile on his face."

    show louis happy
    l "This should be what you've tasked me with, a slice of apple pie, and a delicious cinnamon roll."

    "Louis feels his wing briefly graze hers as she accepts the bag with a fond look in her eyes as she sees the pastries she wanted."

    show ivory neutral
    i "Just in time as well, I'm ever grateful for you going out of your way to do this for me."
    
    show ivory happy
    i "There's just so many chores to do after my shift, I can't possibly do other things I'd need for it anymore!"

    "Louis chuckles at his words as he nods, understanding the hassle well."

    show louis happy
    l "Well, it is my job, Miss Ivory. I'm glad I'm making things easy for you if anything."

    show louis normal
    l "If everything is in order, I shall be taking my leave, then?"
    
    "Louis watches as the passerine bird looks through the content of the bag, before he hears her hum satisfied- a singsong tune."
    
    show ivory happy
    i "You did everything right, splendid!"

    show ivory neutral
    i "Well done, I should be able to mark my task finished for you- ah! I have something for you, before I forget."

    "Louis is left standing in front of the doorway of Ivory's home as she quickly disappears into the comfort of her home, before she returns with a plastic bag in her beak and the familiar pastry in view."

    "He was quick to accept her offer as she leaned forward to hand it to him, in his wings was the cinnamon roll he had bought for her as something part of his task."
    hide ivory neutral
    hide louis normal
    show cinnamonroll
    with dissolve1

    "Louis faces Ivory confused, a bit lost on what this meant."

    i "I figured you must be tired from your delivery, a small snack wouldn't hurt!"

    "Ivory smiles kindly at Louis which he takes rather well, he returns the grin with a thankful look plastered on his face."

    hide cinnamonroll
    show ivory happy at slightright
    show louis anxious at slightleft
    l "I-I'd have to go now, but this is a lot, thank you... are- are you sure you'd want me to have this?"

    show louis normal
    l "I mean, you did order it and all... "

    "Ivory waves him off dismissively again with her wing, pushing him lightly off her doorway with a reassuring smile."

    i "Nonsense! It'd be rude to refuse a gift from a lady bird now, no?"

    "Louis finds himself chuckling, finding amusement at being backed up to a corner. He bows his head promptly."

    show louis happy
    l "I suppose you're right, it would be rude. In that case, thank you for the lovely gift."

    l "I'll see you around, Miss Ivory."

    "Ivory returns Louis' farewell bow, watching Louis take off, shutting the door behind her."

    play music "music/CC Mission Complete.wav" fadein 1 fadeout 1
    scene achievement
    with dissolve3
    show achievementivory at truecenter
    with zoomin

    $ renpy.pause(3.0)
    
    #DAY 1 CONCLUDED
    scene avian care room
    with dissolve3
    $ is_daytime = False

    stop music fadeout 2.0
    play music "music/CC Somber Hospital Theme.wav" fadein 2 fadeout 2
    
    "Louis finds himself perched comfortably right next to the sleeping figure that inhabits the room he currently resides in."
    
    "Humming a light tune to himself as he settles his courier bag off to the side, focusing on the subject that reaps all of his hard work at the moment."
    
    "Louis holds a fond look as he gazes briefly onto the patient who is nestled quietly in their slumber."
    
    show louis happy at tinthospital
    l "I met a lovely customer today, you may be familiar with them- since you're always browsing around in the supermarket."

    show louis normal    
    l "I have a feeling they may be an employee, a cashier, maybe?"
    
    "Louis then reaches for his bag, rummaging through it as he pulls out the familiar gift given to him by his customer."
    
    show louis happy
    l "Miss Ivory, the name of my customer, gave this to me as a parting gift for accomplishing the task she assigned, but...I'd like to leave this to you instead."
    
    "He places down the neat, plastic wrapped cinnamon roll on the bedside table of the patient."
    
    "Louis chuckles heartily, a fond look in his eyes."
    
    show louis happy
    l "You must be craving something sweet, I know it, especially with the doctors only permitting you liquid meals? That is rough, it'll be our little secret, hm?"
    
    "He adjusts where the pastry was placed, hiding it in plain sight behind the withering flowers on a base."
    
    show louis normal
    l "I hope your day has been well, I've noticed... changes, but the doctors say it's just the medication, nothing off the worry."
    
    show louis happy
    l "Make sure you're also looking after yourself, I will have enough to help you recover, so just relax, and focus on getting better!"
    
    "Louis reassures the patient- his mother, as he stands up from his perched position."
    
    l "Aurora has also been doing her part in helping you, y'know her... always harder at work than I am, she'll be the one visiting you tomorrow when the first light hits."
    
    show louis normal
    l "For now... I must go home to her and rest- I'll have a new task assigned to me, no doubt in that. I'll visit you like always after my delivery."
    
    show louis happy
    l "I'll trust the doctors to take care of you in my stead, tomorrow, I'll bring you another gift to keep yourself entertained."
    
    "Louis bows his head in farewell, a gesture action as he wears the grounded smile he has while he bids her goodbye."
    
    show louis normal
    l "Goodnight, mother dearest."

    "As Louis bids his last goodbyes for the day, he exits the room." 
    
    scene avian care hallway
    with dissolve2
    "Before he has a chance to leave- he is stopped promptly by a soft yet stern call of his name, he turns around, faced with a bird much larger than he is."
    
    "???" "Mister Louis? Is that you I see there?"

    show louis normal at tinthospital3
    show aziel neutral at tinthospital2
    "Louis takes in the sight of him, a large- Great Horned Owl stands before him- greeting him in passing with a bow, his piercing gaze keeps Louis' attention on him."
    
    l "Yes...Yes that would be me."
    
    "The brown Owl introduces himself as he clears his throat."
    
    az "I'm Dr. Aziel, Mister Louis, I'm your mother's caretaker until she recovers fully."
    
    az "I was told by the other nurses here that Miss Joan's son is a particular shade of... yellow, brighter than any other Canary around, I see that now."
    
    "Louis, upon realization dawning on him, bows promptly in respect, before meeting the strong gaze of the Owl again, he nodded to his words."
    
    show louis happy
    l "Doctor A-Aziel! Accept my sorrys- I didn't introduce myself sooner."
    
    show louis normal
    l "I'm Louis, yes, Miss Joan is my mother, you got that right."
    
    "Louis chuckles briefly as he offers his wing, the Owl briefly grazes his feathers against Louis as introductions while the Owl hums pleased."
    
    show aziel think
    az "It's nice to finally make your acquaintance, were you on your way out?"
    
    show aziel neutral
    "Aziel motions his head towards the exit."
    
    "Louis nods in affirmation to his question."
    
    show louis happy
    l "Just paying a visit as usual, but my wife's expecting me- so I couldn't linger too long."
    
    "Louis  smiles apologetically."
    
    show aziel neutral
    az "Don't apologize, Mr. Louis. I have my own affairs I need to check-on but let's talk properly on your next visit."
    
    "Aziel offers an arm around the Canary, slowly guiding him out as he acknowledges Louis' dismissal to head home for the night."
    
    l "Thank you, Sir, I'll be sure to stick around longer."
    
    show aziel think
    az "Goodnight, Mr. Louis, until tomorrow then."
    
    show aziel neutral
    "Louis catches a brief glance of the Owl flying off elsewhere into the hospital, with that in mind, he turns to fly off on his own as well."
    
    scene acorn street night
    with dissolve2
    "Safely returning to the comforts of his home, and ending the day off with a successful delivery- and an interesting day with new faces."

    stop music fadeout 3
    scene black
    with dissolve3
    $ quick_menu = False
    show interview2 at truecenter
    $ renpy.pause(90.0, hard=True)
    stop movie
    $ quick_menu = True

    $ day = 2

    jump day_2



#######################################################
#                   DECISION LABELS                  #
#######################################################


label bellbird_decision:
    """ Player's first choice: Interact with Bellbird """
    menu:
        "APPROACH THE BELLBIRD":
            jump approach_the_bellbird
        "AVOID THE BELLBIRD":
            jump avoid_the_bellbird


label avoid_the_bellbird:
    show louis anxious
    "Catching sight of the booming bird, Louis turns on his talon to the opposite direction."

    "Already conscious of his tardiness, he's best off avoiding any interaction about it with Bellbird."
    
    "Louis' bright, yellow feather coating easily drew eyes with the heavy contrast from the more darker interior made the Bellbird's neck crane to follow the yellow that swiftly evaded his view."
    
    show louis anxious at slightleft
    show aven angry at tint2
    a "If that Canary is who I think it is- then you'd stop running away and face me like a Condor!"
    
    "Louis stops dead on his tracks, his eyes darting around the room in hopes some other Canary was in the room with him."
    
    "He sighed knowing he was the one known to keep his feathers clean and polished - he averts his gaze to the approaching Bellbird heading his way."
    
    a "Gave up running, Louis? It's about time you got here, you're late."
    
    "Aven noted obviously as Louis faces him directly."
    
    "Louis glances away as he laughed awkwardly."
    
    l "S-So much for a perfect record, huh...?"
    
    "He lets out a uncomfortable laugh."
    
    "His response was met with silence."
    
    l "My apologies, Sir...y'know how the traffic is-"
    
    jump _bellbird_interaction


label approach_the_bellbird:
    show louis happy at slightleft
    "Louis waves his wing as he walks towards the Bellbird, a smile on his face. The Bellbird notices the approaching Canary."
    
    show aven angry at tint2
    a "Louis, son, what in Phoenix's name has been holding you up? You're an hour past your clock-in time!"
    
    show louis anxious
    l "Sir Aven- I apologize, I didn't think I'd end up late from the morning traffic, the wind resistance was strong enough to clear the clouds..."
    
    "Louis expresses his dismay."
    
    jump _bellbird_interaction


label _were_you_okay_back_there:
    
    show louis normal
    l "Hey there! Are you okay? It sounds like you were having a pretty rowdy time back there?"
    
    "Louis shows his concern towards the Nightingale bird, his gaze was shifty in nature as his eyes darted from the doorway then back to Elio."
    
    "Elio puts a reassuring smile on his face, appreciative of the concern showed to him"
    
    show elio happy
    e "Thanks, friend! And I'm quite well, that's just another day for a humble baker like me!"
    
    show elio neutral
    e "Mistakes are part of the job, I say, it is what makes me more authentic!"    
    
    menu:
        "You're not wrong!":
            jump youre_not_wrong
        "True, until your customers question your safety measures...":
            jump true_until_your_customers_question_your_safety_measures


label _how_long_have_you_been_working_here:

    l "How long have you been working here?"
    
    "Louis contemplates for a moment, looking around the other buildings and boutiques, then back at the Daily Delights that was a shop shoved in a concrete wall." 
    
    show louis normal
    l "So, how long have you been working here? The bakery looks fairly new compared to the other shops around..."
    
    "Elio follows the canary's gaze, his smile grows as he recalls the older days."
    
    show elio neutral
    e "It's true, Daily Delights came a bit later compared to the rest of the buildings here, but that's cause I had to earn the money during college so I can buy this tiny old thing."
    
    "Elio smiles fondly at the memory."
    
    show elio happy
    e "Once I finally got enough funds to cover this thing, it was like a newborn chick, it was shiny, new, and everything else..."
    
    e "Daily Delight's business was booming! Now it's solidified its place among the others, but I've been here waaay later!"
    
    "Elio explains briefly, patting down his apron idly."
    
    show louis happy
    l "That sounds nice! A humble bakery with a humble beginning, a pleasant story to tell."
    
    e "You've got that right! This is my pride and joy."
    
    "Elio beams fondly of his little bakery beginnings."
    
    #jump _new_task_pastry_pieces_tutorial_task
    jump elio_questions


label youre_not_wrong:

    l "You're not wrong..."
    
    "Louis chuckles lightly at his words, a bit amused at the baker in front of him."
    
    show louis happy
    l "Well, that's a look on it. You're not wrong!"
    
    show louis normal
    l "I'm guessing this sorta thing happens often here with you?"
    
    "Elio chuckles a hearty and rumbly one from his chest."
    
    show elio neutral
    e "Unfortunately so, but it shows that I'm all making these delicious things by the wing!"
    
    show elio anxious
    e "I'm running the whole thing by myself, a sort of, one bird show, y'know? Sometimes it takes a while for everything to be in order!"
    
    show elio happy
    e "But rest assured, I've got everything under control!"
    
    "Louis nods understanding his words clearly, not doubting him but it fulfills his curiosity."
    
    show louis normal
    l "I see... isn't it difficult for you to run everything all on your own? Why not get any helpers?"

    show elio neutral    
    e "When I first opened the shop, yeah it was difficult for sure! But after a while, the bakery settled in and business became more casual and mellow, I could manage it fine!"
    
    show louis happy
    l "I'm glad you're doing well then!"
    
    show elio happy
    e "Of course! Baking has been my passion for the longest time, this job is my dream."
    
    jump elio_questions
    #jump _new_task_pastry_pieces_tutorial_task


label true_until_your_customers_question_your_safety_measures:
    
    l "True, until your customers question your safety measures..."
    
    "Louis laughs lightly, but there was a subtle hint of concern lacing in his laugh."
    
    show louis anxious
    l "Well, That's quite true, until your customers start questioning your bakery's safety measures..."
    
    "Louis smiles concerningly for him with slight furrow brow muscles."
    
    "Elio chuckles lightly, scratching the nape of his neck as he nodded in agreement."
    
    show elio happy
    e "You're not wrong! I've gotten a few concerned check-ins from the other locals, but I always assure I know what I'm doing!"
    
    show elio anxious
    e "I'm running the whole thing by myself, a sort of, one bird show, y'know? Sometimes it takes a while for everything to be in order!"
    
    show elio neutral
    "Louis' eyes widened softly, it was making sense to him. He smiled softly at his words."
    
    show louis normal
    l "I see, isn't it difficult for you to run everything all on your own? Why not get any helpers?"
    
    show elio neutral
    e "When I first opened the shop, yeah it was difficult for sure! But after a while, the bakery settled in and business became more casual and mellow, I could manage it fine!"
    
    show louis happy
    l "I'm glad you're doing well then!"

    show elio happy    
    e "Of course! Baking has been my passion for the longest time, this job is my dream."
    
    #jump _new_task_pastry_pieces_tutorial_task
    jump elio_questions


label let_me_look_around_again:
    
    jump delights_pick


label yeah_i_approached_him:

    show louis anxious
    l "Oh yeah, I approached him! It was about something important, so I didn't want to delay it."
    
    "Louis explained sheepishly as he scratched the nape of his neck with his wing."
    
    "Catcher paused for a moment, just staring at Louis before he spoke again."
    
    show catcher neutral
    c "I get it, it's good he was there for you to speak to him directly, he's usually absent overseas."

    show catcher confused
    c "What did he want with you anyways?"
    
    jump peregrine_int_continuation_1


label no_he_definitely_hunted_me_down:
    
    show louis anxious
    l "Ahh... no, he definitely hunted me down..."
    
    "Louis chuckled softly as he recalled the interaction from earlier this morning."
    
    show catcher neutral
    c "You were avoiding him? That would definitely look odd to me, and not to mention make you stand out more to him."
    
    "Louis nodded affirmatively at his words, a small smile on his face."
    
    show louis happy
    l "Well, you're not wrong! That's definitely what happened!"
    
    "Catcher paused for a moment, just staring at Louis before he spoke again."
    
    show catcher confused
    c "What did he want with you anyways?"
    
    "Catcher piqued his curiosity more with a short question."
    
    jump peregrine_int_continuation_1


label peregrine_int_continuation_1:

    "Louis laughs awkwardly, his gaze averting elsewhere as he comes up with the words to explain his situation."
    
    show louis anxious
    l "I-I had an increase of work, I wanted it to be clear, so he was just checking in with me."
    
    show louis normal
    l "I'm taking more work and duty calls from the Food and Shopping district now!"
    
    "Louis explained honestly to Catcher, seeing the Falcon only nod understandably, listening to his words thoroughly."
    
    show catcher confused
    c "What for? You're already employee of the month, are you aiming to make it the whole year-?"
    
    "Catcher jested coolly, nonchalant and casual- he wasn't too worried about Louis."
    
    show louis happy
    "Louis chuckled heartily at Catcher's jest, shaking his head lightly in disagreement."
    
    show louis normal
    l "I wish I could say it's like that... but unfortunately, no, it's for my mother."
    
    "Louis feigned a reassuring smile while he watched Catcher's eyes, somewhat feeling like the Falcon knew and saw through him."
    
    show catcher confused
    c "Mother Joan? Is she alright? Did something happen?"
    
    "Louis' brow muscled knotted subtly, there was something in Catcher's tone that caught him off guard- like it was a bit strained or struggling, with how his words fell flat at the end."
    
    "Nonetheless, Louis kept his facade up with his reassuring smiles and gestures."
    
    show louis normal
    l "Oh, She's just fallen ill, she'll be fine, the extra funds will help her recover greatly, might as well, y'know?"
    
    "Louis could see it in Catcher's eyes, the faint squint gaze at him, as if he's trying to wait for him to reveal more."
    
    "Catcher didn't say anything more, a small silence falling between them."
    
    show catcher neutral
    "........."
    "......"
    "..."
    
    "Catcher spoke up again."
    
    c "It looks like you've got it all under control then."
    
    "Catcher briefly said before changing the topic at hand."
    
    show catcher confused
    c "So, where are you off to, then?"
    
    "Louis notices Catcher's eyes dart from his gaze to the familiar bag he carried around for deliveries."
    
    show louis normal
    l "I'm just about to wrap up a delivery actually,  some pastries for aMiss Ivory."
    
    "Louis mentions his task in passing, hearing a light hum from the Falcon."
    
    show catcher confused
    c "Miss Ivory? She hasn't ordered for a while, glad to know she's alright."
    
    "Catcher commented, a small observing note for Louis."

    l "I take it you delivered to her address a lot?"
    
    show catcher anxious
    c "She was... a favorite of mine, yes."
    
    "Catcher stared at him, not really saying more or less about the topic."
    
    "Louis stood idly for a moment, clearing his throat to break the tension before speaking again- not really wanting the silence to fill the air like before."
    
    l "I see, well if that's the case, I'll make sure to tell her you said 'Hi' when I stop by, I'd best be going then..."
    
    "Louis' words trailed off at the end as he bowed in a gestured departure, Catcher doing the same as he spoke one last time."
    
    show catcher neutral
    c "That would be lovely, I'll see you around... Louis."
    
    "Louis watches as Catcher's bandaged talon was exposed to him as Louis passed him by, the Falcon's gaze lingered on the Canary bird before flying off after their interaction ended."
    
    jump _tutorial_conclusion


label is_the_change_a_good_thing:

    l "Is the change a good thing?"
    
    "Louis nodded understanding her words."
    
    show louis normal
    l "I was told my colleague, Catcher, was the one who answered frequently to your tasks."

    show louis anxious
    l "Is the change of couriers a good thing?"
    
    "Louis shifts on his talons nervously as he awaits her reply."
    
    show ivory neutral
    i "You haven't done anything wrong, no worries, I think...sometimes change is needed, y'know?" 
    
    "The mockingbird flaps her wing dismissively as she laughs softly."
    
    show ivory anxious
    i "N-Not that there was anything wrong with Catcher! He was a lovely courier." 
    
    "Ivory stammered lightly as she defended her words."
    
    show louis happy
    l "Hey- hey, don't worry! I wasn't thinking about that, I'm not getting the wrong idea!"
    
    "Louis reassured, he can see her feel reassured gradually as her smile returned."
    
    jump day_1_concluded


label im_glad_to_be_able_to_serve_you:

    "Louis nodded understanding her words."
    
    show louis happy
    l "I see, well- I'm glad to be able to serve you regardless."
    
    show louis normal
    l "Nothing happened with Catcher, if I can ask?"
    
    "Louis can see Ivory pause, thinking- contemplating on his words."
    
    show ivory anxious
    i "No-I don't believe so, he must just be busy."
    
    "Ivory smiles reassuringly to him, in which Louis returns graciously."
    
    show louis normal
    l "He does get a bit ahead of himself sometimes."
    
    show louis happy
    l "Prioritizing other stuff over the other... typical Catcher for you."
    
    "Louis listens to the mockingbird's soft chuckle. Returning the smile she gives him."
    
    show ivory happy
    i "I'm sure we'll be seeing more of each other then, Louis, was it?"
    
    "Louis nodded in affirmation."
    
    show louis happy
    l "Sure we will, Miss Ivory."
    
    jump day_1_concluded



#######################################################
#              DECISION + MECHANICS LABELS            #
#                  (With Subcategories)               #
#######################################################

################ MAP MECHANICS #################

# Map mechanic that allows players to select locations to travel.
label _tutorial_conclusion:
    
    #TUTORIAL CONCLUSION
    #The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the town street of 'Cornfield City'
    
    scene cornfield town
    show  lightoverlay

    "Louis stands idly on the main street of the town, reminded again of the task in hand as he pulls out his check-list from his pocket, marking the finished ones so far."
    
    show louis normal at tint1
    l "I better get these to Ivory's doorstep before the afternoon comes around..."
    
    "Louis noted mentally as he prepared to take flight again."
    
    #The game highlights the 'map' option, allowing the player to travel to three locations: AVES COURIER CENTER, CORNFIELD CITY (currently standing), ACORN STREET.
    #The map should highlight the 'ACORN STREET' location to guide the player where they need to be in order to finish the task.
    #The player will be transported in front of rows of tree houses - indicating local bird's houses.
    
    scene streetview
    with dissolve3

    "Louis arrives at his final destination shortly, the rows of bird houses filling his view as the familiar area is felt under his talons."
    
    "He strolled casually, his eyes peeled finding the 'red house' on the main street."
    
    show louis anxious at tint4
    
    l "It should be around here...better get these to Miss Ivory before I run out of time and she cancels on me."
    
    "The player will be able to hover their mouse and walk around the area to choose which house they will be able to go to- for this section, only the red house's door is available for access."
    
    "Louis' gaze finally finds the stood out red house on the street, strolling over with the package in hand, he stops right outside the front door of the bird house, tidying himself up before the final delivery."
    
    "Louis hovers over the door, with the prior context of Miss Ivory being Catcher's older customers, he felt a strange unease, a sort of nervousness that was familiar." 
    
    "It was the type of feeling he had felt before when he first started out his courier job, the nervousness of talking to other birds, disturbing them from their peaceful day."
    
    "Louis clears his throat to himself, before knocking loudly with a closed wing."
    
    "He waited, for a moment."
    
    "Even calling out to the bird inside."
    
    show louis happy at slightleft
    l "Miss Ivory? It's Louis, from Aves Courier! I have your delivery!"
    
    "The unease returned when there was a lack of response from the inside, so he waited."
    
    "Again."
    
    "........."
    "......"
    "..."
    
    "???" "Oh dear, I apologize, I didn't hear you over the laundry!"
    
    "The sudden opening of the door Louis stood in front of brought him immediate ease, soothing his worries gone while he wore the practiced smile for his customer."
    
    show ivory neutral at tint5
    "The Canary bird is greeted by a Blue Mockingbird, a passerine bird serene to its surroundings as she smiles warmly back to him in greeting."
    
    show louis normal at tint6
    l "It's quite alright, Miss, I was a little worried you weren't home to receive them."
    
    "Louis voices out his thoughts to her."
    
    "The pink robin flaps her wing dismissively as she laughs softly."
    
    show ivory happy at tint5
    i "No worries, I would've felt the same if I was in your talons." 
    
    show ivory happy
    i "I'm quite used to using your services, I'm pleased to be greeting a new bird on my doorstep this time."
    
    "Louis notes of her words, recalling the interaction he had with the Falcon from earlier."
    
    menu:
        "Is the change a good thing?":
            jump is_the_change_a_good_thing
        "I'm glad to be able to serve you.":
            jump im_glad_to_be_able_to_serve_you

# 2d platform view.
label _peregrine_interaction_1:

    "Louis turns away from Daily Delight Bakery with a waving wing, bidding the humble baker, Elio, a goodbye in his step, with a satisfied order-"

    "He is set to check off another box from his checklist, and that is: traveling to Ivory's doorstep in Acorn Street."
    
    "But before he can continue onto his journey, he notices a familiar Falcon in his view..."

    #The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Daily Delights Bakery, with the character 'Catcher' a few blocks away.
    #The player should be able to move 'Louis' to interact with 'Catcher'.
    
    scene acorn street
    with dissolve3
    show lightoverlay
    
    "The Peregrine Falcon watched the Canary bird with an observant gaze."
    
    "As Louis approached casually, he greeted the Falcon with a familiar chirpy gesture and tone, his movements showing that the two already knew each other prior."
    
    show louis happy at tint3
    l "Catcher! I didn't think I'd well, 'catch' you earlier at HR, where've you been?"
    
    "Louis softly chuckled at his own unexpected joke, finding it rather silly."
    
    show catcher neutral at tint2
    "Catcher had an amused look on his face with the Canary's wording, he had a light smirk plastered on his beak because of it."
    
    show catcher confused
    c "Clever. I had earlier commitments to attend to - word around, you ran into Big A, or was it more like he hunted you down?"
    
    "Catcher asked rather blunt and straightforward, something not out of his usual self."
    
    menu:
        "Yeah- I approached him!":
            jump yeah_i_approached_him
        "No, he definitely hunted me down...":
            jump no_he_definitely_hunted_me_down



label _bellbird_interaction:

    #""" Interaction Placeholder """
    # Future mechanic: This is where you'll hook up the interaction counter for Bellbird.
    # If a mini-game happens here, you can link to it with a jump or call statement later.

    show aven neutral
    a "Oh, enough of that nonsense. Get your gear on, I've got a delivery for you. It's quick and simple. I've heard news of your situation, what happened?"
    show aven questioning
    
    "Aven guides Louis back to the front of the center, a parental arm around Louis's shoulder as they walk back."
    
    "The forwardness of the question causes Louis to fall back into nervous laughter.  He clears his throat as he tries to regain his composure."
    
    show louis anxious
    l "It's not a grave situation, Sir, and thankfully so. My mother, s-she's just fallen ill is all..."
    
    "Louis' words trail off in poorly concealed uncertainty."
    
    "Aven's expression held a stoic look to it, Louis felt how much he held his superior's attention."
    
    a "You're working here instead of being with your mom, son?"
    
    "Aven asks, his question subtly laced with concern."
    
    show louis normal
    "Louis only nods in defeat."
    
    show louis anxious
    show aven thinking
    l "Someone needs to support her, right? My wife, Rory, she's already doing her best with the caretaking service but...she's taking days-off to watch over my mother."
    
    show aven questioning
    a "Ah, Aurora, of course...this job, it doesn't pay well to support bills like that. How're you holding up?"
    
    "Louis chuckles weakly, the creases shaping his face into more of a grimace than a smile."
    
    show louis happy
    l "I've taken more work from other departments. Not just delivery parcels now, I've taken food and regular errands under my wing!"
    
    "Louis' smile was small yet sincere, making Aven more concerned than he already is."
    
    show aven neutral
    a "Don't stress your body, son. There's only so much that mantle of yours can carry."
    
    "Aven pats Louis' back encouragingly, the worried look still plastered on his face."
    
    "Louis nods, a cheery laugh following, appreciating the concern."
    
    l "I'll be fine, sir, truly. I'm not your star employee for nothing, now am I?"
    
    "Aven's concerned look warps into something more reassuring in Louis' eyes, the evident smirk on his beak encouraging him more without his superior needing to say a single word."
    
    "A heartening pat on Louis' back makes him pull his weight off of the depressing thought of his situation, turning to face the Bellbird's eyes with more confidence and assurance."
    
    a "Speaking like a top dog now, that's the spirit!"
    
    a "A new delivery task should be by the front. Complete that today, and I'll add another star to your paramount on the leaderboard."
    
    "Aven tasked Louis without another sweat, the mention of his mountain of achievements makes Louis feel more reassured for today."
    
    "Leaving Louis on his own by the front of the center to tend to other matters, Aven gives Louis the dose of motivation he needed to start off his job."
    
    "Louis is faced with the printed paper in his talons, skimming through the contents of the task, he huffs his chest in ease."
       
    #proceed to pastry pieces mini-game.
    #The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Aves Courier Center.
    
    scene aves courier center
    #show lightoverlay

    voice "voice/nl9.wav"
    nl "That should be a good introduction for you to start with!"
    
    voice "voice/nl10.wav"
    nl "Now, I don't want to spoil you too much on how the game works, but here's a quick rundown:"

    voice "voice/nl11.wav"
    nl "You have your inventory on the left which you can access after dialogues, settings on your right, your task checklist at the upper left corner right beside your map, and that's... about it!"
    
    voice "voice/nl12.wav"
    nl "From this point on, I'll no longer be joining you as Narrator, but I'll be with you for the rest of the game! :D"

    #hide lightoverlay

    # Move forward in the story
    jump _new_task_pastry_pieces_tutorial_task



########## INVENTORY & QUEST MECHANICS ##########

# Includes a map mechanic where the player can select streets in Cornfield City.
# Decision-based but includes task instructions and map navigation.

# Adding on Inventory (merge items?)
label yes_that_would_be_all:
    
    show louis normal
    l "Yes, that would be all!"
    
    "Elio smiles at his words, moving quickly as he works away at the back, packing up Louis' order. It doesn't take too long before he returns."
    
    "Elio hands a paper bag to Louis, a neat packaging for the pastries"
    
    show elio neutral
    e "Here you are. Now you be safe and look after yourself, alright?"
    
    "Louis nods in reassurance, of course- not forgetting to look after himself as well."
    
    show louis happy
    l "No worries, I'll be okay, I'm taking care of myself too, thank you for these!"
    
    "Louis shook the bag in his hold lightly."
    
    "Elio smiles satisfied with another successful order."
    
    show elio happy
    e "It was a pleasure! Feel free to stop by whenever you'd like!"
    
    "Elio waves Louis goodbye as the Canary bird is set back on the path of the task in hand." 
    
    "The player's inventory should have a packaged brown paper bag that when hovered, it should read out: Ivory's Pastries."
    
    jump _peregrine_interaction_1

# Inventory + Minigames
label delights_pick:
    #The game showcases the pastry glass display in full view with Elio barely peeking at the top."
    #It shows there are four (4) hoverable choices to pick from: Plain, Glazed Donut / Chocolate Chip Muffin / A Slice of Apple Pie / A Cinnamon Bun.
    #Louis- the player, has to pick two (2) pastries to be dragged into their inventory: A Slice of Apple Pie & A Cinnamon Bun.
    #The player can choose if they are done or not with buttons that read: CONTINUE BROWSING / FINISH BROWSING.
    $ quick_menu = False
    scene daily delights pick
    with dissolve1
    call screen dailydelightspick
    $ quick_menu = True

    scene daily delights
    with dissolve1

    show elio neutral at slightright
    show louis happy at slightleft
    e "That doesn't sound healthy, are you sure you're alright managing all that work?"
    
    "Elio asks, concerned, worried for the canary's well-being."
    
    l "I'll be quite alright. I need to anyway, it's for someone special to me."
    
    "Louis smiles reassuringly as he hands his pick of pastries to Elio."
    
    show elio neutral
    e "I see... Well, will this be all, then?"
    
    "Elio takes the pasties off of Louis' hands as he reaffirms."
    
    menu:
        "Yes, that would be all.":
            jump yes_that_would_be_all
        "Let me look around again.":
            jump let_me_look_around_again


############### MINI-GAME MECHANICS ##############

# Includes a map mechanic where the player can select streets in Cornfield City.
# Decision-based but includes task instructions and map navigation.
label _new_task_pastry_pieces_tutorial_task:
    #""" New Task: Delivery Mini-game Placeholder """
    # Placeholder for the pastry delivery mini-game. In the future, you'd jump to a mini-game label here.
    # When the mechanics are ready, this will be your go-to spot.

    #show  lightoverlay

    # === Display Task Checklist ===
    
    "Louis looks to his checklist again. 'Bakery Delivery' greets him in bold, red scribbles as he reads on, taking note of the simple instructions listed."
    
    #The game opens up the Louis' checklist, reading the contents it spells out to the player exactly what is expected to be done.
    
    # === Task Instructions: Display step-by-step delivery tutorial ===

    "This is what it reads:"
    "'DELIVERY FOR IVORY'"
    "{color=#8b593c}Ivory has sent in a morning task she wishes to be fulfilled before 12:00 PM MORNING.{/color}"
    "{color=#8b593c}The task is simple enough, she just needs 2 pastry goods delivered to her doorstep since she has been craving sweets lately.{/color}"
    "{color=#8b593c}Visit 'Daily Delights' Bakery in 'Cornfield City'{/color}"
    "{color=#8b593c}Talk with the baker: 'Elio'{/color}"
    "{color=#8b593c}Pick the required pastries from Elio's Bakery{/color}"
    "{color=#8b593c}- A Slice of Apple Pie{/color}"
    "{color=#8b593c}- A Cinnamon Bun{/color}"
    "{color=#8b593c}Check-out the pastries from Elio{/color}"
    "{color=#8b593c}Leave 'Daily Delights' Bakery and go to 'Acorn Street'{/color}"
    "{color=#8b593c}Find the red house on 'Acorn Street'{/color}"
    "{color=#8b593c}Delivery the pastries to Ivory's doorstep{/color}"
    "{color=#8b593c}Mark the task as: DELIVERED{/color}"
    #The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Aves Courier Center
    #The game automatically opens the 'Map' for this section, and the player can choose to only access the town street: 'Cornfield City'
    #The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in 'Cornfield City', the player may only interact with 'Daily Delights' for this section
    #The player is then greeted by a transition cutscene that starts the Bakery Mini-game dialogue
    
    scene cornfield town
    with dissolve3
    pause 3.0
    scene daily delights
    with dissolve3
    #show lightoverlay

    "Louis steps in front of the open bakery wall-store, the letters above him on the sign reads: 'Daily Delights'."
    
    "He scans the other side of the counter but notices no one by the display. Yet the open doorway suggests someone was present- or at least had been recently."
    
    "Not being the most familiar with this bakery, Louis rings the hanging bell by the display, making a ringing 'ding!' sound that echoed throughout the store."
    
    "Louis waited patiently for the owner to arrive to greet him. Instead, something else came to welcome him..."
    
    "Light, gray smoke began pouring out of the doorway, causing a worried look to quickly dawn on Louis' face as he watches the scene, calling out to whoever may be in there."
    
    show louis normal at tint1
    l "Hello??? Does anyone there need help?"
    
    "???" "Everything is fine, YES! D-Don't worry now! I'll be with you in a second!"
    
    "The sound of clanking of metal joined the smoke billowing from the doorway, Louis' concern growing by the minute the more he waited when suddenly..."
    
    show louis normal at tint3
    show elio happy at tint2
    "???" "Dear, PHOENIX, that was a disaster now, wasn't it!"
    
    "The owner of the chirping voice belonged to a Nightingale bird, one covered in black dust and debris, as he coughed."
    
    "Noticing the Canary bird standing opposite of his pastry display, he was quick to put a welcome smile as he patted himself clean."
    
    "He leaned over the glass display as he introduced himself to Louis."
    
    e "Hey friend, sorry about that! I didn't mean to keep you waiting, I'm Elio! Welcome to Daily Delights! Or as  I like to call it: Cornfield City's humblest bakery on the wall."
    
    show elio neutral
    e "What can I help you with?"
    
    "Elio smiles  as he ties the familiar baker apron around his body , waiting for Louis to respond"
    
    jump elio_questions

label elio_questions:
    menu:
        "Were you okay back there?":
            jump _were_you_okay_back_there
        "How long have you been working here?":
            jump _how_long_have_you_been_working_here
        "Complete the delivery":
            jump _fulfill_pastry_pieces_task

# Will be called when interaction is done on 2d platforms.
label _fulfill_pastry_pieces_task:
    #show  lightoverlay

    "Louis returns the smile  as he focuses on the task at hand, amused by the Baker's display."
    
    show louis happy
    l "As much as I'd love to buy something for myself with how delicious these pastries look...I actually have a delivery I need to make."
    
    "Louis pulls up the check-list he had secured in his bag, looking through it briefly as he observes the pastries laid before him inside the glass display."
    
    show elio neutral
    e "A delivery? Are you one of those birds working in Aves Courier?"
    
    "Elio inquired curiously as he watched Louis' movements."
    
    show louis normal
    show elio happy
    l "You...can say that, yeah." 
    
    "He nods as he affirms."
    
    show louis happy
    l "I'm working for multiple departments in the Center, so you're going to be seeing me everywhere for the next few days."

    "Louis smiles towards Elio as he explained, recalling the earlier conversation he had with the Falcon."

    # === Transition to Daily Delights Scene ===
    jump delights_pick


