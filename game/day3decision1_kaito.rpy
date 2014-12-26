label day3decision1_kaito:
    
    "The image of Kaito flashes in your mind…"
    "You sure would love to hear Kaito perform…"
    "And you know it would mean a lot to him if he saw you there."
    "Your mind is made up! You start walking down the hall to head to the gym, where the performance is suppose to be at."

    scene bg gym with fade

    "When you get there, there’s already been multiple acts done already."
    "You suddenly worry that you missed Kaito’s performance, but when you look at the pamplet they give at the entrance, you’re fortunately right on time."
    "There’s also surprisingly a sizeable crowd."
    "You take the seat nearest to the front, hoping he’ll see you."
    "At the moment, someone is currently singing a kawaii pop song."
    "The song is just finishing though and people are clapping."
    "Kaito’s turn is coming up…! Your heart is going DOKI DOKI in excitement."
    "The class representative of Kaito’s class comes up."
    "Classmate" "Up next, we have Kaito singing a song called ‘You!’"
    "People clap again but you make sure you clap even louder."
    
    show kaito normalb with dissolve
    
    "Kaito walks up onto the stage, looking a tad bashful but excited."
    "He really has a wonderful stage presence…"
    "The classmate walks off stage, and the crowd claps politely again.."
    "Kaito approaches the mic."
    
    show kaito worry with dissolve
    
    "Kaito" "Umm… Hello."
    
    show kaito shock with dissolve
    
    "Kaito" "...!"
    
    "When he sees you in the crowd, his eyes light up."
    
    show kaito smileb with dissolve
    
    "He waves at you happily from the stage, oblivious to the crowd suddenly."
    l "SENPAI...!!!"
    "You yell-whisper this from your spot, standing up and waving enthusiastically back."
    "Meanwhile, you definitely feel some jelly bitches glaring daggers at your back."
    
    show kaito normal
    
    "Kaito" "This song is called ‘You’."
    "Kaito" "I hope you all enjoy it!"

    hide kaito with dissolve

    "He bows and walks over to the piano, which has a mic set up near it."
    "The room is dead silent for a moment. Kaito’s eyes are closed."
    "And then he starts to play."
    "..."
    "The bittersweet notes fill the air and he opens his mouth and starts to sing."
    
    show kaito talkingt with dissolve
    
    "Kaito" "{i}Anata wa ima doko de nani wo shite imasu ka?{/i}\n(Where are you now, what are you doing?)"
    "Kaito" "{i}Kono sora no tsuzuku basho ni imasu ka?{/i}\n(Are you in this endless sky?)"
    
    hide kaito with dissolve
    
    "His voice is clear and sharp, full of emotion."
    "The entire room is entranced."
    "However, between his piano strokes, you see Kaito’s tender gaze on you as he sings."
    "Your heart skips a beat."
    "It’s like he’s… speaking to you!"
    
    show kaito worryt with dissolve    
    
    k "{i}Kodoku to zetsubou ni mune wo shimetsukerare{/i}\n(My chest was tightened by loneliness and despair)"
    k "{i}Kokoro ga kowaresou ni naru keredo{/i}\n(My heart felt like it would break)"
    
    show kaito talkingtb with dissolve
    
    k "{i}Omoide ni nokoru anata no egao ga{/i}\n(But your smiling face remained in my memories 
    )"
    k "{i}Watashi wo itsumo hagemashite kureru{/i}\n(Always encouraging me)"
    
    hide kaito with dissolve
    
    l "({i}Kaito-senpai… {/i})"
    l "({i}Maybe I’m just imagining things, but I feel like those words are about me…! {/i})"
    "Everyone is smiling, tears with their eyes at Kaito’s beautiful performance."
    "It’s just so amazing that people take out their lighters and swing it and fro!"
    "His piano playing is full of compassion as well, as the song reaches its climax."
    
    show kaito talkingtb with dissolve
    
    k "{i}Itsumo no you ni egao de ite kuremasu ka? {/i}\n(Will you smile for me like always?)"
    k "{i}Kono sora no tsuzuku basho ni imasu ka?{/i}\n(Right now, it's all I continue to ask for)"
    l "({i}Kaito-senpai… I’ll smile for you… ALWAYS!{/i})" with flash
    
    hide kaito with dissolve
    
    "And with that, the song descends from it’s powerful height back into its much more bittersweet melody, coming full circle."
    
    scene black with dissolve
    
    "The final notes linger in the air."
    
    "..."
    
    scene bg gym with fade
    
    "Everyone breaks out into an applause. You’re clapping loudly too, but you also can’t help feel choked up."
    "His voice and his song just felt so… intimate somehow."
    "Kaito stands up, and takes another bow as the applause continues."
    "He walks back up to the mic."
    
    show kaito normalb with dissolve
    
    k "Thank you!"
    "He still looks somewhat bashful and nervous, but also thoroughly pleased with himself."
    "The crowd quiets down since it looks as if he wants to say more."
    
    show kaito worryb
    
    k "Um…"
    
    show kaito madb with dissolve
    
    k "This song is dedicated to a special girl in my life."
    k "She’s my childhood friend, and this is one of her favorite songs."
    
    show kaito smiletb with dissolve
    
    k "And... I’m so happy she came out today."
    if k_points <= n_points:
        k "Thank you so much for always being my friend!"
        k "We've grown apart over the years, but..."
        k "I’ll never stop loving you…"
        
        show kaito talkingt
        
        k "Like a sister!" with vpunch
        "Everyone cheers at your wonderful sibling-like love."
        "You visibly stiffen in your seat."
        
        hide kaito with dissolve
        
        "Kaito bows again and makes his way off the stage."
        
        scene black with fade
        
        l "({i}I… I feel like I’m missing something.)"
        l "({i}I thought maybe… something would happen.{/i})"
        l "({i}I guess I really am just a friend to him…{/i})"
        l "({i}...Maybe I should have spent more time with him?{/i})"
        l "({i}If I’m just his friend, he might think it’s weird if I ask him to couple's dance…{/i})"
        "You make your way out of the gym."
        
        scene bg bonfire with dissolve
        
        "It’s already dark… And there’s a bunch of girls swarming him, cooing over his performance."
        "Meanwhile, the bonfire dance is already starting… Maybe you shouldn’t bother Kaito."
        
        jump badend

    #Kaito End
    k "It really means a lot to me...."
    
    show kaito worry with dissolve
    
    k "I thought maybe we weren’t as close as we use to be…"
    k "We grew up together, so I thought maybe she just saw me as a brother and nothing more…"
    l "({i}Wait, w-w-where is this going!?{/i})"
    "You’re feeling faint…!"
    "There’s so many people around, looking at you!!"
    
    show kaito smiletb with dissolve
    
    k "But, recently I’ve realized…"
    
    show kaito madb with dissolve
    
    k "You’re much more than a childhood friend to me!" 
    k "What I feel for you is much more!"
    "People in the audience gasp."
    
    show kaito worrytb with dissolve
    
    k "Liz-chan… I… I"
    
    show kaito madb with dissolve
    
    k "I L-LIKE YOU!" with vpunch
    k "W-w-will you go out with me?!"
    "You stand up in your chair, tears in your eyes."
    
    hide kaito with dissolve
    
    l "Y-yes, of course! Of course I will!"
    k "What?? I can’t hear you from here!"
    "Audience member" "She said yes--"
    l "I SAID YES!!" with vpunch
    l "WILL YOU GO WITH THE DANCE TO ME TONIGHT???" with vpunch
    
    show kaito shockb with dissolve
    
    k "Y-yes! Of course!"
    k "I thought you’d never ask!"
    "Everyone breaks out into a giant applause (except the jelly bitches.)"
    
    scene black with dissolve
    
    "..."
    "You two meet outside the gym, in a secluded corner…"
    
    scene bg schoolside_night with dissolve
    
    l "Nee Kaito-senpai… Do you really…? I can’t believe it…"
    
    show kaito smilet with dissolve
    
    k "Shhh… you don’t have to cry."
    k "Here, let’s go to bonfire dance… It’s already started, but we can make it."
    "Kaito takes your hand in his and leads you away."
    
    scene bg bonfire with dissolve
    
    "As you walk toward the glowing fire in the center of the sports field, you spot Myca in the distance."
    l "Myca!!! Look!"
    "You point at your hand in Kaito’s."
    "Myca gasps audibly and starts cheering from across the field."
    m "EYYYYYY~ YOU DID IT! EYYYYYY" with vpunch
    l "EYYYYYYY" with vpunch
    m "AWW YISSSSSSS" with vpunch
    l "YAAAASSSSSSS" with vpunch
    "Kaito just chuckles at your interaction."
    "Your eyes meet again with Kaito’s, and you hold his hand tigether."
    "The music in the background is playing faintly and you join the dozens of couples already swaying to the music."
    "You and Kaito are just SO IN LOVE that you move together in perfect synchronized motions."
    "In the corner of your eye, you see John biting a handkerchief and tears streaming down his face as he watches."
    "Ah, everything is perfect."
    "Eventually, Kaito guides you off the field and you two walk to the empty side of the school building."
    
    scene bg schoolside_night with dissolve
    
    show kaito normalb with dissolve 
    
    k "Nee Liz-chan… You don’t have to call me Kaito-senpai anymore…"
    k "You can just call me Kaito or Kaito-kun…"
    k "Since, starting from tonight, I’ll be your boyfriend…"
    l "And I’ll be your… girlfriend?"
    "Kaito nods, his eyes full of warmth and tenderness."
    l "I’m so happy… I like you so much, Kaito…"
    
    show kaito smiletb with dissolve
    
    k "And I like you…"
    "You embrace him tightly, wishing the night would never end."
    #fade to black
    
    scene black with fade
    
    l "Senpai… noticed me…!"
    
    scene pink with dissolve
    
    show text "~HAPPY NICK END~" with pixellate
    
    show text "~HAPPY NICK END~" with Pause(4)
    
    jump credits
    
    return