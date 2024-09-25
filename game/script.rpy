define l = Character('Louis')
define nl = Character ('Narrator Louis')
define a = Character('Aven')
define e = Character('Elio')
define c = Character('Catcher')
define i = Character('Ivory')
define az = Character('Aziel')

default half = 1

define dissolve3 = Dissolve(3.0)
image streetview = "/Backgrounds/Street View Dialogue.png"
image achievement = "/gui/AchievementBackground.png"
image achievementivory = "/gui/AchievementIvory.png"

label start:

    stop music fadeout 2.0
    $quick_menu = False

    # jump test_parallax_vp
    # jump inventory_test
    # jump mechanism_testing
    jump start_scene

label start_scene:
    # call screen drag_and_drop_inventory
    
    scene white
    show BlackBars

    voice "voice/nl1.wav"    
    nl "Welcome! This is Narrator Louis, pleasure to be guiding you in Avane Studio's first ever- {i}Canary Courier{/i}! Alpha Build- of course!"
    
    voice "voice/nl2.wav"
    nl "Now, to catch you up to speed if you weren't present for our forum dev logs- here's a quick rundown!"
    
    voice "voice/nl3.wav"
    nl "You, the player, will be controlling me- Louis, the canary bird throughout the whole game,"
    
    scene tutorial 1
    with dissolve3
    scene tutorial 2
    with dissolve3

    voice "voice/nl4.wav"
    nl "And in my stead- deliver and fulfill customer orders to get me that sweet 3 star rating!"

    voice "voice/nl5.wav"
    nl "That's the gist of it- the name of the game basically!"

    scene tutorial 3
    with dissolve3

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Aves Courier Center{/color}"
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

    scene streetview
    show BlackBars
    show louis happy

    l "Aves Courier Center, this is where all the magic happens..."
    
    "Louis speaks of his work fondly."
    
    "Louis enters Aves Courier Center, with a big smile on his face, looking forward to whatever comes his way for the day."
    
    "Wandering further into the building, a drilling voice draws his attention towards the center of the room."

    "All eyes on a particularly blind, yet loud, 'Bearded Bellbird' who had a built-in megaphone device strapped around its neck."
    
    menu:
        "APPROACH THE BELLBIRD":
            jump approach_the_bellbird
        "AVOID THE BELLBIRD":
            jump avoid_the_bellbird

label approach_the_bellbird:

    "Approaching the Bellbird Louis waves his wing."

    "As he walks towards the loud bird, a smile on his face as the Bellbird notices the approaching Canary."
    
    a "Louis, son- what on phoenix's name has held up your time? You've been gone an hour past your clock-in time!"
    
    l "Aven- Sir- I apologize, I didn't think I'd end up late from the morning traffic, the wind resistance was strong enough to clear the clouds..."
    
    "Louis expresses his dismay"
    
    jump bellbird_interaction


label avoid_the_bellbird:

    "Catching sight of the booming bird, Louis turns on his talon to the opposite direction."

    "Already conscious of his tardiness, he's best off avoiding any interaction about it with Bellbird."
    
    "Louis' bright, yellow feather coating easily drew eyes with the heavy contrast from the more darker interior made the Bellbird's neck crane to follow the yellow that swiftly evaded his view."
    
    a "If that Canary is who I think it is- then you'd stop running away and face me like a Condor!"
    
    "Louis stops dead on his tracks, his eyes darting around the room in hopes some other Canary was in the room with him."
    
    "He sighed knowing he was the one known to keep his feathers clean and polished - he averts his gaze to the approaching Bellbird heading his way."
    
    a "Gave up running, Louis? It's about time you got here, you're late."
    
    "Aven noted obviously as Louis faces him directly"
    
    "Louis glances away as he laughed awkwardly"
    
    l "S-So much for a perfect record, huh...?"
    
    "He lets out a uncomfortable laugh."
    
    "His response was met with silence."
    
    l "My apologies, Sir...y'know how the traffic is-"
    
    
    jump bellbird_interaction


