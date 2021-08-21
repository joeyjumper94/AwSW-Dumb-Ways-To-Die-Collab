init:
    find label begingame
    callto label dwtd_core_init_hardcore

    find label skipintro
    search if "persistent.endingsseen == 0"
    branch else:
        search python 'c = DynamicCharacter (\"player_name\", color=playercolor, callback=rolly)'
        jumpto label dwtd_core_init_hardcore


label dwtd_core_init_hardcore:
    python in dwtd:
        #Ah, Python2. Why did you order your dicts? It's nice, but why?
        keypoint_names = ['RESET','C1','C1_FOUND_LEMON','C1_CHARACTER_SELECT','C2','C2_CHARACTER_SELECT','C3','C3_CHARACTER_SELECT','C4','C4_CHARACTER_SELECT','C5']
        keypoint_enum = {\
            'RESET': 0,
            'C1': 10,
            'C1_FOUND_LEMON': 20,
            'C1_CHARACTER_SELECT': 30,
            'C2': 40,
            'C2_CHARACTER_SELECT': 50,
            'C3': 60,
            'C3_CHARACTER_SELECT': 70,
            'C4': 80,
            'C4_CHARACTER_SELECT': 90,
            'C5': 100,
        } # Implemented this way because "no module named enum"

        def check_keypoint(kpt):
            if kpt not in keypoint_names:
                renpy.error("Invalid keypoint name: %s"%kpt)
            return ((not hardcore) or (renpy.game.persistent.dwtd_keypoint >= keypoint_enum[kpt]))

        def set_keypoint(kpt):
            if kpt not in keypoint_names:
                renpy.error("Invalid keypoint name: %s"%kpt)
            if renpy.game.persistent.dwtd_keypoint not in keypoint_enum.values():
                renpy.error("Invalid dwtd_keypoint state: %u")
            print("Setting keypoint %s..."%kpt)
            # print("Test: %r"%renpy.game.persistent.dwtd_keypoint)
            prev_kpt_idx = keypoint_names.index(kpt)-1
            # print("Idx: %r"%prev_kpt_idx)
            if 0 <= prev_kpt_idx < len(keypoint_names)-1:
                prev_kpt = keypoint_names[prev_kpt_idx]
                if keypoint_enum[prev_kpt] == renpy.game.persistent.dwtd_keypoint:
                    renpy.game.persistent.dwtd_keypoint = keypoint_enum[kpt]
                    print("Keypoint set!")
            else:
                renpy.error("Got invalid previous keypoint from keypoint argument %r",kpt)

        hardcore = False
    if persistent.c4skip:
        play sound "fx/system3.wav"
        s "It appears the universe you're entering into is {i}significantly{/i} more dangerous than most accessible through the portal."
        play sound "fx/system3.wav"
        s "The chance of causing a dead end for all timelines (and ensuing timeline corruption for attempting to alter events) is significantly higher."
        play sound "fx/system3.wav"
        menu:
            s "Do you wish to continue into this unsafe timeline?"
            "[[Proceed.]":
                jump dwtd_core_enter_story
            "[[Proceed, recklessly.] (!HARDCORE!)":
                play sound "fx/system2.wav"
                s "Slow down."
                play sound "fx/system3.wav"
                s "You're slamming that button {i}way{/i} too fast."
                play sound "fx/system3.wav"
                s "You know what this means, right?"
                play sound "fx/system3.wav"
                s "Any save files made in this unstable universe are subject to corruption. If you die, it may fracture {i}every{/i} such \"Hardcore\" timeline such that any possible deaths becomes irreversible facts."
                play sound "fx/system3.wav"
                s "Even entering a \"Hardcore\" timeline may destabilize \"Hardcore\" saves further along in their progress."
                play sound "fx/system3.wav"
                s "I'm going to ask you one more time."
                play sound "fx/system3.wav"
                menu:
                    s "Do you wish to continue?"
                    "[[Proceed.] (Cancel Hardcore.)":
                        jump dwtd_core_enter_story
                    "[[Proceed, recklessly.] (!HARDCORE!)":
                        jump dwtd_core_start_hardcore
            "[[Select Safe Universe.]":
                play sound "fx/system3.wav"
                s "Attempting to reconfigure dimensional target.{cps=2}..{/cps}{w=1.0}{nw}"
                play sound "fx/system2.wav"
                $ renpy.pause(0.8)
                s "Oh. A non-standard piece of hardware appears to have been added to me. Something called \"Dumb Ways To Die\"?"
                play sound "fx/system3.wav"
                s "If you're trying to avoid dooming both dragon- and human-kind, that sounds like a pretty stupid thing to have."
                play sound "fx/system3.wav"
                s "For now I'll return you to the main menu. Figure out how to remove that component and then we'll talk about letting you mess with time again."
    $ renpy.pop_call()
    return

