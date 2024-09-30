# louis_day2.rpy


#######################################################
#              DECISION + MECHANICS LABELS            #
#                  (With Subcategories)               #
#######################################################


############# MAP MECHANICS #############


# Includes a map mechanic where the player can select locations to travel.
label _lily_task_conclusion:

    #The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the town street of 'Cornfield City'
    scene cornfield town
    
    "Louis finds himself on the main street of the city again, huffing lightly with the heavy items he carried in his bag, he opens his map again to see where he should be headed."
    
    show louis normal
    l "If I get these early to Miss Lily, I should be able to have time to roam around before it gets too dark..."
    
    "Louis noted mentally as he prepared to take flight again."
    
    #The game highlights the 'map' option, allowing the player to travel to three locations: AVES COURIER CENTER, CORNFIELD CITY (currently standing), ACORN STREET.
    #The player will be transported in front of rows of tree houses - indicating local bird's houses.
    
    scene acorn street
    show lightoverlay

    "As Louis arrives at his destination, the familiar- warm sunlit Acorn street, he glances briefly at his checklist just to make sure he knows which house he has to go to."
    
    "Pocketing the paper again, he kept his eyes peeled as the sun set behind him, his eyes landing on the 'blue  house' on the main street."
    
    "But before he continues- something else catches his eyes, just at the end of the road, by the white house- a figure stands idle."
    
    #The player will be able to hover their mouse and walk around the area to choose which house they will be able to go to-
    #for this section, they may choose to access the blue house or the strange figure.
    #The player will be transported in front of rows of tree houses - indicating local bird's houses.
    
    menu:
        "INVESTIGATE THE FIGURE":
            jump investigate_the_figure
        "CONTINUE DELIVERING TO LILY":
            jump _deliver_to_lily_02


############ INVENTORY MECHANICS ##########

# Map mechanic for navigating between locations like ‘Cornfield City’ and ‘Acorn Street’.
# The player needs to collect and manage items from the grocery list.
label _new_task_shopping_spree_:
    
    hide louis normal
    hide aven neutral
    "Louis opens the folded checklist, reading the big writing scribbled in red that says 'Grocery Errands' looking back at him."
    
    "He takes note of what's listed, simple instructions he knows he'll be able to follow through."
    
    #The game opens up the Louis' checklist, reading the contents it spells out to the player exactly what is expected to be done.
    "The checklist reads:"

    "{color=#8b593c}DELIVERY FOR LILY{/color}"
    "{color=#8b593c}Lily has sent in an evening task she wishes to be fulfilled before '6:00 PM EVENING'."
    "{color=#8b593c}The task- though plenty, is pretty simple enough, she just needs 5 supermarket items delivered to her doorstep, baking ingredients for the cake she'll be making before her roommate, Sierra, return home.{/color}"
    "{color=#8b593c}Visit 'Flyway Superstore' Supermarket in 'Cornfield City'{/color}"
    "{color=#8b593c}Pick the required grocery items from the Supermarket:{/color}"
    "{color=#8b593c}- A Dozen of Eggs{/color}"
    "{color=#8b593c}- A Pack of Sugar{/color}"
    "{color=#8b593c}- A Pack of Flour{/color}"
    "{color=#8b593c}- A Berry Branch{/color}"
    "{color=#8b593c}- Two (2) Cartons of Milk{/color}"
    "{color=#8b593c}Talk with the 'cashier': 'Ivory'{/color}"
    "{color=#8b593c}Check-out the pastries from Ivory{/color}"
    "{color=#8b593c}Leave 'Flyway Superstore' Supermarket and go to 'Acorn Street'{/color}"
    "{color=#8b593c}Find the 'blue  house'  on 'Acorn Street'{/color}"
    "{color=#8b593c}Deliver the groceries to Lily's doorstep{/color}"
    "{color=#8b593c}Mark the task as: 'DELIVERED'{/color}"
    #The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) Cornfield Mail Post
    #The game automatically opens the 'Map' for this section, and the player can choose to only access the town street: 'Cornfield City'
    #The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in 'Cornfield City'
    #the player may interact with the character 'Catcher' or go straight to 'Flyway Superstore' for this section
    
    scene cornfield town
    with dissolve2
    #show lightoverlay

    "As he makes his way out, he sees someone familiar in the distance."
    
    menu:
        "GO UP TO HIM":
            jump peregrine_interaction_2
        "ENTER THE FLYAWAY SUPERSTORE":
            jump flyway_superstore