label bellbird_interaction:

    a "Oh- enough of that nonsense. Get your gear on, I've got a delivery for you, it's quick and simple. I've heard news of your situation, what happened?"
    
    "Aven guides Louis back to the front of the center, a parental arm around Louis's shoulder as they walked back"
    
    "Louis laughs awkwardly- being caught off guard with how forward the question is, he clears his throat as he regains his composure."
    
    l "It's not a grave situation, Sir- thankfully so. My  mother, s-she's just fallen ill is all..."
    
    "Louis' words trail off in end with an evident uncertainty in his tone"
    
    "Aven's expression already held a stoic look to it, but it turned serious with the heavy stare his gaze had as Louis felt how much he held his superior's attention."
    
    a "You're working here instead of being with your mom, son?"
    
    "Aven asked with concern lacing subtly on his question."
    
    "Louis only nodded in defeat."
    
    l "Someone needs to support her, right? My wife, Minnie, she's already doing her best with the caretaking service but...she's taking days-off to watch over my mother."
    
    a "Ah, Minerva- of course...this job- it doesn't pay well to support bills like that, how're you holding up?"
    
    "Louis chuckles softly, the creases on his face showed his worn-out body"
    
    l "I've taken more work from other departments. Not just delivery parcels now- I've taken food and regular errands under my wing!"
    
    "Louis' smile was small yet sincere, making Aven more concerned than he already was."
    
    a "Don't stress your body, son. There's only so much that mantle of yours can carry."
    
    "Aven pats Louis' back encouraging, the worried look still plastered on his face"
    
    "Louis nods, a cheery laugh following appreciating the concern"
    
    l "I'll be fine, sir- truly. I'm not your star employee for nothing, now am I?"
    
    "Aven's concerned look warped into something more reassuring in Louis' eyes, the evident smirk on his beak encouraged him more and his superior didn't need to say something for it either."
    
    "A heartening pat on Louis' back makes him pull his weight off of the depressing thought of his situation, turning to face the Bellbird's eyes with more confidence and assurance."
    
    a "Speaking like a top dog now, that's the spirit!"
    
    a "A new delivery task should be by the front, complete that today, and I'll add another star to your paramount on the leaderboard."
    
    "Aven tasked Louis without another sweat, the mention of his mountain of achievements makes Louis feel more reassured for today."
    
    "Leaving Louis on his own by the front of the center to tend to other matters, Aven gives Louis the dose of motivation he needed to start off his job."
    
    "Louis is faced with the printed paper in his talons, skimming through the contents of the task, he huffed his chest in ease."
    
    jump end_of_introduction


label new_task_pastry_pieces_tutorial_task:

    "Louis looks to his checklist again, big writing scribbled in red that says 'Bakery Delivery' greets him as he reads on."
    
    "He takes note of what's listed, simple instructions he knows he'll be able to follow through."
    
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
    
    jump continue_dialogue

label continue_dialogue:

    "Louis steps in front of the open bakery wall-store, the letters above him on the sign reads: 'Daily Delights'."

    "He scans the counter at the other side and notices no one by the display yet the open doorway suggests someone was present at least."
    
    "Not being the most familiar with this bakery, surprisingly, Louis rings the hanging bell by the display, making a ringing 'ding!' sound that echoed throughout the store."
    
    "Louis waited patiently, awaiting for the owner to arrive to greet him, yet something else greeted him instead..."
    
    "A light, gray smoke started pouring out of the doorway, a worrisome look quickly dawning on Louis' face as he watched, calling out concerningly to whoever may be in there."
    
    l "Hello??? Does anyone there need help?"
    
    "???" "Everything is fine, ''YES''! D-Don't worry now! I'll be with you in a second!"
    
    "The smoke was paired with clanking of metal from the doorway, Louis' concern growing by the minute the more he waited then suddenly..."
    
    "???" "Dear, {i}SERAPHIM{/i}, that was a disaster now is it!"
    
    "The owner of the chirping voice belonged to a {i}Nightingale{/i} bird, one covered in black dust and debris, as he coughed."

    "Noticing the canary bird standing opposite of his pastry display, he was quick to put a welcome smile as he patted himself clean."
    
    "He leaned over the glass display as he introduced himself to Louis."
    
    e "Hey, friend- sorry about that! I didn't mean to keep you waiting, I'm Elio! Welcome to Daily Delights! or so I like to call it: Cornfield City's humblest bakery on the wall."
    
    e "What can I help you with?"
    
    "Elio smiles in his words as he tied the familiar baker apron around his body as he waited for Louis to respond"
    
    menu:
        " FULFILL 'PASTRY PIECES' TASK":
            jump fulfill_pastry_pieces_task
        "Were you okay back there?":
            jump were_you_okay_back_there
        "How long have you been working here?":
            jump how_long_have_you_been_working_here


