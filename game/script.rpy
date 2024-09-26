define l = Character('Louis')
define nl = Character ('Narrator Louis')
define a = Character('Aven')
define e = Character('Elio')
define c = Character('Catcher')
define i = Character('Ivory')
define az = Character('Aziel')
define li = Character('Lily')
define m = Character('Maverick')

default half = 1
default day = 1

image streetview = "/Backgrounds/Street View.png"
image acorn street = "/Backgrounds/Acorn Street Day Closed Doors.png"
image acorn street night = "/Backgrounds/Acorn Street Night No Houses.png"
image acorn street night houses = "/Backgrounds/Acorn Street Night.png"
image aves courier center = "/Backgrounds/Aves Courier Center.png"
image daily delights = "/Backgrounds/Daily Delights No Bread.png"

image magic trick 1 = "/magic trick/001.png"
image magic trick 2 = "/magic trick/002.png"
image magic trick 3 = "/magic trick/003.png"
image magic trick 4 = "/magic trick/004.png"
image magic trick 5 = "/magic trick/005.png"
image magic trick 6 = "/magic trick/006.png"
image magic trick 7 = "/magic trick/007.png"
image magic trick 8 = "/magic trick/008.png"
image magic trick 9 = "/magic trick/009.png"

image hospital = "/Backgrounds/hospital hall.jpg"
image basement = "/Backgrounds/basement.png"

image achievement = "/gui/AchievementBackground.png"
image achievementivory = "/gui/AchievementIvory.png"
image achievementlily = "/gui/AchievementLily.png"
image achievementaven = "/gui/AchievementAven.png"

transform slightleft:
    xalign 0.18
    yalign 1.0

transform slightright:
    xpos 852
    yalign 1.0

label start:

    stop music fadeout 2.0
    $quick_menu = False

    # jump test_parallax_vp
    # jump inventory_test
    # jump mechanism_testing

    jump start_scene

label start_scene:

    # call screen drag_and_drop_inventory

    scene tutorial 1
    with dissolve1

    voice "voice/nl1.wav"    
    nl "Welcome! This is Narrator Louis, pleasure to be guiding you in Avane Studio's first ever- {i}Canary Courier{/i}! Alpha Build- of course!"
    
    scene tutorial 2
    with dissolve1

    voice "voice/nl2.wav"
    nl "Now, to catch you up to speed if you weren't present for our forum dev logs- here's a quick rundown!"
    
    scene tutorial 3
    with dissolve1

    voice "voice/nl3.wav"
    nl "You, the player, will be controlling me- Louis, the canary bird throughout the whole game,"

    scene tutorial 4
    with dissolve1
    scene tutorial 5
    with dissolve1

    voice "voice/nl4.wav"
    nl "And in my stead- deliver and fulfill customer orders to get me that sweet 3 star rating!"

    scene tutorial 6
    with dissolve1

    voice "voice/nl5.wav"
    nl "That's the gist of it- the name of the game basically!"

    scene black
    with dissolve1

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game fades into black, booting up the 2D platform game world.{/color}"
    #############################################
    
    voice "voice/nl6.wav"
    nl "You must be wondering, now what's all this for, right?"
    voice "voice/nl7.wav"
    nl "All of this is with cause, of course, but I'll tell you that a bit later on, let's first proceed- to your first task of the day!"
    
    jump opening_sequence
    with dissolve3


label opening_sequence:

    play music "music/CC Main Story Dialogue Theme.wav" fadein 3 fadeout 3

    $quick_menu = True

    scene acorn street
    show BlackBars

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions into the 2D platform view of the world, wherein the character 'Louis' is shown inside of Aves Courier Center.{/color}"
    #############################################

    #INTRODUCTION (DAY 1)
    
    show louis happy
    with dissolve2
    l "Aves Courier Center, this is where all the magic happens..."
    
    "Louis speaks of his work fondly."
    
    "Louis enters Aves Courier Center with a big smile on his face, looking forward to whatever the day may bring..."
    
    "Wandering further into the building, a shrill voice draws his attention towards the center of the room."
    
    "All eyes on a familiar, yet still loud, Bearded Bellbird with a built-in megaphone device strapped around its neck."
    
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
    show aven angry at slightright
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
    
    show aven angry at slightright
    a "Louis, son, what in Phoenix's name has been holding you up? You're an hour past your clock-in time!"
    
    show louis anxious
    l "Sir Aven- I apologize, I didn't think I'd end up late from the morning traffic, the wind resistance was strong enough to clear the clouds..."
    
    "Louis expresses his dismay."
    
    jump _bellbird_interaction


label _bellbird_interaction:
    
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
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}///proceed to pastry pieces mini-game.///{/color}"
    "{color=#f00}///The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Aves Courier Center.///{/color}"
    #############################################
    
    scene acorn street

    voice "voice/nl8.wav"
    nl "That should be a good introduction for you to start with!"
    
    voice "voice/nl9.wav"
    nl "Now, I don't want to spoil you too much on how the game works, but here's a quick rundown:"

    voice "voice/nl10.wav"
    nl "You have your inventory on the left which you can access after dialogues, settings on your right, your task checklist at the upper left corner right beside your map, and that's... about it!"
    
    voice "voice/nl11.wav"
    nl "From this point on, I'll no longer be joining you as Narrator, but I'll be with you for the rest of the game! :D"
    
    jump _new_task_pastry_pieces_tutorial_task


label _new_task_pastry_pieces_tutorial_task:
    
    "Louis looks to his checklist again. 'Bakery Delivery' greets him in bold, red scribbles as he reads on, taking note of the simple instructions listed."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}///The game opens up the Louis' checklist, reading the contents it spells out to the player exactly what is expected to be done.///{/color}"
    "{color=#f00}DELIVERY FOR IVORY{/color}"
    "{color=#f00}Ivory has sent in a morning task she wishes to be fulfilled before ((12:00 PM MORNING)).{/color}"
    "{color=#f00}The task is simple enough, she just needs ((2 pastry goods)) delivered to her doorstep since she has been craving sweets lately.{/color}"
    "{color=#f00}Visit 'Daily Delights' Bakery in 'Cornfield City'{/color}"
    "{color=#f00}Talk with the ((baker)): 'Elio'{/color}"
    "{color=#f00}Pick the required pastries from Elio's Bakery{/color}"
    "{color=#f00}- A Slice of Apple Pie{/color}"
    "{color=#f00}- A Cinnamon Bun{/color}"
    "{color=#f00}Check-out the pastries from Elio{/color}"
    "{color=#f00}Leave 'Daily Delights' Bakery and go to 'Acorn Street'{/color}"
    "{color=#f00}Find the ((red house)) on 'Acorn Street'{/color}"
    "{color=#f00}Delivery the pastries to Ivory's doorstep{/color}"
    "{color=#f00}Mark the task as: ((DELIVERED)){/color}"
    "{color=#f00}///The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Aves Courier Center///{/color}"
    "{color=#f00}///The game automatically opens the 'Map' for this section, and the player can choose to only access the town street: 'Cornfield City'///{/color}"
    "{color=#f00}///The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in 'Cornfield City', the player may only interact with 'Daily Delights' for this section///{/color}"
    "{color=#f00}///The player is then greeted by a transition cutscene that starts the Bakery Mini-game dialogue///{/color}"
    #END FUNCTIONALITY
    ############################################# 
    
    scene acorn street

    "Louis steps in front of the open bakery wall-store, the letters above him on the sign reads: 'Daily Delights'."
    
    "He scans the other side of the counter but notices no one by the display. Yet the open doorway suggests someone was present- or at least had been recently."
    
    "Not being the most familiar with this bakery, Louis rings the hanging bell by the display, making a ringing 'ding!' sound that echoed throughout the store."
    
    "Louis waited patiently for the owner to arrive to greet him. Instead, something else came to welcome him..."
    
    "Light, gray smoke began pouring out of the doorway, causing a worried look to quickly dawn on Louis' face as he watches the scene, calling out to whoever may be in there."
    
    show louis normal at center
    l "Hello??? Does anyone there need help?"
    
    "???" "Everything is fine, YES! D-Don't worry now! I'll be with you in a second!"
    
    "The sound of clanking of metal joined the smoke billowing from the doorway, Louis' concern growing by the minute the more he waited when suddenly..."
    
    show louis normal at slightleft
    show elio happy at slightright
    "???" "Dear, PHOENIX, that was a disaster now, wasn't it!"
    
    "The owner of the chirping voice belonged to a Nightingale bird, one covered in black dust and debris, as he coughed."
    
    "Noticing the Canary bird standing opposite of his pastry display, he was quick to put a welcome smile as he patted himself clean."
    
    "He leaned over the glass display as he introduced himself to Louis."
    
    e "Hey friend, sorry about that! I didn't mean to keep you waiting, I'm Elio! Welcome to Daily Delights! Or as  I like to call it: Cornfield City's humblest bakery on the wall."
    
    show elio neutral
    e "What can I help you with?"
    
    "Elio smiles  as he ties the familiar baker apron around his body , waiting for Louis to respond"
    
    menu:
        "FULFILL 'PASTRY PIECES' TASK":
            jump _fulfill_pastry_pieces_task
        "Were you okay back there?":
            jump _were_you_okay_back_there
        "How long have you been working here?":
            jump _how_long_have_you_been_working_here

label _fulfill_pastry_pieces_task:
    
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
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game showcases the pastry glass display in full view with Elio barely peaking at the top."
    "{color=#f00}It shows there are four (4) hoverable choices to pick from: Plain, Glazed Donut / Chocolate Chip Muffin / A Slice of Apple Pie / A Cinnamon Bun."
    "{color=#f00}Louis- the player, has to pick two (2) pastries to be dragged into their inventory: A Slice of Apple Pie & A Cinnamon Bun."
    "{color=#f00}The player can choose if they are done or not with buttons that read: CONTINUE BROWSING / FINISH BROWSING."
    #############################################
    
    show elio neutral
    e "That doesn't sound healthy, are you sure you're alright managing all that work?"
    
    "Elio asks, concerned, worried for the canary's well-being."
    
    show louis happy
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
    
    jump _new_task_pastry_pieces_tutorial_task


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
    
    jump _new_task_pastry_pieces_tutorial_task


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
    
    jump _new_task_pastry_pieces_tutorial_task


label yes_that_would_be_all:

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}///The game proceeds with the dialogue if the player chooses: (Yes that would be all.) option.///{/color}"
    #############################################
    
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


label let_me_look_around_again:

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game goes back to the pastry selection screen if the player chooses the: (Let me look around again.) option.{/color}"
    "{color=#f00}These two options will come up again for the second time once the player is finished browsing.{/color}"
    #############################################
    
    jump _fulfill_pastry_pieces_task


