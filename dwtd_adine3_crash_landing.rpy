init python:
    def dwtd_adine3_crash_landing_link(ml):
        ml.find_label('mpsave') \
            .search_say("Her speed quickly increased while she moved towards the water. Then, she did a roll, and another, followed by the third. Dangerously close to the water's surface, she suddenly pulled up, but as she did so, one of her feet went below the surface, where it apparently caught onto something, causing her to spin out of control.", 400) \
            .hook_to("dwtd_adine3_crash_landing") \
            .search_show("adine disappoint c") \
            .link_from("dwtd_adine3_crash_landing_end")

    dwtd_adine3_crash_landing_link(magmalink())

label dwtd_adine3_crash_landing:

    m "I saw her feeble attempt to regain control as she barely managed to steady herself enough to get back to the beach."
    m "She was heading straight for me, her eyes wide with terror."

    if dwtd.check_keypoint():
        call screen dwtd_qte("Dodge!")

    else:
        play sound "fx/system3.wav"
        s "What's wrong? Afraid of a little hug?"
        $ _return = False

    if not _return:
        $ dwtd.will_die()
        stop music
        play sound "fx/impact3.ogg"
        scene black with None
        $ renpy.pause(0.2)
        scene black with Shake ((0, 0, 0, 0), 2.0, dist=20)
        $ renpy.pause(2.0)
        m "The weight of her body slammed into mine.{w=1.0} It felt like every bone in my body had shattered as pain coursed through my entire being."
        m "I heard her roll off, eliciting a painful grunt."
        Ad sad c "Ah...{w=0.2} [player_name]!"
        m "..."
        scene beach with dissolvemed
        show adine sad c with dissolve
        play music "mx/threat.ogg"
        Ad sad c "[player_name]!{w=0.2} [player_name], are you okay!?"
        m "I couldn't focus, the pain was unlike anything I've felt before. My chest felt tight, I could barely breath."
        Ad sad c "D-{w=0.1}don't worry!{w=0.2} I'm going to get help!"
        hide adine with easeoutleft
        play sound "fx/takeoff.ogg"
        m "She ran and took off with urgency. I peered up to see her hastily rise into the air. She had a bit of a waver in her form, she must've landed on one her wings during the impact."
        m "I clutched at my chest, breathing was becoming harder by the second."
        c "{cps=15}Please...{/cps}"
        scene black with dissolvemed
        m "Before too long, I couldn't even breath. I tried to take in anything, but my lungs simply refused."
        stop music fadeout 2.0
        m "The sounds of the waves splashing onto the shore began to diminish. I began to feel drowsy, the pain almost ebbing away..."
        $ renpy.pause (0.8)
        $ dwtd.deathsound(5)
        show dwtd_youdied_text at top with easeintop
        $ renpy.pause(4.0)
        call dwtd_youdied("Incoming Flyer", "Oof, that's unlucky... I know it's the beach episode, but come on!{w=0.5} Constant vigilance!")

    play sound "fx/impact3.ogg"
    m "I managed to dodge her flailing form before she landed harshly. She rolled on the ground a few times, coming to a stop a second later." with Shake ((0, 0, 0, 0), 2.0, dist=10)
    c "Adine!"
    m "With a painful grunt, she pushed herself up with a frown."

    jump dwtd_adine3_crash_landing_end
