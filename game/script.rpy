# You can place the script of your game in this file.


image pink = Solid((240,128,128,255))

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg classroom = "bg/BG101_01.png"
image bg classroom_sunset = "bg/BG101_02.png"
image bg classroom_night = "bg/BG101_03.png"
image bg room = "bg/BG305_01.png"
image bg house_outside = "bg/BG203_01.png"
image bg bluesky = "bg/BG303_01.png"
image bg park_sunset = "bg/BG104_02.png"
image bg white = Solid((255, 255, 255, 255))
image bg school_hall = "bg/BG301_01.png"
image bg school_hall2 = "bg/BG102_01.png"
image bg school_hall2_sunset = "bg/BG102_02.png"
image bg roof = "bg/BG105_01.png"
image bg cloudysky = "bg/BG306_01.png"
image bg gym = "bg/BG204_01.png"
image bg bonfire = "bg/BG104_05.png"
image bg schoolside_night = "bg/BG201_02.png"
image ghost = "bg/ghost.png"
image bg school_gate = "bg/BG209_01.png"
image bg school_front = "bg/BG208_01.png"

#--------------Other------------------------

image myca normal = "others/sylvie_normal.png"
image myca giggle = "others/sylvie_giggle.png"
image myca smile = "others/sylvie_smile.png"
image myca surprised = "others/sylvie_surprised.png"

image blackwelder normal = "others/blackwelder_normal.png"

#--------------Splash Screen-----------------

image kaitoscene2 = "others/kaitoscene2.png"
image nickscene2 = "others/nickscene2fglasses.png"

#--------------Kaito-------------------------

#kaito normal size avatar, hand on back of head

image kaito worry = "kaito/handbackofheadworry.png"
image kaito laugh = "kaito/handbackofheadlaugh.png"
image kaito frown = "kaito/handbackofheadfrown.png"
image kaito smile = "kaito/handbackofheadtalk.png"
image kaito normal = "kaito/handbackofheadnormal.png"

image kaito worryb = "kaito/handbackofheadworryblush.png"
image kaito laughb = "kaito/handbackofheadlaughblush.png"
image kaito frownb = "kaito/handbackofheadfrownblush.png"
image kaito smileb = "kaito/handbackofheadtalkblush.png"
image kaito normalb = "kaito/handbackofheadnormalblush.png"

#kaito normal size avatar, touching chest
image kaito worryt = "kaito/touchingchestworryblush.png"
image kaito shock = "kaito/touchingchestshock.png"
image kaito mad = "kaito/touchingchestmad.png"
image kaito smilet = "kaito/touchingchestsmile.png"
image kaito laught = "kaito/touchingchestlaugh.png"
image kaito talkingt = "kaito/touchingchesttalk.png"

#kaito normal size avatar, touching chest, blushing
image kaito worrytb = "kaito/touchingchestworryblush.png"
image kaito shockb = "kaito/touchingchestshockblush.png"
image kaito madb = "kaito/touchingchestmadblush.png"
image kaito smiletb = "kaito/touchingchestsmileblush.png"
image kaito talkingtb = "kaito/touchingchesttalkblush.png"

#kaito normal size avatar, arms crossed
image kaito worrya = "kaito/crossedarmworry.png"
image kaito frowna = "kaito/crossedarmfrown.png"
image kaito laugha = "kaito/crossedarmtalk.png"
image kaito smilea = "kaito/crossedarmsmile.png"

#kaito normal size avatar, arms crossed
image kaito worryab = "kaito/crossedarmworryblush.png"
image kaito frownab = "kaito/crossedarmfrownblush.png"
image kaito laughab = "kaito/crossedarmtalkblush.png"
image kaito smileab = "kaito/crossedarmsmileblush.png"

#----------------Nick-----------------------

#nick normal size avatar (arms crossed)
image nick serious = "nick/crossedarmsdefault2.png"
image nick worry = "nick/crossedarmsworry2.png"
image nick smile = "nick/crossedarmssmile2.png"
image nick shock = "nick/crossedarmsshocked2.png"
image nick talka = "nick/crossedarmstalk2.png"

#nick normal size avatar with blush (arms crossed)
image nick seriousb = "nick/crossedarmsdefault2blush.png"
image nick worryb = "nick/crossedarmsworry2blush.png"
image nick smileb = "nick/crossedarmssmile2blush.png"
image nick shockb = "nick/crossedarmsshocked2blush.png"
image nick talkb = "nick/crossedarmstalk2blush.png"

#nick normal size avatar, turned aways
image nick default = "nick/turnedawaydefault.png"
image nick smilet = "nick/turnedawaysmile.png"
image nick worryt = "nick/turnedawayworry.png"
image nick laught = "nick/turnedawaylaugh"
image nick madt = "nick/turnedawaymad.png"

