init python:
    def dwtd_core_hardcore_link(ml):
        ml.find_label('begingame') \
            .hook_call_to('dwtd_core_init_hardcore')
        
        ml.find_label('skipintro') \
            .search_if('persistent.endingsseen == 0') \
            .branch_else() \
            .search_python('c = DynamicCharacter (\"player_name\", color=playercolor, callback=rolly)') \
            .hook_to('dwtd_core_init_hardcore')

        # Initialize keypoints
        ml.find_label('seccont') \
            .hook_call_to('dwtd_set_keypoint_c1')
        ml.find_label('chapter2') \
            .hook_call_to('dwtd_set_keypoint_c2')
        ml.find_label('chapter3') \
            .hook_call_to('dwtd_set_keypoint_c3')
        ml.find_label('chapter4') \
            .hook_call_to('dwtd_set_keypoint_c4')
        ml.find_label('chapter5') \
            .hook_call_to('dwtd_set_keypoint_c5')
    dwtd_core_hardcore_link(magmalink())

label dwtd_core_init_hardcore:
    init python in dwtd:
        def get_chapter():
            if renpy.python.store_dicts['store'].get('chapter5unplayed',True) == False:
                return 5
            elif renpy.python.store_dicts['store'].get('chapter4unplayed',True) == False:
                return 4
            elif renpy.python.store_dicts['store'].get('chapter3unplayed',True) == False:
                return 3
            elif renpy.python.store_dicts['store'].get('chapter2unplayed',True) == False:
                return 2
            else:
                return 1

        def check_keypoint(dev = False):
            if dev:
                renpy.say(None, "Welcome to the dev menu. How would you like this death to proceed?", interact=False)
                renpy.ast.say_menu_with(None, renpy.game.interface.set_transition)
                opts = [
                    ("Correct Hardcore save file", True),
                    ("Broken Hardcore save file", False),
                    ("Normal save file", True)
                ]
                return renpy.display_menu(opts)

            if hardcore:
                kpt = get_chapter()
                if not (1 <= kpt <= 5):
                    renpy.error("Invalid chapter index retrieved by dwtd.get_chapter()")
                if not (0 <= renpy.game.persistent.dwtd_keypoint <= 5):
                    renpy.error("Invalid keypoint index in persistent.dwtd_keypoint")
                return renpy.game.persistent.dwtd_keypoint >= kpt
            else:
                return True

        def set_keypoint(ch):
            print(ch)
            if hardcore:
                if 1 <= ch <= 5:
                    if ch-1 == renpy.game.persistent.dwtd_keypoint:
                        renpy.game.persistent.dwtd_keypoint = ch
                else:
                    renpy.error("Got invalid previous keypoint from keypoint argument %r",kpt)
        
        def will_die():
            if hardcore:
                renpy.game.persistent.dwtd_keypoint = 0

        hardcore = False
    if persistent.endingsseen == 0:
        return
    if persistent.c4skip:
        $ dwtd.hardcore = False
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
            persistent.dwtd_keypoint = 0
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
        set_keypoint(1)
    return
label dwtd_set_keypoint_c2:
    python in dwtd:
        set_keypoint(2)
    return
label dwtd_set_keypoint_c3:
    python in dwtd:
        set_keypoint(3)
    return
label dwtd_set_keypoint_c4:
    python in dwtd:
        set_keypoint(4)
    return
label dwtd_set_keypoint_c5:
    python in dwtd:
        set_keypoint(5)
    return