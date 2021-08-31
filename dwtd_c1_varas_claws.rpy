init:
    find say "Reza didn't seem to share the same interest and instead was more smitten with the generator, but given our reasons for coming here in the first place, I couldn't blame him for his enthusiasm being focused on something else." as dwtd_varas_claws_init
    search say "I regained my footing and watched as it disappeared into the distance. Even though I'd seen enough dragons to recognize their variations in size, color, and other attributes, I guessed this one must have been a juvenile of its species.\nShortly afterwards, Sebastian joined me outside, having taken care of the tab." as dwtd_varas_claws_return
    callto label dwtd_varas_claws_check from dwtd_varas_claws_init return dwtd_varas_claws_return

label dwtd_varas_claws_check:
    stop music fadeout 1.0
    window hide
    if dwtd.check_keypoint():
        call screen dwtd_qte("Pay Attention!",1.5)
    else:
        play sound "fx/system3.wav"
        s "Looks like this \"Hardcore\" timeline is broken. you will never see her coming."
        $ _return=False
        
    if _return:
        m "I looked up and saw someone zip towards me just a little too close, causing me to stumble back. It was a rather small dragon with a bag clamped in their maw who apparently had somewhere to be."
        scene cgvara at Pan ((0, 326), (580, 0), 5) with dissolvemed
        $ renpy.pause(3.5)
        scene town3 with fade
        return
    else:
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
