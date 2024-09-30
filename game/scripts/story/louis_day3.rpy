# louis_day3.rpy


#######################################################
#              DECISION + MECHANICS LABELS            #
#                  (With Subcategories)               #
#######################################################


########### QUEST MECHANICS ###########


# Quest Management (Update Checklists)
label _new_task_caught_on_camera_finale:
    
    #NEW TASK: CAUGHT ON CAMERA (Finale)
    scene aves courier center inside
    with dissolve2
    show aven neutral at tint2
    show louis normal at tint3
    
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
    
    scene aves courier center inside
    show broken camera
    "Louis opened the box without hesitation, untying the knot before he was greeted with what seems to be... a broken video recorder?"
    hide broken camera

    show louis scared at tint3
    l "Sir?"
    
    "Louis' voice held confusion with what he was holding in his wings as he searched the bellbird's face for an explanation."
    
    show aven neutral at tint2
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
    
    "This time, the list reads:"
    #The game opens up the Louis' checklist, reading the contents it spells out to the player exactly what is expected to be done.
    "{color=#8b593c}'DELIVERY FOR AVEN'{/color}"
    "{color=#8b593c}Aven has assigned a very special task just for Louis to complete, while for this task-{/color}"
    "{color=#8b593c}there is no time requirement to fulfill, he is tasked to help out 'Maverick' from the 'Feathered Fixer' Hardware to restore 'one (1) broken video recorder' back to it's new and working state.{/color}"
    "{color=#8b593c}- Visit 'Feathered Fixer' Hardware in 'Cornfield City'{/color}"
    "{color=#8b593c}- Talk with 'the repairman': 'Maverick'{/color}"
    "{color=#8b593c}- Fix the 'broken video recorder' with Maverick{/color}"
    "{color=#8b593c}- Check-out the 'fixed video recorder' from Maverick{/color}"
    "{color=#8b593c}- Leave 'Feathered Fixer' Hardware and go to 'Aves Courier Center'{/color}"
    "{color=#8b593c}- Find 'Aven'{/color}"
    "{color=#8b593c}- Deliver the fixed video recorder back to Aven{/color}"
    "{color=#8b593c}- Mark the task as: 'DELIVERED'{/color}"
    #############################################
    
    jump _the_fix_the_recorder


############ MAP MECHANICS ############


# 2d Platform Interaction
label _aven_task_conclusion:

    #The game transitions into the 2D platform view of the world, wherein the character 'Louis' is shown inside of Aves Courier Center.

    scene aves courier center inside

    "Louis paces around the office room, waiting for his boss, Aven, to show up for the video recorder he was tasked to fulfill."
    
    "The Canary kept thinking about the interaction with the Falcon from earlier."
    
    "A sense of worry and dread lingers in his system, making him overthink if it was right to act the way he did towards him."
    
    "???" "What's got your talons shivering, son?"
    
    "The sound of the door closing breaks Louis out of his trance, his eyes meeting the bird he waited for. The Canary smiles weakly as he scratches the nape of his neck."
    
    show louis anxious at shadow3
    l "S-Sorry, Sir. I was just lost in thought."
    
    "Louis bows in greeting, in which Aven returns in respect."
    
    show aven neutral at shadow2
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
    
    hide aven neutral
    hide louis happy
    show camera fixed
    "Louis looks at the video recorder wearily in his wing, looking back at the Bellbird's beckoning motion."
    hide camera fixed
    
    show louis anxious at shadow3
    show aven neutral at shadow2
    l "A-Are you sure, Sir?"
    
    "Aven nods firmly."

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


