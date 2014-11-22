# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg classroom = "bg/BG101_01.png"
image bg room = "bg/BG305_01.png"
image bg bluesky = "bg/BG303_01.png"

#--------------Kaito-------------------------

#kaito normal size avatar, hand on back of head
image kaito worry = "kaito/ST31A01S.png"
image kaito laugh = "kaito/ST31A02S.png"
image kaito frown = "kaito/ST31A03S.png"
image kaito smile = "kaito/ST31A04S.png"
image kaito normal = "kaito/ST31A05S.png"

#kaito normal size avatar, hand on back of head, blushing
image kaito worryb = "kaito/ST31A11S.png"
image kaito laughb = "kaito/ST31A12S.png"
image kaito frownb = "kaito/ST31A13S.png"
image kaito smileb = "kaito/ST31A14S.png"
image kaito normalb = "kaito/ST31A15S.png"

#kaito normal size avatar, touching chest
image kaito worryt = "kaito/ST33A01S.png"
image kaito shock = "kaito/ST33A02S.png"
image kaito mad = "kaito/ST33A03S.png"
image kaito smilet = "kaito/ST33A04S.png"

#kaito normal size avatar, touching chest, blushing
image kaito worrytb = "kaito/ST33A11S.png"
image kaito shockb = "kaito/ST33A12S.png"
image kaito madb = "kaito/ST33A13S.png"
image kaito smiletb = "kaito/ST33A14S.png"

#kaito normal size avatar, arms crossed
image kaito worrya = "kaito/ST32A01S.png"
image kaito frowna = "kaito/ST32A02S.png"
image kaito anxious = "kaito/ST32A03S.png"
image kaito smilea = "kaito/ST32A04S.png"

#kaito normal size avatar, arms crossed
image kaito worryab = "kaito/ST32A11S.png"
image kaito frownab = "kaito/ST32A12S.png"
image kaito anxiousb = "kaito/ST32A13S.png"
image kaito smileab = "kaito/ST32A14S.png"

#----------------Nick-----------------------

#nick normal size avatar (arms crossed)
image nick worry = "nick/ST31A01S.png"
image nick smile = "nick/ST31A02S.png"
image nick shock = "nick/ST31A03S.png"
image nick serious = "nick/ST31A04S.png"

#nick normal size avatar with blush
image nick worryb = "nick/ST31A11S.png"
image nick shockb = "nick/ST31A13S.png"
image nick seriousb = "nick/ST31A14S.png"

#nick normal size avatar, turned away
image nick smilet = "nick/ST32A01S.png"
image nick worryt = "nick/ST32A02S.png"
image nick laught = "nick/ST32A03S.png"
image nick madt = "nick/ST32A04S.png"

#nick normal size avatar, turned away, blushing
image nick laughtb = "nick/ST32A13S.png"
image nick madtb = "nick/ST32A14S.png"

#nick normal size avatar, arm up
image nick worrya = "nick/ST33A01S.png"
image nick frown = "nick/ST33A02S.png"
image nick smilea = "nick/ST33A03S.png"
image nick mada = "nick/ST33A04S.png"

#nick normal size avatar, arm up
image nick worryab = "nick/ST33A11S.png"
image nick frownb = "nick/ST33A12S.png"
image nick smileab = "nick/ST33A13S.png"
image nick madab = "nick/ST33A14S.png"

# Declare characters used by this game.
define k = Character('Kaito', color="#c8ffc8")
define n = Character('Nick', color="#c8ffc8")
define l = Character('Liz', color="#c8c8ff")
define m = Character('Myca', color="#c8c8ff")
define j = Character('John', color="#c8ffc8")


# The game starts here.
label start:
    
    scene bg room
    with fade    
    
  

