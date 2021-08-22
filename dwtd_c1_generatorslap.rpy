init:
    find label _call_skiptut_3:
        search say "Shh, be quiet. I'll let you know more as soon as I can. But for now, let's just play along. After all, we already have one of these babies." as dwtd_cw_stopslap_linknode
        search say "God knows we need them."
        callto label dwtd_c1_stopslap from dwtd_cw_stopslap_linknode return here

label dwtd_c1_stopslap:
    m "Reza lifted his hand, seemingly to give the generator a light pat."

    if dwtd.check_keypoint("C1"):
        call screen dwtd_qte("Stop him.")
    else:
        play sound "fx/system3.wav"
        s "This timeline is hardcore, pal. You can't reload to fix this."
        $ _return = False
    if not _return:
        $ dwtd.will_die()
        $ renpy.pop_call()
        stop music fadeout 1.0
        play sound "fx/explosion.ogg"
        scene black with Shake ((0, 0, 0, 0), 3.0, dist=50)
        $ renpy.pause (4.0)
        scene dwtdfirecafe with dissolveslow
        call dwtd_youdied("You didn't stop Reza from slapping the generator and blew up.")
    
    m "I grabbed Reza's wrist moments before his hand made contact with the generator."
    c "Maybe you shouldn't slap it like that, it might be fragile."
    Rz annoyed "Why are you so careful all of a sudden?"
    c "Let's just make sure we don't break any of them before they go through the portal."
    show reza normal with dissolve
    return
