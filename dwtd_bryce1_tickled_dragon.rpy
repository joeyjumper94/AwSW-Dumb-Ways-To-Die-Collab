init python:
    def dwtd_draco_domiens_link(ml):
        (ml.find_label('bryce1')
            .search_say("(Guess I must have passed out after I got Bryce home.)", depth = 1000)
            .hook_call_to('dwtd_draco_domiens_check')
            .search_menu()
            .add_choice('[[Tickle him.]', jump = 'dwtd_draco_domiens_death')
        )
    dwtd_draco_domiens_link(magmalink())

label dwtd_draco_domiens_check:
    if not dwtd.check_keypoint():
        play sound "fx/system3.wav"
        s "Looks like this \"Hardcore\" timeline is broken. you have a terminal case of stupidity."
        $ renpy.pop_call()
        c "Hey, Bryce."
        jump dwtd_draco_domiens_death
    return

label dwtd_draco_domiens_death:
    $ dwtd.will_die()
    m "since Byrce didn't respond, I decided to tickle him."
    hide cgbryce
    hide black
    show bryce laugh
    with fade
    Br "AHAHAHAHAHAHAHA."
    m "Bryce was writhing in laughter"
    play sound "fx/impact3.ogg"
    play sound2 "fx/bite.ogg"
    m "Byrce suddenly launches ontop of me and a sharp pain wracks by body"
    m "As Bryce's laughter subsided he got off of me"
    Br normal "[player_name] don't do that."
    m "I couldn't breathe"
    Br stern "[player_name], are you ok?"
    Br sad "[player_name]."
    scene black with dissolveslow
    $ dwtd.deathsound(5)
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause(4.0)
    call dwtd_youdied("Draco Dormiens Nunquam Titillandus","Draco Dormiens Nunquam Titillandus\nIt is a Latin Phrase, it means Never Tickle a Sleeping Dragon.")