# Map mechanic for traveling to Louis' home at Acorn Street to finish the day.
label day_3_concluded:

    play music "music/CC Mission Complete.wav" fadein 1 fadeout 1
    scene achievement
    with dissolve3
    show achievementaven at truecenter
    with zoomin

    $ renpy.pause(3.0)

    #DAY 3 CONCLUDED

    scene avian care room
    with dissolve3
    $ is_daytime = False

    stop music fadeout 2.0
    play music "music/CC Somber Hospital Theme.wav" fadein 2 fadeout 2
    
    "Louis toys around with the new video recorder in his possession as he walked across the polished floors of the hospital's hallways."
    
    "Inside his mother's hospital room, he held the video recorder in his wing, he fidgets with the gadget idle, almost missing the doctor that catches him at the corner of his eye."
    
    show aziel alarmed at tinthospital2
    az "Mister Louis!"
    
    "The Owl catches the Canary by the wing, pulling him softly to get his attention."
    
    show louis anxious at tinthospital3
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
    
    show louis happy
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
    
    #The game transitions to the 'Acorn Street' Background, wherein the 'yellow house' is the character 'Louis' home.
    #The player will be transported in front of rows of tree houses - indicating local bird's houses
    #Use the art of Day_3_Concluded_BG.png for background."

    scene acorn street day 3
    with dissolve3
    
    "Louis has a sing-song chirp in his step as he stops right in front of his home, sighing in relief, he composes himself again, making sure to contain his flowing joy over the good news."
    
    show louis happy
    l "Aurora is going to be so... so happy!"
    
    "Louis says to himself with a happy chirp."

    #As the player approaches and clicks on the 'yellow house', the game fades to black, signifying the end of the first half.
    
    stop music fadeout 3
    scene black
    with dissolve3
    $ quick_menu = False
    show evangeline at truecenter
    $ renpy.pause(82.0, hard=True)
    stop movie

    scene black
    with Dissolve(9.0)

    jump itch


######## INVENTORY/ITEM MECHANICS ########

# Player has a checklist of items for repairing the video recorder, handed over to Maverick.
label _the_fix_the_recorder:
    
    #THE FIX THE RECORDER
    
    #The game automatically opens the 'Map' for this section, and the player can choose to only access the town street: 'Cornfield City'
    #The game transitions back into the 2D platform view of the world, wherein the character 'Louis' is shown in front of the (front) 'Feathered Fixer' Hardware in 'Cornfield City'.
    
    scene cornfield town
    with dissolve3
    #show lightoverlay

    "Louis' eyes gazes offer the familiar pavement he finds himself standing on almost everyday on his job."
    
    "For once, the Falcon he's grown accustomed to chatting with before he started his task was nowhere in sight." 
    
    "While it felt odd for Louis, he didn't dwell on it much. Focusing more on the task at hand instead."
    
    #The player may only interact with 'Feathered Fixer' Hardware for this section

    scene feathered fixer
    with dissolve3
    #THE SMOKING EAGLE
    
    "Louis enters the Feathered Fixer Hardware with the box of the broken recorder in his wing, glancing around the store, searching for someone who might be named Maverick."
    
    show louis normal at tint3
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

    show maverick neutral at tint2
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


########### MINI-GAME MECHANICS ###########

# Mini-game for fixing the video recorder using a drag-and-drop mechanic to disassemble and reassemble parts.
label _patch_it_up:
    
    #PATCH IT UP

    scene feathered fixer
    with dissolve3
    show broken camera
    
    #The game will now guide the player on how the parts of the video recorder will be fixed, the following choices below will dictate what part is added onto the video recorder,
    #the mechanic will mostly be drag and drop.
    #Use the anatomy of the video recorder file hardware_camera_separated.png and hardware_camera_broken.png

    "With the broken video recorder set flat on the table, all wings were on deck as both Louis and Maverick oversaw the on-going operation."
    
    "The Eagle picks up the video recorder, inspecting the front before removing the broken camera lenses."
    hide broken camera

    show maverick smile at slightright
    m "Alright, kid. You'll just help me disassemble the parts and I can handle the rest of the heavy work."
    
    "The Eagle instructs Louis bluntly."
    
    #show maverick neutral
    m "I need you to hand me that screw driver."

    hide maverick smile
    call screen hardwarepick
    if _return == "screwdriver":
        pass
    else:
        jump wrong_choice
    
    show maverick smile at slightright
    "Louis hands the tiny screwdriver to Maverick."
    
    m "I should have some spare parts that should match whatever...this thing has."
    
    "The Eagle commented as he started unscrewing the screws of the video recorder's lenses."
    
    "Louis watches the Eagle at work, finding it hard to believe that the Eagle's rough exterior to be working on a task that needed delicate feathers."
    
    "The Canary feels the urge to ask him something, just to satisfy his curiosity, plus, the small talk helps fill up the silence."
    
    jump _you_look_like_youve_been_doing_this_for_a_long_time