label _peregrine_interaction_1:

    "Louis turns away from Daily Delight Bakery with a waving wing, bidding the humble baker, Elio, a goodbye in his step, with a satisfied order-"

    "He is set to check off another box from his checklist, and that is: traveling to Ivory's doorstep in Acorn Street."
    
    "But before he can continue onto his journey, he notices a familiar Falcon in his view..."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Daily Delights Bakery, with the character 'Catcher' a few blocks away.{/color}"
    "{color=#f00}The player should be able to move 'Louis' to interact with 'Catcher'.{/color}"
    #############################################
    
    scene acorn street
    
    "The Peregrine Falcon watched the Canary bird with an observant gaze."
    
    "As Louis approached casually, he greeted the Falcon with a familiar chirpy gesture and tone, his movements showing that the two already knew each other prior."
    
    show louis happy at slightleft
    l "Catcher! I didn't think I'd well, 'catch' you earlier at HR, where've you been?"
    
    "Louis softly chuckled at his own unexpected joke, finding it rather silly."
    
    show catcher neutral at slightright
    "Catcher had an amused look on his face with the Canary's wording, he had a light smirk plastered on his beak because of it."
    
    show catcher confused
    c "Clever. I had earlier commitments to attend to - word around, you ran into Big A, or was it more like he hunted you down?"
    
    "Catcher asked rather blunt and straightforward, something not out of his usual self."
    
    menu:
        "Yeah- I approached him!":
            jump yeah_i_approached_him
        "No, he definitely hunted me down...":
            jump no_he_definitely_hunted_me_down

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
    
    "........."
    "......"
    "..."
    
    "Catcher spoke up again."
    
    show catcher neutral
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

label _tutorial_conclusion:
    
    #TUTORIAL CONCLUSION
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the town street of 'Cornfield City'.{/color}"
    #############################################
    
    scene acorn street

    "Louis stands idly on the main street of the town, reminded again of the task in hand as he pulls out his check-list from his pocket, marking the finished ones so far."
    
    show louis normal
    l "I better get these to Ivory's doorstep before the afternoon comes around..."
    
    "Louis noted mentally as he prepared to take flight again."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game highlights the 'map' option, allowing the player to travel to three locations: AVES COURIER CENTER, CORNFIELD CITY (currently standing), ACORN STREET.{/color}"
    "{color=#f00}The map should highlight the 'ACORN STREET' location to guide the player where they need to be in order to finish the task.{/color}"
    "{color=#f00}The player will be transported in front of rows of tree houses - indicating local bird's houses.{/color}"
    #############################################
    
    scene streetview 

    "Louis arrives at his final destination shortly, the rows of bird houses filling his view as the familiar area is felt under his talons."
    
    "He strolled casually, his eyes peeled finding the 'red house' on the main street."
    
    show louis anxious
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
    
    show ivory neutral at slightright
    "The Canary bird is greeted by a Blue Mockingbird, a passerine bird serene to its surroundings as she smiles warmly back to him in greeting."
    
    show louis normal
    l "It's quite alright, Miss, I was a little worried you weren't home to receive them."
    
    "Louis voices out his thoughts to her."
    
    "The pink robin flaps her wing dismissively as she laughs softly."
    
    show ivory happy
    i "No worries, I would've felt the same if I was in your talons." 
    
    show ivory happy
    i "I'm quite used to using your services, I'm pleased to be greeting a new bird on my doorstep this time."
    
    "Louis notes of her words, recalling the interaction he had with the Falcon from earlier."
    
    menu:
        "Is the change a good thing?":
            jump is_the_change_a_good_thing
        "I'm glad to be able to serve you.":
            jump im_glad_to_be_able_to_serve_you


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

label day_1_concluded:
    
    scene achievement
    with dissolve3
    show achievementivory at truecenter
    with zoomin

    $ renpy.pause(3.0)
    
    #DAY 1 CONCLUDED
    scene hospital
    with dissolve3

    stop music fadeout 2.0
    
    "Louis finds himself perched comfortably right next to the sleeping figure that inhabits the room he currently resides in."
    
    "Humming a light tune to himself as he settles his courier bag off to the side, focusing on the subject that reaps all of his hard work at the moment."
    
    "Louis holds a fond look as he gazes briefly onto the patient who is nestled quietly in their slumber."
    
    show louis happy
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
    
    "Before he has a chance to leave- he is stopped promptly by a soft yet stern call of his name, he turns around, faced with a bird much larger than he is."
    
    "???" "Mister Louis? Is that you I see there?"

    show louis normal at slightleft
    show aziel neutral at slightright
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
    hide aziel neutral
    
    "Safely returning to the comforts of his home, and ending the day off with a successful delivery- and an interesting day with new faces."

    scene black
    with dissolve3
    $ day = 2

    jump day_2


label day_2:

    play music "music/CC Main Story Dialogue Theme.wav" fadein 3 fadeout 3

    scene aves courier center
    with dissolve3

    show louis normal at slightleft
    show aven neutral at slightright
    
    "Louis finds himself trailing behind his boss, Aven, once again before the day starts- but in contrast to being in Aves Courier Center..."

    "They are in the surroundings of stacks of different boxes in size, weight and color alongside bags of envelopes filed to different places with unique contents of writing inside, he presumes."
    
    "Louis stands idly as Aven is busy rummaging through Aves Courier's own section of mails catered for the center's tasks and duties."
    
    show aven questioning
    "The Canary bird glances around the place, observing until the bellbird speaks."
    
    a "You can look around if you want, the thing I'm finding ain't in any of these boxes...I'm gonna be a while."

    show aven thinking
    "Aven exits from Louis' view, leaving him standing in the room on his own."
    
    hide aven thinking
    hide louis normal
    "Louis hums in thought, being left to his own devices- he might as well explore what the room has to offer for a bit."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The 'Cornfield Mail Post' background will have some interactable items to note: 'A Newspaper Bulletin Board', 'A Stack of Boxes at the far end right', and some 'Mail scattered on the ground.'{/color}"
    "{color=#f00}The character 'Louis' will be able to move around this room, and the player may hover over items that should highlight the interactable items.{/color}"

    menu:
        "A Newspaper Bulletin Board":
            jump _a_newspaper_bulletin_board
        "A Stack of Boxes":
            jump _a_stack_of_boxes
        "A Letter Mail Scattered on the Floor":
            jump _a_letter_mail_scattered_on_the_floor
    #############################################    


label _a_newspaper_bulletin_board:
    
    "Louis finds himself standing a wide bulletin board. As he stares at the newspaper clippings attached on the corkboard, he picks up an old newspaper that catches his eye in particular."
    
    "The newspaper held with curiosity in his wings as he read on quietly to himself, his eyes widening at the words of the headline that read:"
    
    "BEN, AN 11 YEAR OLD CHICK PUT DXWN IN AVIAN CARE HOSPITAL"
    
    "The headline covered mostly the paper with layers of text, what caught Louis' eye mostly was the rectangular drawn picture that took up most of the space next to the contents of the newspaper."
    
    # SHOW PICTURE

    "It showed the drawing of a young mockingbird chick, or from the looks of what he could observe."

    "There was a part of him that made him recall seeing familiar patterns before, but he didn't want to assume- what if the dots he was connecting turned out to be wrong?"
    
    "Trying to find more context, the headline description itself didn't give him much, if it wasn't ripped off, it was covered with black ink that was entirely illegible to his eyes."
    "There were a few things he's sure of upon reading, however..."
    
    "Was that this mockingbird passed early, mysteriously so- in the hands of the local hospital where his mother resides in, if that wasn't in the tiniest bit concerning then he wasn't sure what is."
    
    "Not wanting to let his thoughts run south even more, he places the newspaper clipping to where he found it, leaving it be."
    
    jump _bellbirds_suspicion


label _a_stack_of_boxes:
    
    "Louis stands near a stack boxed that seemed to be addressed directly to Aves Courier Center specifically-"

    "But there his eyes catches the opposite, picking up the rectangular box on the top of the stack, he immediately recognizes the names tagged on the box as it reads:"
    
    "TO: AZIEL, FROM: AVEN"
    
    "His brow muscles knot together as his curiosity piques, there was a bit of scratching damage on the box itself, but it wasn't enough for him to see entirely what it was inside..."
    
    "Until he started feeling guilty."
    
    "Louis wasn't one to pry so much more, look through the personal belongings of others unless he was explicitly told so that he was allowed, killing the part that made him wonder-"
    
    "He puts the box back at the top of the stack, leaving it be there without another thought of it."
    
    jump _bellbirds_suspicion


label _a_letter_mail_scattered_on_the_floor:
    
    "Louis walked briefly before looking down as his talon felt the texture change from the usual concrete to a rustling sound, upon realizing he was standing on multiple, scattered envelopes-"
    
    "He stepped back to not wrinkle more of the mail."
    
    "He picks up a particularly worn out envelope compared to the rest, seeing as it was addressed to Aven, his boss, specifically coming from Avian Care Hospital."
    
    "As he opened the letter curiously, the familiar doctor came to his view as the letter came from Doctor Aziel. He piqued a bit as he read out a bit of the contents of the letter:"
    
    "To Aven,\nAves Courier Center"
    
    "While I hope this letter finds you in good health, this is an urgent warning to whoever this letter may cross, Aven or not,  there has been a new patient placed under my wing, an alarming one at that."
    
    "If his records are true, then he will be under my strict guidance-"
    
    "Louis stopped reading before he becomes anymore intrusive than he already has been, glancing at the letter one last time-"
    
    "-We must have this conversation once you're free, Aven. I fear this situation concerns not only me, but you as well. Meet with me when you can."
    
    "Best, Aziel.\nAvian Care Hospital"
    
    "Louis hurriedly places the paper letter back to the envelope where it came from, from the sudden growing nervousness his wing shook and accidentally dropped the mail he held."
    
    "Stepping back as he tried to recollect his composure, he wasn't sure how recent that letter was, but he wasn't supposed to be seeing it."

    "While it'll be hard to erase the contents of that letter from his memory, he was best not touching anything else before it cost him."
    
    jump _bellbirds_suspicion


label _bellbirds_suspicion:
    
    "At the sound of Aven's boisterous voice, Louis jolts, startled at the sudden loud sound before he eases up again once he hears his boss' booming laughter."
    
    "Aven subtly raises a brow at Louis' rather jittery movements, slinging a wing around his shoulders, the bellbird spoke to him with concern in his voice."
    
    show aven questioning at slightright
    a "You alright, son? Anything happen while I was gone?"
    
    "Aven asks Louis with a slight furrow on his brow muscle as his attention was trained on the Canary."
    
    menu:
        "ADMIT THE TRUTH":
            jump admit_the_truth
        "DENY ANYTHING'S WRONG":
            jump deny_anythings_wrong


label admit_the_truth:
    
    "Louis shuttles around his talons for a brief moment of silence dawning between him and the awaiting bellbird."
    
    "He breathes in, before exhaling as Louis turns to face Aven directly into his gaze, the strong stare sending a bit of nervous jitters down to his tail."
    
    show louis anxious at slightleft 
    l "I think I saw some things I wasn't supposed to see..."
    
    "Louis smiles awkwardly as he rubs the nape of his neck with his wing, averting his gaze."
    
    "Aven stares at him with a tilted head."
    
    show aven questioning
    a "And what exactly did you see-?"
    
    "Louis feels Aven probe at him as he asked, he could feel the bellbird's intense gaze at him."
    
    jump the_truth


label deny_anythings_wrong:
    
    "Louis stands still as his eyes meet Aven's head-on, being like that for a moment."
    
    "Before he breaks away the stare first."
    
    "Louis shakes his head promptly, almost insistently."
    
    show louis anxious at slightleft
    l "I-I just knocked over some stuff-"
    
    "Louis' laughs come out a bit loud- an awkward edge to it as his laughs trails off with a sudden stop."
    
    "Louis could feel the bellbird's stare at him, as if his gaze was chipping away at his demeanor, seeing through his lies and into the truth within his soul."
    
    "Louis felt less sure about himself."
    
    "Louis clears his throat, muttering an apology under his beak."
    
    "Aven squints his eyes at Louis, his suspicion growing under Louis' unusual behavior."
    
    show aven neutral
    a "Nobody's gonna burn you alive if you tell the truth, son."
    
    "Louis could feel Aven's reassuring wing on his shoulder, glancing up at him- meeting his gaze, the bellbird's smile reassuringly."
    
    "He was telling Louis 'it's okay, I'm not gonna get mad.' from his gaze alone."
    
    menu:
        "THE TRUTH":
            jump the_truth
        "DENY DENY DENY":
            jump deny_deny_deny