#    "???" "Liz-chan…"
#    "You hear a voice... Who could it be?!?!"
#    l "Oh… Nick… or is it Kaito??"
#    k "Liz-chan…"
#    l "Oh it’s Kaito, my love…!"
#    k "Liz-chan… "
#    l "Uhh yes, Kaito, that’s my name…"
#    k "Liz-chan… WAKE UP!"
#    l "GYA!??!"
#    "You sit up sharply, jolted awake! You’re at first terrified that you’re late for school and are ready to run out the door with a piece of toast in your mouth, but then realize Kaito really is standing at the foot of your bed."
#    show kaito normal
#    with dissolve      
#    k "Liz-chan, it’s time for school! Wake up, silly head!!"
#    k "Kaito-senpai!?"
#    "You blush, feeling embarrassed at being woken up like this, but also because you just had an awesome dream about him. Then you realize you were talking in your sleep!"
#    l "Oh no…! I didn’t say anything just now, did I??"
#    k "Um… nothing that I understood."
#    "You just laugh nervously. You then collect yourself and look at the time. It’s actually a little bit early!"
#    l "Oh wow, why are you here so early? Not that I mind…"
#    k "I forgot to mention it yesterday, but I need to get to class early for some culture festival preparations."
#    show kaito normalb
#    k "I know I could have let you sleep in, but it wouldn’t feel right walking to class without you."
#    "You can feel your cheeks turning red."
#    l "N-no, it’s no problem at all!!"
#    "You both look down and there is an awkward silence. You, needing to do something with your hands, put on your glasses because you’re like usually blind in the morning without them."
#    show kaito normal
#    l "W-well… I’m gonna go get ready then!"
#    k "Oh, right! I’ll be downstairs."
#    "You do your usual morning routine while thinking about what just happened."
#    l "(Hmm, it’s normal for us to walk to school together, so this isn’t really unusual. But, he normally waits for me in front of my house or in the living room… "
#    l "(Could he have gone up to my room because he couldn’t wait to see me?!)"
#    "Your hands spring up to your face in delight, giggling with delight as you try to suppress your excitement. "
#    l "(No, no, I’m sure he really is in a rush… It’s fine… He doesn’t love me like the way I love him, of course…!)"
#    "You sigh to yourself again, deflating."
#    "You head downstairs, feeling fresh and rejuvenated. You’re not usually a morning person… But you can be if Kaito is there!!"
#    k "Are you ready to go?"
#    l "Yeah!"
#    "Liz's Mom" "(IN HMONG) Bao, don’t forget your breakfast and lunch!!!"
#    "Your mother hurries from the kitchen and rushes to you, handing you some bentos."
#    l "Thanks mom."
#    k "Good morning, Mrs. Fang"
#    "Liz's Mom" "Oh Kaito, you take of my daughter and make lots of grandchildren, ok???"
#    "You both blush furiously. She says that a lot about you, Kaito, and your child birthing hips, but you feel embarrassed every time still. Kaito chuckles."
#    k "I’ll be sure to do that!"
#    l "Ehhh!?"
#    "Flustered, you punch Kaito lightly (even though he staggers from the punch), and leave quickly."

#    scene bg bluesky
#    with fade   
    
