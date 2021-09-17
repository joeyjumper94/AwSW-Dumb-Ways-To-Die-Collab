init python:
    def dwtd_c4_showerslip_link(ml):
        ml.find_label("a4shower") \
            .search_say("She started squirming, and suddenly, her tail whacked around and hit me in the face, causing me to stumble and fall over backwards.") \
            .hook_to("dwtd_c4_showerslip") \
            .search_say("Are you okay?") \
            .link_from("dwtd_c4_showerslip_end")
    dwtd_c4_showerslip_link(magmalink())
    
label dwtd_c4_showerslip:
    if dwtd.check_keypoint():
        call screen dwtd_qte("Catch yourself.")
    else:
        play sound "fx/system3.wav"
        s "This timeline is hardcore, pal. You can't reload to fix this."
        $ _return = False
    if not _return:
        $ dwtd.will_die()
        $ renpy.pop_call()
        stop music
        play sound "fx/impact3.ogg"
        scene black ((0, 0, 0, 0), 2.0, dist=50)
        $ renpy.pause (3.0)
        $ dwtd.deathsound(5)
        show dwtd_youdied_text at top with easeintop
        $ renpy.pause (4.0)
        call dwtd_youdied("Shower Slip", "You cracked your skull open in the shower and died. {w}Think about how Adine feels...")
    m "I caught myself right before my skull made contact with the hard shower floor."
    jump dwtd_c4_showerslip_end