label fulfill_pastry_pieces_task:

    "Louis smiles as he focuses on the task at hand, amused by the Baker's display."
    
    l "This bakery looks as lovely as its pastries- I actually have a delivery to make for today."
    
    "Louis pulls up the check-list he has secured in his bag, looking through it briefly as he observes the pastries laid before him inside the glass display."
    
    e "A delivery? Are you one of those birds working in Aves Courier?"
    
    "Elio inquired curiously as he watched Louis' movements."
    
    l "You...can say that, yeah."
    
    "He nods as he affirms."
    
    l "I'm working for multiple departments in the Center, so you're going to be seeing me everywhere the next few days."
    
    "Louis recalls with a smile towards Elio as he explained."

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game showcases the pastry glass display in full view with Elio barely peaking at the top.{/color}"
    "{color=#f00}It shows there are four (4) hoverable choices to pick from: Plain, Glazed Donut / Chocolate Chip Muffin / A Slice of Apple Pie / A Cinnamon Bun.{/color}"
    "{color=#f00}Louis- the player, has to pick two (2) pastries to be dragged into their inventory: A Slice of Apple Pie & A Cinnamon Bun.{/color}"
    "{color=#f00}The player can choose if they are done or not with buttons that read: CONTINUE BROWSING / FINISH BROWSING.{/color}"
    #END FUNCTIONALITY
    #############################################
    
    e "That doesn't sound healthy, are you sure you're alright managing all that work?"
    
    "Elio asks, concerned, worried for the canary's well-being."
    
    l "I'll be quite alright- I need to anyways, it's for someone special to me."
    
    "Louis smiled reassuringly as he handed his picks of pastries to Elio."
    
    e "I see... Well, will this be all, then?"
    
    "Elio takes the pasties off of Louis' hands as he reaffirms again."
    
    menu:
        "Yes, that would be all.":
            jump yes_that_would_be_all
        "Let me look around again.":
            jump let_me_look_around_again

label were_you_okay_back_there:
    
    l "Hey there! Were you okay back there? It sounds like you were having a pretty rowdy time back there?"
    
    "Louis shows his concern towards the Nightingale bird, his gaze was shifty in nature as his eyes darted from the doorway then back to Elio."
    
    "Elio puts a reassuring smile on his face, appreciative of the concern showed to him"
    
    e "Thanks, friend! And I'm quite well- that's just another day for a humble baker like me!"
    
    e "Mistakes are part of the job- I say it is what makes me more authentic!"
    
    menu:
        "You're not wrong!":
            jump youre_not_wrong
        "True, until your customers question your safety measures...":
            jump true_until_your_customers_question_your_safety_measures


label how_long_have_you_been_working_here:

    "Louis contemplates for a moment, looking around the other buildings and boutiques, then back at the Daily Delights that was a shop shoved in a concrete wall." 
    
    l "So, how long have you been working here? The bakery looks fairly new compared to the other shops around..."
    
    "Elio follows the canary's gaze, his smile grows as he recalls the older days."
    
    e "It's true Daily Delights came a bit later compared to the rest of the buildings here, but that's cause I had to earn the money during college so I can buy this tiny old thing."
    
    "Elio smiles fondly at the memory."
    
    e "Once I finally got enough funds to cover this thing, it was like a newborn chick, it was shiny- new, and everything else...Daily Delight's business was booming! Now it's solidified its place among the others, but I've been here waaay later!"
    
    "Elio explains briefly, patting down his apron idly."
    
    l "That sounds nice! A humble bakery with a humble beginning, a pleasant story to tell."
    
    e "You've got that right! This  is my pride and joy."
    
    "Elio beams fondly of his little bakery beginnings."
    
    jump _fulfill_pastry_pieces_task


