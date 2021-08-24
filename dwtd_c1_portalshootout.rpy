init:
    find label continuation
    search menu "Well, you didn't make it easy."
    search say "More than enough. I'm afraid this whole place will be gone soon. And we better not be here when it happens." as dwtd_c1_portalshootout_start
    search menu
    branch "Yeah, I know."
    callto label dwtd_c1_portalshootout from dwtd_c1_portalshootout_start return here

    search show "reza gunpoint dk"
    callto label dwtd_c1_portalshootout_2


label dwtd_c1_portalshootout:
    if not dwtd.check_keypoint():
        play sound "fx/system3.wav"
        s "Looks like this \"Hardcore\" timeline is broken. Maverick's just going to be late."
    else:
        menu:
            "Yeah, I know.":
                return
            "What are you talking about?":
                pass
            "Just spit it out already!":
                pass
    $ renpy.pop_call()
    $ dwtd.will_die()
    Rz "I hoped you'd see it too, but then it took me a while to understand, and I had a head start on you. In any case..."




    Rz "It's amazing to think it's even possible, but sad to know it won't last."
    c "What won't?"
    Rz "When do you think we are? Think, [player_name]. That moon is ours, but rotated. The beaches, the flora. Even the dragons themselves look like our dinosaurs."
    Rz "This is the Cretaceous. And that..."
    scene chap1 at Pan((0, 100), (0, 0), 2.0) with dissolve
    m "He pointed into the sky."
    show chap1:
        ease 1.0 zoom 3.0 xpos -1.9
    Rz "That's the end."
    scene np1n dk at Pan ((350,200), (350,200), 0.0)
    show reza normal dk
    with dissolve
    Rz "I've been talking with our leadership. Secret messages, just like the one I gave you. We have to take the generators we can, while we can."
    Rz "You're here to keep them distracted. Keep them thinking that the deal is proceeding as normal."
    c "Shouldn't we warn them?"
    Rz annoyed dk "Warn them? [player_name]..."
    Rz "No, we have to do it. You know the state we're in."
    m "With the tense subject, my gaze couldn't help but snap when I noticed movement nearby. It looked like wind had rustled a bush. Except for the fact there was no wind."
    Rz angry dk "We could barely deflect something like Chicxulub before our fall. I haven't heard anything about them even having a space program!"
    c "Reza."
    Rz annoyed dk "[player_name], don't you {i}dare{/i} get soft on me. You're my only backup out here."
    c "Reza, look."
    m "He turned around to face the movement I'd seen, before drawing his gun."
    play sound "fx/rev.ogg"
    Rz gunpoint dk "You! How dare you follow us, even here!" with vpunch
    m "The disturbance came closer, revealing itself to be Maverick hiding nearby to listen in on our conversation."
    show reza gunpoint dk at Position(xpos = 0.8)
    show np1n dk at Position(xpos=1.05, xanchor="right")
    with ease
    show maverick angry flip dk at Position(xpos=0.0) with easeinleft

    Mv "You come here to steal our generators? And to fail to warn us of what?"
    c "Reza, wait. I'm not sure-{w=1.0}{nw}"
    show maverick nice flip dk with dissolve
    Rz gunself dk "Which side are you on, [player_name]? We can't let him tell the others."
    show maverick angry flip dk with dissolve
    c "But--"
    show reza gunpoint dk with dissolve
    play sound "fx/rev.ogg"
    queue sound "fx/growl.wav"
    $ renpy.pause (0.8)
    call screen dwtd_qte("Stop Reza.", 1.5)
    if _return:
        show reza gunself dk with dissolve
        play sound "fx/gunshot2.wav"
        $ renpy.pause(0.3)
        show maverick rage flip dk with dissolve
        show maverick at Position(xpos=0.6) with move6
        show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor='top')
        show reza at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor='top')
        with move9
        play sound2 "fx/bite.ogg"
        $ renpy.pause(0.5)

        play sound "fx/impact3.ogg"

        scene starsrx at Pan((0, 200), (0, 0), 20.0)
        show starsr at Pan((0, 200), (0, 0), 20.0)
        show stars at Pan((0, 200), (0, 0), 20.0)
        with dissolve

        m "My attempt to stop Reza only made him target me first. At the distance I'd closed in on him, he had no trouble putting the bullet where it hurt."

        hide stars with dissolveslow3

        m "I lay in the grass, not thinking anything at all."

        scene black with dissolveslow

        $ renpy.pause (0.5)

        call dwtd_deathsound(5)
        show dwtd_youdied_text at top with easeintop
        $ renpy.pause(4.0)
        
        call dwtd_youdied("Reza shot you for the one and only crime warranting immediate execution under your home city's laws: being a traitor. Maybe don't do that to him?")
    else:
        play sound "fx/gunshot2.wav"
        $ renpy.pause(0.2)
        play sound "fx/dragonpain.wav"
        show maverick angry flip dk:
            easeout 0.3 xpos -0.05
        $ renpy.pause(2.0)
        Rz angry dk "That's not stopping him. Run, [player_name]!"
        show reza angry flip dk
        $ renpy.pause(0.3)
        hide reza normal flip dk with easeoutright
        m "I struggled to shake off the shock of our mission going sideways so quickly. By the time I'd taken my first step, Maverick was on top of me."

        show maverick rage flip dk:
            ease 0.8 zoom 1.5 xpos 0.0
        play sound "fx/whooshimpact.wav"
        $ renpy.pause(0.8)
        play sound "fx/bite.ogg"
        scene black with hpunch
        play sound2 "fx/rolldownhill.ogg"

        m "I hit the ground in a world of pain."

        scene starsrx at Pan((0, 200), (0, 0), 20.0)
        show starsr at Pan((0, 200), (0, 0), 20.0)
        show maverick angry c flip dkr:
            zoom 2.0
            yanchor -0.5
            ypos -0.1
            ease 0.5 xpos -0.3
            ease 0.5 xpos -0.4
            ease 0.5 xpos -0.3
            ease 0.5 xpos -0.4
            pause 0.4
            easeout 0.1 ypos -0.4
        with dissolve
        $ renpy.pause(2.0)
        
        play sound "fx/bitescr.ogg"
        m "Everything faded as I felt a chunk of my flesh torn away."
        play sound "fx/snarl.ogg"

        $ renpy.pause (0.3)
        play sound2 ["fx/takeoff.ogg", "<silence .5>", "fx/gunshots3.ogg", "fx/dragonpain.wav"]

        hide maverick with easeoutright
        hide starsr with dissolvemed

        $ renpy.pause (7.0)
        call dwtd_deathsound(5)
        show dwtd_youdied_text at top with easeintop
        $ renpy.pause(4.0)
        call dwtd_youdied("In your last moments, you learned what it was like to be torn apart alive.")