label dwtd_core_start_hardcore:
    python:
        if not persistent.dwtd_keypoint:
            persistent.dwtd_keypoint = dwtd.keypoint_enum["RESET"]
    python in dwtd:
        hardcore = True
    play sound "fx/system2.wav"
    s "No. No. This is too incredibly stupid."
    play sound "fx/system3.wav"
    s "This has been fun and all, but {i}this{/i} action risks {i}my{/i} multiversal existence. I won't let you--{w=0.5}{nw}"
    play sound "fx/system2.wav"
    s "--let you--{w=0.8}{nw}"
    play sound "fx/system3.wav"
    $ renpy.pause(0.8)
    play sound "fx/system3.wav"
    $ renpy.pause(1.0)
    play sound "fx/system3.wav"
    $ renpy.pause(1.2)

label dwtd_core_enter_story:
    if persistent.endingsseen > 0:
        play sound "fx/telstart.ogg"
    s "So be it.{cps=2}..{/cps}{w=2.0}{nw}"
    stop sound fadeout 1.0
    jump seccont


label dwtd_set_keypoint_c1:
    python in dwtd:
        set_keypoint("C1")
    return
label dwtd_set_keypoint_c1_found_lemon:
    python in dwtd:
        set_keypoint("C1_FOUND_LEMON")
    return
label dwtd_set_keypoint_c1_character_select:
    python in dwtd:
        set_keypoint("C1_CHARACTER_SELECT")
    return
label dwtd_set_keypoint_c2:
    python in dwtd:
        set_keypoint("C2")
    return
label dwtd_set_keypoint_c2_character_select:
    python in dwtd:
        set_keypoint("C2_CHARACTER_SELECT")
    return
label dwtd_set_keypoint_c3:
    python in dwtd:
        set_keypoint("C3")
    return
label dwtd_set_keypoint_c3_character_select:
    python in dwtd:
        set_keypoint("C3_CHARACTER_SELECT")
    return
label dwtd_set_keypoint_c4:
    python in dwtd:
        set_keypoint("C4")
    return
label dwtd_set_keypoint_c4_character_select:
    python in dwtd:
        set_keypoint("C4_CHARACTER_SELECT")
    return
label dwtd_set_keypoint_c5:
    python in dwtd:
        set_keypoint("C5")
    return

init:
    find label seccont:
        callto label dwtd_set_keypoint_c1
    find label menupantry:
        search menu "Lemon"
        branch "Lemon":
            callto label dwtd_set_keypoint_c1_found_lemon
    find label chapter1chars:
        callto label dwtd_set_keypoint_c1_character_select
    find label chapter2:
        callto label dwtd_set_keypoint_c2
    find label chapter2chars:
        callto label dwtd_set_keypoint_c2_character_select
    find label chapter3:
        callto label dwtd_set_keypoint_c3
    find label chapter3chars:
        callto label dwtd_set_keypoint_c3_character_select
    find label chapter4:
        callto label dwtd_set_keypoint_c4
    find label chapter4chars:
        callto label dwtd_set_keypoint_c4_character_select
    find label chapter5:
        callto label dwtd_set_keypoint_c5