label yes_that_would_be_all:

    l "Yes, that would be all!"
    
    "Elio smiles at his words, moving quickly as he works his way at the back, packing up Louis' order before handing it over to him."
    
    "Elio hands a paper bag to Louis, a neat packaging for the pastries"
    
    e "Here you are, now you be safe and look after yourself, alright?"
    
    "Louis nods in reassurance, of course- not forgetting to look after himself as well."
    
    l "No worries, I'll be okay- I'm taking care of myself too, thank you for these!"
    
    "Louis shook the bag in his hold lightly."
    
    "Elio smiles satisfied with another successful order."
    
    e "It was a pleasure! Feel free to stop by whenever you'd like!"
    
    "Elio waves Louis goodbye as the canary bird is set back on the path of the task in hand." 
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The player's inventory should have a packaged brown paper bag that when hovered, it should read out: Ivory's Pastries.{/color}"
    #############################################
    
    menu:
        "PEREGRINE INTERACTION":
            jump peregrine_interaction
        "SMALL NOTE":
            jump small_note


label let_me_look_around_again:

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game goes back to the pastry selection screen if the player chooses the: 'Let me look around again.' option.{/color}"
    "{color=#f00}These two options will come up again for the second time once the player is finished browsing.{/color}"
    "{color=#f00}The game proceeds with the dialogue if the player chooses: 'Yes that would be all.' option.{/color}"
    #############################################
    
    jump _fulfill_pastry_pieces_task

label youre_not_wrong:

    "Louis chuckles lightly at his words, a bit amused at the baker in front of him."
    
    l "Well, that's a look on it. You're not wrong!"
    
    l "I'm guessing this sorta thing happens often here with you?"
    
    "Elio chuckles a hearty and rumbly one from his chest."
    
    e "Unfortunately so, but it shows that I'm all making these delicious things by the wing!"
    
    e "I'm running the whole thing by myself, a sort of, one bird show, y'know? Sometimes it takes a while for everything to be in order!"
    
    e "But rest assured, I've got everything under control!"
    
    "Louis nods understanding his words clearly, not doubting him but it fulfills his curiosity."
    
    l "I see- it isn't difficult for you to run everything all on your own? Why not get any helpers?"
    
    e "When I first opened the shop, yeah it was difficult for sure! But after a while, the bakery settled in and business became more casual and mellow, I could manage it fine!"
    
    l "I'm glad you're doing well then!"
    
    e "Of course! Baking has been my passion for the longest time, this job is my dream."
    
    jump _fulfill_pastry_pieces_task


label true_until_your_customers_question_your_safety_measures:

    "Louis laughs lightly, but there was a subtle hint of concern lacing in his laugh."
    
    l "Well, That's quite true, until your customers start questioning your bakery's safety measures..."
    
    "Louis smiles concerningly for him with slight furrow brow muscles."
    
    "Elio chuckles lightly, scratching the nape of his neck as he nodded in agreement."
    
    e "You're not wrong! I've gotten a few concerned check-ins from the other locals, but I always assure I know what I'm doing!"
    
    e "I'm running the whole thing by myself, a sort of, one bird show, y'know? Sometimes it takes a while for everything to be in order!"
    
    "Louis' eyes widened softly, it was making sense to him. He smiled softly at his words."
    
    l "I see- it isn't difficult for you to run everything all on your own? Why not get any helpers?"
    
    e "When I first opened the shop, yeah it was difficult for sure! But after a while, the bakery settled in and business became more casual and mellow, I could manage it fine!"
    
    l "I'm glad you're doing well then!"
    
    e "Of course! Baking has been my passion for the longest time, this job is my dream."
    
    jump _fulfill_pastry_pieces_task


label peregrine_interaction:

    "Louis turns away from Daily Delight Bakery with a waving wing, bidding the humble baker, Elio, a goodbye in his step, with a satisfied order."

    "He is set to check off another box from his checklist, and that is: traveling to Ivory's doorstep in Acorn Street."
    
    "But before he can continue onto his journey- he notices a familiar falcon in his view..."

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Daily Delights Bakery, with the character 'Catcher' a few blocks away.{/color}"
    "{color=#f00}The player should be able to move 'Louis' to interact with 'Catcher'.{/color}"
    #############################################
    
    "The Peregrine Falcon watched the Canary bird with an observant gaze."
    
    "As Louis approached casually, he greeted the Falcon with a familiar chirpy gesture and tone, his movements showing that the two already knew each other prior."
    
    l "Catcher! I didn't think I'd well, 'catch' you earlier at HR- where've you been?"
    
    "Louis softly chuckled at his own unexpected joke, finding it rather silly."
    
    "Catcher had an amused look on his face with the Canary's wording, he had a light smirk plastered on his beak because of it."
    
    c "Clever. I had earlier commitments to attend to - word around, you ran into Big A, or was it more like he hunted you down?"
    
    "Catcher asked rather blunt and straightforward, something not out of his usual self."
    
    menu:
        "Yeah- I approached him!":
            jump yeah_i_approached_him
        "No, he definitely hunted me down...":
            jump no_he_definitely_hunted_me_down