label dwtd_c1_portalshootout_2:
    if not dwtd.check_keypoint():
        play sound "fx/system3.wav"
        s "Hardcore timelines can't be fixed!"
    else:
        call screen dwtd_qte("Intervene.", 1.0)
        if not _return:
            return
    $ renpy.pop_call()
    $ dwtd.will_die()
    play sound "fx/gunshot2.wav"
    show reza angry dk
    show maverick scared flip dk
    with dissolve
    play soundloop "fx/hiss.ogg" fadein 1.0

    m "I threw myself into Reza's gun arm, forcing the gun away and saving Maverick the bullet. Instead, a new, round hole had appeared in the cardboard box on the portal platform."
    show maverick angry dk with dissolve
    $ renpy.pause (0.3)
    hide maverick with easeoutleft
    play sound2 "fx/takeoff.ogg"
    Rz "That's right! Run!"
    play sound "fx/rev.ogg"
    show reza gunpoint dk with dissolve
    c "Reza! Stop!"
    Rz angry dk "Get out of my way, [player_name]! I'll deal with you later. You know we can't let him--"

    stop soundloop fadeout 0.5
    play sound "fx/explosion.ogg"
    scene black with hpunch
    $ renpy.pause(3.0)
    play sound2 "fx/rolldownhill.ogg"
    scene np1 dwtd_explosion at Pan((50,0), (400,200), 10.0) with dissolveslow
    play soundloop "fx/fire2.ogg" fadein 2.0
    $ renpy.pause(7.0)
    call dwtd_deathsound(5)
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause(4.0)
    call dwtd_youdied("I warned you about dead-end timelines. But did you listen? Oh no. You had to try to stop Reza with a generator sitting on the portal platform.")