########### MINI-GAME MECHANICS ###########

# Mini-game mechanics with a "hover and pick" interaction for grocery items in the supermarket.
# Decision combined with an inventory system(drag-drop) for collecting items.
label flyway_superstore:

    scene flyaway superstore
    
    "Louis finds himself inside the all familiar sign of the supermarket that read: 'Flyway Superstore' wherein he gets his own deal of supplies for daily living himself, pushing past the other birds in his way."
    
    "He took out his checklist again, scanning his eyes over the items he needed to collect for the task at hand."
    
    "Louis easily browsed through the 'general goods' section of the rows of shelves, each aisle containing different items."
    
    #The game showcases a packed grocery shelf aisle in full view- it shows there are four (5) hoverable choices to pick from:{/color}"
    #An Egg Tray / A Carton of Milk / A Bag of Sugar / A Bag of Flour / A Branch of Berries.{/color}"
    #Louis- the player, has to pick two (6) grocery items to be dragged into their inventory: (1) An Egg Tray / (2) A Carton of Milk / (1) A Bag of Sugar / (1) A Bag of Flour / (1) A Branch of Berries.{/color}"
    #The player can choose if they are done or not with buttons that read: CONTINUE BROWSING / FINISH BROWSING.{/color}"

    "Referencing his checklist, he picked up what his client needed."

    show supermarket items
    with dissolve1
    "An egg tray, two cartons of milk, some sugar, flour, and some berries."
    #############################################
    
    "Louis hums satisfied as he begins to walk towards the cashier after getting all the stuff he needed to get for his customer."
    hide supermarket items
    show louis normal at tint4
    l "This should be all Miss Lily needs..."
    
    "Louis rummages through the items, double-checking just in case he missed anything-"
    
    "A chirping call catches the attention of the Canary, his gaze landing on the familiar mockingbird from the day before."
    
    show louis normal at tint6
    show ivory happy at tint5
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

    scene flyaway superstore
    show grocerybag
    "Louis received the newly packaged bag of groceries from Ivory as she placed the receipt in with a clap of her wings, satisfied with her neat work."
    hide grocerybag
    
    show ivory happy at slightright
    show louis happy at slightleft
    i "That should be all of it!"
    
    "Louis hums as he nods."
    
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


########## POINT & CLICK MECHANICS #########


# Player hovers over interactable items in the mail post room to select and read.
# The player investigates a bulletin board.
label _a_newspaper_bulletin_board:
    
    "Louis finds himself standing a wide bulletin board. As he stares at the newspaper clippings attached on the corkboard, he picks up an old newspaper that catches his eye in particular."
    
    "The newspaper held with curiosity in his wings as he read on quietly to himself, his eyes widening at the words of the headline that read:"
    
    "BEN, AN 11 YEAR OLD CHICK PUT DXWN IN AVIAN CARE HOSPITAL"
    
    "The headline covered mostly the paper with layers of text, what caught Louis' eye mostly was the rectangular drawn picture that took up most of the space next to the contents of the newspaper."
    
    show post clipping
    with dissolve1

    "It showed the drawing of a young mockingbird chick, or from the looks of what he could observe."

    "There was a part of him that made him recall seeing familiar patterns before, but he didn't want to assume- what if the dots he was connecting turned out to be wrong?"
    
    "Trying to find more context, the headline description itself didn't give him much, if it wasn't ripped off, it was covered with black ink that was entirely illegible to his eyes."
    "There were a few things he's sure of upon reading, however..."
    
    "Was that this mockingbird passed early, mysteriously so- in the hands of the local hospital where his mother resides in, if that wasn't in the tiniest bit concerning then he wasn't sure what is."
    
    "Not wanting to let his thoughts run south even more, he places the newspaper clipping to where he found it, leaving it be."
    hide post clipping
    
    jump post_choice