label end_of_introduction:

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Aves Courier Center{/color}"
    #############################################
    
    nl "That should be a good introduction for you to start with!"
    
    nl "Now- I don't want to spoil you too much on how the game works, but here's a quick rundown:" 
    "You have your inventory on the left in which you can access after dialogues and settings on your right, your task checklist at the upper left corner right beside your map, and that's... about it!"
    
    nl "From this point on, I'll no longer be joining you as Narrator- but I'll be with you for the rest of the game! :D"
    
    jump new_task_pastry_pieces_tutorial_task


label small_note:

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game then gives the player two choices to choose from they both read either: WRAP UP DAILY DELIGHTS VISIT / STAY AND ASK MORE QUESTIONS.{/color}"
    "{color=#f00}The STAY AND ASK MORE QUESTIONS option will only be available if the player does not choose the two other ask options and goes straight for FULFILL 'PASTRY PIECES' TASK option.{/color}"
    #############################################
    
    menu:
        " FULFILL 'PASTRY PIECES' TASK":
            jump _fulfill_pastry_pieces_task
        "PEREGRINE INTERACTION":
            jump peregrine_interaction


label yeah_i_approached_him:
    
    l "Oh yeah- I approached him! It was about something important, so I didn't want to delay it."
    
    "Louis explained sheepishly as he scratched the nape of his neck with his wing."
    
    "Catcher paused for a moment, just staring at Louis before he spoke again."
    
    c "I get it, it's good he was there for you to speak to him directly, he's usually absent overseas."
    
    c "What did he want with you anyways?"
    
    jump peregrine_int_continue


label no_he_definitely_hunted_me_down:
    
    l "Ahh... no, he definitely hunted me down..."
    
    "Louis chuckled softly as he recalled the interaction from earlier this morning."
    
    c "You were avoiding him? That would definitely look odd to me, and not to mention make you stand out more to him."
    
    "Louis nodded affirmatively at his words, a small smile on his face."
    
    l "Well, you're not wrong! That's definitely what happened!"
    
    "Catcher paused for a moment, just staring at Louis before he spoke again."
    
    c "What did he want with you anyways?"
    
    "Catcher piqued his curiosity more with a short question."
    
    jump peregrine_int_continue


label peregrine_int_continue:

    "Louis laughs awkwardly, his gaze averting elsewhere as he comes up with the words to explain his situation."
    
    l "I-I had an increase of work, I wanted it - to be clear, so he was just checking in with me."
    
    l "I'm taking more work and duty calls from the Food and Shopping courier district now!"
    
    "Louis explained honestly to Catcher, seeing the Falcon only nod understandably, listening to his words thoroughly."
    
    c "What for? You're already employee of the month, are you aiming to make it the whole year-?"
    
    "Catcher jested coolly, nonchalant and casual- he wasn't too worried about Louis."
    
    "Louis chuckled heartily at Catcher's jest, shaking his head lightly in disagreement."
    
    l "I wish I could say it's like that- but unfortunately, no, it's for my mother."
    
    "Louis feigned a reassuring smile while he watched Catcher's eyes, somewhat feeling like the Falcon knew and saw through him."
    
    c "Mother Joan? Is she alright - did something happen?"
    
    "Louis' brow muscled knotted subtly, there was something in Catcher's tone that caught him off guard- like it was a bit strained or struggling, with how his words fell flat at the end."
    
    "Nonetheless, Louis kept his facade up with his reassuring smiles and gestures."
    
    l "Oh- She's just fallen ill, she'll be fine, the extra funds will help her recover greatly, might as well, y'know?"
    
    "Louis could see it in Catcher's eyes, the faint squint gaze at him, as if he's trying to wait for him to reveal more."
    
    "Catcher didn't say anything more, a small silence falling between them."
    
    "......"
    "..."
    
    "Catcher spoke up again."
    
    c "It looks like you've got it all under control then."
    
    "Catcher briefly said before changing the topic at hand."
    
    c "So, where are you off to, then?"
    
    "Louis notices Catcher's eyes dart from his gaze to the familiar bag he carried around for deliveries."
    
    l "I'm just about to wrap up a delivery actually - some pastries for Ivory."
    
    "Louis mentions his task in passing, hearing a light hum from the Falcon."
    
    c "Miss Ivory? She hasn't ordered for a while, glad to know she's alright."
    
    "Catcher commented, a small observing note for Louis."
    
    l "I take it you delivered to her address a lot?"
    
    "Catcher nodded, one firm nod at his words, not really saying more or less about the topic."
    
    "Louis stood idly for a moment, before speaking again- not really wanting the silence to fill the air like before."
    
    l "I see- well if that's the case, I'll make sure to tell her you said 'Hi' when I stop by, I'd best be going then..."
    
    "Louis' words trailed off at the end as he bowed in a gestured departure, Catcher doing the same as he spoke one last time."
    
    c "That would be lovely, I'll see you around, Louis."
    
    "Louis watches as Catcher's bandaged talon was exposed to him as Louis passed him by, Catcher flying off after their interaction ended."
    
    jump tutorial_conclusion


