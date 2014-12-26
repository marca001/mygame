label day3decision1_nick:
    
    "The image of Nick flashes in your mind…"
    "You’re not good with spooky stuff, but your class did work on the haunted house and it would be a shame never to see it."
    "And you Nick was work especially hard on it."
    "It would mean a lot to him if you visited at least..."
    "Your mind is made up! You start walking down the hall to head to your classroom."
    
    scene bg school_hall2_sunset with fade

    "When you arrive at the front of the classroom, you can see the entrance is decked out very spookily."
    "There’s little bats and ghosts hung around the entrance."
    "Okay, maybe it’s not that scary on the outside, but maybe it is on the inside…"
    "Surprisingly, Nick is loitering at the entrance with fliers in hand."
    "He’s staring at the ground, mumbling."
    
    show nick madt with dissolve
    
    n "Come see our Haunted House…!"
    n "It’s… it’s spooky…"
    l "...Really Nick?"
    
    show nick shock with dissolve
    
    n "...!"
    
    l "Who put you on advertising duty?"
    
    show nick seriousb with dissolve
    
    n "Hey, I didn’t choose this."
    l "Well, you’re lucky because today your advertising worked. I’d like admittance for one, please!"
    
    show nick serious
    
    n "Even though you already know what’s inside?"
    l "That’s not the same as the actual thing…"
    l "Hey~ Won’t you come with me? I’m really scared of spirits and stuff~…!"
    l "({i}No really, I am.{/i})"
    
    show nick frown with dissolve
    
    n "Hmph… I guess."
    n "Not like I’m accomplishing anything out there…"
    
    scene black with dissolve
    
    "Nick puts his fliers away and you both enter the room, which is almost completely dark."
    "Okay, maybe you did this to flirt with him, but you find yourself actually getting kind of freaked out."
    l "W-was our class always this dark?"
    if d1d2_nick:
        l "Oh, hey, there’s that tree I made!"
        n "..."
    else:
        n "That would be my lighting skills. We just covered the windows and..."
        l "Nevermind, I’m losing immersion."
    "You two spend a few seconds walking alone in the dark. Spooky music clearly from a speaker starts to increase in volume."
    "From behind a black curtain somewhere, you hear someone whispering."
    l "W-what was that?"
    "???" "{color=#f00}...h-help… m..e…{/color}"
    "You grab Nick’s hand without realizing. Nick freezes up, but you can hardly tell because you’re getting nervous and walking faster."
    l "Oh god, why is our classroom like a maze?! How is this possible?"
    "???" "{color=#f00}...death… is coming...{/color}"
    l "?!"
    l "Ohh godd, that whispering is SO creepy…"
    "???" "{color=#f00}...the economy is in ruins…{/color}"
    l "T-this is terrifying!"
    "???" "{color=#f00}...college will leave your generation in several thousands dollars in debt…{/color}"
    l "N-NO!" with vpunch
    "???" "{color=#f00}{b}AND WITH NO GUARANTEE OF A JOB!!{/b}{/color}" with vpunch
    l "NOOOO!!!" with vpunch
    "You grab onto Nick’s arm tightly and bury your head into his shoulder."
    
    show nick shockb with dissolve
    
    n "?!"
    
    l "How can you not find this scary!?"
    
    show nick seriousb with dissolve
    
    "You look up at Nick. He actually looks really embarrassed for some reason."
    "He’s completely red in the face…"
    n "Well, I worked on almost all this…"
    n "So I know exactly what happens..."
    l "Oh that’s true! You really are talented, Nick-kun!"
    l "This whole thing looks amazing!"
    
    show nick defaultb with dissolve
    
    "Nick turns away, embarrassed."
    n "It’s not a big deal… A-also…"
    "He motions at your interlinked arms. Your boob is pressing up against him."
    l "O-oh! How embarrassing! Sorry, I was just scared and..."
    n "It’s okay…"
    "Now you’re both blushing in the dark…"
    
    hide nick with dissolve
    
    "???" "{color=#f00}Look, can you guys just focus? I worked really hard on this act.{/color}"
    l "Is that you, Kevin?"
    "Kevin" "{color=#f00}Yeah! Hi Liz!{/color}"
    l "Hi! Wow, Kevin’s really good at this, huh?"
    "You turn to Nick… But he isn’t there."
    l "N-nick-kun?"
    "No response. Not even Kevin responds."
    l "Okay this isn’t funny anymore…!"
    "You walk forward in the dark maze. It continues to be eerily quiet except for the distant creepy music in the background."
    l "G-guys?!"
    l "..."
    "A cold hand touches your shoulder."
    "Trembling you turn around and it’s…"
    
    show ghost with moveinright
    
    "A GHOST!" with vpunch #ghosthouse
    l "GAHHHHHHHH!!!!!!!!!!!!!!!!!!!!!" with vpunch
    
    scene black
    
    "You screech and turn tail, dashing forward blindly."
    "You run and run and then someone catches your arm and pulls you toward them."
    
    show nick shock with dissolve
    
    n "Hey, hey, it’s okay! Calm down!"
    l "N-nick-kun!?"
    
    show nick seriousb with dissolve
    
    n "I’m here."
    "Without realizing, you hug him tightly, feeling warm and protected."
    "He wraps his arms around you back, surprisingly."
    l "C-can we get out of here?"
    
    show nick smile with dissolve
    
    n "Of course. Actually…"
    "Holding your hand now, he lifts up a black curtain and leads you through it."
    
    scene bg classroom_night with dissolve
    
    l "Whoa… what’s this?"
    n "One of the secret exits for employees."
    
    $ n_points = 1
    
    if n_points <= k_points:
        "When you step through, you gasp with relief at being out of there."
        "It’s obviously a behind-the-scenes supply room where the performers work their magic."
        l "Well, this is cool…"
        l "Also, why’d you disappear earlier?!"
                
        show nick serious with dissolve
        
        n "Oh, I thought it’d be funny."
        l "Eh!? That’s so mean, Nick-kun."
        
        show nick smilea with dissolve
        
        n "Heh... It was amusing watching you."
        
        show nick worryab with dissolve
        
        n "But, I didn’t think you’d get that scared."
        n "So… sorry about that."        
        "He mumbles that to the ground, but he genuinely seems somewhat regretful."
        l "Aww, it’s okay."
        
        show nick serious with dissolve
        
        n "Well, unless you want to finish the rest of the maze, you can leave here."
        l "Yeahhhh, I’m not doing that."
        "Nick lifts up another mysterious curtain and reveals you guys are actually surprisingly close to the entrance."
        n "I still have to finish my shift here."
        
        show nick smiletb with dissolve
        
        n "...T-thanks for coming by, though."
        l "Alright. And no problem!"
        
        scene black with dissolve
        
        "..."
        
        scene bg school_hall2_night with dissolve
        
        "You step out of the classroom, relieved."
        "You’re honestly impressed your class could be so scary."
        "As you walk through the hallway to outside, you see it’s already dark outside and there’s the bonfire outside."
        l "({i}OH CRAP.{/i})" with vpunch
        l "({i}I TOTALLY FORGOT TO ASK NICK TO THE DANCE…!{/i})" with vpunch
        "You feel your courage wilting…"
        "When you think about it, you were alone earlier… and Nick didn’t say anything."
        "Maybe… maybe he doesn’t feel the same way about you afterall?"
        "Or maybe he’s just not ready?"
        "Either way, you definitely feel like you missed something."
        l "({i}Maybe I should have spent more time with him...{/i})"
        
        scene bg bonfire with dissolve
        
        "You sigh out loud in the night air and try to be optimistic."
        jump badend

    #Nick end
    "When you step through, you gasp."
    "It still looks somewhat like a supply room, but the room has lit candles spread out all around."
    "Combined with glow of the candles and the moonlight through the windows, the room actually looks very pretty."
    l "What is all this…?"
    
    show nick worryab with dissolve
    
    n "U-um…"
    n "Well, you said you wanted to get out of there, right? That’s all it is."
    
    show nick defaultb with dissolve
    
    n "Just… a place for you and me."
    l "Nick-kun…"
    
    show nick talkb with dissolve
    
    n "I disappeared earlier because I wanted to make sure everything was set up okay."
    
    show nick seriousb
    
    n "So… yeah."
    l "It looks great! But, what’s it all for…?"
    
    show nick worryb with dissolve
    
    n "...Uh."
    "Nick looks extremely embarrassed now, but continues talking shakily."
    
    show nick madab with dissolve
    
    n "L-look, you wanted a formal response, right?!"
    n "T-to your confession…"
    
    show nick worryab with dissolve
    
    n "So, this is my answer…"
    "He takes a deep breath..."
    
    show nick talkb with dissolve
    
    n "Yes…"
    n "I like you too!"
    
    show nick smileb with dissolve
    
    n "Liz... Will you go out with me?"
    
    "You’re rendered speechless, your hand covering up your mouth as tears form in your eyes."
    l "Nick-kun…!"
    
    show nick shockb
    
    l "NICK-KUN!" with vpunch
    "You tackle-hug him! He flails for a second but wraps his arms around you."
    l "I’m so happy!!!"
    
    show nick smileb with dissolve
    
    n "...Me too."
    "He holds you tighter."
    "For a moment, everything is perfect in that candlelit room…"
    l "S-so, if we’re going out now, will you dance with me at the bonfire dance?"
    
    show nick worry 
    
    n "Eh!?" with vpunch
    
    scene black with dissolve
    
    "..."
    
    scene bg bonfire with dissolve
    
    "You manage to drag Nick out onto the field where the bonfire dance has already started."
    "You see dozens of happy couples already swaying with their partners to the music playing in the background."
    
    show nick worryab with dissolve
    
    n "D-do I have to?"
    l "Yes! Don’t worry, I’ll help you out."
    
    "You takes his hand in yours and gently lead him."
    
    hide nick with dissolve
    
    "As you walk toward the glowing fire in the center of the sports field, you spot Myca in the distance."
    l "Myca!!! Look!"
    "You point at your hand in Nick’s."
    "Myca gasps audibly and starts cheering from across the field."
    m "EYYYYYY~ YOU DID IT! EYYYYYY" with vpunch
    l "EYYYYYYY" with vpunch
    m "AWW YISSSSSSS" with vpunch
    l "YAAAASSSSSSS" with vpunch
    "Nick just shakes his head, smiling."
    "The dance starts off pretty awkward, but you two are laughing the whole time."
    "It is very fortunate you had the dance already memorized just for such an occasion…"
    "Eventually, he gets it down and you two are synched perfectly, gazing into each other’s eyes."
    "Nick doesn’t say much, but his -dere expressions say it all…"
    "In the corner of your eye, you see John biting a handkerchief and tears streaming down his face as he watches."
    "Ah, everything is perfect."
    
    scene bg schoolside_night with dissolve    
    
    "Eventually, you two break off from the crowd and make your way to the empty side of the school building."
    l "Did you have fun?"
    
    show nick smileb with dissolve
    
    n "I did, actually."
    n "I-I didn't think think I'd like these sort of things."
    n "But when I'm with you, it's different..."
    "Your heart skips a beat. You can’t believe Nick is going to say things like this from now on."
    l "I’m so happy…! I really do like you, Nick-kun."
    
    show nick smileab with dissolve
    
    n "I like you too, Liz…"
    n "A-actually…"
    n "Can I call you… Lizzy?"
    n "If you don’t mind…"
    l "O-of course not!" with vpunch
    n "Okay, then… "
    
    show nick smiletb with dissolve
    
    n "L… Lizzy..."
    l "Oh, Nick-kun~!"
    "You embrace him tightly, wishing the night would never end."
    
    scene black with dissolve
    
    l "NICK-KUN... DAISUKI!!!"
    
    scene pink with dissolve
    
    show text "~HAPPY KAITO END~" with pixellate
    
    show text "~HAPPY KAITO END~" with Pause(4)    
    
    jump credits
    
    return