# Player interacts with a stack of boxes in the room, making decisions based on what Louis finds.
label _a_stack_of_boxes:
    
    "Louis stands near a stack boxed that seemed to be addressed directly to Aves Courier Center specifically-"

    "But there his eyes catches the opposite, picking up the rectangular box on the top of the stack, he immediately recognizes the names tagged on the box as it reads:"
    
    show post package
    with dissolve1

    "TO: AZIEL, FROM: AVEN"
    
    "His brow muscles knot together as his curiosity piques, there was a bit of scratching damage on the box itself, but it wasn't enough for him to see entirely what it was inside..."
    
    "Until he started feeling guilty."
    
    "Louis wasn't one to pry so much more, look through the personal belongings of others unless he was explicitly told so that he was allowed, killing the part that made him wonder-"
    
    "He puts the box back at the top of the stack, leaving it be there without another thought of it."
    hide post package
    
    jump post_choice


# Player interacts with scattered mail to pick up and read a letter.
label _a_letter_mail_scattered_on_the_floor:
    
    "Louis walked briefly before looking down as his talon felt the texture change from the usual concrete to a rustling sound, upon realizing he was standing on multiple, scattered envelopes-"
    
    "He stepped back to not wrinkle more of the mail."
    
    "He picks up a particularly worn out envelope compared to the rest, seeing as it was addressed to Aven, his boss, specifically coming from Avian Care Hospital."
    
    "As he opened the letter curiously, the familiar doctor came to his view as the letter came from Doctor Aziel. He piqued a bit as he read out a bit of the contents of the letter:"
    
    show post letter
    with dissolve1

    "To Aven,\nAves Courier Center"
    
    "While I hope this letter finds you in good health, this is an urgent warning to whoever this letter may cross, Aven or not,  there has been a new patient placed under my wing, an alarming one at that."
    
    "If his records are true, then he will be under my strict guidance-"
    
    "Louis stopped reading before he becomes anymore intrusive than he already has been, glancing at the letter one last time-"
    
    "-We must have this conversation once you're free, Aven. I fear this situation concerns not only me, but you as well. Meet with me when you can."
    
    "Best, Aziel.\nAvian Care Hospital"
    
    "Louis hurriedly places the paper letter back to the envelope where it came from, from the sudden growing nervousness his wing shook and accidentally dropped the mail he held."
    
    "Stepping back as he tried to recollect his composure, he wasn't sure how recent that letter was, but he wasn't supposed to be seeing it."

    "While it'll be hard to erase the contents of that letter from his memory, he was best not touching anything else before it cost him."
    hide post letter
    
    jump _bellbirds_suspicion


#######################################################
#                   STORY LABELS                     #
#######################################################


label day_2:
    $ day = 2
    $ is_daytime = True

    play music "music/CC Main Story Dialogue Theme.wav" fadein 5 fadeout 3

    scene aves courier center inside
    with Dissolve(10.0)

    show louis normal at shadow3
    show aven neutral at shadow2
    
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

    "There are several things lying around."
    
    #The 'Cornfield Mail Post' background will have some interactable items to note: 'A Newspaper Bulletin Board', 'A Stack of Boxes at the far end right', and some 'Mail scattered on the ground.
    #The character 'Louis' will be able to move around this room, and the player may hover over items that should highlight the interactable items.

    jump post_choice

label post_choice:
    menu:
        "A Newspaper Bulletin Board":
            jump _a_newspaper_bulletin_board
        "A Stack of Boxes":
            jump _a_stack_of_boxes
        "A Letter Mail Scattered on the Floor":
            jump _a_letter_mail_scattered_on_the_floor