label tutorial_conclusion:

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the town street of 'Cornfield City'{/color}"
    #############################################
    
    "Louis stands idly on the main street of the town, reminded again of the task in hand as he pulls out his check-list from his pocket, marking the finished ones so far."
    
    l "I better get these to Ivory's doorstep before the afternoon comes around..."
    
    "Louis noted mentally as he prepared to take flight again."
    
    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The game highlights the 'map' option, allowing the player to travel to three locations: AVES COURIER CENTER, CORNFIELD CITY (currently standing), ACORN STREET.{/color}"
    "{color=#f00}The map should highlight the 'ACORN STREET' location to guide the player where they need to be in order to finish the task.{/color}"
    "{color=#f00}The player will be transported in front of rows of tree houses - indicating local bird's houses.{/color}"
    #############################################
    
    "Louis arrives at his final destination shortly, the rows of bird houses filling his view as the familiar area is felt under his talons."
    
    "He strolled casually, his eyes peeled finding the {i}red house{/i} on the main street."
    
    l "It should be around here...better get these to Miss Ivory before I run out of time and she cancels on me."

    #############################################
    #FUNCTIONALITY HERE
    "{color=#f00}The player will be able to hover their mouse and walk around the area to choose which house they will be able to go to- for this section, only the red house's door is available for access.{/color}"
    #############################################
    
    "Louis' gaze finally finds the stood out red house on the street, strolling over with the package in hand."
    "He stops right outside the front door of the bird house, tidying himself up before the final delivery."
    
    "Louis hovers over the door, with the prior context of Miss Ivory being Catcher's older customers- he felt a strange unease, a sort of nervousness that was familiar."
    
    "It was the type of feeling he had felt before when he first started out his courier job, the nervousness of talking to other birds, disturbing them from their peaceful day."
    
    "Louis clears his throat to himself, before knocking loudly with a closed wing."
    
    "He waited, for a moment."
    
    "Even calling out to the bird inside."
    
    l "Miss Ivory? It's Louis, from Aves Courier! I have your delivery!"
    
    "The unease returned when there was a lack of response from the inside, so he waited."
    
    "Again."
    
    "......"
    "..."
    
    i "Oh dear- I apologize, I didn't hear you over the laundry!"
    
    "The sudden opening of the door Louis stood in front of brought him immediate ease, soothing his worries gone while he wore the practiced smile for his customer."
    
    "The canary bird is greeted by a Mockingbird, a passerine bird serene to its surroundings as she smiles warmly back to him in greeting."
    
    l "It's quite alright, Miss- I was a little worried you weren't home to receive them."
    
    "Louis voices out his thoughts to her."
    
    "The pink robin flaps her wing dismissively as she laughs softly."
    
    i "No worries- I would've felt the same if I was in your talons." 
    
    i "I'm quite used to using your services, I'm pleased to be greeting a new bird on my doorstep this time."
    
    "Louis notes of her words, recalling the interaction he had with the Falcon from earlier."
    
    menu:
        "Is the change a good thing?":
            jump is_the_change_a_good_thing
        "I'm glad to be able to serve you.":
            jump im_glad_to_be_able_to_serve_you


