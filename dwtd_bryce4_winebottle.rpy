init python:
    def dwtd_bryce4_winebottle_link(ml):
        ml.find_label('bryce4') \
            .search_say("You don't need to apologize for anything.", 400) \
            .hook_to("dwtd_bryce4_winebottledodge") \
            .search_say("Do you think it's easy for me? Seeing so many people die on my watch?", 500) \
            .link_from("dwtd_bryce4_winebottledodge_end")

    dwtd_bryce4_winebottle_link(magmalink())

label dwtd_bryce4_winebottledodge:

    show bryce angry with dissolve

    m "Suddenly, he twisted his body, gripping the now empty bottle at its neck, and pulled back as far as his forelegs would allow it."

    if dwtd.check_keypoint():
        call screen dwtd_qte("Dodge!")

    else:
        play sound "fx/system3.wav"
        s "There's no escape from the wine bottle now..."
        $ _return = False

    if not _return:
        $ dwtd.will_die()
        stop music
        play sound "fx/bottlesmash2.ogg"
        scene black with None
        $ renpy.pause(0.2)
        scene black with Shake ((0, 0, 0, 0), 2.0, dist=10)
        play sound "fx/impact3.ogg"
        $ renpy.pause(2.0)
        m "The bottle struck me on the head, shattering instantly.{w=0.5} The sharpnel wedged itself deep into my skin, tearing right into my skull."
        m "{cps=12}That was{/cps}{w=0.5} {cps=10}the last thing I...{/cps}"
        $ renpy.pause (2.0)
        Br sad "{cps=5}...{/cps}"
        Br sad "{cps=8}Dammit...{/cps}"
        $ renpy.pause (0.8)
        $ dwtd.deathsound(5)
        show dwtd_youdied_text at top with easeintop
        $ renpy.pause(4.0)
        call dwtd_youdied("Wine Anger","Haven't you learned by now to dodge?")

    stop music
    play sound "fx/bottlesmash2.ogg"
    m "I dodged just in time to feel the bottle whip right by my head. It shattered instantly into pieces."
    Br "{cps=8}...{/cps}"
    c "{cps=8}...{/cps}"
    Br "{cps=8}...{/cps}"
    show bryce sad with dissolve
    $ renpy.pause (1.0)
    Br sad "{cps=12}...I.{/cps}"
    Br sad "{cps=12}I am so sorry...{/cps}"
    c "..."
    m "I glanced to where the bottle had shattered and flinched at the shards scattered about. If I didn't get out of the way..."
    c "..."
    c "Why did you do that, Bryce?"
    Br sad "...{w=0.5}Sorry.{w=0.5} I lost control."
    m "He let out a loud sigh, the guilt on his face apparent."
    play music "mx/shoal.ogg" fadein 2.0

    jump dwtd_bryce4_winebottledodge_end
