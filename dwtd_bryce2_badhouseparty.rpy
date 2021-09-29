init python:
    def dwtd_bryce2_badhouseparty_link(ml):
        ml.find_label('bryce2cont2') \
            .search_if() \
            .search_say("That makes me wonder. I know you can use your forelegs well enough for things, but what about your hind legs? Can you walk on those?") \
            .search_menu("That's just the way we are.") \
            .search_menu("No way.") \
            .search_menu("That was awesome!") \
            .search_say("That was exhausting. Just the right time for a beer.") \
            .hook_to('dwtd_bryce2_badhouseparty_check') \
            .search_menu("Stop him.") \
            .branch() \
            .search_say("I snatched the beer out of his reach at the last moment.") \
            .link_from('dwtd_bryce2_badhouseparty_check_failed') \
            .search_say("While he was still flailing around on the ground, I dashed through the front door.") \
            .hook_to('dwtd_bryce2_badhouseparty_death',return_link=False)
    dwtd_bryce2_badhouseparty_link(magmalink())

label dwtd_bryce2_badhouseparty_check:
    if not dwtd.check_keypoint():
        $ dwtd.will_die()
        play sound "fx/system3.wav"
        s "Looks like this \"Hardcore\" timeline is broken. Guess you're not a fan of alcoholism."
        jump dwtd_bryce2_badhouseparty_check_failed
    jump dwtd_bryce2_badhouseparty_check_return

label dwtd_bryce2_badhouseparty_death:
    $ dwtd.will_die()
    $ brycestatus = "bad"
    stop music fadeout 2.0
    scene black with dissolvemed
    m "Once outside, I leaned out over Bryce's balcony railing to pour out the beer."
    Br angry "Just give--"
    m "Bryce stumbled through the door into me, reaching over my head for the spilling beer. The impact of his weight jarred me into the rail."
    m "Suddenly, I was overbalanced. My legs lifted off the balcony floor, then all of me was in the air, following the beer."
    c "Sh--{w=0.8}{nw}"
    play sound "fx/wooshimpact.wav"
    $ renpy.pause(0.7)
    play sound2 "fx/squish.ogg"
    show dwtd_youdied_text at top with vpunch
    $ renpy.pause(2.0)
    $ dwtd.deathsound(2)
    $ renpy.pause(4.0)
    call dwtd_youdied("Bad House Party","You fell from a second floor balcony headfirst into a puddle of spilled beer.")
