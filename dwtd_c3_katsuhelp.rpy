init:
    find label c3arc
    search if
    branch "seenkatsu == False"
    search menu
    branch "Sure, I'll help you."
    search say "Slowly, the cart started moving, and after a few seconds, it was freed from the perilous clutches of the muddy puddle."
    callto label dwtd_c3_katsuhelp


label dwtd_c3_katsuhelp:
    if not dwtd.check_keypoint():
        play sound "fx/system3.wav"
        s "This is a Hardcore timeline. You can't undo this."
    else:
        call screen dwtd_qte("Jump aside.")
        if _return:
            m "You jump aside as it begins to move rapidly, almost picked up by Katsuharu."
            return
    $ renpy.pop_call()
    $ dwtd.will_die()
    play sound "fx/cartdown.ogg"
    m "The cart begins to move freely abruptly, knocking me over and rolling on top."
    Ka excited dk "It's free!"
    m "I flailed, trying to make noise even as the cart crushed the air from my lungs."
    Ka normal dk "Hm?"
    Ka exhausted dk "Oh! Hold on!"
    play sound "fx/cartlift.ogg"
    m "He pressed back up against the cart, trying to budge it off of me. As a result of his disturbing its weight, something in my chest gave way."
    play sound "fx/loremkick.ogg"
    scene black with None

    $ renpy.pause (0.5)

    call dwtd_deathsound(5)
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause(4.0)
    call dwtd_youdied("Be careful with strangers asking for you to walk over to their carts.")