label day_2_continuation:
    
    show aven neutral at shadow2
    a "I won't keep you too long, son, I know you've got deliveries to tend to, now off you go."
    
    "Aven says as he prepares to send Louis off, handing him the familiar paper checklist midway."
    
    "Louis graciously accepts the checklist, glancing at it briefly- he realized it would be his task for today."
    
    show louis normal at shadow3
    l "Thank you, sir, I should be one call away whenever you need me again."
    
    "Louis returns Aven's bow as they both part ways."
    
    "Louis ends off the short visit and interaction as he flies off to start his new task."
    
    jump _new_task_shopping_spree_


label day_2_concluded:

    play music "music/CC Mission Complete.wav" fadein 1 fadeout 1
    scene achievement
    with dissolve3
    show achievementlily at truecenter
    with zoomin

    $ renpy.pause(3.0)
    
    scene avian care room
    with dissolve3
    $ is_daytime = False

    stop music fadeout 2.0
    play music "music/CC Somber Hospital Theme.wav" fadein 2 fadeout 2

    #DAY 2 CONCLUDED
    
    "The scene of the game opens up in the 'Aven's Care Hospital' room where it is overseeing the background, only the character 'Louis' will be present for this section."
    
    "Louis finds himself in familiar surroundings once again, the sort of artificial smell that he can't tell if it's good or not for his body- feels his lungs."
    
    "As the Canary stays perched on the side of his resting loved-one, reading out to them as a sort of way to keep the liveliness, well, alive despite the silence and tranquility."
    
    show louis normal at tinthospital
    l "Oh, this part is good."
    
    "Louis scoots over, showing his resting mother the book he's reading out to her."
    
    show louis happy
    l "Hear this one, 'I would recognize you in total darkness, were you mute and I deaf- I would recognize you in another lifetime entirely-'"
    
    show louis anxious
    l "'I would search for you until the very last star in the sky burnt out of oblivion...', such a good one liner for a tragic... tale."
    
    "Louis smiles somberly at the thought, glancing at the sleeping figure with a fond look."
    
    "The Canary closes the book on the chapter he last read on, placing it back into his bag filled with wonders as his attention is back on the resting figure."
    
    "Louis thought that the cold, plain white room was a bit unsettling to him, originally- he was going to bring the flowers back to his wife; but his mother's patient room could use a bit more color."
    
    "Especially when both him and his wife the hospital as their second home ever since his mother fell ill."
    
    show louis normal
    l "I bought you a gift again, consider it...something from your son and your daughter-in-law."
    
    "Louis smiles as he gently places the bouquet of flowers into the pot now that he had previously cleared the withering roses from before."
    
    show louis happy
    l "These are...sweet peas, now that I'm looking at it!"
    
    "Louis chirps up happily upon realization."
    
    show louis normal at tinthospital3
    l "While it's not the colors you would've wanted...it's still your favorite."
    
    "Louis goes to perch beside the sleeping figure once again, idling about with a light sway until he hears the door to the room open."
    
    show aziel confused at tinthospital2
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
    
    stop music fadeout 3
    scene black
    with dissolve3
    $ quick_menu = False
    show devlog01 at truecenter
    $ renpy.pause(91.0, hard=True)
    stop movie
    $ quick_menu = True

    $ day = 3
    jump day_3



#######################################################
#                   DECISION LABELS                  #
#######################################################


label _bellbirds_suspicion:
    
    "At the sound of Aven's boisterous voice, Louis jolts, startled at the sudden loud sound before he eases up again once he hears his boss' booming laughter."
    
    "Aven subtly raises a brow at Louis' rather jittery movements, slinging a wing around his shoulders, the bellbird spoke to him with concern in his voice."
    
    show aven questioning at shadow2
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
    
    show louis anxious at shadow3
    l "I think I saw some things I wasn't supposed to see..."
    
    "Louis smiles awkwardly as he rubs the nape of his neck with his wing, averting his gaze."
    
    "Aven stares at him with a tilted head."
    
    show aven questioning at shadow2
    a "And what exactly did you see-?"
    
    "Louis feels Aven probe at him as he asked, he could feel the bellbird's intense gaze at him."
    
    jump the_truth