label the_truth:
    
    show louis scared
    show aven questioning
    l "It's... stuff addressed to you, I just skimmed over it by accident- curiosity killed the cat, and all that...I-I'm sorry, sir."
    
    "Louis' evident stammer betrays his cool and calm act as his anxiousness was basically radiating off of him."
    
    "Louis can hear the bellbird's hearty laugh, and with that- he feels himself being a bit more at ease despite the guilt and anxiety eating at him."
    
    show aven thinking
    a "Whatever it was you saw, son- I've either seen it already or somebody else saw it, stuff in this room has been here for ages."
    
    a "They recently moved more of the recent stuff to the room next door- so relax, ain't no cat is gonna go biting your tongue for a little curiosity."
    
    show aven neutral
    a "Being curious is normal."
    
    "Louis feels the reassuring pat on his back as Aven speaks."
    
    show louis anxious
    l "I-I see- still, sir- it was wrong of me-"
    
    show aven neutral
    a "You say sorry too much, Louis. And for what? Giving in to your natural bird instincts?"
    
    "Aven scolds Louis with a light tone to his voice."
    
    show aven thinking
    a "It's fine, really, who knows? What you know might help you in the future."
    
    "Aven winks before giving Louis another reassuring pat on the back before detaching from him."
    
    "Louis wears a thankful smile as he bows curtly, seeing Aven return the bow as he snickered lightly at him, motioning his head towards the exit, he follows after the bellbird."
    
    jump day_2_continuation


label deny_deny_deny:
    
    "Louis stays still and silent for a moment."
    
    "He lightly shrugs off Aven's hold on him with an apologetic smile- masked to be reaffirming."
    
    show louis anxious
    l "I-It's fine, sir- it was really just that."
    
    "Louis persists, repeating his words of certainty to Aven."
    
    "Aven continues to watch him, like a hawk to a prey as it clicks to him-"
    
    "Louis lies to him, insistently."
    
    "Louis shifts on his talons once a while, uncomfortable with the growing tension despite the lack of words said."
    
    "Louis dares meet Aven's gaze again-"
    
    "Eyes that were already boring back at him, without a sight of a blink."
    
    show aven thinking
    a "...if that's your truth, Louis."
    
    "Louis winces lightly at the change of tone, the sound of his name."
    
    "Aven reaches his hold on Louis again, almost dragging him on his feet when he ushers him out."


label day_2_continuation:
    
    show aven neutral
    a "I won't keep you too long, son, I know you've got deliveries to tend to, now off you go."
    
    "Aven says as he prepares to send Louis off, handing him the familiar paper checklist midway."
    
    "Louis graciously accepts the checklist, glancing at it briefly- he realized it would be his task for today."
    
    show louis normal
    l "Thank you, sir, I should be one call away whenever you need me again."
    
    "Louis returns Aven's bow as they both part ways."
    
    "Louis ends off the short visit and interaction as he flies off to start his new task."
    
    jump _new_task_shopping_spree_


label _new_task_shopping_spree_:
    
    hide louis normal
    hide aven neutral
    "Louis opens the folded checklist, reading the big writing scribbled in red that says 'Grocery Errands' looking back at him."
    
    "He takes note of what's listed, simple instructions he knows he'll be able to follow through."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game opens up the Louis' checklist, reading the contents it spells out to the player exactly what is expected to be done.{/color}"
    "{color=#f00}DELIVERY FOR LILY{/color}"
    "{color=#f00}Lily has sent in an evening task she wishes to be fulfilled before '6:00 PM EVENING'{/color}"
    "{color=#f00}The task- though plenty, is pretty simple enough, she just needs '5 supermarket items' delivered to her doorstep, baking ingredients for the cake she'll be making before her roommate, Sierra, return home.{/color}"
    "{color=#f00}* Visit 'Flyway Superstore' Supermarket in 'Cornfield City'{/color}"
    "{color=#f00}* Pick the required grocery items from the Supermarket:{/color}"
    "{color=#f00}    * A Dozen of Eggs{/color}"
    "{color=#f00}    * A Pack of Sugar{/color}"
    "{color=#f00}    * A Pack of Flour{/color}"
    "{color=#f00}    * A Berry Branch{/color}"
    "{color=#f00}    * Two (2) Cartons of Milk{/color}"
    "{color=#f00}* Talk with the 'cashier': 'Ivory'{/color}"
    "{color=#f00}* Check-out the pastries from Ivory{/color}"
    "{color=#f00}* Leave 'Flyway Superstore' Supermarket and go to 'Acorn Street'{/color}"
    "{color=#f00}* Find the 'blue  house'  on 'Acorn Street'{/color}"
    "{color=#f00}* Deliver the groceries to Lily's doorstep{/color}"
    "{color=#f00}* Mark the task as: 'DELIVERED'{/color}"
    "{color=#f00}The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Cornfield Mail Post{/color}"
    "{color=#f00}The game automatically opens the 'Map' for this section, and the player can choose to only access the town street: 'Cornfield City'{/color}"
    "{color=#f00}The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in 'Cornfield City',{/color}"
    "{color=#f00}the player may interact with the character 'Catcher' or go straight to 'Flyway Superstore' for this section{/color}"
    #############################################
    
    scene acorn street
    
    menu:
        "PEREGRINE INTERACTION 2":
            jump peregrine_interaction_2
        "FLYWAY SUPERSTORE":
            jump flyway_superstore

label peregrine_interaction_2:
    
    show louis happy at slightleft

    "Louis finds himself in the sight of the familiar Falcon once again, this time- he does not hesitate to approach."
    
    "He calls out to him,"
    l "Catcher!"
    
    "Waving his wing to catch his attention as he walked towards him, the usual bright smile plastered on his beak as he faces Catcher's permanent scowl."
    
    "Catcher bows to Louis in greeting, tilting his head at his chirpy attitude."
    
    show catcher confused at slightright
    c "You look way too smiley to see me."
    
    show catcher neutral
    c "You did something."
    
    "Louis' smile gradually falls as the Falcon easily sees through his exterior."
    
    show catcher confused
    c "What is it?"
    
    "Louis sighs lightly with a passing laugh, awkwardly playing with the ends of his wings' feathers together."
    
    show louis anxious
    l "Just another run with the big boss- we stopped by the office's main parcel room today."
    
    "Louis almost missed Catcher's tail perking up subtly at the corner of his eye."
    
    show catcher confused
    c "Oh yeah?"
    
    "Louis watches as Catcher briefly recomposed himself, feeling all of the Falcon's attention on him."
    
    c "Must've seen something if you're telling me as soon as you leave the post office, hmm?"
    
    "Louis laughs at his words, unsure if he really is an open book- or was it that he's worked with Catcher so long he saw through his resolve?"
    
    show louis anxious
    l "I guess you can say that..."
    
    menu:
        "MENTION WHAT YOU SAW":
            jump mention_what_you_saw
        "SAY NOTHING":
            jump say_nothing


label flyway_superstore:

    #scene supermarket
    scene streetview
    
    "Louis finds himself inside the all familiar sign of the supermarket that read: 'Flyway Superstore' wherein he gets his own deal of supplies for daily living himself, pushing past the other birds in his way."
    
    "He took out his checklist again, scanning his eyes over the items he needed to collect for the task at hand."
    
    "Louis easily browsed through the 'general goods' section of the rows of shelves, each aisle containing different items."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game showcases a packed grocery shelf aisle in full view- it shows there are four (5) hoverable choices to pick from:{/color}"
    "{color=#f00}An Egg Tray / A Carton of Milk / A Bag of Sugar / A Bag of Flour / A Branch of Berries.{/color}"
    "{color=#f00}Louis- the player, has to pick two (6) grocery items to be dragged into their inventory: (1) An Egg Tray / (2) A Carton of Milk / (1) A Bag of Sugar / (1) A Bag of Flour / (1) A Branch of Berries.{/color}"
    "{color=#f00}The player can choose if they are done or not with buttons that read: CONTINUE BROWSING / FINISH BROWSING.{/color}"
    #############################################
    
    "Louis hums satisfied as he begins to walk towards the cashier after getting all the stuff he needed to get for his customer."
    
    show louis normal
    l "This should be all Miss Lily needs..."
    
    "Louis rummages through the items, double-checking just in case he missed anything-"
    
    "A chirping call catches the attention of the Canary, his gaze landing on the familiar mockingbird from the day before."
    
    show louis normal at slightleft
    show ivory happy at slightright
    i "Louis! It's so good to see you again!"
    
    "As Louis approached the cashier, placing down the goods he was tasked to get towards the mockingbird, he bowed in greeting- as Ivory gracefully returned."
    
    show louis happy
    l "Miss Ivory! I was not expecting you- you work here then?"
    
    "Louis observed as the mockingbird nodded in affirmation."
    
    i "Yes! You stand corrected, I'm here working  if I'm not at home, resting."
    
    "Ivory chirps happily as Louis nods in understanding."
    
    show louis normal
    l "I see, well it's always nice for a small chat on the job."
    
    "Louis smiles as he hands over the items he needs checked out."
    
    show ivory neutral
    i "You've got a lot here today, seems your customer's got a big cake planned."
    
    l "It would appear so, have you ever baked before, Miss Ivory?"
    
    "Louis inquired as he watched the mockingbird scan the items one by one."
    
    "Ivory nods, a small smile on her face as she recalls."
    
    show ivory happy
    i "I used to do it a lot when I was much younger, my younger sibling loved cinnamon rolls."
    
    "Louis watched as the mockingbird smiled under her beak as she continued with her work."
    
    "He could feel the fondness just from the way she spoke of the passing memory."
    
    show louis happy
    l "Now I'm feeling bad I got that bread from you."
    
    "Louis chuckles as he remembers her gift, Ivory shook her head dismissively with a light giggle."
    
    show ivory neutral
    i "I gave it to you, Louis, it's a gift from me to you."
    
    show louis normal
    l "I know, I know- you know what I mean..."
    
    "Louis received the newly packaged bag of groceries from Ivory as she placed the receipt in with a clap of her wings, satisfied with her neat work."
    
    show ivory happy
    i "That should be all of it!"
    
    "Louis hums as he nods."
    
    show louis happy
    l "Thank you, Miss Ivory, I'll make sure to give your cinnamon roll back, if you don't want it then for your sibling, at least?"
    
    show louis normal
    "Louis offered adamantly, the Canary watched as Ivory's gaze lingered on him."
    
    "Ivory smiles wistfully as she only nodded."
    
    show ivory anxious
    i "It'd be very unlady-like of me to refuse a gift, either way."
    
    show ivory neutral
    i "But alright, Louis, for my sibling, I will accept it."
    
    "Despite Ivory's obvious smile, Louis can faintly hear the somber undertone laced in her voice."
    
    "He curiously wondered the cause, but chose to feign ignorance, as he nodded."
    
    "Louis bowed in farewell as he collected the grocery bag into his wings, searching for something in Ivory's eyes- unsure what it was, maybe reassurance? Is what he was looking to get."
    
    "Ivory returned Louis' bow, curt and graceful with that customer service smile."
    
    show ivory neutral
    i "I'll see you around, Louis."
    
    "And with a smile- Louis exits 'Flyway Superstore' with the packaged items held from his wings and into his bag."
    
    jump _lily_task_conclusion