label is_the_change_a_good_thing:
    
    "Louis nodded understanding her words."
    
    l "I was told my colleague, Catcher, was the one who answered frequently to your tasks."
    
    l "Is the change of couriers a good thing?"
    
    "Louis shifts on his talons nervously as he awaits her reply."
    
    i "You haven't done anything wrong, no worries, I think...sometimes change is needed, y'know?" 
    
    "The mockingbird flaps her wing dismissively as she laughs softly."
    
    i "N-Not that there was anything wrong with Catcher! He was a lovely courier." 
    
    "Ivory stammered lightly as she defended her words."
    
    l "Hey- hey, don't worry! I wasn't thinking about that, I'm not getting the wrong idea!"
    
    "Louis reassured, he can see her feel reassured gradually as her smile returned."
    
    jump continue_dialogue_tut


label im_glad_to_be_able_to_serve_you:
    
    "Louis nodded understanding her words."
    
    l "I see, well- I'm glad to be able to serve you regardless."
    
    l "Nothing happened with Catcher, if I can ask?"
    
    "Louis can see Ivory pause, thinking- contemplating on his words."
    
    i "No-I don't believe so, he must just be busy."
    
    "Ivory smiles reassuringly to him, in which Louis returns graciously."
    
    l "He does get a bit ahead of himself sometimes."
    
    l "Prioritizing other stuff over the other... typical Catcher for you."
    
    "Louis listens to the mockingbird's soft chuckle. Returning the smile she gives him."
    
    i "I'm sure we'll be seeing more of each other then, Louis, was it?"
    
    "Louis nodded in affirmation."
    
    l "Sure we will, Miss Ivory."
    
    jump continue_dialogue_tut


label continue_dialogue_tut:

    "Louis rummages through his bag, sorting out other stuff out of the way as he pulls out the paper bag containing the contents of Ivory's orders." 

    "He handed it over gently with a small smile on his face."
    
    l "This should be what you've tasked me with, a slice of apple pie - and a delicious cinnamon roll."
    
    "Louis feels his wing briefly graze hers as she accepts the bag with a fond look in her eyes as she sees the pastries she wanted."
    
    i "Just in time as well- I'm ever grateful for you going out of your way to do this for me."
    
    i "There's just so many chores to do after my shift- I can't possibly do other things I'd need for it anymore!"
    
    "Louis chuckles at his words as he nods, understanding the hassle well."
    
    l "Well, it is my job, Miss Ivory. I'm glad I'm making things easy for you if anything."
    
    l "If everything is in order- I shall be taking my leave, then?"
    
    "Louis watches as the passerine bird looks through the content of the bag, before he hears her hum satisfied- a singsong tune."
    
    i "You did everything right- splendid!"
    
    i "Well done, I should be able to mark my task finished for you- ah! I have something for you, before I forget."
    
    "Louis is left standing in front of the doorway of Ivory's home as she quickly disappears into the comfort of her home, before she returns with a plastic bag in her beak and the familiar pastry in view."
    
    "He was quick to accept her offer as she leaned forward to hand it to him, in his wings was the cinnamon roll he had bought for her as something part of his task."
    
    "Louis faces Ivory confused, a bit lost on what this meant."
    
    i "I figured you must be tired from your delivery- a small snack wouldn't hurt!"
    
    "Ivory smiles kindly at Louis which he takes rather well, he returns the grin with a thankful look plastered on his face."
    
    l "I-I'd have to go now- but this is a lot, thank you...are- are you sure you'd want me to have this?"
    
    l "I mean, you did order it and all..."
    
    "Ivory waves him off dismissively again with her wing, pushing him lightly off her doorway with a reassuring smile."
    
    i "Nonsense! It'd be rude to refuse a gift from a lady bird now, no?"
    
    "Louis finds himself chuckling, finding amusement at being backed up to a corner. He bows his head promptly."
    
    l "I suppose you're right, it would be rude. In that case- thank you for the lovely gift."
    
    l "I'll see you around, Miss Ivory."
    
    "Ivory returns Louis' farewell bow, watching Louis take off, shutting the door behind her."
    
    scene achievement
    with dissolve3
    show achievementivory
    with zoomin

    pause 4
    
    jump day_1_concluded


