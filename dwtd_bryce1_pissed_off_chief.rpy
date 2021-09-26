init python:
    def dwtd_pissed_off_chief_link(ml):
        (ml.find_label('bryce1')
            .search_say("You know, I'm just about done here for the day, but if you want to discuss it over a beer or something, I'd be more than happy.")
            .hook_call_to("dwtd_pissed_off_chief_check")
            .search_menu()
            .branch("I don't usually drink, though.")
            .search_menu()
            .branch("[[press him about wanting to go to a bar.]")
            .search_menu()
            .branch("It can't be that hard.")
            .search_say("Alright, kiddo, that's enough. You better go now before you make me really mad.")
            .hook_call_to("dwtd_pissed_off_chief_menu")
        )
    dwtd_pissed_off_chief_link(magmalink())

label dwtd_pissed_off_chief_check:
    if not dwtd.check_keypoint():
        play sound "fx/system3.wav"
        s "Looks like this \"Hardcore\" timeline is broken. you have a terminal case of stupidity."
        c "I don't usually drink, though."
        Br "That's fine, you don't have to."
        show bryce smirk b with dissolve
        Br "Or maybe we'll find something you'll like."
        c "Actually, I find it worrisome that the chief of police prefers to get drunk instead of hearing important information about a case."
        show bryce brow b with dissolve
        Br "You're quite right. In my own free time I do prefer to get drunk instead of dealing with work. If you find that \"worrisome\", maybe you should try out my job sometime."
        c "It can't be that hard."
        $ renpy.pause (0.5)
        show bryce stern b with dissolve
        Br "Alright, kiddo, that's enough. You better go now before you make me really mad."
        jump dwtd_pissed_off_chief_death
    return

label dwtd_pissed_off_chief_menu:
    menu:
        "[[leave]":
            return
        "[[make fun of him]":
            label dwtd_pissed_off_chief_death:
            $ dwtd.will_die()
            c "ooh yeah you're real scary"
            stop music fadeout 1.0
            play sound "fx/growl.wav"
            show bryce angry b with dissolve
            m "I suddenly realize I made a grave mistake.{w=0.5}{nw}"
            play sound2 "fx/slice.ogg"
            m "I felt a pain across my neck and chest"
            show bryce stern b with dissolve
            queue sound2 "fx/impact.wav"
            m "I felt dizzy and collapsed."
            show bryce sad b with dissolve
            scene black with dissolveslow
            #stuff from the death scene
            $ dwtd.deathsound(2)
            show dwtd_youdied_text at top with easeintop
            $ renpy.pause(4.0)
            call dwtd_youdied("Pissed Off Chief","It is probably a bad idea to piss off someone who is twice your size and has sharp claws")