label deny_anythings_wrong:
    
    "Louis stands still as his eyes meet Aven's head-on, being like that for a moment."
    
    "Before he breaks away the stare first."
    
    "Louis shakes his head promptly, almost insistently."
    
    show louis anxious at shadow3
    l "I-I just knocked over some stuff-"
    
    "Louis' laughs come out a bit loud- an awkward edge to it as his laughs trails off with a sudden stop."
    
    "Louis could feel the bellbird's stare at him, as if his gaze was chipping away at his demeanor, seeing through his lies and into the truth within his soul."
    
    "Louis felt less sure about himself."
    
    "Louis clears his throat, muttering an apology under his beak."
    
    "Aven squints his eyes at Louis, his suspicion growing under Louis' unusual behavior."
    
    show aven neutral at shadow2
    a "Nobody's gonna burn you alive if you tell the truth, son."
    
    "Louis could feel Aven's reassuring wing on his shoulder, glancing up at him- meeting his gaze, the bellbird's smile reassuringly."
    
    "He was telling Louis 'it's okay, I'm not gonna get mad.' from his gaze alone."
    
    menu:
        "THE TRUTH":
            jump the_truth
        "DENY DENY DENY":
            jump deny_deny_deny


label the_truth:
    
    show louis scared at shadow3
    show aven questioning at shadow2
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
    
    show louis anxious at shadow3
    l "I-It's fine, sir- it was really just that."
    
    "Louis persists, repeating his words of certainty to Aven."
    
    "Aven continues to watch him, like a hawk to a prey as it clicks to him-"
    
    "Louis lies to him, insistently."
    
    "Louis shifts on his talons once a while, uncomfortable with the growing tension despite the lack of words said."
    
    "Louis dares meet Aven's gaze again-"
    
    "Eyes that were already boring back at him, without a sight of a blink."
    
    show aven thinking at shadow2
    a "...if that's your truth, Louis."
    
    "Louis winces lightly at the change of tone, the sound of his name."
    
    "Aven reaches his hold on Louis again, almost dragging him on his feet when he ushers him out."

    jump day_2_continuation


label peregrine_interaction_2:
    
    show louis happy at tint3

    "Louis finds himself in the sight of the familiar Falcon once again, this time- he does not hesitate to approach."
    
    "He calls out to him,"
    l "Catcher!"
    
    "Waving his wing to catch his attention as he walked towards him, the usual bright smile plastered on his beak as he faces Catcher's permanent scowl."
    
    "Catcher bows to Louis in greeting, tilting his head at his chirpy attitude."
    
    show catcher confused at tint2
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
    
    show catcher neutral
    "........."
    "......"
    "..."
    
    "The Falcon's continued silence keeps the Canary talking."
    
    show louis normal
    l "-One thing for sure, our boss and that local doctor... they know each other past default pleasantries."
    
    show louis anxious
    l "Something tells me they've worked with or for each other before, though I don't assume much- I chose not to see the entire thing."
    
    
    "Louis feels Catcher's watchful gaze on him, but he knows- the Falcon knows better than to probe."
    
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


