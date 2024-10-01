image streetview = "/Backgrounds/Street View.png"
image acorn street = "/Backgrounds/Acorn Street Day Closed Doors.png"
image acorn street no houses = "/Backgrounds/Acorn Street Day No Houses.png"
image acorn street night = "/Backgrounds/Acorn Street Night Closed Doors.png"
image acorn street night houses = "/Backgrounds/Acorn Street Night.png"
image acorn street day 3 = "/Backgrounds/Day 3 Concluded BG.png"
image aves courier center = "/Backgrounds/Aves Courier Center.png"
image aves courier center inside = "/Backgrounds/Aves Courier Center Interior.png"
image daily delights = "/Backgrounds/Daily Delights No Bread.png"
image daily delights pick = "/Backgrounds/Daily Delights Ivory.png"
image cornfield mail post = "/Backgrounds/Cornfield Mail Post.png"
image cornfield town = "/Backgrounds/Cornfield Town Map.png"
image feathered fixer = "/Backgrounds/Feathered Fixer Side View.png"
image flyaway superstore = "/Backgrounds/Flyaway Superstore.png"
image avian care hallway = "/Backgrounds/Avian Care Hallway.png"
image avian care room = "/Backgrounds/Avian Care Patient Room.png"

image magic trick 1 = "/magic trick/001.png"
image magic trick 2 = "/magic trick/002.png"
image magic trick 3 = "/magic trick/003.png"
image magic trick 4 = "/magic trick/004.png"
image magic trick 5 = "/magic trick/005.png"
image magic trick 6 = "/magic trick/006.png"
image magic trick 7 = "/magic trick/007.png"
image magic trick 8 = "/magic trick/008.png"
image magic trick 9 = "/magic trick/009.png"

image bennykane 1 = "/benny kane/001.png"
image bennykane 2 = "/benny kane/002.png"
image bennykane 3 = "/benny kane/003.png"
image bennykane 4 = "/benny kane/004.png"
image bennykane 5 = "/benny kane/005.png"
image bennykane 6 = "/benny kane/006.png"

image hospital = "/Backgrounds/hospital hall.jpg"
image hospital blur = "/Backgrounds/hospital hall blurry.png"
image hospital dark = "/Backgrounds/hospital hall dark.png"
image hospital dark blur = "/Backgrounds/hospital hall dark blur.png"
image basement = "/Backgrounds/basement.png"
image basement2 = "/Backgrounds/basement2.png"
image attic = "/Backgrounds/attic.jpg"
image corrupted outside = "/Backgrounds/Cornfield Town UPDATED.png"
image corrupted store = "/Backgrounds/Flyaway Superstore UPDATED.png"
image corrupted store dark = "/Backgrounds/Flyaway Superstore UPDATED dark.png"
image corrupted store blur = "/Backgrounds/Flyaway Superstore UPDATED Blurry.png"
image corrupted hospital = "/Backgrounds/Avian Care Patient Room UPDATED.png"
image daycare 1 = "/Backgrounds/Daycare Room 1.png"
image daycare 2 = "/Backgrounds/Daycare Room 2.png"
image bedroom = "/Backgrounds/bedroom.png"
image bedroom blur = "/Backgrounds/bedroom blur.png"
image bedroom attic = "/Backgrounds/bedroom attic.png"
image bedroom basement = "/Backgrounds/bedroom basement.png"

image achievement = "/gui/AchievementBackground.png"
image achievementivory = "/gui/AchievementIvory.png"
image achievementlily = "/gui/AchievementLily.png"
image achievementaven = "/gui/AchievementAven.png"
image newspaper text = "/gui/newspapertext.png"
image blackopacity = "/gui/BlackOpacity.png"
image post clipping = "/images/items/post office items/post_clipping.png"
image post letter = "/images/items/post office items/post_letter.png"
image post package = "/images/items/post office items/post_package.png"
image supermarket items = "/images/items/supermarket.png"
image broken camera = "/images/items/broken camera.png"
image camera fixed = "/images/items/fixed camera.png"
image itch = "/gui/itch page.png"
image cinnamonroll = "/images/items/hospital rewards/hospital_cinnaroll.png"
image grocerybag = "/images/items/supermarket items/grocery_paperbag.png"
image bouquet = "/images/items/hospital rewards/hospital_bouquet.png"

