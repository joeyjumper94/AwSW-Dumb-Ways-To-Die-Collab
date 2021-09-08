init python:
    def dwtd_c3_katsuhelp_link(ml):
        ml.find_label("c3arc") \
            .search_if("seenkatsu == False") \
            .branch() \
            .search_menu("Sure, I'll help you.") \
            .branch() \
            .search_say("Slowly, the cart started moving, and after a few seconds, it was freed from the perilous clutches of the muddy puddle.") \
            .hook_call("dwtd_c3_katsuhelp")
    dwtd_c3_katsuhelp_link(magmalink())

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

    $ dwtd.deathsound(5)
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause(4.0)
    call dwtd_youdied("Stranger's Cart", "Be careful with strangers asking for you to walk over to their carts.")