label investigate_the_figure:

    stop music fadeout 1.0

    show BlackBars zorder 9

    show deadanim zorder 10 at scarypos
    #show dead2 onlayer effect at truecenter
    #with { "effect": dissolve2 }
    "Louis approached the figure cautiously, unsure of what to expect but he always had the curious spirit in him that told him what he shouldn't be doing." 
    
    "Yet he proceeded anyway, the figure came more into view as he walked."
    
    show louis normal at tint6
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
    
    show louis anxious
    l "O-Oh! W-We were? My-My apologies..."
    
    "A part of Louis thought to himself, was this an evil spirit his mother spoke of? He had never interacted with them before, an unfamiliar face so to say- but then again he's assuming again."
    hide deadanim with dissolve1

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
    
    $ half = 0.5
    scene acorn street
    show magic trick 1 at magicpos

    "???" "I was just showing you a magic trick, friend!"
    
    show magic trick 2 at magicpos
    
    "The Crow spins around on its talons as Louis watches, it did this a few times before it stopped, facing him once again."
    
    show magic trick 3 at magicpos

    "It huffs his chest as it closes its eyes, its chest bubbling up- ridiculously big."
    
    show magic trick 4 at magicpos

    "Louis takes a step back instinctively, his naturally cautious being acting ahead of him, but he watches on to cater his curiosity."
    
    show magic trick 5 at magicpos

    "The Crow opened its eyes as it looked down on the Canary."
    
    "???" "Ready?"
    
    "Louis nods, despite his cautionary stance, he lets it proceed."

    show magic trick 6 at magicpos
    
    "The Crow smiles as it continues, its chest bubbling up like a hot air balloon on an open summer day- casting a shadow before Louis as its size grew."
    
    show magic trick 7 at magicpos

    "And before Louis knew it- the bubbled up chest exploded, from his beak came a rainfall of stars and fireworks."
    
    "Like a magic trick."

    show magic trick 8 at magicpos
    
    "Louis watches the sky in awe as a whimsical shower of colors dawns onto him."

    show magic trick 9 at magicpos
    
    "Louis looks back at the Crow that admired its handiwork, its stare blank but its smile big and proud."

    $ half = 1
    scene acorn street
    show lightoverlay
    show blackbars zorder 10
    with dissolve3
    
    show louis normal at tint3
    show crow default at tint2
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
    hide crow normal
    
    "The Canary leaves promptly- hurriedly on his talons, as if something in him clicks; an understanding he had not connected the dots before."
    
    #The 'INVESTIGATE THE FIGURE' option approach will still be available if the player chooses the 'DELIVER TO LILY' interaction first, the only difference?
    #'Louis' won't be able to mention it to Lily and have extra dialogue accessed.

    play music "music/CC Main Story Dialogue Theme.wav" fadein 3 fadeout 3

    menu:
        "DELIVER TO LILY":
            jump _deliver_to_lily_01
    
    # menu:
    #     "LILY TASK CONCLUSION":
    #         jump _lily_task_conclusion
    #     "DELIVER TO LILY":
    #         jump deliver_to_lily
    #     "DELIVER TO LILY 0.1":
    #         jump _deliver_to_lily_01

# label deliver_to_lily:
#     menu:
#         "DELIVER TO LILY 0.1":
#             jump _deliver_to_lily_01
#         "DELIVER TO LILY 0.2":
#             jump _deliver_to_lily_02

label _deliver_to_lily_01:
    
    scene acorn street
    show lightoverlay
    with dissolve3

    "Louis recollects himself first before continuing, after that interaction with the Crow- he needed a moment to breathe and refocus."
    
    "Standing at the front door of the blue house, Louis raised his wing and knocked, softly at the wood."
    
    "Louis waited for a moment."
    
    "Until he heard light shuffling coming from the inside, and soon... the door opened."
    
    "The Canary is greeted by a beautiful shade of blue, a Lovebird specifically a Cerulean Budgie, who welcomes him with a loving smile."
    
    "???" "Ah, you must be the courier I've been expecting?"
    
    show lily happy at tintlily
    "The budgie extends a wing in which Louis happily takes with a firm graze."
    
    show louis normal at tint3
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
    
    hide lily neutral
    hide louis happy
    show bouquet
    "Louis watches as Lily sets the bag elsewhere for now."
    
    hide bouquet
    show louis happy at tint3
    show lily neutral at tintlily
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
    
    show lightoverlay

    "Louis recollects himself first before continuing, after that interaction with the Crow- he needed a moment to breath and refocus."
    
    "Standing at the front door of the blue house, Louis raised his wing and knocked, softly at the wood."
    
    "Louis waited for a moment."
    
    "Until he heard light shuffling coming from the inside, and soon... the door opened."
    
    "The Canary is greeted by a beautiful shade of blue, a Lovebird specifically a Cerulean Budgie, who welcomes him with a loving smile."
    
    show lily neutral at tint2
    "???" "Ah, you must be the courier I've been expecting?"
    
    "The budgie extends a wing in which Louis happily takes with a firm graze."
    
    show louis normal at tint3
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