label mention_what_you_saw:
    
    "Louis thinks for a moment, recalling the information he got from the post office visit."
    
    show louis anxious
    l "Well, I saw an old newspaper clipping of some- old mockingbird chick being put down in the hospital."
    
    "Louis shudders lightly, knowing it's the same hospital his mother is in."
    
    show louis scared
    l "A bit concerning to me, for obvious reasons."
    
    "Catcher nods at his words understandably."
    
    show louis anxious
    l "And letters addressed to our boss, Aven, from Doctor Aziel- from the local hospital."
    
    "Catcher's brow muscle raises in interest, almost leaning in closer to listen to Louis."
    
    show louis anxious
    l "Something about a... peculiar patient- but I can't say for sure."
    
    "........."
    "......"
    "..."
    
    "The Falcon's continued silence keeps the Canary talking."
    
    show louis normal
    l "-One thing for sure, our boss and that local doctor... they know each other past default pleasantries."
    
    show louis anxious
    l "Something tells me they've worked with or for each other before, though I don't assume much- I chose not to see the entire thing."
    
    
    "Louis feels Catcher's watchful gaze on him, but he knows- the Falcon knows better than to probe."
    
    show catcher neutral
    c "I see."
    
    "Catcher only comments, staring at Louis- his eyes are unreadable."
    
    "Louis keeps Catcher's gaze, waiting if he was going to say something else or not."
    
    "........."
    "......"
    "..."
    
    show catcher angry
    pause 0.1
    show catcher neutral
    c "Your curiosity wanders to places it shouldn't."
    
    "Louis feels the growing tension break with Catcher's fleeing chuckle."
    
    show catcher neutral
    c "You didn't need to tell me, but I appreciate it."
    
    "Louis feels Catcher's firm pat on his back."
    
    "There was an unusual kinship when it came to Catcher in Louis' eyes, strangely he could trust him- but felt threatened by him at the same time."
    
    "It was a confusing understanding between them, but Louis never crossed the boundary of Catcher's comfort-and the Falcon did the same for him."
    
    jump _peregrine_int_2_conclusion


label say_nothing:
    
    "Louis stays quiet, debating whether he should tell the Falcon of what he saw or not. Looking at his own talons- he avoided Catcher's gaze before he met his eyes again."
    
    "Louis shrugs nonchalantly, a bit better at hiding his expression compared to last time."
    
    show louis normal
    l "Regular errands for the big boss, same thing- same old."
    
    "Louis' eyes held no notable expression in particular, that- was something Catcher relied on to read through him."
    
    show louis anxious
    "Louis kept Catcher's gaze, following even the slightest change in his gaze, mimicry in a way."
    
    "........."
    "......"
    "..."
    
    "Catcher took a step towards him, a comfortable distance- yet an alarming stance, staring down at Louis against the bright sunlight."
    
    show catcher neutral
    c "I see."
    
    show catcher confused
    "Catcher's eyes linger..."
    
    "Before he averts his gaze."
    
    show catcher neutral
    c "...Whatever helps you sleep soundlessly, my friend."
    
    "Louis feels Catcher's firm pat on his back, but his hold lingers- like a squeeze on his shoulder, but it left before he could ponder more."
    
    c "You need to start telling that guy to lay off of you, it's the second time."
    
    "Louis feels Catcher's watchful gaze on him, but he knows- the Falcon knows better than to probe."
    
    jump _peregrine_int_2_conclusion


label _peregrine_int_2_conclusion:
    
    "Catcher glances at the folded paper Louis carried in his wing, motioning his head at it, he assumed openly."
    
    show catcher confused
    c "That, your new task?"
    
    "Louis follows where the Falcon was looking at."
    
    "He nodded in confirmation."
    
    show louis normal
    l "Just a simple grocery errand, baking ingredients for Miss Lily."
    
    "Louis explained briefly as Catcher hummed in acknowledgement."
    
    show catcher neutral
    c "You best get to it then- I know how dearly baking is to her roommate, Sierra."
    
    "Catcher's knowing comment makes Louis curious all over again."  
    
    show louis happy
    l "Something tells me you're what other birds tell me you are."
    
    "There was a teasing tone there mixed with Louis' curious undertone."
    
    "Catcher's brow muscle raises as he looks at the shorter Canary at him."
    
    show catcher confused
    c "And what exactly have other avians been whispering to your ear?"
    
    "Catcher matched Louis' tone with ease, invoking equal amounts of intrigue himself."
    
    "Catcher was an enigma, there were times Louis was definitely confused with his peculiar behavior, and there were times- it sounded and felt like he had you wrapped around his talon."
    
    "Louis chuckles lightly, he liked a bit of banter before he was back at work, and Catcher- albeit rare, provided him that when it was relevant."
    
    l "You're one of the oldest employees, you're being lowkey on purpose, now, aren't you?"
    
    "Louis sees the small smirk on Catcher's beak, before it morphed into a subtle grin."
    
    show catcher neutral
    c "Can't be stealing your thunder now, can I?"
    
    "The Falcon jests."
    
    c "I just prefer... brooding in my own shadow, you can say."
    
    "The Canary laughs, the sound of earnest joy that makes the Falcon pause."
    
    l "Please- never say it that way again!"
    
    "Catcher only smiles at his words, before he straightens his posture."
    
    "Louis watches as the Falcon bows to him, in farewell- returning the bow, he knows the conversation has come to an end."
    
    "Catcher's eyes were something that Louis could never read no matter how long he looked, trying to dig into that sea of darkness was something he didn't push."

    c "I'll get going."
    
    "Catcher prepares his wings as he looked back at Louis"

    c "You shouldn't let me keep you so long,"
    
    "A warning."
    
    "........."
    "......"
    "..."
    
    c "I know how to waste time."
    
    hide catcher neutral
    "Those were the last words Louis heard from the Falcon before he watched him fly off."
    
    "Louis watches Catcher's retreating figure exit his view as their conversation ponders for a moment in his mind, he thought, What a strange fowl."
    
    "He prepares to leave himself, continuing on his agenda and finishing the task at hand."
    
    jump flyway_superstore


label _lily_task_conclusion:

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the town street of 'Cornfield City'{/color}"
    #############################################
    
    "Louis finds himself on the main street of the city again, huffing lightly with the heavy items he carried in his bag, he opens his map again to see where he should be headed."
    
    show louis normal
    l "If I get these early to Miss Lily, I should be able to have time to roam around before it gets too dark..."
    
    "Louis noted mentally as he prepared to take flight again."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game highlights the 'map' option, allowing the player to travel to three locations: AVES COURIER CENTER, CORNFIELD CITY (currently standing), ACORN STREET.{/color}"
    "{color=#f00}The player will be transported in front of rows of tree houses - indicating local bird's houses.{/color}"
    #############################################
    
    scene acorn street

    "As Louis arrives at his destination, the familiar- warm sunlit Acorn street, he glances briefly at his checklist just to make sure he knows which house he has to go to."
    
    "Pocketing the paper again, he kept his eyes peeled as the sun set behind him, his eyes landing on the 'blue  house' on the main street."
    
    "But before he continues- something else catches his eyes, just at the end of the road, by the white house- a figure stands idle."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The player will be able to hover their mouse and walk around the area to choose which house they will be able to go to-{/color}"
    "{color=#f00}for this section, they may choose to access the blue house or the strange figure.{/color}"
    "{color=#f00}The player will be transported in front of rows of tree houses - indicating local bird's houses.{/color}"
    #############################################
    
    menu:
        "INVESTIGATE THE FIGURE":
            jump investigate_the_figure
        "DELIVER TO LILY":
            jump deliver_to_lily


label investigate_the_figure:

    "Louis approached the figure cautiously, unsure of what to expect but he always had the curious spirit in him that told him what he shouldn't be doing." 
    
    "Yet he proceeded anyway, the figure came more into view as he walked."
    
    show louis normal at slightleft
    l "Hello?"
    
    "Louis' voice came off more of a whisper, peeking at his side as if his body lingered just in case anything happened."
    
    show crow default at slightright
    "The figure craned its neck at him, upon closer look- now he can see it properly."
    
    "A Carrion Crow stood staring at him."
    
    "The milky white gaze boring into his, like the moon was staring back at him."
    
    "Louis coughs as he shifts unnervingly on his talons, turning away until- it spoke to him."
    
    "???" "Where are you going? We haven't finished playing?"
    
    "Louis stops dead in his tracks as he turns to look again."
    
    "The crow tilts its head at him, confusingly as it takes a quick step towards him."
    
    l "O-Oh! W-We were? My-My apologies..."
    
    "A part of Louis thought to himself, was this an evil spirit his mother spoke of? He had never interacted with them before, an unfamiliar face so to say- but then again he's assuming again."
    
    "The Crow smiles at Louis."
    
    "Louis' eyes widened softly- it wasn't the sort of smile he'd expect to receive."
    
    "Even though the Crow's stare and exterior was cold and soulless, its smile carried a hint of warmth just from the creases it showed on its face."
    
    "Louis' brow muscle furrows as he returns the smile."
    
    show louis anxious
    l "I apologize- that must've been rather rude of me to leave so sudden."
    
    show louis normal
    l "Where were we?"
    
    "Louis' attention is fully trained on the Crow that stood before him, despite him being a bit taller, they strangely met eye to eye."
    
    "The Crow chirps, the sound is shallow and empty, but happily nonetheless."
    
    scene white
    show magic trick 1

    "???" "I was just showing you a magic trick, friend!"
    
    show magic trick 2
    
    "The Crow spins around on its talons as Louis watches, it did this a few times before it stopped, facing him once again."
    
    show magic trick 3

    "It huffs his chest as it closes its eyes, its chest bubbling up- ridiculously big."
    
    show magic trick 4

    "Louis takes a step back instinctively, his naturally cautious being acting ahead of him, but he watches on to cater his curiosity."
    
    show magic trick 5

    "The Crow opened its eyes as it looked down on the Canary."
    
    "???" "Ready?"
    
    "Louis nods, despite his cautionary stance, he lets it proceed."

    show magic trick 6
    
    "The Crow smiles as it continues, its chest bubbling up like a hot air balloon on an open summer day- casting a shadow before Louis as its size grew."
    
    show magic trick 7

    "And before Louis knew it- the bubbled up chest exploded, from his beak came a rainfall of stars and fireworks."
    
    "Like a magic trick."

    show magic trick 8
    
    "Louis watches the sky in awe as a whimsical shower of colors dawns onto him."

    show magic trick 9
    
    "Louis looks back at the Crow that admired its handiwork, its stare blank but its smile big and proud."
    
    scene acorn street
    with dissolve3
    
    show louis normal at slightleft
    show crow default at slightright
    l "So you're like... some sort of magician?"
    
    "Louis asks bluntly while the Crow finally meets his gaze, its look lost and confused."
    
    "Louis takes the silence as fact as he applauds with his wings softly."
    
    show louis normal
    l "It's really impressive, I'll give you that! B-But-"
    
    show louis anxious
    l "I'll have to leave for now, we can- uh- continue later..."
    
    show louis scared
    l "...Okay?"
    
    "The Crow stares back at Louis, a silence that should have come off as unnerving- was surprisingly quaint and at ease."
    
    "The Crow eventually responds- with a small smile and a tilt of its head as it leaned forward, playfully nodding at the Canary."
    
    "???" "Will you bring a snack next time? Oh- I love sweets, can you please get me a cinnamon roll?"
    
    "The Crow requests, Louis stands still on his talons, staring."
    
    show louis anxious
    l "O-Of course, see you-..."
    hide louis anxious
    
    "The Canary leaves promptly- hurriedly on his talons, as if something in him clicks; an understanding he had not connected the dots before."
    
    #############################################
    #FUNCTIONALITY HERE - Ale (me) can take care of this
    "{color=#f00}The 'INVESTIGATE THE FIGURE' option approach will still be available if the player chooses the 'DELIVER TO LILY' interaction first, the only difference?{/color}"
    "{color=#f00}'Louis' won't be able to mention it to Lily and have extra dialogue accessed.{/color}"
    #############################################
    
    menu:
        "LILY TASK CONCLUSION":
            jump _lily_task_conclusion
        "DELIVER TO LILY":
            jump deliver_to_lily
        "DELIVER TO LILY 0.1":
            jump _deliver_to_lily_01