#nick normal size avatar, turned away, blushing
image nick defaultb = "nick/turnedawaydefaultblush.png"
image nick smiletb = "nick/turnedawaysmileblush.png"
image nick worrytb = "nick/turnedawayworryblush.png"
image nick laughtb = "nick/turnedawaylaughblush.png"
image nick madtb = "nick/turnedawaymadblush.png"

#nick normal size avatar, arm up
image nick frown = "nick/armupdefault2.png"
image nick worrya = "nick/armupworry.png"
image nick smilea = "nick/armupsmile.png"
image nick mada = "nick/armupmad.png"

#nick normal size avatar, arm up
image nick frownb = "nick/armupdefault2blush.png"
image nick worryab = "nick/armupworryblush.png"
image nick smileab = "nick/armupsmileblush.png"
image nick madab = "nick/armupmadblush.png"

# Declare characters used by this game.
define k = Character('Kaito', color="#c8ffc8")
define n = Character('Nick', color="#c8ffc8")
define l = Character('Liz', color="#c8c8ff")
define m = Character('Myca', color="#c8c8ff")
define j = Character('John', color="#c8ffc8")

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

#-----------------------------------------------



# The game starts here.
label start:
    
    $ k_points = 0
    $ n_points = 0
    
    $ kaito_dream = False    
    $ d1d2_kaito = False
    $ d1d2_nick = False
    $ d2d1_kaito = False
    $ d2d1_nick = False    
    $ d2d2_kaito = False
    $ d2d2_nick = False        
    
    call day1morning1
    
    call day1morning2

    call day1afternoon
    
    call day2morning
    
    call day2_classroomtransition1
    
    call day3morning
    
    call badend
    
    
label credits:
    
    scene black with dissolve
    
    show text "~~CREDITS~~" with moveinbottom
    
    show text "~~CREDITS~~" with Pause(1.5)
    
    hide text "~~CREDITS~~" with moveouttop
    
    show text "Writing, Directing, Programming\nMyca Arcangel\n\n\"Hope you had fun! I know I'm moving far, but our HEARTS ARE ALWAYS CONNECTED!\nSeriously though, we're best friends... \nWe'll be 2gether4ever love u bae\"" with moveinbottom
    
    show text "Writing, Directing, Programming\nMyca Arcangel\n\n\"Hope you had fun! I know I'm moving far, but our HEARTS ARE ALWAYS CONNECTED!\nSeriously though, we're best friends... \nWe'll be 2gether4ever love u bae\"" with Pause(5)
    
    hide text "Writing, Directing, Programming\nMyca Arcangel\n\n\"Hope you had fun! I know I'm moving far, but our HEARTS ARE ALWAYS CONNECTED!\nSeriously though, we're best friends... \nWe'll be 2gether4ever love u bae\"" with moveouttop    
    
    show text "Programming & Editing\nStephanie Arcangel\n\n\"Merry Christmas, Liz! It was fun working on this for you. Hope some of the expression transitions made you doki doki (lol...) \"" with moveinbottom
    
    show text "Programming & Editing\nStephanie Arcangel\n\n\"Merry Christmas, Liz! It was fun working on this for you. Hope some of the expression transitions made you doki doki (lol...) \"" with Pause(3)
    
    hide text "Programming & Editing\nStephanie Arcangel\n\n\"Merry Christmas, Liz! It was fun working on this for you. Hope some of the expression transitions made you doki doki (lol...) \"" with moveouttop        

    show text "Art and Background(googling)\nStacey Arcangel\n\n\"Hey, Liz! Merry Christmas! Hope you like all the art! (...my back hurts...) Wishing you and Nick a wonderful holiday and the best wishes to your future together! Love you Liz!! \"" with moveinbottom
    
    show text "Art and Background(googling)\nStacey Arcangel\n\n\"Hey, Liz! Merry Christmas! Hope you like all the art! (...my back hurts...) Wishing you and Nick a wonderful holiday and the best wishes to your future together! Love you Liz!!\"" with Pause(3)
    
    hide text "Art and Background(googling)\nStacey Arcangel\n\n\"Hey, Liz! Merry Christmas! Hope you like all the art! (...my back hurts...) Wishing you and Nick a wonderful holiday and the best wishes to your future together! Love you Liz!!\"" with moveouttop    
    
    show text "Music\nIncoming DLC for $2.99!" with moveinbottom
    
    show text "Music\nIncoming DLC for $2.99" with Pause(2)
    
    hide text "Music\nIncoming DLC for $2.99" with moveouttop        
    
    show text "~Thanks For Playing~" with pixellate
    
    show text "~Thanks For Playing~" with Pause(5)
    
    show text "~And Thanks For Being an Amazing Friend~" with pixellate
    
    show text "~And Thanks For Being an Amazing Friend~" with Pause(5)
    

    return
