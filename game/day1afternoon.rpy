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
        
            call day1decision2_kaito
        
        "Help Nick’s class":  
            
            call day1decision2_nick    
    
    
    return