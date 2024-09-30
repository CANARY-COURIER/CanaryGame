
label catcher_day_one:

    $ half = 2
    $ day = 1
    $ quick_menu = True

    scene bedroom blur
    with dissolve3
    # faded bedroom
    play music "music/CC Horror 2nd Half.ogg" fadein 2 fadeout 2

    no "As Catcher peels his eyelids open, his head throbs, a blaring headache that makes his vision go blurry, he balances himself, looking around the dark room he assumes he's in."

    no "With the rough textured feeling of the floorboards beneath him, the Falcon gets used to where his talons stand."
     
    no "Stumbling around the room, his wings grazes the walls, searching for the light switch as he grunts after bumping into something at the side of him."

    no "The small switch is almost missed by the Falcon, with a firm grasp on the walls, Catcher flickers the switch open, revealing the scene to be... a bedroom?"

    scene bedroom
    with dissolve3

    ca "Where the... shit am I...?"

    no "The Falcon mutters to himself confusingly."

    no "Catcher looks at his side, now seeing that the object he had bumped into was a perching chair. He continues to glance around the room, taking note of every detail."

    ca "This is certainly not {i}my{/i} room."

    no "The Falcon walks around the room quietly, careful in his movements."

    no "The spacious room catches his attention the most, filled with the typical items like a bed, a stool, a bedside table with an old lamp, nothing to Catcher was clicking in the slightest."

    no "His eyes wander, taking in the sight of two doors in his view."

    no "The Falcon assumes one door leads down, while the other goes up."

    jump attic_basement_choice

label attic_basement_choice:
    scene bedroom
    menu:
        "THE ATTIC":
            jump attic_exploration
        "THE BASEMENT":
            jump basement_exploration


label attic_exploration:

    scene bedroom attic
    with dissolve1

    no "The Falcon chooses to go up."

    no "Catcher pulls on the string attached to the ceiling, he assumes this should be the door that opens up the hatch that leads to the room above."

    no "The attic door opens, as Catcher drags the stringed door down, stairs were quickly unfolding before him, a loud, creaking sound following it that fills up the unsettling ambience that surrounded the room."

    no "With a loud thud, the entrance to the room is revealed to the Falcon, he looks up momentarily; the darkness from above is the only thing he can see."

    no "Still he persists, climbing up the staircase slowly, his hesitance creeps in."

    no "He peeks his head through the hatch, eyes scanning around the dark room before ascending further."

    scene attic
    with dissolve3

    no "The dim lighting from below and the lone window on the end of the room  barely provides any solid clearance on what Catcher is looking at when he steps his talon in the attic, his eyes gazing around."

    no "But it was only filled with old boxes and sheet-covered items."

    no "Roaming around the room for something, Catcher's eyes land on something that piques his interest."

    no "The Falcon walks over to the side of the attic, tilting his head as what looks like a frame of a painting."

    no "Upon further inspection, Catcher drags the white sheet that covered a portion of the frame to reveal what hides underneath-"

    no "As suspected, the frame indeed revealed a picture. Not quite a painting from how it feels under Catcher's talons, but it showed him something that made his brow muscle raise."

    no "Before him was a portrait of a familiar Bellbird and Owl, Aven and Aziel were right there; wing to wing right next to each other with big smiles on their beaks."

    no "Catcher took note of the way the portrait looked, professional, clean and- both wearing similar articles of clothing."

    no "The Falcon snickers in disbelief."

    ca "Of course, they're related."

    no "The Falcon turns to look at the rest of the room, peeking through boxes as he moves away from the portrait only to be greeted with nothing."

    no "He decides to leave and go back down."

    jump attic_basement_choice


label basement_exploration:

    scene bedroom basement
    with dissolve1

    no "The Falcon chooses to go down, an exhale of a deep breath follows as he isn't so fond of the complete darkness he knows will greet him."

    no "Catcher approaches the door that separates him and the other room, staring at the knob as he thinks carefully if he should go through with this or not."

    menu:
        "PROCEED":
            jump basement_proceed
        "GO BACK":
            jump attic_basement_choice

label basement_proceed:
    scene basement
    with dissolve3

    no "Putting on the little courage he has, he twists open the door knob, revealing to him a staircase leading down as he had suspected."

    no "Catcher takes in the sight, how ominous it all felt to him."

    no "The Falcon can feel his feather lightly being brushed by the window coming from behind him, the ambience that reeked from below, the void that stared back at him as he stood in that doorway."
    
    no "For a moment, he hesitates again; whether he should continue or not."

    menu:
        "PROCEED":
            jump basement_proceed2
        "GO BACK":
            jump attic_basement_choice

