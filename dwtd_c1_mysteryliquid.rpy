init python:
    def dwtd_c1_mysteryliquid_link(ml):
        (ml.find_label("menufridge")
            .search_menu()
            .branch("Examine an unlabeled container.")
            .search_say("(It's salty.)")
            .hook_to("dwtd_c1_mysteryliquid_drink")
            .search_if()
            .hook_to("dwtd_c1_mysteryliquid_achievement")
        )
    dwtd_c1_mysteryliquid_link(magmalink())

label dwtd_c1_mysteryliquid_drink:
    $ dwtd.will_die()
    c "(Hmm. I don't feel so...)"
    play sound "fx/platecrash.ogg"
    stop music fadeout 1.5
    $ renpy.pause(1.5)
    scene black with dissolvemed
    play sound "fx/impact.wav"
    $ renpy.pause(4.0)
    show dwtd_youdied_text at top with easeintop
    # But it's okay, you get an achievement, bucko!
    jump dwtd_c1_mysteryliquid_drink_return

label dwtd_c1_mysteryliquid_achievement:
    call dwtd_youdied("Drank a Mysterious Liquid", "You decided to drink a liquid that you knew absolutely nothing about.")
