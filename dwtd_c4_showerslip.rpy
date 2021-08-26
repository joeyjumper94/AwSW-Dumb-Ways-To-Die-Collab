init:
    find label a4shower:
        search say "She started squirming, and suddenly, her tail whacked around and hit me in the face, causing me to stumble and fall over backwards." as dwtd_c4_showerslip_linknode
        search say "Are you okay?"
        callto label dwtd_c4_showerslip from dwtd_c4_showerslip_linknode return here
    
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
        call dwtd_youdied("You cracked your skull open in the shower and died. {w}Think about how Adine feels...")
    m "I caught myself right before my skull made contact with the hard shower floor."
    return