label basement_proceed2:

    no "The Falcon ventures forth, continuing into the darkness of the room below."

    no "The floorboards of the stairs make an uncanny creak whenever Catcher's talons continue to descend, the lack of lighting making his eyes strain and lose focus."

    scene basement2
    with dissolve3

    no "As Catcher reaches the end of the staircase, he is greeted by a light switch when, upon flickering it open, only provides a dim enough light to illuminate a portion of the basement room."

    no "The room itself wasn't inherently special as the room above. All Catcher could make out was a couch and a coffee table, some shelves behind it but it was pretty much empty... abandoned sort of way."

    no "Observing a bit more as his eyes squint through the door room; his talon bump into something that moved across the ground."

    no "Perching down to feel whatever it was he had kicked, he feels a square-shaped item as he picks it up with his talons."

    no "Upon further inspection, it appears to be a cassette tape."

    no "Searching through the darkness- the room provides a small box television."

    no "Holding the cassette tape and putting one and two together, Catcher approaches the little DVD box that's stationed just right next to the television."

    scene black
    with dissolve3

    call screen tape

    $ quick_menu = False
    show arguement at truecenter
    $ renpy.pause(139.0, hard=True)
    stop movie
    $ quick_menu = True

    scene black
    with dissolve3

    no "The tape ends and Catcher is left standing frozen on the spot, lost in thought on whatever it was he just watched."

    no "Unsure of what to make of it all, he buries the tape deep in his mind, turning to leave the basement."

    jump done_exploring

label done_exploring:
    
    scene bedroom
    with dissolve3

    no "The Falcon decides to venture out of the bedroom and beyond what the house has to offer."

    no "He has seen and found enough, deciding there was nothing left to explore; he wanders through the house seeking its exit."

    no "There wasn't much. Due to the small amount of space to move in the house in general, it was just the same repeating four corners on where Catcher could walk and fit himself in."

    no "With his eyes on the ground, eventually he finds the light, his temporary euphoria. Stumbling out of the doorway with a light huff on his talons."

    no "Exiting the house with a soft 'click' of the door behind him."

    jump go_outside

label go_outside:

    scene corrupted outside
    with dissolve3

    ca "Is this... {i}a nightmare{/i}?"

    no "The Falcon asks no one but himself."

    no "Catcher looks around the dull street, the dead leaves of autumn's embrace colored the concrete with little to no movement from the wind."

    no "The sight of the orange forest beyond the houses haunts his spine, sending a shiver and a tingle he suddenly feels down to his talons; he takes a step back to compose himself and to still his breathing."

    no "At a final glance around the area leading him to no bird in sight, he settles to fly somewhere else, where he'll know he can have a bird to chirp with."

    #The game transitions back into the 2D platform view of the world, wherein the character 'Catcher' is shown in front of the main 'Acorn Street' background.
    #The game should highlight the 'Map' for this section, and the player can choose to only access the town street: 'Cornfield City'
    #Travel to: A ghost town

    no "Catcher glances at his surroundings taking it in as something he is all too familiar with, he wanders around aimlessly with no direction, feeling alone."

    no "He decides to go to places that would usually be crowded with people."

    no "The Falcon strolls with an emotionless look on his face towards two areas he's familiar with: the Flyway Superstore, and the Avian Care Hospital."

    no "He decides to go to the Flyway Superstore first."

    #While the game allows the player to explore 'Cornfield City', but a text or dialogue should pop up (Catcher: No, I don't want to go here.)
    #if the player chooses to go to the other locations not stated in the choices.

    jump corrupted_superstore