#    "You and Kaito walk to school like usual. It’s nice and cool out, with the sky only mildly peppered with clouds, the sun shining brightly, and the breeze blowing gently."
#    "You talk about the usual things with Kaito such as classwork and the culture festival coming up."
#    show kaito normal
#    with dissolve  
#    l "I’ll see if I can help your class, but our class is doing a haunted house and there’s still a lot of work to do."
#    k "No worries if you can’t. I know that you guys probably have a lot of props to make."
#    show kaito frown
#    with dissolve      
#    "Kaito seems to tense up a bit."
#    k "So, you’ll be working with your friend Nick, then?"
#    l "O-oh, yeah..."
#    "You suppress a blush but talk about how he’s in charge of the lighting and the props and such. Kaito nods, but doesn’t seem particularly interested in the details."
#    k "Are you alright hanging out with him? I know he never answered you…"
#    l "Oh, uh, of course! It’s been like so long! I’m totally over him! He’s old news!"
#    "You force out a laugh and a smile, trying to assure him. ."
#    show kaito worryb
#    with dissolve
#    k "Okay… You’re my childhood friend, so it pains me to see you hurt."
#    l "Aw, Kaito, you don’t have to worry. I’m so glad you’re looking out for me."
#    show kaito laughb
#    with dissolve    
#    k "Of course, you’re like a sister to me!"
#    l "Yeah, you’re not only like another brother, but also my senpai!"
#    l "(But what I feel for you is much more than that…)"
    scene bg classroom
    with fade         
    "You two continue your conversation until you reach the school. You split up as you head to the second year classroom, and Kaito heads up to the third year classrooms."
    "When you get there, you remember that you and Kaito left for school earlier than usual. The classroom is near empty…"
    "Except for a certain someone sitting in his seat."
        
    show nick serious
    with dissolve  
    
    l "NICK-KUN~"

    show nick shockb
    with dissolve
    
    show nick seriousb
    with dissolve    

    "Nick looks up at you and seems genuinely surprised. What’s that…? Did he blush just now? In that brief moment, he quickly looks back down at the game he is playing again."
    n "Hi Liz..."
    "You drop your stuff on your desk, which is in front of his, and swing around in your seat to turn and face him."
    l "Whatcha doin’? Are you always here so early?"
    "Nick just nods."
    n "Yeah… This is normal for me."
    l "Well, this is sooo early for me! I’m not use to this!"
    n "Why are you here then?"
    l "Ehh, I usually walk to school with my friend and he dragged me along."
    n "Your friend…?"
    
    show nick smile
    with dissolve      
    
    n "Oh you mean Kaito?"    
    "Nick smirks amusedly."
    n "Right, sure, \"friend\"."
    l "Ehhh?! It’s not like that!"
    "You squirm and blush. Nick seems amused but also something… else??"
    
    show nick worryt
    with dissolve        
    
    n "Whatever… I’m sure he feels differently at least."
    "Nick looks away, suddenly seeming moody and sullen."
    l "N-no, really, I’m sure he has always seen me just as a little sister!"
    n "Hmph… it’s none of my concern."
    l "Aw, don’t be like that~"
    "The conversation continued on like in the early hours of the morning. To others, your borderline flirting and his hot-and-cold behavior might seem weird, but this was a normal conversation between you two."
    "Initially, Nick was a lot more withdrawn from you and… generally, well, anyone. You didn’t often see him really hanging out with anyone, especially when he first transferred in at the beginning of the semester."
    "Due to his mysterious nature, K-pop boy band member build, and superior jaw structure, you felt immediately drawn to him. Perhaps it was your maternal instinct kicking it, but you felt the need to be by his side and make sure he was okay."
    "Sure enough, you had begun to develop feelings for him, and confessed… Yet…"
    
    show nick shock
    
    "???" "HEY LIZ!!!" with vpunch
    "You mentally scream inside as you hear his slimy voice oozing into your ears."
    
    show nick shock at right
    
    show kaito smilet with dissolve
    
    "It was… John."
    j "HEYY LIZZ WHAT ARE YOU UP TO?!?!" with vpunch
    "The thunderous sound of his stomping against the floorboards increases in volume as he near lunges for you."
    l "(EWWW…!!!!)"
    "You slink away from him and impulsively hide behind Nick."
    l "Oh… Hey, John…."
    "You give your utmost effort to feign polite happiness and it results in a faltering, struggling mess of a smile."
    "This guy, John… You met him last year as one of your cousins needed help getting him off her back, so you volunteered to \"befriend\" him as a distraction. And it worked… A little too well, in fact."
    "Now he took every chance to impress Liz with his Kermit the Frog impressions and generally finding every chance to show him what a wonderful, nice guy he is."
    "Regardless, you’ve been able to fend off any of his advances. In fact, thanks to him, you were able to hold onto Nick’s shoulder tightly whenever John blabbered at her."
    "Just as the first bell rang, the students who had been trickling in shuffled to their seats, marking the start of class. You finally let go of Nick’s shoulders, yet for a brief moment, you feel Nick’s fingers brush against your hands, as if he had impulsively reached for you."
    "Your eyes meet briefly in surprise, both of your faces red, but you look away and quickly return to your seat as you try to gain some composure for class."
    


    return