label wrong_choice:
    m "Are 'ya seein' right? this ain't the one I need."
    jump _patch_it_up

label wrong_choice2:
    m "Are 'ya seein' right? this ain't the one I need."
    jump _you_look_like_youve_been_doing_this_for_a_long_time

label _you_look_like_youve_been_doing_this_for_a_long_time:
    
    "Louis continues to watch Maverick tinker at work, careful with how he handles the already broken-up video recorder." 
    
    "The Canary clears his throat, making the Eagle glance up at him."
    
    show louis normal at slightleft
    l "You... You look like you've been doing this for a long time."
    
    "Louis initiates, choosing his words carefully."
    
    show maverick confused at slightright
    "The eagle nods at his words, focusing on his wings."
    
    show maverick neutral
    m "I had prior medical trainin' when I was still in the army."
    
    show maverick smile
    m "Fixing up broken objects ain't so different from patchin' up a few wounded birdies."
    
    "The eagle says simply, his wing turning to Louis."
    
    "Louis watches as the whole structure the camera lens is attached to pops out from the video recorder."
    
    show maverick neutral
    m "Wrench."
    
    hide maverick neutral
    hide louis normal
    call screen hardwarepick
    if _return == "wrench":
        pass
    else:
        jump wrong_choice2
    #The player should drag and drop the 'wrench' item to Maverick, in which he will continue to remove from the video recorder's anatomy.
    #The previous item should return to where it was previously dragged from.
    
    "Louis hands the wrench to Maverick."
    
    show louis happy at slightleft
    show maverick neutral at slightright
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
    m "Give me that glue, this thing you ought to fix quickly."
    hide maverick neutral
    hide louis normal
    call screen hardwarepick
    if _return == "glue":
        pass
    else:
        jump wrong_choice2
    
    "Louis continues to watch as the Eagle takes the tube glue and begins to  meticulously put glue on the tip of the toothpick he had previously handed over."
    
    show louis normal at slightleft
    show maverick confused at slightright
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

    "Louis takes his time to put the parts together in the right order."
    
    #The player is presented with the individually 'fixed' parts of the broken video recorder, the game will guide the player which part goes where first by highlighting
    #(either by simple glow or circled)  the individual parts lightly.
    #Use the anatomy of the video recorder file hardware_camera_separated.png
    #In the order of application: the camera lens structure is the main foundation.
    #The player must first connect the microphone handle to the microphone, then the player will be able to connect the microphone to the camera lens.
    #Afterwards, the player should connect the display panel to the camera lens body, then connect the last two 'red' and 'green' wires to finish.
    
    show maverick smile
    m "Good work kid, now give it to me and I'll do some final touches."
    
    #The player should drag and drop the assembled video recorder to 'Maverick'
    
    hide maverick
    with dissolve1
    "The Eagle hums pleasingly, standing up from the previously perched off spot behind the counter and heading towards the back, exiting Louis' view."
    
    #The game showcases the hardware store without the table, putting the counter/cashier background back in view.
    show maverick smile at slightright
    with dissolve1
    "The Eagle comes back with the video recorder in his wing."
    
    scene feathered fixer
    show camera fixed
    with dissolve1
    
    m "Here you go kid."
    
    "Maverick places the fixed video recorder into Louis' wings, he didn't touch any of the cracked parts as he said:"
    
    m "the thing is too old to find spare parts that matched that model exactly."
    
    "So most of the model was still, quite broken with the exception it can still power-up with batteries it requires."
    
    "The Canary inspects the video recorder in his wing, watching the display panel booth up as he pushes the power button to open it."
    hide camera fixed
    with dissolve2
    show louis happy at slightleft
    l "Wow!"
    
    l "It's still rough looking, but it works!"
    
    "Louis chirps happily at the Eagle, keeping the video recorder secured in his wings."
    
    "The Eagle nods knowingly, polishing his wings with a clean rag, removing the spilled oil that got in his feathers as he looks at the Canary."
    
    show maverick smile at slightright
    m "Of course it works, I fixed it."
    
    show maverick neutral
    "The Eagle says as a matter of fact, arrogance lacing his tone"
    
    show maverick smile
    m "Now, scram! I'm gonna feel grumpy if I don't get my snooze in."
    
    "Maverick says as his last word in, waving his wing out towards the exit of the hardware store as he perches back to his previous position, head against the counter and his eyes closed."
    
    "Louis laughs lightly to himself, seeing as the Eagle's ended the conversation as soon as his task was done, still the Canary bows to the sleeping Eagle in farewell."  
    
    "He turns to leave with a bright smile on his face."
    
    jump _peregrine_interaction_3