label deliver_to_lily:
    menu:
        "DELIVER TO LILY 0.1":
            jump _deliver_to_lily_01
        "DELIVER TO LILY 0.2":
            jump _deliver_to_lily_02

label _deliver_to_lily_01:
    
    scene acorn street
    with dissolve3

    "Louis recollects himself first before continuing, after that interaction with the Crow- he needed a moment to breath and refocus."
    
    "Standing at the front door of the blue house, Louis raised his wing and knocked, softly at the wood."
    
    "Louis waited for a moment."
    
    "Until he heard light shuffling coming from the inside, and soon... the door opened."
    
    "The Canary is greeted by a beautiful shade of blue, a Lovebird specifically a Cerulean Budgie, who welcomes him with a loving smile."
    
    "???" "Ah, you must be the courier I've been expecting?"
    
    show lily happy at slightright
    "The budgie extends a wing in which Louis happily takes with a firm graze."
    
    show louis normal at slightleft
    l "Yes! That would be me, I'll assume you are Miss Lily, then?"
    
    show louis happy
    l "My name's Louis, Miss."
    
    "Lily smiles gracefully with a nod, acknowledging his presence."
    
    li "That is indeed me, it's a pleasure to meet the bird behind my worries."
    
    "Louis chuckled softly as he played silently with the feathers of his wings."
    
    show louis happy
    l "Just your typical delivery-boy, Miss, your delivery should..."
    
    show louis normal
    
    "Louis rummages through his bag before pulling out the familiar paper bag filled with the grocery items Lily has tasked Louis with."
    
    show louis happy
    l "...be right here!"
    
    "Louis hands over the paper bag towards Lily, holding it by the bottom to make sure it doesn't fall."
    
    "Lily takes the bag into her wings carefully, she inspects quietly- digging through the contents before smiling at the Canary."
    
    li "Wonderful!"
    
    show lily neutral
    li "This should be everything I needed, thank you, dear."
    
    "Louis watches as Lily sets the bag elsewhere for now."
    
    li "The ingredients, it's for my roommate, Sierra."
    
    show lily anxious
    li "Her grandmother's late passing anniversary is coming up, so we're preparing her favorite treats before Sierra leaves and visits her family on the weekend."
    
    "Louis hums at the new information, his interest piquing at the thought."
    
    show louis normal
    l "If I can ask- a sort of tradition? Within your species?"
    
    "Lily giggles softly before nodding."
    
    show lily happy
    li "I guess you can say that."
    
    "Louis ponders for a moment, as his gaze shifts from where he once was- the figure at the end of the street, he turns to the budgie again."
    
    show louis normal
    l "I'll have to get going now, but can I ask you something before I do?"
    
    "Lily's brow muscle raises as she holds her wings close to herself, listening, waiting for the Canary to continue."
    
    show louis anxious
    l "Are you...familiar with a Crow around here? One that does magic tricks in particular..."
    
    "Lily's eyes widened, not out of shock or surprise - but a certain excitement twinkling in her eyes."
    
    show lily confused
    li "A Crow? Now, dear, what did it look like?"
    
    "Lily asks softly. Louis could feel the budgie's focus trained on him."
    
    show louis anxious
    l "Well- it- he was crying, but I'd figure it was just face paint..."
    
    "Louis rambles rather unsurely."
    
    "Louis watches as Lily thought quietly to herself, a light humming from her beak as she kept her gaze at him before trailing off towards outside."
    
    show lily neutral
    li "There's a saying from the past... you look pretty young so you probably weren't told."
    
    "Lily started as her eyes met the Canary's again."
    
    li "That when a bird passes and continues to the afterlife, the gates of death strip them of who they are, only letting them remember their memories, not a name- nor a face."
    
    "Louis listens to her words intently, a thoughtful furrow between his eyes."
    
    li "They become Crows of all sorts, Louis, a murder of them as souls constantly pass through those gates of death everyday."
    
    show lily happy
    li "Sierra always says her grandmother is this...frail, weak magpie, interesting stuff..."
    
    "Louis' eyes kept the strong gaze Lily bore into his, he kept quiet- pondering, lost in his thoughts."
    
    "........."
    "......"
    "..." 
    
    l "Interesting, yes..."
    
    "Louis bows curtly, as his smile returns."
    
    "Louis watches as Lily briefly exists from view, before returning with a bouquet of flowers in her wings, holding it securely close to her chest."
    
    show lily happy
    li "That should answer your thirst for knowledge for a while!"
    
    "Lily hands the bouquet to Louis, even as he takes it from her wings into his, confusion was written all over his face."
    
    show lily neutral
    li "Consider it as a thank you, dear- of course, what I say could just be mythos and superstition-"
    
    "Lily rambles as she talks about it happily, a clear interest for her."
    
    show lily happy
    li "But my, isn't it fascinating."
    
    "Louis smiles at her words, nodding slowly- sort of agreeing."
    
    show louis scared
    l "Well, you're not wrong, it definitely serves food for thought."
    
    "Louis laughs shortly, it definitely fascinated him to an extent."
    
    show louis anxious
    l "I'll keep your words true, in my mind."
    
    show louis normal
    l "Thank you, for these lovely flowers."
    
    "Louis smiles at Lily, in which she returns ever so gracefully."
    
    show lily happy
    li "Thank you as well, Louis- be safe on your way back."
    
    "Louis bows in farewell as Lily bows in return out of respect, with a satisfied smile; Louis leaves Lily's doorstep, the shutting of the door behind him ending their interaction."
    
    jump day_2_concluded

label _deliver_to_lily_02:
    
    #############################################
    #FUNCTIONALITY HERE - Ale (me) can take care of this
    "{color=#f00}This is the written segment wherein IF the player DID NOT choose to do the 'INVESTIGATE THE FIGURE' option before the 'DELIVER TO LILY' option{/color}"
    #############################################
    
    "Louis recollects himself first before continuing, after that interaction with the Crow- he needed a moment to breath and refocus."
    
    "Standing at the front door of the blue house, Louis raised his wing and knocked, softly at the wood."
    
    "Louis waited for a moment."
    
    "Until he heard light shuffling coming from the inside, and soon... the door opened."
    
    "The Canary is greeted by a beautiful shade of blue, a Lovebird specifically a Cerulean Budgie, who welcomes him with a loving smile."
    
    show lily neutral
    "???" "Ah, you must be the courier I've been expecting?"
    
    "The budgie extends a wing in which Louis happily takes with a firm graze."
    
    show louis normal
    l "Yes! That would be me- I'll assume you are Miss Lily, then?"
    
    show louis happy
    l "My name's Louis, miss."
    
    "Lily smiles gracefully with a nod, acknowledging his presence."
    
    show lily happy
    li "That is indeed me, it's a pleasure to meet the bird behind my worries."
    
    "Louis chuckled softly as he played silently with the feathers of his wings."
    
    show louis normal
    l "Just your typical delivery-boy, Miss, your delivery should..."
    
    "Louis rummages through his bag before pulling out the familiar paper bag filled with the grocery items Lily has tasked Louis with."
    
    show louis happy
    l "...be right here!"
    
    "Louis hands over the paper bag towards Lily, holding it by the bottom to make sure it doesn't fall."
    
    "Lily takes the bag into her wings carefully, she inspects quietly- digging through the contents before smiling at the Canary."
    
    li "Wonderful!"
    
    show lily neutral
    li "This should be everything I needed- thank you, dear."
    
    "Louis watches as Lily sets the bag elsewhere for now."
    
    li "The ingredients, it's for my roommate, Sierra."
    
    show lily anxious
    li "Her grandmother's late passing anniversary is coming up, so we're preparing her favorite treats before Sierra leaves and visits her family on the weekend."
    
    "Louis hums at the new information, his interest piquing at the thought."
    
    show louis normal
    l "If I can ask, a sort of tradition? Within your species?"
    
    "Lily giggles softly before nodding."
    
    show lily happy
    li "I guess you can say that."
    
    "Louis ponders for a moment, as his gaze shifts from where he once was- the figure at the end of the street, he turns to the budgie again."
    
    show louis anxious
    l "I'll have to get going now if we're done here."
    
    "Louis smiles as he waits for Lily's response."
    
    "Louis watches as Lily briefly exists from view, before returning with a bouquet of flowers in her wings, holding it securely close to her chest."
    
    "Lily hands the bouquet to Louis, even as he takes it from her wings into his, confusion was written all over his face."
    
    li "Consider it as a thank you, dear."
    
    "Louis smiles at her gift, quite fond  of his customer's rewards."
    
    show louis happy
    l "Thank you- for these lovely flowers."
    
    "Louis smiles at Lily, in which she returns ever so gracefully."
    
    show lily neutral
    li "Thank you as well, Louis- be safe on your way back."
    
    "Louis bows in farewell as Lily bows in return out of respect, with a satisfied smile; Louis leaves Lily's doorstep, the shutting of the door behind him ending their interaction."
    
    jump day_2_concluded


