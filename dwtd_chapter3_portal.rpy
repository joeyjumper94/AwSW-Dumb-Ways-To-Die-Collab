
# Premise is Sebastian turns it on successfully but it's broken, but neither the player nor Sebastian knows, right? Except for an odd whirr, hiss, or buzz. Loud buzz. 
# Interrupt mental monologue? Or just do it at the end, Sebastian had to kick it a couple times to make it start. 
# Sebastian presses the button, unless you stop him. You know more about it than him. It shouldn't sound like that, and you remember an incident where a machine exploded after such a sound. 
# Buzz grows louder and becomes a loud crackle. By this time it's too late.
# Teleport occurs, you know how it goes. 
# Appear, stuck in space, Sebastian's there too. You grasp each other's hands, or maybe torso, and then asphyxiate. 
# "strange painful sensation" and hypoxia within 15 seconds. Burning sensation on one side, freezing on the other? Blinded by a sun?
# Breathless


init:
    find label c3conty
    search say "The next thing that did happen was that I heard Sebastian's voice." for 1000 as dwtb_c3_portal_linknode
    search say "Let's head back. The Chief has to know about this right away."
    callto label dwtd_c3_portal_label from dwtb_c3_portal_linknode return here


label dwtd_c3_portal_label:
    # n "The next thing that did happen was that I heard Sebastian's voice."
    window hide 
    nvl clear
    hide black
    show sebastian normal b
    with dissolvemed
    $ renpy.pause (0.3)
    Sb "Damn, it's not working."
    c "Are you joking again?"
    stop music fadeout 2.0
    $ renpy.pause (0.5)
    # sound: thud
    m "Sebastian kicked the control box hard, then touched the interface."
    # sound: activation? whirr, buzz
    m "Suddenly, the portal buzzed to life." 
    # Sb smile b "Just like the old telly. A bit of percussive maintenance does wonders."
    Sb smile b "There we go, a bit of percussive maintenance does wonders."
    # Sb drop "I suppose it can't be perfect if it's this old."
    

    if not dwtd.check_keypoint():
        play sound "fx/system3.wav"
        s "This is a Hardcore timeline. You can't undo this."
    else:
        call screen dwtd_qte("Stop him.")
        if _return:
            c "Wait, I've heard that buzzing sound before. Are you sure the portal is functioning?"
            Sb disapproval b "What do you mean? Get back in place."
            c "I'm not comfortable anywhere near this thing. It didn't make that sound on the other side. Maybe it's broken?"
            # observe strange effects, sparks, bad interface readings, maybe error messages that Sebastian didn't read?
            Sb "..."
            # sound: shutdown?
            m "Sebastian shut down the interface and crouched down. Opening the door, he peered in."
            show portalb at Pan ((0, 0), (600, 380), 8.0) with dissolvemed
            play music "mx/threat.ogg"
            $ renpy.pause (2.0)
            Sb disapproval b "Huh. Good call, [player_name]."
            c "Can you fix it?"
            Sb normal b "I don't think so. This doesn't look like a simple act of vandalism. It looks like some parts were torn out."
            hide portalb
            hide black
            with fade
            c "I guess that means I'm not leaving, huh."
            Sb "Not yet, at least."
            c "Well, what do we do now?"
            Sb "Let's head back. The Chief has to know about this right away."
            # Sb "I've never trusted big electronic machines like this. Guess I'm not wrong."
            return


        # more panic? do we put such emotions in the player's monologue?
        # less text?
        # if sebastian is blinded, shouldn't he be lit?

        # check out tel.wav
        # what is double_vision_on and double_vision_off?

        $ renpy.pop_call()
        $ dwtd.will_die()

        Sb normal b "And...there you go."
        # sound: crackle, zip, zoop, bang
        m "The two arms lit with power. From the control box, the buzz grew into a loud crackle that drowned out Sebastian's next exclamation."
        # show tp screens
        # sound: tel.wav?
        # check out $ double_vision_on and double_vision_off
        scene black with dissolve
        m "Suddenly, a familiar sensation coursed through my body, as if it were torn into a trillion particles, each with a new destination."
        m "I saw darkness and light, strange forms, and a thousand images of mundane black, breathtaking wonders, and incomprehensible patterns."
        m "I did my best to remember this experience, the last I would ever observe such cosmic beauty, even if it was through an acid trip."
        # fade from vague starscape to defined starscape
        scene dwtd_plain_space with dissolve  # longer dissolve?
        # sound: nothing, music: ominous and minimalistic? industrial 
        m "Space did not disappear. It stabilized into a plain background of stars as my breath was ripped from my lungs."
        # m "I looked around wildly, and despite my failing vision found Sebastian. Did the portal suck him out here too? Where are we, when are we? What happened to our land? Sebastian seemed to be blinded by a nearby sun." 

        # should be shy, but maybe replace blush with shadow. dk seems to dim some, any way to dim further?
        # should he be lit up by the alleged sun?
        show sebastian shy b dk with dissolve
        m "I looked around wildly, and despite my failing vision found Sebastian. Did the portal suck him out here too? He seemed to be blinded by a nearby sun." 
        m "I reached out, and as my vision faded I felt his grasp."

        scene black ((0,0,0,0), 2.0, dist=50)
        $ renpy.pause(2.0)
        $ dwtd.deathsound(5) 
        show dwtd_youdied_text at top with easeintop
        $ renpy.pause (4.0)
        call dwtd_youdied("Spaced", "You used a broken portal, and it spat you out in space.")
        # call dwtd_youdied("Spaced", "The portal malfunctioned and sucked you and Sebastian into space. At least it's not your fault.")
        # they'll miss Sebastian, but maybe not you