label day_1_concluded:

    #############################################
    #FUNCTIONALITY HERE
    "The scene of the game opens up in the 'Aven's Care Hospital' room where it is overseeing the background, only the character 'Louis' will be present for this section."
    #############################################
    
    "Louis finds himself perched comfortably right next to the sleeping figure that inhabits the room he currently resides in."
    
    "Humming a light tune to himself as he settles his courier bag off to the side, focusing on the subject that reaps all of his hard work at the moment."
    
    "Louis holds a fond look as he gazes briefly onto the patient who is nestled quietly in their slumber."
    
    l "I met a lovely customer today, you may be familiar with them- since you're always browsing around in the supermarket."
    
    l "I have a feeling they may be an employee, a cashier, maybe?"
    
    "Louis then reaches for his bag, rummaging through it as he pulls out the familiar gift given to him by his customer."
    
    l "Miss Ivory, the name of my customer- gave this to me as a parting gift for accomplishing the task she assigned, but...I'd like to leave this to you instead."
    
    "He places down the neat, plastic wrapped cinnamon roll on the bedside table of the patient."
    
    "Louis chuckles heartily, a fond look in his eyes."
    
    l "You must be craving something sweet, I know it- especially with the doctors only permitting you liquid meals? That is rough, it'll be our little secret, hm?"
    
    "He adjusts where the pastry was placed, hiding it in plain sight behind the withering flowers on a base."
    
    l "I hope your day has been well, I've noticed... changes, but the doctors say it's just the medication, nothing off the worry."
    
    l "Make sure you're also looking after yourself, I will have enough to help you recover, so just relax- and focus on getting better!"
    
    "Louis reassures the patient- his mother, as he stands up from his perched position."
    
    l "Aurora has also been doing her part in helping you, y'know her... always harder at work than I am, she'll be the one visiting you tomorrow when the first light hits."
    
    l "For now... I must go home to her and rest- I'll have a new task assigned to me, no doubt in that. I'll visit you like always after my delivery."
    
    l "I'll trust the doctors to take care of you in my stead, tomorrow- I'll bring you another gift to keep yourself entertained."
    
    "Louis bows his head in farewell, a gesture action as he wears the grounded smile he has while he bids her goodbye."
    
    l "Goodnight, mother dearest."
    
    "As Louis bids his last goodbyes for the day, he exits the room." 
    
    "Before he has a chance to leave- he is stopped promptly by a soft yet stern call of his name, he turns around, faced with a bird much larger than he is."
    
    "???" "Mister Louis? Is that you I see there?"
    
    "Louis takes in the sight of him, a large- Great Horned Owl stands before him- greeting him in passing with a bow, his piercing gaze keeps Louis' attention on him."
    
    l "Yes...Yes that would be me."
    
    "The brown owl introduces himself as he clears his throat."
    
    az "I'm Dr. Aziel, Mister Louis- I'm your mother's caretaker until she recovers fully."
    
    az "I was told by the other nurses here that Miss Joan's son is a particular shade of... yellow, brighter than any other canary, I see that now."
    
    "Louis, upon realization dawning on him, bows promptly in respect, before meeting the strong gaze of the owl again, he nodded to his words."
    
    l "Doctor A-Aziel! Accept my sorrys- I did not introduce myself sooner."
    
    l "I'm Louis, yes- Mother Joan is my mother, you got that right."
    
    "Louis chuckles briefly as he offers his wing, the owl briefly grazes his feathers against Louis as introductions while the owl hums pleased."
    
    az "It's nice to meet you, finally making your acquaintance- were you on your way out?"
    
    "Aziel motions his head towards the exit."
    
    "Louis nods in affirmation to his question."
    
    l "Just paid a visit as usual, but my wife's expecting me- so I couldn't linger too long."
    
    "Louis  smiles apologetically."
    
    az "Don't apologize, Mr. Louis. I have my own affairs I need to check-on but let's talk properly on your next visit."
    
    "Aziel offers an arm around the canary, slowly guiding him out as he acknowledges Louis' dismissal to head home for the night."
    
    l "Thank you- Sir, I'll be sure to stick around longer."
    
    az "Goodnight, Mr. Louis, until tomorrow then."
    
    "Louis catches a brief glance of the owl flying off elsewhere into the hospital, with that in mind, he turns to fly off on his own as well."
    
    "Safely returning to the comforts of his home, and ending the day off with a successful delivery- and an interesting day with new faces."