label day_2_concluded:

    scene achievement
    with dissolve3
    show achievementlily at truecenter
    with zoomin

    $ renpy.pause(3.0)
    
    #DAY 1 CONCLUDED
    scene hospital
    with dissolve3

    stop music fadeout 2.0

    #DAY 2 CONCLUDED
    
    "The scene of the game opens up in the 'Aven's Care Hospital' room where it is overseeing the background, only the character 'Louis' will be present for this section."
    
    "Louis finds himself in familiar surroundings once again, the sort of artificial smell that he can't tell if it's good or not for his body- feels his lungs."
    
    "As the Canary stays perched on the side of his resting loved-one, reading out to them as a sort of way to keep the liveliness, well, alive despite the silence and tranquility."
    
    show louis normal
    l "Oh, this part is good."
    
    "Louis scoots over, showing his resting mother the book he's reading out to her."
    
    show louis happy
    l "Hear this one, 'I would recognize you in total darkness, were you mute and I deaf- I would recognize you in another lifetime entirely-'"
    
    show louis anxious
    l "'I would search for you until the very last star in the sky burnt out of oblivion...', such a good one liner for a tragic... tale."
    
    "Louis smiles somberly at the thought, glancing at the sleeping figure with a fond look."
    
    "The Canary closes the book on the chapter he last read on, placing it back into his bag filled with wonders as his attention is back on the resting figure."
    
    "Louis thought that the cold, plain white room was a bit unsettling to him, originally- he was going to bring the flowers back to his wife; but his mother's patient room could use a bit more color."
    
    "Especially when both him and his white treat the hospital as their second home ever since his mother fell ill."
    
    show louis normal
    l "I bought you a gift again, consider it...something from your son and your daughter-in-law."
    
    "Louis smiles as he gently places the bouquet of flowers into the pot now that he had previously cleared the withering roses from before."
    
    show louis happy
    l "These are...sweet peas, now that I'm looking at it!"
    
    "Louis chirps up happily upon realization."
    
    show louis normal at slightleft
    l "While it's not the colors you would've wanted...it's still your favorite."
    
    "Louis goes to perch beside the sleeping figure once again, idling about with a light sway until he hears the door to the room open."
    
    show aziel confused at slightright
    az "Sir Louis?"
    
    "Louis turns around to meet the Owl's eyes, a hint of surprise but not unwelcome."
    
    show louis happy
    l "Dr. Aziel! I-I wasn't expecting you, sir-"
    
    "Louis raised up to his talons to greet the unsuspected doctor's visit. As the two briefly linked up, exchanging a passing shake of their wings in greeting."
    
    show aziel think
    az "Don't worry, Louis, I'm only here to do routine check-ups."
    
    "Louis watches as the Owl strides past him, tending to his mother's dextrose and noting down his observations on a clipboard silently."
    
    show louis normal
    l "N-Nothing out of ordinary, I suppose?"
    
    "Louis stiffens momentarily as the Owl turns around to face him."
    
    "Seeing Aziel shake his head in dismissal was enough to ease the Canary again, with a small sigh of relief, he smiled under his beak."
    
    az "I'm sure I'll be able to give you news soon, for now... why don't you go rest and check-in back tomorrow."
    
    show aziel neutral
    "The Owl takes a good look at Louis, a slight knit of his brows as his expression is laced with worry."
    
    az "You're working hard, you should go back to your wife and take that much needed rest, hm?"
    
    "Louis could see the worried look of the Owl as he spoke to him, while the Canary debated for a moment...he settled it with an understanding nod."
    
    show louis normal
    l "You're right... I still have work tomorrow, but it helps being here before the day ends."
    
    "Aziel sees the Canary's weak smile, the Owl's knowing smile as he nodded at Louis' words."
    
    show aziel think
    az "I'm sure it does, for you especially."
    
    show aziel neutral
    az "I'll take care of your mother from here, go home, son."
    
    "The words of familiarity and kinship is something Louis never fails to hear, to be surrounded by good birds who've done nothing but good for him was something..."
    
    "........."
    "......"
    "..."
    
    "He was going to remember for a very long time."
    
    show louis anxious
    l "I'll see you again tomorrow, Doc."
    
    show louis normal
    "Louis' smile held a vulnerability to it, one in which the owl returns just as genuine."
    
    "With that, Louis leaves the hospital, flying off back to the silent sanctuary of his home to end the day."
    
    scene black
    with dissolve3

    $ day = 3
    jump day_3


label day_3:

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions into the 2D platform view of the world, wherein the character 'Louis' is shown inside of  Aves Courier Center{/color}"
    #############################################
    
    play music "music/CC Main Story Dialogue Theme.wav" fadein 3 fadeout 3

    scene acorn street
    with dissolve3
    
    "Louis is perched quietly at the side next to the wall, away from the rest of the bustling birds of Aves Courier Center, no... he was waiting."
    
    #Okay game time # I do not know what this means (ale)
    
    "While he waited, his eyes observed- he was used to working with all of this."
    
    "The morning chaos with all the avians flapping their wings around, getting into routine. It was quite...warm, to say the least."
    
    "Louis was fond of all the flocks of colors the birds gave the morning; it gave him the burst of energy to get him through the day."
    
    show aven neutral at slightright
    a "Louis! Son! There you are."
    
    "The booming sound of the bearded bellbird's voice rang through the room, sounding the alarm of every bird's attention on the Canary bird."
    
    "Louis laughs awkwardly at the amount of eyes on him, regardless- he clears his throat, the familiar smile on his beak as he meets his boss."
    
    show louis anxious at slightleft
    l "Sir Aven! I'm here early, just as you asked."
    
    "Louis could feel the bellbird's wing around his shoulder as Aven approached."
    
    show aven thinking
    a "As I know my top employee would, come, boy, I've got a special task just for you."

    show aven neutral    
    "Despite the chaos, the bellbird could comb through the flocks of colors that flew past him and Louis' sight, birds parting for their boss to make way out of his feathers."
    
    "The game fades in the inside of 'Cornfield Mail Post' with the character 'Louis' right next to 'Aven' the NPC."
    
    jump _new_task_caught_on_camera_finale


label _new_task_caught_on_camera_finale:
    
    #NEW TASK: CAUGHT ON CAMERA (Finale)
    
    "Louis watches his boss shuffle around the room, the bellbird grumbling under his breath as the Canary watches curiously at the side."
    
    "Then he finds it-"
    
    "A box among the sea of parcels mixed in between- a box, something Louis knows he's seen before."
    
    show aven neutral
    a "Folks around here keep misplacing this lil thing everytime I go here!"
    
    "The bellbird balances himself on his talons before approaching Louis with the box in his wing."
    
    show aven thinking
    a "Here, son."
    
    "Louis receives the box from Aven, the Canary tilts his head curiously at the sight of it once again, but now the wrapped was gone-"
    
    "Signs of it being opened, he assumes by the bellbird himself."
    
    show aven neutral
    a "Open it."
    
    "Louis opened the box without hesitation, untying the knot before he was greeted with what seems to be... a broken video recorder?"
    
    show louis scared
    l "Sir?"
    
    "Louis' voice held confusion with what he was holding in his wings as he searched the bellbird's face for an explanation."
    
    show aven neutral
    a "I know, I know. Listen, I can't say too much since it's confidential information."
    
    show aven thinking
    a "But I am entrusting this task to you as my most trusted employee, I know you're gonna get the job done."
    
    show aven neutral
    "Louis nodded as he listened to Aven's words, the fact of the matter was understandable to him enough-"
    
    "But he had a question that lingered at the back of his mind, unexpectedly so."
    
    show louis anxious
    l "These sorts of tasks, Sir- doesn't Catcher take care of them? I mean, this thing..."
    
    "Louis shakes the box lightly so as to not damage the contents more."
    
    show louis anxious
    l "It's pretty much broken, no doubt- I thought he'd be more fitting to handle this as he's assigned to more hands-on tasks like this."
    
    "Louis' probes as he knew this sort of 'fixer-upper' thing was out of his scope for the job."
    
    "Aven, surprisingly to Louis- hummed and nodded in agreement- though he didn't really expect to hear what comes out of the bellbird next-"
    
    show aven angry
    a "That's right, but son, the Falcon's not you, now is he?"

    show aven neutral
    "Louis stood on his talons for a moment, unsure on what to say but he started to nod slowly at his words."
    
    show louis normal
    l "I-I suppose you're right..."
    
    "Now, Louis wasn't the type to bad mouth any bird- even if his mind assumed sometimes out of his own curiosity, but something tells him there was more than what he's led to believe."
    
    show aven thinking
    a "Catcher's a good worker, don't get me wrong- but he's a strange fella."
    
    "Aven commented as he looked down on the Canary."
    
    show aven neutral
    a "You're more... reliable, to say it simply. Just for this task specifically."
    
    "Louis feels Aven's beckoning pat on his back."
    
    "Being guided towards the exit, the Canary looked at the bellbird again when he was instructed what he needed to do."
    
    show aven neutral
    a "The task is simple, son, go to my pal: Maverick in hardware, help him get that fixed, report back to me when it's as good as new."
    
    "Louis nodded affirmatively with those words."
    
    show louis normal
    l "Sounds simple enough, yes."
    
    show aven thinking
    a "Good."
    
    "The bellbird goes back to what he was doing, searching through the mail and parcels addressed to Aves Courier Center, looking at Louis with one last thing."
    
    show aven neutral
    a "Right, I just need it by today, that thing's tricky to fix I'd think, so take all the time you two will need."
    
    "With that out of the way, the bellbird shoos Louis away with his wing, rummaging through the cardboard boxes stacked on top of each other."
    
    "Louis only bows in goodbye with that, knowing he won't be acknowledged any longer- he turns to leave, setting to fly off towards the city again."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game opens up the Louis' checklist, reading the contents it spells out to the player exactly what is expected to be done.{/color}"
    "{color=#f00}DELIVERY FOR AVEN{/color}"
    "{color=#f00}Aven has assigned a very special task just for Louis to complete, while for this task-{/color}"
    "{color=#f00}there is no time requirement to fulfill, he is tasked to help out 'Maverick' from the 'Feathered Fixer' Hardware to restore 'one (1) broken video recorder' back to it's new and working state.{/color}"
    "{color=#f00}* Visit 'Feathered Fixer' Hardware in 'Cornfield City'{/color}"
    "{color=#f00}* Talk with 'the repairman': 'Maverick'{/color}"
    "{color=#f00}* Fix the 'broken video recorder' with Maverick{/color}"
    "{color=#f00}* Check-out the 'fixed video recorder' from Maverick{/color}"
    "{color=#f00}* Leave 'Feathered Fixer' Hardware and go to 'Aves Courier Center'{/color}"
    "{color=#f00}* Find 'Aven'{/color}"
    "{color=#f00}* Deliver the fixed video recorder back to Aven{/color}"
    "{color=#f00}* Mark the task as: 'DELIVERED'{/color}"
    #############################################
    
    jump _the_fix_the_recorder