label corrupted_superstore:

    $ half = 2
    $ quick_menu = True
    scene corrupted store
    with dissolve3

    show BlackBars zorder 10

    no "The Falcon approaches Flyway Superstore, with the buzzing lights of the signage above greeting him eerily, entering the building as the glass doors with chimes close behind him."

    no "Catcher feels a chill. The lack of life makes him stand lonely and uneasy."

    no "Standing in what once a bustling area filled with chatter and the sound of walking reduced to nothing but... him, makes him feel unsettled."

    no "Catcher sighs under his breath, trying to compose himself as the tense atmosphere dawns on his body."

    no "Walking along the long cold isles of the Superstore to each with their own isolated batch of food supplies, the sound of the blaring lights above echo throughout the vicinity."

    no "The Falcon couldn't shake off the heavy feeling that weighed on him."

    no "The deserted Superstore only serves to haunt him of his thoughts rather than soothe it, turning to leave, he stops dead on his tracks, catching sight of a familiar bird in view."

    no "Catcher recognizes her all too well, Ivory, the blue mockingbird that once... held his attention."

    no "As he approaches her, his talons move methodically, following one goal in mind as the sight of her consumes his empty thoughts."

    no "But what once was a happy-chirp of a bird, the Ivory that stands before Catcher was barely a shell of what he thought of her that for a moment he said to himself... is this really her?"

    show catcher happy 2 at slightleft
    ca "Ivory? Miss Ivory?"

    no "The Falcon approaches casually, despite his weary state, he masks his uneasiness with an unnatural looking smile."

    no "The mockingbird looks up to the Falcon, with eyes as soulless as the colors of her feathers."

    show ivory normal 2 at slightright
    iv "Yes?"

    iv "Do you need assistance with anything?"

    no "Ivory politely asks, as if reciting a routined script."

    no "Catcher shifts on his talons, feeling a twitch in his brow muscle as she speaks."

    ca "How are you?"

    no "The Falcon asks, his question coming off more as a demand."

    no "Ivory's gaze falls on the floor, saying nothing until she looks up at him again."

    show ivory sad 2
    iv "I'm fine."

    iv "I have no reason not to be anything but fine, I'd think?"

    no "Ivory replies, uncertain in her tone, staring back at the Falcon."

    no "........."
    no "......"
    no "..."

    show catcher sad 2
    ca "Of course."

    ca "You're right."

    no "........."
    no "......"
    no "..."

    no "Catcher shifts again, the silence for once, unsettling him."

    show catcher normal 2
    ca "I've missed you."

    no "Catcher puts it down bluntly, the stare lingering head on."

    ca "I've missed our time together."

    no "Catcher takes a step towards her, his stance coming off strong."

    no "Ivory freezes, the mockingbird breaking her gaze from him."

    show catcher sad 2
    ca "Don't you want it too? The time we spent together?"

    show catcher happy 2 at slightleft
    ca "It was fun, wasn't it."

    no "The Falcon's voice strains, his tone coming off flat and obsessive almost, paired with the stare down he gave the mockingbird."

    no "Catcher takes a step forward."

    no "Ivory takes two steps back."

    show ivory angry 2
    iv "It wasn't."

    iv "Don't mistake my consideration for kindness, Catcher."

    no "The mockingbird defends, her stance weary and guarded."

    show catcher angry 2
    ca "Oh {i}come on{/i}, you don't mean that."

    show catcher sad 2
    ca "I never-never saw you as anything like I should be taking advantage of or anything-"

    no "The Falcon puts his hands up, as if surrendering yet his talons reach out towards her, as if being close to her will soothe him."

    iv "Maybe not me, but you still did what you've done!"

    no "The mockingbird snaps at him, her voice filled with disdain."

    no "Catcher flinches at her tone, his brow muscles knitted together in confusion."

    show catcher angry 2
    ca "What I've done? What-What do you mean? What could I have possibly done for you to speak to me {b}this way{/b}."

    no "The Falcon's voice continues to be strained, what should be the tone of confusion came off as hostile, demanding and thunderous."

    no "The mockingbird's gaze hardens, her eyes squinting at the Falcon's display."

    iv "Oh don't act clueless, you know what {b}you've done!{/b}"

    iv "To me- to my benny, you-you're a {b}MONSTER{/b}."

    no "The mockingbird feigns a lunge at the Falcon, Catcher instinctively recoils."

    ca "What-I did nothing to him! I don't even know what you're ACCUSING me of-?!"

    iv "Oh- {b}you did nothing{/b}, of course you'd say that! You don't even remember {b}WHAT YOU DID{/b}!"

    show ivory normal 2
    iv "{b}Let me remind you!{/b}"

    no "The mockingbird was quick in her movements- shoving a paper in Catcher's direction, forcing him to grasp on it firmly,"

    no "sending him tumbling back lightly from the impact, staggering his movements as he looks down on the paper that was forced onto his talons."

    scene corrupted store blur
    with dissolve2

    call screen bennynewspaper

    show newspaper text
    no "The Falcon's eyes widened at the contents of the newspaper as he read on:"
    hide newspaper text

    no "Catcher looks up from the newspaper article, meeting the mockingbird's eyes."

    ca "I-I don't understand-what does this have to do with anything-"

    ca "This has {b}nothing to DO{/b} with me?!-"

    show ivory angry 2
    iv "-This has {b}EVERYTHING{/b} to do with {b}YOU{/b}."

    no "The mockingbird moves, jabbing her wing dead center into the Falcon's feathery chest."

    no "Jabbing him again, and again-"

    no "And again."

    no "With each intentful jab, her movements became more rigid, the emotions finally catching up to her as her words slice through his soul like a knife."

    #play music "music/crying woman.wav" fadein 2 fadeout 2

    show ivory sad sad
    voice "voice/i1.wav" 
    iv "You took him {b}away from me{/b}-"

    voice "voice/i2.wav" 
    iv "I will {b}never{/b} get to see him again {b}because of YOU{/b}."

    no "The mockingbird's talons claw at the Falcon's chest, grabbing- begging, trying to release the sorrow in her voice."

    scene corrupted store dark
    show ivory sad sad sad
    voice "voice/i3.wav" 
    iv "{b}YOU TOOK HIM AWAY.{/b}"
    voice "voice/i4.wav" 
    iv "{b}YOU TOOK HIM AWAY.{/b}"
    voice "voice/i5.wav" 
    iv "{b}YOU TOOK HIM AWAY.{/b}"
    voice "voice/i6.wav" 
    iv "{b}YOU TOOK HIM AWAY.{/b}"
    voice "voice/i8.wav" 
    iv "{b}YOU TOOK HIM AWAY.{/b}"

    voice "voice/i9.wav" 
    no "The cries of the mockingbird repeats, haunting his being, tainting his soul, over and over- like a broken record."

    voice "voice/i10.wav" 
    no "Ivory repeats, unresponsive to whatever else the Falcon chooses to say or do, with her woes echoing through the building- he leaves quickly."

    no "Exiting the vicinity with nothing but a mortal reminder of her sorrow."

    stop music fadeout 3

    jump the_crow

