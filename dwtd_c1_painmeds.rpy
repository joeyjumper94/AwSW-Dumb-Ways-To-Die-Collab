init:
    find label menu5 as dwtd_c1_painmeds_check_in
    callto label dwtd_c1_painmeds_check from dwtd_c1_painmeds_check_in return here
    search menu
    branch "Look in the bathroom."
    search menu
    branch "Look inside the cabinet."
    search menu
    branch "Take some."
    seach if
    branch "medstaken == 2:"
    seach say "(Can't hurt... because they're pain meds. Hehe.)"
    callto label dwtd_c1_painmeds_death

label dwtd_c1_painmeds_check:
    if not dwtd.check_keypoint():
        play sound "fx/system3.wav"
        s "Looks like this \"Hardcore\" timeline is broken. you have a fatal addiction."
        scene bath with dissolve
        play sound "fx/slide.ogg"
        $ renpy.pause(1.0)
        c "(No razors. There are some pain meds, though.){w=1.0}{nw}"
        c "(I'm not sure if this is a good idea, but here we go.){w=1.0}{nw}"
        play sound "fx/meds.wav"
        $ renpy.pause(2.5)
        c "(more? All right.){w=1.0}{nw}"
        play sound "fx/meds.wav"
        $ renpy.pause(2.5)
        c "(I'm feeling... strange.){w=1.0}{nw}"
        c "(I suppose one more can't hurt.){w=1.0}{nw}"
        c "(Can't hurt... because they're pain meds. Hehe.){w=1.0}{nw}"
        jump dwtd_c1_painmeds_death
    else:
        return
        

label dwtd_c1_painmeds_death:
    $ renpy.popcall()
    $ dwtd.will_die()
    play sound "fx/meds.wav"
    $ renpy.pause(1.5)
    scene bath with fadequick
    $ renpy.pause(1.5)
    scene bath with fadequick
    stop music fadeout 1.0
    $ renpy.pause(2.5)
    scene black with dissolve
    play sound "fx/impact.wav"
    $ renpy.pause(4.5)
    if persistent.c1meds == False:
        $ mp.prescription = True
        $ mp.save()
        $ persistent.c1meds = True
        $ achievement.grant("Prescription")
        $ persistent.achievements+=1
        call syscheck from _call_syscheck_dwtd_c1_painmeds
        play sound "fx/system.wav"
        if system == "normal":
            s "You took a dragon's dose pain medication. This was not a good idea."
        elif system == "advanced":
            s "You took a dragon's dose pain medication. You should probably have known that was a bad idea."
        else:
            s "You took a dragon's dose pain medication. Possibly the stupidest thing I've seen you do... yet."
    $ dwtd.deathsound(2)
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause(4.0)
    call dwtd_youdied("Pain Meds","I guess pain meds actually can hurt.")