label _the_fix_the_recorder:
    
    #THE FIX THE RECORDER
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game automatically opens the 'Map' for this section, and the player can choose to only access the town street: 'Cornfield City'{/color}"
    "{color=#f00}The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) 'Feathered Fixer' Hardware in 'Cornfield City'.{/color}"
    #############################################
    
    scene acorn street

    "Louis' eyes gazes offer the familiar pavement he finds himself standing on almost everyday on his job."
    
    "For once, the Falcon he's grown accustomed to chatting with before he started his task was nowhere in sight." 
    
    "While it felt odd for Louis, he didn't dwell on it much. Focusing more on the task at hand instead."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The player may only interact with 'Feathered Fixer' Hardware for this section{/color}"
    #############################################

    #THE SMOKING EAGLE
    
    "Louis enters the Feathered Fixer Hardware with the box of the broken recorder in his wing, glancing around the store, searching for someone who might be named Maverick."
    
    show louis normal at slightleft
    l "...Hello?"
    
    "Louis calls out softly under his beak, pensively approaching on his talons as he approaches the counter."
    
    "The faint sight of fleeing smoke grabs the Canary's attention."
    
    "Louis thought to himself, is this another 'overbaked' situation?, approaching the counter before leaning forward, proving himself wrong in his assumptions."
    
    "The Canary watches as a Bald Eagle is perched asleep, his head resting against the counter as a lit cigarette huffs lightly under his beak."
    
    "Louis shifts on his talons, unsure how to approach the situation."
    
    "Louis clears his throat softly."
    
    "........."
    "......"
    "..."
    
    "No response."
    
    "Louis clears his throat again, loudly and firmly this time-"
    
    "???" "WHO GOES THERE-?!"
    
    "The sudden movement of the Eagle, standing on his talons and flapping his big, brown wings defensively made Louis step back a few with a startling stance."

    show maverick neutral at slightright
    "He was faced with a bird twice his size."
    
    show louis normal
    l "S-Sir!"
    
    show louis anxious
    l "Please calm down, I'm here to fulfill a task!"
    
    "Louis feels a shiver down his back from the Eagle's strong gaze on him."
    
    show louis anxious
    l "F-From my boss, Aven, Sir!"
    
    "Louis presents the box with the broken recorder inside, sliding it on top of the counter hurryingly."
    
    "The Eagle watches the Canary's movements, settling his wings to his side as he inspected with his right, seeing eye."
    
    "The white hazing cloud that consumes the Eagle's left eye sends Louis a shiver down his spine."
    
    "???" "'Ya sure Aven sent you?"
    
    "The Eagle asks, huffing out a large amount of smoke out of the cigar he keeps in his mouth."
    
    "Louis nods swiftly, the light jitter of his beak makes his nervousness known to the Eagle."
    
    "The Eagle observes."
    
    "........."
    "......"
    "..."
    
    "Before he speaks again."
    
    m "Call me, Maverick..."
    
    "Maverick's gaze on the canary lingers, observing Louis openly."
    
    show maverick smile
    m "...little tweety."
    
    "Louis can't help but feel his brow muscle raise at the nickname(?)"
    
    "The Eagle inhales, the crackling light from the cigarette burning bright before it dims as Maverick speaks."
    
    show maverick neutral
    m "I got a word from 'ya old man, you need this piece of junk fixed, right?"
    
    "Taking the box in his wing, the Eagle inspects the contents inside."
    
    "Clicking his tongue as he lifted the video recorder up from the box, the broken pieces of the video recorder quickly made him displeased."
    
    "Louis nodded as he leaned against the counter, inspecting the video recorder alongside the Eagle."
    
    show louis normal
    l "Not completely hopeless...right?"
    
    "Louis asked as he fidgeted with the ends of his feathers."
    
    "Maverick shook his head firmly."
    
    show maverick neutral
    m "All this junk needs is some replacement with newer parts, a bit of a clean-up and a quick test run."
    
    show maverick smile
    m "And you, kid, are gonna help me with it."
    
    "The eagle hums as he spares no time, stepping back from his counter as he grunts, pulling up the make-shift table connected to the counter top."
    
    "Maverick lays the broken video recorder on the table top, turning around as he flaps his wings, reaching for the necessary tools he'd need to fix the video recorder like it's brand new."
    
    "He lays the tools in front of him and Louis,"
    
    "separating the broken parts of the video recorder, putting them to the side and pulling out a box of equipment, finding a new substitute to replace the broken pieces."
    
    show louis anxious
    l "This... is a lot of stuff."
    
    "Louis awes with all the equipment laid before him."
    
    m "You're watchin' a professional at work, kid."
    
    "Louis sees a light smirk on the Eagle's beak."
    
    show maverick neutral
    m "You don't gotta do much, kid."
    
    m "Just do what you're told, hand me what I need, and pay attention."
    
    "Louis nods understandable, the instructions clear and simple enough."
    
    jump _patch_it_up


label _patch_it_up:
    
    #PATCH IT UP
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game will now guide the player on how the parts of the video recorder will be fixed, the following choices below will dictate what part is added onto the video recorder,{/color}"
    "{color=#f00}the mechanic will mostly be drag and drop.{/color}"
    "{color=#f00}Use the anatomy of the video recorder file hardware_camera_separated.png and hardware_camera_broken.png{/color}"
    #############################################

    "With the broken video recorder set flat on the table, all wings were on deck as both Louis and Maverick oversaw the on-going operation."
    
    "The Eagle picks up the video recorder, inspecting the front before removing the broken camera lenses."
    
    show maverick smile
    m "Alright, kid. You'll just help me disassemble the parts and I can handle the rest of the heavy work."
    
    "The Eagle instructs Louis bluntly."
    
    show maverick neutral
    m "I need you to hand me that screw driver."
    
    "The player should drag and drop the 'screwdriver' item to Maverick, in which he will remove the main camera lenses from the video recorder's anatomy."
    
    "Louis hands the tiny screwdriver to Maverick."
    
    m "I should have some spare parts that should match whatever...this thing has."
    
    "The Eagle commented as he started unscrewing the screws of the video recorder's lenses."
    
    "Louis watches the Eagle at work, finding it hard to believe that the Eagle's rough exterior to be working on a task that needed delicate feathers."
    
    "The Canary feels the urge to ask him something, just to satisfy his curiosity, plus, the small talk helps fill up the silence."
    
    jump _you_look_like_youve_been_doing_this_for_a_long_time


label _you_look_like_youve_been_doing_this_for_a_long_time:
    
    "Louis continues to watch Maverick tinker at work, careful with how he handles the already broken-up video recorder." 
    
    "The Canary clears his throat, making the Eagle glance up at him."
    
    show louis normal
    l "You...You look like you've been doing this for a long time."
    
    "Louis initiates, choosing his words carefully."
    
    show maverick confused
    "The eagle nods at his words, focusing on his wings."
    
    show maverick neutral
    m "I had prior medical trainin' when I was still in the army."
    
    show maverick smile
    m "Fixing up broken objects ain't so different from patchin' up a few wounded birdies."
    
    "The eagle says simply, his wing turning to Louis."
    
    "Louis watches as the whole structure the camera lens is attached to pops out from the video recorder."
    
    show maverick neutral
    m "Wrench."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The player should drag and drop the 'wrench' item to Maverick, in which he will continue to remove from the video recorder's anatomy.{/color}"
    "{color=#f00}The previous item should return to where it was previously dragged from.{/color}"
    #############################################
    
    "Louis hands the wrench to Maverick."
    
    show louis happy
    l "Why not go into healthcare then? Rather than just work on-"
    
    "Louis eyes the surroundings while the Eagle tinkered away."
    
    show louis normal
    l "-fixing other bird's old junk?"
    
    show maverick neutral
    m "I'd rather hear the nonsensical dilly dallies of the local town folk 'round here than..."
    
    "Maverick looks at Louis as his cigarette huffs light smoke."
    
    show maverick angry
    m "Whining, painful whining."
    
    "The display panel follows as Maverick removes the careful screw that was attached to the camera lens' structure."
    
    "Louis notices as the Eagle inspects the separated items, tugging onto the interior as the loose wiring hangs idle from the video recorder."
    
    show maverick smile
    m "Look at this old thing."
    
    "The Eagle shows Louis the microphone, with one light shake- it also snaps in half completely, exposing the wire in the middle."
    
    show maverick neutral
    m "Give me a toothpick and that glue, this thing you ought to fix quickly."
    
    "The player should drag and drop the 'toothpick' and 'tube glue' item to Maverick, in which he will continue to remove from the video recorder's anatomy."
    
    "The previous item should return to where it was previously dragged from."
    
    "Louis continues to watch as the Eagle takes the tube glue and begins to  meticulously put glue on the tip of the toothpick he had previously handed over."
    
    show louis normal
    show maverick confused
    l "So the hardware thing was your idea, then?"
    
    "Louis curiously asks."
    
    show maverick smile
    m "Funnily enough, no."
    
    "The eagle answers with a short snicker."
    
    "Maverick set aside the patched up microphone and dragged the interior wires out, inspecting it with a light hum."
    
    show maverick neutral
    m "This one should be an easy fix."
    
    "The Eagle continues with the glue on the toothpick, applying it to fix the open wiring of the video recorder."
    
    show maverick neutral
    m "Aven actually helped me set-up this whole junk up."
    
    "Maverick motions around the hardware store with his free wing."
    
    show maverick smile
    m "It's close by to everything, and that bird... breaks a lot more than you'd know."
    
    "Maverick hums as he's finished fixing all the necessary parts individually, turning to Louis as a huff of smoke comes from his cigarette again."
    
    show maverick neutral
    m "Now kid, all you gotta do is re-assemble the parts, and it should be good to go."
    
    "The Eagle turns the parts to Louis expectantly."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The player is presented with the individually 'fixed' parts of the broken video recorder, the game will guide the player which part goes where first by highlighting{/color}"
    "{color=#f00}(either by simple glow or circled)  the individual parts lightly.{/color}"
    "{color=#f00}Use the anatomy of the video recorder file hardware_camera_separated.png{/color}"
    "{color=#f00}In the order of application: the camera lens structure is the main foundation.{/color}"
    "{color=#f00}The player must first connect the microphone handle to the microphone, then the player will be able to connect the microphone to the camera lens.{/color}"
    "{color=#f00}Afterwards, the player should connect the display panel to the camera lens body, then connect the last two 'red' and 'green' wires to finish.{/color}"
    #############################################
    
    show maverick smile
    m "Good work kid, now give it to me and I'll do some final touches."
    
    "The player should drag and drop the assembled video recorder to 'Maverick'."
    
    "The Eagle hums pleasingly, standing up from the previously perched off spot behind the counter and heading towards the back, exiting Louis' view."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game showcases the hardware store without the table, putting the counter/cashier background back in view.{/color}"
    #############################################
    
    "The Eagle comes back with the video recorder in his wing."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}Use the art of the video recorder file hardware_camera_final_fix{/color}"
    #############################################
    
    show maverick smile
    m "Here you go kid."
    
    "Maverick places the fixed video recorder into Louis' wings, he didn't touch any of the cracked parts as he said:"
    
    m "the thing is too old to find spare parts that matched that model exactly."
    
    "So most of the model was still, quite broken with the exception it can still power-up with batteries it requires."
    
    "The Canary inspects the video recorder in his wing, watching the display panel booth up as he pushes the power button to open it."
    
    show louis happy
    l "Wow!"
    
    l "It's still rough looking, but it works!"
    
    "Louis chirps happily at the Eagle, keeping the video recorder secured in his wings."
    
    "The Eagle nods knowingly, polishing his wings with a clean rag, removing the spilled oil that got in his feathers as he looks at the Canary."
    
    show maverick smile
    m "Of course it works, I fixed it."
    
    show maverick neutral
    "The Eagle says as a matter of fact, arrogance lacing his tone"
    
    show maverick smile
    m "Now, scram! I'm gonna feel grumpy if I don't get my snooze in."
    
    "Maverick says as his last word in, waving his wing out towards the exit of the hardware store as he perches back to his previous position, head against the counter and his eyes closed."
    
    "Louis laughs lightly to himself, seeing as the Eagle's ended the conversation as soon as his task was done, still the Canary bows to the sleeping Eagle in farewell."  
    
    "He turns to leave with a bright smile on his face."
    
    jump _peregrine_interaction_3