label the_crow:

    scene corrupted outside
    with dissolve3
    show BlackBars zorder 10

    play music "music/CC Horror 2nd Half.ogg" fadein 2 fadeout 2

    no "The Falcon's steps are broad and rigid, the effects of the Superstore encounter still present in his feathers as Catcher makes his way to the neighboring hospital to seek the solstice of a familiar friend."

    no "His talons finds itself in the front of a dimly lit building, a place that feels unrecognizable to his eyes yet a part of himself resonates with."

    no "The surroundings of the building was overgrown with weeds and plantation, a lone bench sitting in the middle of all the lived-in moss that crawled up the walls."

    no "The Falcon's eyes gazing on the bench, his stare lingers and as if he manifested his reality true-"

    no "His friend sat perched by the entrance, the crying crow watching the scenery around it, the empty road that leads to everywhere yet nothing at all."

    no "Catcher approaches quietly, perching himself right beside the crow, glancing at him wearily. The Falcon's breathing remains unsteady and sporadic, still calming himself down from earlier events."

    show crow default 2 at slightright
    cro "Catcher? Are you okay?"

    no "The crying crow shows his concern, turning his complete attention towards the Falcon."

    no "Catcher meets the white void of the crow's eyes, nodding quickly, shaken up and confused still."

    show catcher sad 2 at slightleft
    ca "Y-Yes I'm-I'm fine."

    no "The Falcon stills his breathing, yet his appalled resolve is still visible on his face."

    show catcher normal 2
    ca "You're- You're alright, right? Like,"

    ca "You're here, breathing, with me. Right?"

    no "The crow tilts its head on him, its expression dull and soulless, but its intentions say otherwise."

    show catcher sad 2
    ca "Benny, please answer me."

    no "The Falcon pleads softly, the crying crow- Benny responding with a nod."

    b "Yes, of course I am!"

    b "Where else should I be?"

    no "The crow laughs, dry and croaked, but the tone of its voice feels like it would've sounded kind, playful- childlike."

    show catcher angry 2
    ca "Then-Then what does this mean?"

    no "The Falcon brings up the newspaper from before, showcasing it to the crow, his voice laced with concern and fright."

    no "Catcher shares the newspaper article, about the crow's supposed murder, letting the crow read over his shoulder about the contents that filled the paper; its eyes unreadable and blank..."

    no "Until it turns to look at Catcher."

    b "T-That's... wow... Are you okay?"

    no "The crow asks Catcher, showing the little worry his face can muster up."

    show catcher sad 2
    ca "Y-Yeah, I think so... it's-it's Ivory..."

    b "Do you wanna tell me what happened?"

    no "The crow asks lightly, careful not to probe or overstep the shaken up Falcon."

    no "Catcher meets Benny's eyes, trying to find comfort in the sea of nothing."

    show catcher angry 2
    ca "I just- I don't- understand why your sister- why {b}Ivory{/b} would accuse me of- of doing {b}this{/b} to you."

    no "If the Falcon could try a bit harder, then maybe... he would finally be able to show his true feelings."

    b "I-I- I don't know..."

    b "Do you think she just... mistook you for someone else, K-Catcher?"

    no "The crow's attention on the Falcon was full and intense, its gaze remained connected to Catcher the whole time."

    no "Catcher looks at his dear friend, confusion and frustration building up in him."

    show catcher sad 2
    ca "I don't know, I really don't-"

    ca "Ivory- She sounded so... so {i}sure{/i} and genuine..."

    no "The Falcon keeps the crow's stare."

    ca "I doubt... she'd mistake anyone for that..."

    no "The Falcon's voice comes off as a whisper, his eyes trailing to the ground, tone- filled with vulnerability and turmoil."

    hide catcher sad 2
    show crow default 2

    b "It's okay, Kane."

    no "Catcher stiffens, hesitantly meeting the crow's gaze."

    no "........."
    no "......"
    no "..."

    b "She just mistook you for a little boy..."

    $ quick_menu = False
    b "{b}Don't you remember?{/b}"

    show blackopacity zorder 101 at truecenter
    with Dissolve(7.0)
    pause 7.0
    stop music
    show crow snapped neck
    pause 1.0
    show crow default 2
    show black
    with Dissolve(4.0)

    $ quick_menu = True
    no "Catcher jolts, startled from the initial panic that starts to seep back through his system. Entering the hospital to get away from Benny or whatever it was he just saw."

    no "He feels like a memory is popping back in his head, one that's been haunting him for years, forgetting it for a while until it comes back to taunt and remind him of his sins."

    no "Catcher is becoming more and more panicked as these events unfold, he doesn't remember what took place during those times and thinks these were all just bad dreams."

    no "Yet suddenly now they felt so real to him."

    stop music fadeout 3

    jump the_hospital