#######################################################
#                   STORY LABELS                     #
#######################################################

label day_3:
    $ is_daytime = True
    #The game transitions into the 2D platform view of the world, wherein the character 'Louis' is shown inside of  Aves Courier Center
    
    play music "music/CC Main Story Dialogue Theme.wav" fadein 3 fadeout 3

    scene aves courier center
    #show lightoverlay
    with dissolve3
    
    "Louis is perched quietly at the side next to the wall, away from the rest of the bustling birds of Aves Courier Center, no... he was waiting."
    
    #Okay game time # I do not know what this means (ale)
    
    "While he waited, his eyes observed- he was used to working with all of this."
    
    "The morning chaos with all the avians flapping their wings around, getting into routine. It was quite...warm, to say the least."
    
    "Louis was fond of all the flocks of colors the birds gave the morning; it gave him the burst of energy to get him through the day."
    
    show aven neutral at tint2
    a "Louis! Son! There you are."
    
    "The booming sound of the bearded bellbird's voice rang through the room, sounding the alarm of every bird's attention on the Canary bird."
    
    "Louis laughs awkwardly at the amount of eyes on him, regardless- he clears his throat, the familiar smile on his beak as he meets his boss."
    
    show louis anxious at tint3
    l "Sir Aven! I'm here early, just as you asked."
    
    "Louis could feel the bellbird's wing around his shoulder as Aven approached."
    
    show aven thinking
    a "As I know my top employee would, come, boy, I've got a special task just for you."

    show aven neutral    
    "Despite the chaos, the bellbird could comb through the flocks of colors that flew past him and Louis' sight, birds parting for their boss to make way out of his feathers."
    
    jump _new_task_caught_on_camera_finale


#######################################################
#                   DECISION LABELS                  #
#######################################################

# Options involving interactions with Catcher (Phoenix).
label _peregrine_interaction_3:
    
    scene cornfield town

    "Louis smiles happily with a new video recorder in his wing as he walks out of the Feathered Fixer Hardware store with a light bounce on his step."
    
    "???" "-Chirping happily again, Louis?"
    
    "Louis jolts at the sound of a familiar voice. Turning to his side to see the Falcon approaching him with that permanent stoic expression on his face."
    
    show louis happy at tint3
    l "P-Phoenix, Catcher, I didn't see you there!"
    
    "Louis laughs nervously, still startled from the initial surprise."
    
    "The Falcon only snickers under his beak, eyeing up the video recorder the Canary carries in his wing, he makes a passing motion with his head towards it."
    
    show catcher confused at tint2
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


# Player can choose to resist Catcher’s questioning.
label resist:
    
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


# Player can choose to give in to Catcher's pressure.
label give_in:
    
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


# The continuation after the decision during the interaction with Catcher.
label _peregrine_int_3_continuation:
    
    show catcher anxious
    c "I'll catch you around, Louis. Something... came up."
    
    "An obvious lie, both Louis and Catcher knew the excuse wouldn't fly on a normal day, but something about today was...different."
    
    "The Falcon briefly initiates the bow of farewell. Before the Canary could even reciprocate; Catcher was already flying away out of his view."
    
    "There was something that itches the back of Louis' head, he just couldn't quite... put a feather on what it is."
    
    jump _aven_task_conclusion

