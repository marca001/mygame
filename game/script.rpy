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




#--------------Other------------------------

image myca normal = "others/sylvie_normal.png"
image myca giggle = "others/sylvie_giggle.png"
image myca smile = "others/sylvie_smile.png"
image myca surprised = "others/sylvie_surprised.png"

image blackwelder normal = "others/blackwelder_normal.png"


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

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

#-----------------------------------------------



# The game starts here.
label start:
    
    $ k_points = 0
    $ n_points = 0
    $ kaito_dream = False    
    
    #call day1morning1
    
    #call day1morning2

    call day1afternoon
    
    call day2morning

    return