label _peregrine_interaction_3:
    #PEREGRINE INTERACTION 3
    
    scene streetview

    "Louis smiles happily with a new video recorder in his wing as he walks out of the Feathered Fixer Hardware store with a light bounce on his step."
    
    "???" "-Chirping happily again, Louis?"
    
    "Louis jolts at the sound of a familiar voice. Turning to his side to see the Falcon approaching him with that permanent stoic expression on his face."
    
    show louis happy at slightleft
    l "P-Phoenix, Catcher, I didn't see you there!"
    
    "Louis laughs nervously, still startled from the initial surprise."
    
    "The Falcon only snickers under his beak, eyeing up the video recorder the Canary carries in his wing, he makes a passing motion with his head towards it."
    
    show catcher confused at slightright
    c "A task?"
    
    "Louis follows Catcher's gaze, nodding in affirmation."
    
    show louis normal
    l "Yeah, it's...for our boss."
    
    "The Canary's voice trails off as he watches the Falcon's reaction."
    
    show catcher neutral
    c "Strange."
    
    "Catcher takes a step closer to Louis, eyeing him down, his eyes unreadable to the Canary."
    
    "........."
    "......"
    "..."
    
    show catcher angry
    c "Why is it that... the old bird chooses you to fulfill his task?"
    
    "Now, it was no secret to Louis or any other bird who worked in Aves Courier that Catcher was the one who always answered Aven's beck and call."
    
    "Especially the tasks confidential to just the Falcon and the Bellbird."
    
    "Louis' gaze darted away, avoiding Catcher's intent stare."
    
    show louis anxious
    l "I-I don't know...it's sudden to me too..."
    
    
    "Louis feigns ignorance, his voice making it obvious of his nervous tone."
    
    "The Falcon remains close to the Canary, towering over him with his height as Catcher stared Louis down."
    
    show catcher confused
    c "Really now?"
    
    menu:
        "RESIST":
            jump resist
        "GIVE IN":
            jump give_in

label resist:
    #RESIST
    
    "Louis nods firmly, standing his ground as he keeps Catcher's eyes on him." 
    
    show louis anxious
    l "Yes, I'm sure of it-"
    
    "Louis averts his gaze subtly."
    
    show louis normal
    l "I was just beeped the night before I had to meet him...I had to wake up earlier than I did because of it!"
    
    "Louis laughs softly at the thought, recalling how the Bellbird woke him up in the middle of the night for the information."
    
    "Louis could feel the watchful eye of the Falcon as he observed him, not returning his laughter, but just staring."
    
    "........."
    "......"
    "..."
    
    show catcher angry
    c "...Right."
    
    "Catcher clears his throat as he breaks the tense stare away from the Canary."
    
    jump _peregrine_int_3_continuation


label give_in:
    #GIVE IN
    
    "Louis sighs in defeat, knowing himself that he can never truly keep up a white lie for his own good, too honest and a bird true to his morals."
    
    show louis anxious
    l "Sorry, Catcher..."
    
    show louis scared
    l "But I'm telling the truth- it was unexpected to me and...Aven chose me on purpose."
    
    "Louis sees Catcher's brow muscle raise at his revelation, intrigue in his eyes as he takes a step closer to the Canary."
    
    show catcher confused
    c "What did he say?"
    
    "Catcher probes, curiosity in his tone."
    
    "Louis hesitates, tucking the video recorder in his bag as he fidgets on his talons."
    
    show louis scared
    l "A-Are you sure? It's not... you know-"
    
    show catcher angry
    c "Yes."
    
    "Catches cuts in quickly with an assured response."
    
    "........."
    "......"
    "..."
    
    "Louis gulps unsurely, yet he continues."
    
    show louis scared
    l "It wasn't a job that you could handle."
    
    "Despite the blunt words, Louis still tries to reassure Catcher."
    
    show louis anxious
    l "I-Is what he said- trust me I wanted to turn it down..."
    
    show catcher neutral
    c "It's fine, Louis."
    
    "The Falcon's tone shifts, it was subtle, unnoticeable even...but Louis notices it."
    
    jump _peregrine_int_3_continuation


label _peregrine_int_3_continuation:
    
    #PEREGRINE INT. 3 CONTINUATION
    
    show catcher anxious
    c "I'll catch you around, Louis. Something... came up."
    
    "An obvious lie, both Louis and Catcher knew the excuse wouldn't fly on a normal day, but something about today was...different."
    
    "The Falcon briefly initiates the bow of farewell. Before the Canary could even reciprocate; Catcher was already flying away out of his view."
    
    "There was something that itches the back of Louis' head, he just couldn't quite... put a feather on what it is."
    
    jump _aven_task_conclusion


label _aven_task_conclusion:
    
    #AVEN TASK CONCLUSION
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions into the 2D platform view of the world, wherein the character 'Louis' is shown inside of Aves Courier Center.{/color}"
    #############################################

    scene aves courier center

    "Louis paces around the office room, waiting for his boss, Aven, to show up for the video recorder he was tasked to fulfill."
    
    "The Canary kept thinking about the interaction with the Falcon from earlier."
    
    "A sense of worry and dread lingers in his system, making him overthink if it was right to act the way he did towards him."
    
    "???" "What's got your talons shivering, son?"
    
    "The sound of the door closing breaks Louis out of his trance, his eyes meeting the bird he waited for. The Canary smiles weakly as he scratches the nape of his neck."
    
    show louis anxious at slightleft
    l "S-Sorry, Sir. I was just lost in thought."
    
    "Louis bows in greeting, in which Aven returns in respect."
    
    show aven neutral at slightright
    a "It's alright, son. Have you been waiting long?"
    
    "The Bellbird asks as he places a wing on Louis' shoulder, focusing his attention on the Canary."
    
    "Louis nods assuringly, reaching out for his bag and rummaging through its contents before pulling out the fixed video recorder from before."
    
    show louis normal
    l "I'm fine, Sir-I got this one fixed!"
    
    "Louis holds up the video recorder happily."
    
    "Aven smiles gently, taking the video recorder onto his wing."
    
    show aven questioning
    a "Good job son! I'm taking it as old Maverick wasn't too hard on you?"
    
    "Aven asks, seeing the Canary laugh at his question."
    
    show louis happy
    l "He was... something, for sure. Nothing I expected!"
    
    "Louis smiles as he recalls the interaction with the Eagle."
    
    show aven thinking
    a "That bird's a prickly ol' fella, don't mind him."
    
    "The Bellbird inspects the video recorder in his wing, humming approvingly."
    
    "Aven walks towards his desk, plugging something to the video recorder to his computer, turning the Canary again as he waits."
    
    show aven neutral
    a "Tell you what son. I just need some of the...the videos in this old junk and you can have the camera for yourself, hm?"
    
    "Aven offers as he stands behind the desk, opposite to Louis."
    
    "Louis' eyes widened softly, surprised at the offer."
    
    show louis happy
    l "Oh Sir, you don't have to...really, it's a kind gesture."
    
    "Louis turned down lightly out of respect for his superior."
    
    show aven neutral
    a "I'm insisting Son, it's not much, I promise."
    
    "Aven repeats his offer, unplugging the video recorder from the computer, handing the video recorder in his wing."
    
    "Louis looks at the video recorder wearily in his wing, looking back at the Bellbird's beckoning motion."
    
    show louis anxious
    l "A-Are you sure, Sir?"
    
    "Aven nods firmly."
    
    show aven neutral
    a "Take it, son."
    
    "The Bellbird beckons again, this time, the Canary accepts the video recorder, holding it onto his wing."
    
    show louis anxious
    l "T-Thank you, Sir."
    
    show louis happy
    l "You're too kind..."
    
    "Louis smiles warmly at Aven, the type of smile that reaches his eyes."
    
    "The Bellbird chuckles heartily, before perching down by the desk in front of Louis, averting his attention to the computer in front of him."
    
    show aven thinking
    a "I'll mark this day as a task-completed, so you don't have to worry about missing a day of work."
    
    "Avens informs Louis, dismissing him with a motion of his wing."
    
    show aven neutral
    a "You can go, you're free from work for the rest of the day."
    
    "Louis meets Aven's eyes again, with an approving nod from his boss, Louis bows in appreciation."
    
    show louis happy
    l "Thank you, Sir. I'll be on my way then!"
    
    "The Bellbird bows in farewell, with the Canary returning it respectfully. Leaving the office, Louis sighs contently, knowing where his next stop will be."
    
    "Setting his mind on a new object, he leaves the premises of Aves Courier Center, flying off to a new location."
    
    
    
    jump day_3_concluded

label day_3_concluded:

    # ACHIEVEMENT UNLOCKED: 1 STAR FROM AVEN

    scene achievement
    with dissolve3
    show achievementaven at truecenter
    with zoomin

    $ renpy.pause(3.0)

    #DAY 3 CONCLUDED

    scene hospital
    with dissolve3

    stop music fadeout 2.0
    
    "Louis toys around with the new video recorder in his possession as he walked across the polished floors of the hospital's hallways."
    
    "The scene of the game opens up in the 'Aven's Care Hospital' room where it is overseeing the background, only the character 'Louis' will be present for this section."
    
    "Inside his mother's hospital room, he held the video recorder in his wing, he fidgets with the gadget idle, almost missing the doctor that catches him at the corner of his eye."
    
    show aziel alarmed at slightright
    az "Mister Louis!"
    
    "The Owl catches the Canary by the wing, pulling him softly to get his attention."
    
    show louis anxious at slightleft
    l "D-Doctor Aziel! I didn't see you, forgive me-"
    
    "Aziel laughs softly, shaking his head dismissively."
    
    show aziel neutral
    az "It's quite alright, Louis, I was actually waiting for you."
    
    "Louis' brow muscle raises in surprise."
    
    show louis anxious
    l "Oh? Is-Is there anything of the matter, doctor?"
    
    "Louis blurts out, out of partial curiosity and mostly worry."
    
    "The Owl shakes his head, putting a wing around the Canary's shoulder, guiding him to another part of the room as he smiles reassuringly."
    
    show aziel think
    az "Quite the opposite of whatever it is you think of, I'd say for sure."
    
    "The Owl chirps happily as he pats Louis' back."
    
    show louis scared
    l "You're really squeezing the anticipation out of me here, Doc!"
    
    "Aziel laughs at Louis' eagerness."
    
    show aziel alarmed
    az "Relax, Louis. The good news is...things are looking up!"
    
    "Louis blinks for a moment...before a wide smile grows on his beak, looking at the Owl directly."
    
    "Aziel watches Louis' reaction, smiling to himself as he continues."
    
    show aziel neutral
    az "There's a good chance your mother will recover, she was showing signs of waking up, it's only a matter of time and patience when she does."
    
    "The Owl finished, tucking in his wings into the pristine white coat he wore."
    
    "The Canary beams brightly the more he listens to the Owl talk, so much so his wings started feeling giddy as he softly flapped around with a small bounce on his talons."
    
    "Unable to handle his joy, he reaffirms with the Owl, just in case."
    
    show louis anxious
    l "Are-Are you positive, Doc?"
    
    "Aziel nods firmly, a small smile on his beak as he gazes at the Canary."
    
    "Louis rejoices quietly again, scattering on his talons, turning to leave just as he had only arrived."
    
    show louis happy
    l "I must go, Dr. Aziel. I-I'm sorry but-I have to tell my wife!"
    
    "........."
    "......"
    "..."
    
    "The game transitions to the 'Acorn Street' Background, wherein the 'yellow house' is the character 'Louis' home."
    
    "The player will be transported in front of rows of tree houses - indicating local bird's houses"
    
    "Use the art of Day_3_Concluded_BG.png for background."
    
    "Louis has a sing-song chirp in his step as he stops right in front of his home, sighing in relief, he composes himself again, making sure to contain his flowing joy over the good news."
    
    show louis happy
    l "Aurora is going to be so... so happy!"
    
    "Louis says to himself with a happy chirp."
    
    "As the player approaches and clicks on the 'yellow house', the game fades to black, signifying the end of the first half."
    
    return