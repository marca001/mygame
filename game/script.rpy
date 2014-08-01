# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg classroom = "bg/BG101_01.png"
image bg room = "bg/BG305_01.png"
image bg bluesky = "bg/BG306_01.jpg"

image kaito worry = "kaito/ST31A01S.png"
image kaito laugh = "kaito/ST31A02S.png"
image kaito frown = "kaito/ST31A03S.png"
image kaito smile = "kaito/ST31A04S.png"
image kaito normal = "kaito/ST31A05S.png"

image kaito worryb = "kaito/ST31A11S.png"
image kaito laughb = "kaito/ST31A12S.png"
image kaito frownb = "kaito/ST31A13S.png"
image kaito smileb = "kaito/ST31A14S.png"
image kaito normalb = "kaito/ST31A15S.png"

# Declare characters used by this game.
define k = Character('Kaito', color="#c8ffc8")
define n = Character('Nick', color="#c8ffc8")
define l = Character('Liz', color="#c8c8ff")

# The game starts here.
label start:
    
    scene bg room
    with fade    
    
    show kaito normal
    with dissolve    

    "Liz-chan…"
    l "Oh… Nick… or is it Kaito??"
    k "Liz-chan…"
    l "Oh it’s Kaito, my love…!"
    k "Liz-chan… "
    l "Uhh yes, Kaito, that’s my name…"
    k "Liz-chan… WAKE UP!"
    l "GYA!??!"
    "You sit up sharply, jolted awake! You’re at first terrified that you’re late for school and are ready to run out the door with a piece of toast in your mouth, but then realize Kaito really is standing at the foot of your bed."
    k "Liz-chan, it’s time for school! Wake up, silly head!!"
    k "Kaito-senpai!?"
    "You blush, feeling embarrassed at being woken up like this, but also because you just had an awesome dream about him. Then you realize you were talking in your sleep!"
    l "Oh no…! I didn’t say anything just now, did I??"
    k "Um… nothing that I understood. You did say ‘love’, but I figure you were talking about cake or something!"
    "You laugh nervously and just agree. You then collect yourself and look at the time. It’s actually a little bit early!"
    l "Oh wow, why are you here so early? Not that I mind…"
    k "I forgot to mention it yesterday, but I need to get to class early for some culture festival preparations."
    show kaito normalb
    k "I know I could have let you sleep in, but it wouldn’t feel right walking to class without you."
    "You can feel your cheeks turning red."
    l "N-no, it’s no problem at all!!"
    "You both look down and there is an awkward silence. You, needing to do something with your hands, put on your glasses because you’re like usually blind in the morning without them."
    l "W-well… I’m gonna go get ready then!"
    k "Oh, right! I’ll be downstairs."
    "You do your usual morning routine while thinking about what just happened."


    return
