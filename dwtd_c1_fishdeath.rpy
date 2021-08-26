init:
    find label _call_skiptut_3:
        search if 'food == "fish"'
        search if 'food == "fish"'
        branch 'food == "fish"':
            search say "Not that this whole situation was already bizarre enough, there was also now the vague sense of danger conveyed by Reza's earlier words. I did not even have an idea what kind of threat might be lurking out there." as dwtd_c1_fishdeath_linknode
        search say "Sure thing."
        callto label dwtd_c1_fishdeath from dwtd_c1_fishdeath_linknode return here

label dwtd_c1_fishdeath:
    m "I looked back down to the fish on the plate in front of me."

    menu:
        "[[Take a bite.]":
            $ dwtd.will_die()
            $ renpy.pop_call()
            m "I took a bite of my somewhat unusual breakfast. While I already thought the smell was quite peculiar, the taste had been even worse. I imagined it might be the kind of delicacy that had an acquired taste. One that I certainly hadn't acquired yet. I decided to get outside before it was too late."
            m "However, when getting up from the table, my legs became weak and my vision went blurry."
            stop music fadeout 2.0
            scene black with dissolveslow
            play sound "fx/impact3.ogg"
            with Shake ((0, 0, 0, 0), 1.5, dist=10)
            $ renpy.pause (3.0)
            $ dwtd.deathsound(5)
            show dwtd_youdied_text at top with easeintop
            $ renpy.pause(4.0)
            call dwtd_youdied("Something Fishy","Turns out the fish wasn't edible for humans. That's too bad.")
                

        "[[Don't eat it.]" if dwtd.check_keypoint():
            pass

    m "I decided against eating my somewhat unusual breakfast."
    m "Eventually, I got up, ready to be on my way for whatever else the day might bring."

    show sebastian normal b with dissolve
    
    Sb "Are you done?"
    c "Sure am."
    Sb "How'd you like it?"
    c "Well, I didn't actually try the fish."
    Sb "Trust me, you aren't the only one concerened by that dish."
    return