label the_hospital:

    scene hospital
    with dissolve3
    show BlackBars zorder 10

    play music "music/CC Somber Hospital Theme.wav" fadein 2 fadeout 2

    no "The Falcon drags his talons across the dark and long empty hallways of the hospital, unease and terrified to the tail, Catcher searches around for nothing but confusion and a cry for help."

    no "The glitching fluorescent lights and the smell of an overused air purifier fills his nose, feeling nostalgia from the aroma, a regular scent that his system got used to unhealthily so."

    no "Only the sound of the buzzing lights from above fill the silence in the hallways, The Falcon continues to walk, reaching a dead end or an ominous patient room he refuses to go to;"

    no "Somehow, he finds some bird present."

    no "As he enters a new hallway his eyes settle on a figure at the end of the room, his eyes squinting, adjusting to the bright light illuminating above him as he approaches hesitantly."

    ca "Hello?"

    no "The Falcon calls out to the figure."

    no "His voice bounces off the walls, echoing throughout yet he receives no response."

    no "Catcher continues on, approaching the face of the figure becoming knowing to him, despite his hesitance there was a sense of urgency in his movement;"

    no "The uneven breathing and a thirst to solve his issue plaguing his mind."

    no "Standing before him, was the face of a Bellbird- the same one he carried out tasks to, even the ones that were unethical enough for him to speak of."

    no "The Bellbird looks older compared to the time the Falcon saw him. An alarmed yet concerning look on his face as he watches Catcher's panic-stricken behavior."

    no "The Falcon spares no time to seek answers, desperately trying to calm himself with a talon over his chest as he speaks."

    show catcher happy 2
    ca "Thank-Thank Phoenix, {i}you're here{/i}."

    no "The Falcon grasps on the Bellbird's arms, a face of relief dawning his face."

    no "Catcher's confusion remains, a growing agitation building up as his confusion lingers."

    show catcher sad 2
    ca "What's-What's happening to me?"

    ca "Why are there voices in my head {i}crying to me{/i}?"

    no "The Falcon pleads, his grip tightening over the Bellbird's feathers."

    ca "This-This isn't normal- why are the birds around me tell-telling me something that isn't real-?!"

    ca "What's {b}WRONG{/b} with me?!"

    no "Catcher's voice trembles and breaks, afraid and confused like a chick asking for its mother."

    show catcher angry 2
    ca "Why can't I answer {b}ANY{/b} of what they're telling me?!"

    ca "{b}WHAT HAVE {i}I{/i} DONE-?!{/b}"

    no "The Bellbird flinches, the spat that came out of the Falcon's beak was raw and grounding."

    no "Aven clenches his jaw -"

    no "........."
    no "......"
    no "..."

    no "Yet his words weigh like nothing is wrong."

    show catcher angry 2 at slightleft
    show aven neutral 2 at aven2pos
    av "You did nothing, you've done {b}nothing.{/b}"

    av "Kane, you're fine."

    no "The Bellbird's choice of words was picked apart- meticulous and careful on how he should proceed."

    no "The Falcon caws out a frustrated jeer."

    show catcher sad 2
    ca "-Why does every bird keep calling me that-?! Who is Kane-?!"

    show catcher angry 2
    no "Aven moves to hold Catcher down by the shoulder, grounding him on the pristine floors of the hospital."

    show aven sad 2
    av "Shhh..."

    no "The Bellbird shushes the Falcon, calming him down methodically."

    ca "What's happening... Am I okay, Aven? {b}AM I OKAY-???{/b}"

    no "The Falcon's words swallow and croak."

    show catcher sad 2
    ca "Tell me, Doctor- Pieter, {b}tell me{/b}."

    no "Catcher begs, his words coming out a slur, he's not entirely sure what he's saying anymore."

    ca "{b}What are the voices telling me? What do my dreams mean?{/b}"

    no "The shudder and cling of the Falcon's movements never wavering with desperation."

    show aven confused 2
    av "{b}There is no reason for you to not be fine.{/b}"

    no "Aven's words ring a reminder."

    show aven happy 2
    av "You're {b}special{/b}, Kane. {b}You're special{/b}."

    no "The Bellbird cradles the weeping Falcon in his wings, how he soothes his shaking with a fatherly pet, shushing him down and tending to his lonesome body."

    show aven neutral 2
    av "You have to take these, so you can stay {b}fine{/b}."

    no "Piete feigns reassurance in his tone as he hands Kane vials of medicine."

    hide aven netraul 2
    hide catcher sad 2
    scene hospital blur
    call screen pills

    scene hospital

    show BlackBars zorder 10
    show aven neutral 2 at aven2pos
    show catcher sad 2 at slightleft
    av "There's {b}nothing wrong{/b} with you, okay?"

    show aven happy 2
    av "You've just got to manage your illness, {i}big doses{/i}, got it?"

    no "The Bellbird pats the Falcon gently as he spoke close for him to whisper into his ears."

    show aven neutral 2
    av "I don't want you coming back here now just because you stopped taking them, hm?"

    show aven happy 2
    av "You were doing so, so well with them before."

    no "Pieter pats Kane firmly on the back."

    no "The Bellbird urges the Falcon to consume what he gave him-reassured that this is the only way to get better."

    no "In spite of Catcher's desperate efforts and need to find resolve, he hesitates, looking at the Bellbird worryingly like- like he doesn't believe these specific medications were helping him."

    ca "But-But I've felt better without these, I was fine!"

    ca "I should be {i}cured{/i}, right, Doctor?"

    ca "By why {i}aren't{/i} I-?!"

    no "A Look of horror dawns on the Bellbird, shaking the Falcon by the wings urgently as he speaks."

    show aven confused 2
    p "You've... stopped taking... them?"

    no "The Falcon forces himself to nod hurriedly."

    show aven angry 2
    p "You... You foolish boy- always the {b}troublemaker{/b}!"

    no "The Bellbird pursues again, taking matters to his own wings."

    no "The Falcon stumbles back, feeling his beak forced open as the sickly, familiar substance starts to drown his throat with the bitter flavor, sending his mind afloat."

    no "His throat struggles to swallow, the sound of a bubbling gargle fills the once soundless halls with Catcher's struggle as he chokes and sneers."

    p "This is a part of the routine, you mustn't stop taking them unless you are told {b}not to{/b}!"

    no "The Bellbird spats in frustration as the Falcon breaks free from his hold-"

    #BACKGROUND DARKER + BLURRED except for catcher
    no "Catcher's heavy breathing as he tries to recollect his thoughts, his body wavers, his mind stirs as he struggles to take a good look at the Bellbird."

    show catcher sad 2
    ca "Don't..."

    no "The Falcon's gaze shakes, the ground beneath him spinning with his thoughts."

    ca "...touch me-"

    no "A loud thud is the last thing the Falcon hears."

    scene white
    with dissolve3

    pause 1.0

    stop music fadeout 3

    stop music fadeout 3
    scene black
    with Dissolve(3.0)
    $ quick_menu = False
    show HAHA at truecenter
    $ renpy.pause(73.0, hard=True)
    stop movie
    $ quick_menu = True

    jump new_day_2_begin

