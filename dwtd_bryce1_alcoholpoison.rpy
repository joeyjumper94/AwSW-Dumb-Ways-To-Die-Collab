init:
    find label bryce1
    callto label dwtd_bryce1_alcoholpoison_init

    search menu "I don't usually drink, though."
    branch "I don't usually drink, though."
    callto label dwtd_bryce1_alcoholpoison_deny

    find label waitmenu
    search say "Noted. I'll be right back."
    callto label dwtd_bryce1_alcoholpoison_deny if not beer
    search if "beer == False" for 1000
    branch "beer == False":
        search menu
        branch "Not really. I guess I can stay for a little while."
        search menu
        branch "I don't really drink, though."
        callto label dwtd_bryce1_alcoholpoison_deny
    search menu "I would, but I don't think I can beat someone like you."
    branch "I would, but I don't think I can beat someone like you.":
        callto label dwtd_bryce1_alcoholpoison_deny
    search menu "That sounds easy enough."
    branch "That sounds easy enough.":
        callto label dwtd_bryce1_alcoholpoison_deny
    search menu "Heck, no."
    search menu "Alright, it's a buzz."
    branch "Alright, it's a buzz.":
        callto label dwtd_bryce1_alcoholpoison_deny
    search menu "I may have underestimated this..."
    branch "I may have underestimated this...":
        callto label dwtd_bryce1_alcoholpoison_deny
    search menu "M-Might as well do that now..."
    branch "M-Might as well do that now...":
        callto label dwtd_bryce1_alcoholpoison_deny
    

    search say "Hey, are you okay? You fell down, and you look kinda messed up."
    jumpto label dwtd_bryce1_alcoholpoison_end if dwtd.bryce1_alcoholpoisoning >= 4





    python in dwtd:
        bryce1_alcoholpoisoning = 0;

label dwtd_bryce1_alcoholpoison_init:
    python in dwtd:
        bryce1_alcoholpoisoning = 0;

        if get_chapter() == 1:
            bryce1_alcoholpoisoning = renpy.python.store_dicts['store'].get('medstaken', 0);
    return

label dwtd_bryce1_alcoholpoison_deny:
    $ dwtd.bryce1_alcoholpoisoning += 1;
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
    call dwtd_youdied("If you're such a lightweight, perhaps you shouldn't dive right into a drinking contest with a dragon. Alcohol poisoning is a dangerous issue.")