image checklist lily = "/gui/lily's checklist.png"
image checklist ivory = "/gui/ivory's checklist.png"
image checklist aven = "/gui/aven's checklist.png"

image deadanim = Movie(channel="movie_dp", play="images/dead video.webm", loop=False, size = (225,200)) #image="/images/last_frame.png"
image benny video = Movie(channel="movie_dp", play="images/bennyvideo.webm", loop=False, size = (210,1080)) #image="/images/last_frame.png"
image burning = Movie(channel="movie_dp", play="images/burning.webm", loop=False, size = (210,1080)) #image="/images/last_frame.png"
image interview2 = Movie(channel="movie_dp", play="images/interview2.webm", size = (1300,1200), loop=False)
image devlog01 = Movie(channel="movie_dp", play="images/devlog 01.webm", size = (1300,1200), loop=False)
image evangeline = Movie(channel="movie_dp", play="images/Evangelineknows.webm", size = (1300,1200), loop=False)
image arguement = Movie(channel="movie_dp", play="images/arguement.webm", size = (1300,1200), loop=False)
image HAHA = Movie(channel="movie_dp", play="images/HAHA.webm", size = (1300,1200), loop=False)
image static = Movie(play="images/tvstatic.webm", loop=False, size = (1920,1080))

image lightoverlay = "/gui/Light_Overlay.png"

transform checklistpos:
    yoffset -20
    xalign 0.5
    zoom 1.5

transform magicpos:
    yoffset -50
    xalign 0.5
    zoom 0.82

transform aven2pos:
    xoffset 1000
    yalign 1.0

transform slightleft:
    xalign 0.18
    yalign 1.0

transform slightright:
    xpos 852
    yalign 1.0

transform scarypos:
    xpos 1700
    ypos 895

transform stretchedpos:
    xpos 1710
    ypos -1500
    ysize 4000

transform stretchedpos2:
    xpos 1710
    ypos -1500
    ysize 4300

transform tint1:
    matrixcolor TintMatrix("#feeabb")*SaturationMatrix(1.0000)*ContrastMatrix(1.0370)
    center

transform tint2:
    matrixcolor TintMatrix("#feeabb")*SaturationMatrix(1.0000)*ContrastMatrix(1.0370)
    slightright

transform tint3:
    matrixcolor TintMatrix("#feeabb")*SaturationMatrix(1.0000)*ContrastMatrix(1.0370)
    slightleft

transform tint4:
    matrixcolor TintMatrix("#feeabb")*SaturationMatrix(1.0000)*ContrastMatrix(1.0370)
    center

transform tint5:
    matrixcolor TintMatrix("#feeabb")*SaturationMatrix(1.0000)*ContrastMatrix(1.0370)
    slightright

transform tint6:
    matrixcolor TintMatrix("#feeabb")*SaturationMatrix(1.0000)*ContrastMatrix(1.0370)
    slightleft

transform tintlily:
    matrixcolor TintMatrix("#feeabb")*SaturationMatrix(1.0000)*ContrastMatrix(1.0370)
    xalign 0.8
    yalign 1.0

transform tinthospital:
    matrixcolor TintMatrix("#adb2bb")*SaturationMatrix(0.9630)*ContrastMatrix(1.0370)
    center

transform tinthospital2:
    matrixcolor TintMatrix("#adb2bb")*SaturationMatrix(0.9630)*ContrastMatrix(1.0370)
    slightright

transform tinthospital3:
    matrixcolor TintMatrix("#adb2bb")*SaturationMatrix(0.9630)*ContrastMatrix(1.0370)
    slightleft
    
transform shadow1:
    matrixcolor TintMatrix("#eccdae")*SaturationMatrix(0.9630)*ContrastMatrix(1.0370)
    center

transform shadow2:
    matrixcolor TintMatrix("#eccdae")*SaturationMatrix(0.9630)*ContrastMatrix(1.0370)
    slightright

transform shadow3:
    matrixcolor TintMatrix("#eccdae")*SaturationMatrix(0.9630)*ContrastMatrix(1.0370)
    slightleft