label new_day_2_begin:

    $ half = 2
    $ day = 2

    scene daycare 2
    with dissolve3

    play music "music/CC Specific Scene (Piano).ogg" fadein 3 fadeout 3

    no "The Falcon peels his eyelids open, groaning at the throbbing pain coming from his head as he holds it in his wing."

    no "Catcher looks around where he is, he notices how he's tucked into one of the patient's rooms in the hospital."

    no "Deciding to leave and explore whatever had just happened to him, he stands up and heads towards the first door he sees that leads out."

    no "As Catcher walks around the long halls of the hospital that seems to be in good condition, the cleanliness of the floors is reflected with the bright light from above."

    no "Hearing only his talons, he notices no one else is roaming the halls with him, peeping through one of the doors with windows hoping to see some bird, yet all the rooms seem to remain empty."

    no "The cold long hallways filled with the smell of overused air fresheners feel nostalgic to him as he walks further and further down the hallways familiar to his jagged memory."

    no "Feeling like he's been walking down the same hall for quite a while, he pauses suddenly, hearing the faint laughter and mumbling of birds in the distance."

    no "It sounds like chicks, laughing and talking amongst themselves. Catcher approaches, picks up his pace and sees a door in front of him."

    no "He can tell the sounds are coming from behind this door so he calms his pace and listens closely, hearing some chicks cry and the others shout."

    scene daycare 1
    with dissolve1

    no "As he approaches the door and takes a peek through the little window, he sees young chicks, some barely in their teens, he guesses who are all in this one room."

    no "The nurses and caretakers to the side chatting amongst themselves."

    no "Some interact with the chicks, others just standing there watching the chicks although they seem to be almost asleep with their eyes open."

    no "His attention is taken by a nurse with a face who feels familiar to him."

    no "The nurse attentively watches two chicks play with a wide smile plastered across her face, while his mind is focused on why this nurse seems so familiar to him like he knows them."

    no "His eyes dance around the room searching for the chicks that the nurse has her attention on."

    no "His brow muscles knit together as his gaze hardens at the sight. He sees the same face that's been haunting him in his dreams."

    no "The young mockingbird chick's face slowly warped, changing itself to a young, blonde human child."

    stop music
    scene black
    pause 1.0

    play music "music/CC Specific Scene (Melodic).ogg" fadein 1 fadeout 2
    play sound "music/suffocation.mp3" fadein 5 fadeout 2

    show bennykane 1
    $ renpy.pause(4.0, hard=True)
    show bennykane 2
    $ renpy.pause(4.0, hard=True)
    show bennykane 3
    $ renpy.pause(4.0, hard=True)
    show bennykane 4
    $ renpy.pause(4.0, hard=True)
    show bennykane 5
    $ renpy.pause(4.0, hard=True)
    show bennykane 6
    $ renpy.pause(4.0, hard=True)

    scene black
    pause 2.0

    stop music
    stop sound

    no "Catcher's eyes widened."

    no "His cheeks feel a damp wetness as his wing grazes his face, realizing then- he's crying."

    no "Tears slowly stream down his face yet his expression is blank, this is memory... A memory he had forgotten either willingly, or not."

    no "He remembers their names... Benny, the friend that laid limp in his arms."

    no "Elise, Benny's sister who he vaguely remembers the way her hands violently yank his hair away from Benny's still body;"

    no "The torment in her cries, her scream repeatedly asking him: 'Kane- WHAT DID YOU DO?!'"

    no "Eventually getting separated by a group of nurses and care-takers in the area, seeing her disgusted and horrified eyes as she picks up her brother's lifeless body off of the ground while the children around him were sent into a panic."
    
    no "Crying layered one over the other deafening everyone's ears off."

    no "This memory... was the same 'dream' he had been having... the same one that haunts him to till this day-"

    $ half = 1.5
    show static at truecenter
    $ renpy.pause(2.0, hard=True)
    stop movie
    $ half = 2

    jump kill_your_darlings

