label day2_classroomtransition1:
    
    scene bg room with fade
    
    "Back in the classroom, you slouch over on your desk and think about what happened during lunch."
    "The school festival is tomorrow and you still feel completely unsure of how things will play out…"
    if n_points > k_points:
        "You feel like you’ve been spending a lot of time with Nick lately, but there’s still a chance with Kaito…"
    elif n_points < k_points:
        "You feel like you’ve been spending a lot of time with Kaito lately, but there’s still a chance with Nick…"
    else:
        "You feel like you’ve been seeing both Nick and Kaito a lot lately and it could go either way…"
    "Without realizing, you’ve doodled a bunch of cute chibi pictures of yourself stressing out in the corner of your notes."
    "Seeing cute versions of yourself stressing out stresses you out even more, so you decide to draw your cat, Momo, instead."
    "Time flies by and before you know it the last bell is about to ring and students are shuffling their papers rapidly in excitement."
    "Blackwelder" "Okay, that’s all for today! Enjoy the festival tomorrow!"
    "Blackwelder" "Don’t forget to do your homework still."
    "Everyone" "Hai~"
    "The class disperses. Most hurry and make their way out, a few stay behind and to get ready for the festival."
    m "Hey, I’m going ahead."
    l "Oh yeah, you’re going to Anime Club?"
    m "Yeah, we’ve got that Hare Hare Yuukai rehearsal."
    m "I, uh, assume you’re not coming?"
    l "Uhhh, I’m fine here…"
    m "Pffft. Okay, be safe on your way home. See you tomorrow!"
    "You wave at her as she leaves. You look around the class and see some students rushing out, others staying and moving their desks."
    "It’s the last afternoon you’ll have to work on the festival..."
    "Again, you remember Kaito asking for help, but also know Nick will be working hard here in the class…"
    
    menu:
        
        "Help out Kaito.":
        
            $ k_points += 1
            $ d2d2_kaito = True
            call day2decision2_helpkaitoout
        
        "Help out Nick":  
            
            $ n_points += 1
            $ d2d2_nick = True
            call day2decision2_helpnickout  
    
    
    return