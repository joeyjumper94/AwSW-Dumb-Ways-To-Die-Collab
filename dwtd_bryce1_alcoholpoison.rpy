init python:
    def dwtd_bryce1_alcoholpoison_link(ml):
        ml.find_label('bryce1') \
            .hook_call('dwtd_bryce1_alcoholpoison_init') \
            .search_menu("I don't usually drink, though.") \
            .branch() \
            .search_say("That's fine, you don't have to.") \
            .hook_call('dwtd_bryce1_alcoholpoison_deny') \

        nothingyet = ml.find_label('waitmenu') \
            .search_say("Noted. I'll be right back.") \
            .hook_call('dwtd_bryce1_alcoholpoison_deny',condition="beer == False") \
            .search_if("beer == False")
        nothingyet.branch() \
            .search_menu("Not really. I guess I can stay for a little while.") \
            .branch() \
            .search_menu("I don't really drink, though.") \
            .branch() \
            .search_show("bryce laugh") \
            .hook_call('dwtd_bryce1_alcoholpoison_deny')

        cantbeat = nothingyet.search_menu("I would, but I don't think I can beat someone like you.")
        cantbeat.branch() \
            .search_say("How about a handicap, then? I'll go easy on you.") \
            .hook_call('dwtd_bryce1_alcoholpoison_deny')

        easyenough = cantbeat.search_menu("That sounds easy enough.")
        easyenough.branch() \
            .search_python("renpy.pause (0.5)") \
            .hook_call('dwtd_bryce1_alcoholpoison_deny')

        buzz = easyenough.search_menu("Alright, it's a buzz.")
        buzz.branch() \
            .search_python("renpy.pause (0.5)") \
            .hook_call('dwtd_bryce1_alcoholpoison_deny')

        underestimated = buzz.search_menu("I may have underestimated this...")
        underestimated.branch() \
            .search_say("You can always give up.") \
            .hook_call('dwtd_bryce1_alcoholpoison_deny')

        mightaswell = underestimated.search_menu("M-Might as well do that now...")
        mightaswell.branch() \
            .search_python("renpy.pause (0.5)") \
            .hook_call('dwtd_bryce1_alcoholpoison_deny')

        mightaswell.search_say("Hey, are you okay? You fell down, and you look kinda messed up.") \
            .hook_to('dwtd_bryce1_alcoholpoison_end',condition="dwtd.bryce1_alcoholpoisoning >= 4")
    dwtd_bryce1_alcoholpoison_link(magmalink())




init python in dwtd:
    bryce1_alcoholpoisoning = 0

label dwtd_bryce1_alcoholpoison_init:
    python in dwtd:
        bryce1_alcoholpoisoning = 0

        if get_chapter() == 1:
            bryce1_alcoholpoisoning = renpy.python.store_dicts['store'].get('medstaken', 0)
    return

label dwtd_bryce1_alcoholpoison_deny:
    $ dwtd.bryce1_alcoholpoisoning += 1
    return

label dwtd_bryce1_alcoholpoison_end:
    scene black with dissolveslow
    Br brow "[player_name]? Hey."
    $ renpy.pause(0.8)
    play sound "fx/hit2.ogg"
    $ renpy.pause(0.6)
    Br stern "[player_name], this isn't funny. Don't tell me this was too much for you."
    Wr "Is something wrong?"
    Br stern "[player_name] isn't moving. After falling over..."
    play sound "fx/chair.wav"
    $ renpy.pause(1.2)
    Wr "... I'm not feeling any breathing."
    Br angry "What?!" with hpunch
    $ renpy.pause(0.8)
    $ dwtd.deathsound(2)
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause(4.0)
    call dwtd_youdied("Alcohol Poisoning","If you're such a lightweight, perhaps you shouldn't dive right into a drinking contest with a dragon. Alcohol poisoning is a dangerous issue.")