label kill_your_darlings:

    scene hospital
    with dissolve3
    show BlackBars zorder 10

    play music "music/CC Somber Hospital Theme.wav" fadein 2 fadeout 2

    show catcher sad 2
    no "The Falcon snaps awake back to where he once was, again, he's tucked into one of the patient's rooms in the hospital."

    no "His head throbs like before, painful of what occurred as he recalls what happened. The Falcon vaguely remembers Dr. Aven forcing the same medications he's been taking for years down his throat."

    no "Catcher shudders remembering the memory. His body feels weak as he tries to stand on his talon from the bed, pondering to himself."

    show catcher angry 2
    ca "Why would I do that, did I really? Was that really me?"

    no "He breathes heavily, trying to understand it all."

    show catcher sad 2
    ca "Doctor Aven- Aziel... they said I'll be fine but why-why...there should be nothing wrong with me..."

    no "Questioning himself more as struggles to keep himself stable on his talons, dragging his movements towards the door."

    show catcher normal 2
    ca "I'm okay. {b}I'm okay.{/b}"

    no "The Falcon exhales."

    ca "I'm fine. I have medication, I'm doing {i}fine{/i}, so {b}I should be fine{/b}."

    show catcher sad 2
    ca "I wouldn't...I'm okay? I wouldn't do such a thing... why would I...?"

    show catcher angry 2
    ca "Did... they lie to me?"

    no "Catcher wobbles slightly in his step, grasping the wall as he tries to balance himself upright."

    show catcher sad 2
    ca "I was supposed to be {i}cured{/i}, I am better."

    ca "I should be better...why would he give me more-? They said I should take it...2 times a day, high dosage and-and..."

    show catcher angry 2
    ca "I {i}should{/i} be {b}FINE. WHY AM I {i}NOT CURED{/i}-?!{/b}"

    no "The Falcon stumbles."

    show catcher sad 2
    ca "Why would they lie to me..."

    no "A quiet sob to himself, Catcher takes the pills sitting by the table next to the door."

    no "His vision was too blurry to read the labels but he was able to make out that it had two manufacturing dates, 1958 and 1960s."

    scene hospital blur
    with dissolve3
    call screen pills2

    jump farewell_father_dearest

