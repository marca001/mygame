label day1afternoon:
    
    m "Gee, I wonder why! Anyway, I’m gonna start grabbing supplies for the haunted house stuff."
    l "Oh yeah, I probably should help out with that, right?"
    m "Ehh, not necessarily. A lot of students switch around what class they help with, I did that yesterday. Don’t think they really care."
    l "That’s true…"
    l "{i}(I did mention to Kaito I said I’d see if I could help their class…){/i}"
    "From the corner of your eye, you see Nick alone, still putting some stuff away and getting ready to help with some props."
    l "{i}(But, I’m sure Nick wouldn’t mind the help as well… ){/i}"

    menu:
        
        "Help Kaito’s class":
        
            $ k_points += 1
            call day1decision2_kaito
        
        "Help Nick’s class":  
            
            $ n_points += 1
            call day1decision2_nick    
        
    "You immediately call up your heterosexual life partner. You tell her the events verbatim and maybe a bit of exaggeration."
    "Myca makes humping noises at you over the phone along with words of encouragement."
    "She mostly says things along the line of \"Dude he definitely wants the V\" and \"You got this bet thing in the bag\" and \"hawt\"."
    "Later, you hold your extremely pudgey and round cat up in the air over you. Not only does your kitty look cute hovering over you, but the cat’s obesity serves as a nice muscle-building exercise for your arms."
    l "Sigh… Oh Momo! Does he love me??? DOES HE???"
    "Momo" "Meow."
    l "Oh Momo, that makes no sense. You should have another kitty cat treat."
    "You put Momo down and he waddles over to his food bowl. You dump some treats in it."
    l "I love you Momo!! So cute!!"
    "Momo" "Meow meow."
    "Your sister strolls by later and remarks your cat is, like, super fat and could die. "
    "You respond that she should stop bodyshaming your cat and accept him for who he is."
    "This inspires you to watch more funny videos of cats. You’re later tired out and head to bed."
    "You fall into a deep sleep as your thoughts drift to the exciting possibilities of tomorrow."
        
    
    
    return