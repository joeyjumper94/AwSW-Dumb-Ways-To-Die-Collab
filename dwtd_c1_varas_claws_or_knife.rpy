
init python:
    def dwtd_c1_vara_death_link(ml):
        ml.find_label("seccont") \
            .search_say("Reza didn't seem to share the same interest and instead was more smitten with the generator, but given our reasons for coming here in the first place, I couldn't blame him for his enthusiasm being focused on something else.", 800) \
            .hook_to("dwtd_c1_vara_death") \
            .search_say("I gave her a generous tip on your behalf. I hope you don't mind.") \
            .link_from("dwtd_c1_vara_death_end")
    dwtd_c1_vara_death_link(magmalink())
    
        
label dwtd_c1_vara_death:
    stop music fadeout 1.0
    window hide
    if renpy.random.randint(0,1) == 1:
        #Created by Eval
        nvl clear
        m "My thoughts were interrupted as something started running in my direction."
        scene black with dissolve
        scene dwtdvaraknife at Pan ((580, 0), (0, 326), 5) with dissolvemed
        $ renpy.pause (3.5)
        c "(Wait, what's that in her bag?)"
        if dwtd.check_keypoint():
            call screen dwtd_qte("Dodge.")
        else:
            play sound "fx/system3.wav"
            s "This timeline is hardcore, pal. You can't reload to fix this."
            $ _return = False
        if not _return:
            $ dwtd.will_die()
            $ renpy.pop_call()
            stop music fadeout 1.0
            play sound "fx/slice.ogg"
            $ renpy.pause (1.0)
            stop sound
            scene black with dissolve
            play sound "fx/impact3.ogg"
            m "I fell to the ground, clutching at the searing pain that ran through my leg."
            $ renpy.pause (0.5)
            Vr none "...{w=0.5}{nw}"
            play sound "fx/slice.ogg"
            $ renpy.pause (5.0)
            $ dwtd.deathsound(4)
            show dwtd_youdied_text at top with easeintop
            $ renpy.pause (4.0)
            call dwtd_youdied("Slice and Dice", "Vara slashed your leg and accidentally got you in the neck. How unlucky.")
        m "I narrowly avoided the blade of the knife as it zipped past me, causing me to stumble back."
        if dwtd.check_keypoint():
            call screen dwtd_qte ("Avoid falling.")
        else:
            play sound "fx/system3.wav"
            s "This timeline is hardcore, pal. You can't reload to fix this."
            $ _return = True
        if _return:
            $ dwtd.will_die()
            $ renpy.pop_call()
            stop music fadeout 1.0
            m "I attempted to shift my body weight to regain my footing. However, I was only able to change the direction in which I fell."
            m "As I was falling, I noticed the sheen of the knife's blade as it made it's way closer to my neck."
            scene black
            play sound "fx/slice.ogg"
            $ renpy.pause (5.0)
            $ dwtd.deathsound(4)
            show dwtd_youdied_text at top with easeintop
            $ renpy.pause (4.0)
            call dwtd_youdied("Unfortunate", "You probably would have been fine if you didn't redirect your fall into Vara's knife.")
        scene town3 with fade
        m "I managed to regain my footing at the last moment and watched as what appeared to be a little dragon disappeared into the distance. Even though I'd seen enough dragons to recognize their variations in size, color, and other attributes, I guessed this one must have been a juvenile of its species."
        c "(Why is a baby dragon carrying around a knife?)"
    else:
        #Created by joeyjumper94
        if dwtd.check_keypoint():
            call screen dwtd_qte("Pay Attention!",1.0)
        else:
            play sound "fx/system3.wav"
            s "Looks like this \"Hardcore\" timeline is broken. you will never see her coming."
            $ _return = False
        if not _return:
            $ dwtd.will_die()
            play sound "fx/slice.ogg"
            show vara normal flip at left with easeinleft
            m "My thoughts were interrupted as a sharp pain tore through my leg, I looked down and saw blood gushing from the wound"
            show vara shocked flip with dissolvemed
            play sound2 "fx/impact.wav"
            m "I felt dizzy and collapsed."
            show vara sad flip with dissolvemed
            scene black with dissolveslow
            #stuff from the death scene
            $ dwtd.deathsound(2)
            show dwtd_youdied_text at top with easeintop
            $ renpy.pause(4.0)
            call dwtd_youdied("Vara's Claws","When there are dragons rushing about with sharp claws, perhaps one should pay attention to their surroundings.")        
        m "I looked up and saw someone zip towards me just a little too close, causing me to stumble back. It was a rather small dragon with a bag clamped in their maw who apparently had somewhere to be."
        scene cgvara at Pan ((0, 326), (580, 0), 5) with dissolvemed
        $ renpy.pause(3.5)
        scene town3 with fade
        m "I managed to regain my footing at the last moment and watched as what appeared to be a little dragon disappeared into the distance. Even though I'd seen enough dragons to recognize their variations in size, color, and other attributes, I guessed this one must have been a juvenile of its species."
    m "Shortly afterwards, Sebastian joined me outside, having taken care of the tab."
    show sebastian normal b with dissolve
    play music "mx/sail.ogg" fadein 1.0
    jump dwtd_c1_vara_death_end