label farewell_father_dearest:

    scene hospital
    with dissolve2
    show BlackBars zorder 10

    no "Tears fall on the Falcon's face as his emotions slowly start draining his perception of everything."

    no "Walking slowly towards the door and keeping his balance the best he can, he twists the doorknob open."

    show catcher sad 2
    ca "There's two different labels on that container with different dates... what... were they giving me... all these years... am I okay-?"

    show catcher normal 2
    ca "Was this really all to cure me... {b}cure me of {i}what{/i}...?{/b}"

    show catcher sad 2
    no "His voice shakes as his suppressed emotions come out as he uncontrollably weeps while struggling to walk out the hospital room."
    
    show catcher angry 2
    ca "Where is he?"

    no "The Falcon mutters to himself, finding determination on what's really being done to him."

    no "The memory felt as real as it is, and it was his. The birds he knew in there- they were real, he knew their names, their relations- their lives."

    no "He knows now that what happened is his reality, but there were too many questions to be asked- he couldn't even trust {b}himself{/b}."

    no "The Falcon's pace quickens, the determined drive to find the Bellbird is at its peak. His curiosity grows, so does his anger."

    no "An unsettling feeling grows within his chest, a brewing hate mixed with bitterness and grinded teeth."

    show catcher angry 2
    ca "They {b}{i}lied{/i} to me.{/b}"

    show catcher angry 2 at slightleft
    show aven confused 2 at aven2pos
    show BlackBars zorder 10
    no "The Falcon almost sees red as the Bellbird enters his line of sight at the end of the hall."

    no "Angered at the mere sight of him, how his vision blurs from his reality to the warped reality in his head."

    scene hospital dark
    show catcher angry 2 at slightleft
    show aven burnt at aven2pos
    show BlackBars zorder 10
    no "The {color=#f00}burnt face{/color} of the Bellbird warps his vision."
    #scared text + functionality FIX THIS LATER ALE ALSO GLITCHED

    show aven confused 2
    no "Adrenaline builds through his body, the Falcon's jaw clenches as he feels the ends of his talon sharpen."

    no "He feels his chest burning. Discreetly under his wing, his talons clasp around the syringe of anesthesia he hid in his jacket."

    no "Approaching the Bellbird with a murderous intent."

    show catcher angry 2
    av "Kane-?"

    no "The Falcon strikes once the Bellbird is within reach- stabbing the syringe straight to the Bellbird's neck, his other talon making sure the old bird was captured in his hold."

    ca "{b}{i}You should have told your son who I was when you were still alive.{/i}{/b}"

    no "As Aven's body quickly reacts to the chemical being injected into him, Catcher holds the old Bellbird in his wings, as he skillfully reaches into his pocket for the Methanol and matches he keeps in his jacket."

    no "Drenching the Methanol on his feathers, letting the Bellbird fall to the ground as his body makes a flat 'thud', he ignites the match, mercilessly letting it fall on the Bellbird's feathers."

    hide aven confused 2
    hide catcher angry 2
    no "The Falcon  watches as the burning bird dances with the kindling flame rising."

    show catcher angry 2
    ca "Your brother did {b}the same thing{/b}."

    no "Catcher turns to walk past the unconscious, burning Bellbird."

    show hospital dark blur
    with dissolve3
    ca "Down goes the father, the mother of your son- may your wife's soul be blessed... and your brother."

    ca "{i}Monsters{/i} that walk this ground."

    no "The Falcon leaves."

    stop music fadeout 3
    scene black
    with Dissolve(10.0)
    $ quick_menu = False
    show evangeline at truecenter
    $ renpy.pause(82.0, hard=True)
    stop movie

    show black
    with dissolve3
    play music "music/CC End Credit Track.mp3" fadein 2 fadeout 2
    call screen credits_display

    return
