# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg classroom = "bg/BG101_01.png"
image bg classroom_sunset = "bg/BG101_02.png"
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


#--------------Other------------------------

image myca normal = "others/sylvie_normal.png"
image myca giggle = "others/sylvie_giggle.png"
image myca smile = "others/sylvie_smile.png"
image myca surprised = "others/sylvie_surprised.png"

image blackwelder normal = "others/blackwelder_normal.png"


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
    
    #call day1morning1
    
    #call day1morning2

    #call day1afternoon
    
    #call day2morning
    
    call day2_classroomtransition1
    
    call day3morning
    
    #credits ..

    return
