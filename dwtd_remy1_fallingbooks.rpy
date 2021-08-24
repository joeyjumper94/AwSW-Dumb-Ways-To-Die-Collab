init:
    find label remy1:
        search say "In any case, I'll be working on something else in the meantime, so let me know once you're done." as dwtd_r1_bookshelfcrush_linknode
    find label remycont
    callto label dwtd_r1_bookshelfcrush_start from dwtd_r1_bookshelfcrush_linknode return here

# Don't judge this code, okay?

label dwtd_r1_bookshelfcrush_start:
    show remy normal flip
    $ renpy.pause (0.3)
    hide remy with easeoutright

    jump dwtd_r1_bookshelfcrush_init

label dwtd_r1_bookshelfcrush_init:
    $ dwtd_booksort_status = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth"
    }

    $ dwtd_booksort_correct = {
        1: "inception",
        2: "first",
        3: "tribe",
        4: "second",
        5: "invention",
        6: "spark",
        7: "third",
        8: "enlightenment"
    }

    $ TheSecondWar = True
    $ TheTribe = True
    $ TheInvention = True
    $ TheEnlightenment = True
    $ TheThirdWar = True
    $ TheInception = True
    $ TheSpark = True
    $ TheFirstWar = True
    $ remyanswers = 0

    # Variable to determine whether you avoided the shelf
    $ dwtd.avoided_r1_bookshelf = False

    $ dwtd_booksort_number = 1

    $ dwtd_booksort_incident = renpy.random.randint(1, 8)

    # Can't call this at first due to how I coded it

    nvl clear
    window show

    n "Hints:"
    n "{i}The Third War{/i} is directly preceded by {i}The Spark{/i}."
    n "{i}The First War{/i} is directly preceded by {i}The Inception{/i}."
    n "{i}The Invention{/i} is not the third, seventh, or last book."
    n "{i}The Second War{/i} is the 4th book."
    n "There is only one book before {i}The First War{/i}."
    n "{i}The Enlightenment{/i} comes at some point after {i}The Third War{/i}."
    window hide

    jump dwtd_r1_bookshelfcrush

label dwtd_r1_bookshelfcrush:
    if dwtd_booksort_number == 9:
        jump dwtd_booksort_end
    
    $ dwtd_booksort_text = dwtd_booksort_status[dwtd_booksort_number]
    $ dwtd_booksort_answer = dwtd_booksort_correct[dwtd_booksort_number]
    $ dwtd_booksort_number += 1

    if dwtd_booksort_number == dwtd_booksort_incident:
        $ renpy.music.set_pause(True, "music")
        play sound "fx/fall3.ogg"
        
        if dwtd.check_keypoint():
            call screen dwtd_qte("Dodge.")
        else:
            play sound "fx/system3.wav"
            s "This timeline is hardcore, pal. You can't reload to fix this."
            $ _return = False
        if not _return:
            stop music
            $ renpy.music.set_pause(False, "music")
            $ dwtd.will_die()
            $ renpy.pop_call()
            scene black with Shake ((0, 0, 0, 0), 1.5, dist=50)
            $ renpy.pause (2.0)
            call dwtd_deathsound(5)
            show dwtd_youdied_text at top with easeintop
            $ renpy.pause(4.0)
            call dwtd_youdied("You got crushed by the bookshelf while sorting the books. Try to be quicker on your feet next time.")
        $ dwtd.avoided_r1_bookshelf = True
        m "I narrowly avoided the bookshelf as it came crashing down in front of me."
        show remy look with easeinright
        Ry "Are you alright? I heard a big crash."
        c "That bookshelf almost came crashing down and killed me!"
        Ry "That's weird, they've never done that before."
        Ry normal "For the meantime, why don't you just sort those books over here while we replace that shelf."
        c "Alright."
        Ry "See you in a bit!"
        show remy normal flip
        $ renpy.pause (0.3)
        hide remy with easeoutright
        $ renpy.music.set_pause(False, "music")

    label dwtd_hint_return:
        pass

    if dwtd_booksort_number <= 4:
        label dwtd_booksort_menu:
            menu:
                "The [dwtd_booksort_text] book is:"

                "The Second War" if TheSecondWar:
                    $ TheSecondWar = False
                    if dwtd_booksort_answer == "second":
                        $ remyanswers += 1
                
                "The Tribe" if TheTribe:
                    $ TheTribe = False
                    if dwtd_booksort_answer == "tribe":
                        $ remyanswers += 1
                
                "The Invention" if TheInvention:
                    $ TheInvention = False
                    if dwtd_booksort_answer == "invention":
                        $ remyanswers += 1
                
                "The Enlightenment" if TheEnlightenment:
                    $ TheEnlightenment = False
                    if dwtd_booksort_answer == "enlightenment":
                        $ remyanswers += 1
                
                "[[Show more books.]":
                    jump dwtd_booksort_menux
                
                "[[Show hints.]":
                    jump dwtd_remy_hints
        
            jump dwtd_r1_bookshelfcrush
            
        label dwtd_booksort_menux:
            menu:
                "The [dwtd_booksort_text] book is:"

                "The Third War" if TheThirdWar:
                    $ TheThirdWar = False
                    if dwtd_booksort_answer == "third":
                        $ remyanswers += 1
                
                "The Inception" if TheInception:
                    $ TheInception = False
                    if dwtd_booksort_answer == "inception":
                        $ remyanswers += 1
                
                "The Spark" if TheSpark:
                    $ TheSpark = False
                    if dwtd_booksort_answer == "spark":
                        $ remyanswers += 1
                
                "The First War" if TheFirstWar:
                    $ TheFirstWar = False
                    if dwtd_booksort_answer == "first":
                        $ remyanswers += 1
                
                "[[Show more books.]":
                    jump dwtd_booksort_menu
                
                "[[Show hints.]":
                    jump dwtd_remy_hints 
            
            jump dwtd_r1_bookshelfcrush
    else:
        menu:
            "The [dwtd_booksort_text] book is:"

            "The Second War" if TheSecondWar:
                $ TheSecondWar = False
                if dwtd_booksort_answer == "second":
                    $ remyanswers += 1
                
            "The Tribe" if TheTribe:
                $ TheTribe = False
                if dwtd_booksort_answer == "tribe":
                    $ remyanswers += 1
            
            "The Invention" if TheInvention:
                $ TheInvention = False
                if dwtd_booksort_answer == "invention":
                    $ remyanswers += 1
            
            "The Enlightenment" if TheEnlightenment:
                $ TheEnlightenment = False
                if dwtd_booksort_answer == "enlightenment":
                    $ remyanswers += 1
            
            "The Third War" if TheThirdWar:
                $ TheThirdWar = False
                if dwtd_booksort_answer == "third":
                    $ remyanswers += 1
            
            "The Inception" if TheInception:
                $ TheInception = False
                if dwtd_booksort_answer == "inception":
                    $ remyanswers += 1
            
            "The Spark" if TheSpark:
                $ TheSpark = False
                if dwtd_booksort_answer == "spark":
                    $ remyanswers += 1
            
            "The First War" if TheFirstWar:
                $ TheFirstWar = False
                if dwtd_booksort_answer == "first":
                    $ remyanswers += 1
            
            "[[Show hints.]":
                jump dwtd_remy_hints 
    
        jump dwtd_r1_bookshelfcrush

label dwtd_remy_hints:
    nvl clear
    window show

    n "Hints:"
    n "{i}The Third War{/i} is directly preceded by {i}The Spark{/i}."
    n "{i}The First War{/i} is directly preceded by {i}The Inception{/i}."
    n "{i}The Invention{/i} is not the third, seventh, or last book."
    n "{i}The Second War{/i} is the 4th book."
    n "There is only one book before {i}The First War{/i}."
    n "{i}The Enlightenment{/i} comes at some point after {i}The Third War{/i}."
    window hide
    jump dwtd_hint_return

label dwtd_booksort_end:
c "I think that's it."

show remy normal with easeinright

Ry "Oh, you're done? Let's take a look, then."

if remyanswers == 8:

    $ mp.remybooks = 8
    $ mp.save()

    $ remymood += 3
    show remy smile with dissolve
    Ry "Seems you got it all right. Well done, [player_name]."

    if persistent.c1booksort == False:

        $ persistent.c1booksort = True

        $ achievement.grant("Librarian")

        $ persistent.achievements += 1

        call syscheck from _dwtd_call_syscheck_85

        play sound "fx/system.wav"

        if system == "normal":

            s "You brought Remy's books into the correct order!"

        elif system == "advanced":

            s "You brought Remy's books into the correct order. Amazing."
        else:


            s "You brought Remy's books into the correct order. What an achievement."

    menu:
        "Phew, that was hard work.":
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "It gets easier with practice."
            jump remycont
        "That wasn't too hard...":

            $ renpy.pause (0.5)
            show remy normal with dissolve
            jump remycont
        "I didn't know I could have this much fun in a library.":

            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "I can't tell if you are serious, but I appreciate your help regardless."
            jump remycont

elif remyanswers >= 6:

    $ mp.remybooks = 6
    $ mp.save()

    $ remymood += 1
    Ry "No, this doesn't seem to be completely right. It looks like [remyanswers] books are in the right place, though."
    menu:
        "Let me try again.":
            $ remymood -= 1
            Ry "Alright, I'll come back in a bit."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            jump dwtd_r1_bookshelfcrush_init
        "This is the best I can do.":

            Ry "Alright, let me fix that up for you."
            play sound "fx/booksort.wav"
            $ renpy.pause (3.0)
            show remy smile with dissolve
            Ry "There, that should be it."
            show remy normal with dissolve
            jump remycont
        "[[Give up and leave.]":

            c "I give up. This is stupid and you're stupid for making me do your work for you."
            show remy look with dissolve
            Ry "Well, it's not like I'm forcing you to stay here. You can see yourself out, if you can still find the exit."
            stop music fadeout 1.0
            scene black with fade
            nvl clear
            window show
            n "Apparently Remy hadn't approved of my unwillingness to be his slave."
            n "Did he really think I wanted to spend my free time doing his work for him?"
            n "Thanks, but no thanks, buddy."
            window hide
            nvl clear

            $ remystatus = "bad"

            $ remyscenesfinished = 1

            if chapter4unplayed == False:

                jump chapter4chars

            elif chapter3unplayed == False:

                jump chapter3chars

            elif chapter2unplayed == False:

                jump chapter2chars
            else:


                jump chapter1chars

elif remyanswers == 1:

    $ mp.remybooks = 1
    $ mp.save()

    show remy look with dissolve
    Ry "Sorry to disappoint you, but it seems only a single book is in the right place."
    menu:
        "Let me try again.":
            $ remymood -= 1
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "Alright, I'll come back in a bit."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            jump dwtd_r1_bookshelfcrush_init
        "This is the best I can do.":

            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "I see. Let me fix that up for you, then."
            play sound "fx/booksort.wav"
            $ renpy.pause (3.0)
            show remy smile with dissolve
            Ry "There, that should be it."
            show remy normal with dissolve
            jump remycont
        "[[Give up and leave.]":

            c "I give up. This is stupid and you're stupid for making me do your work for you."
            Ry "Well, it's not like I'm forcing you to stay here. You can see yourself out, if you can still find the exit."
            stop music fadeout 1.0
            scene black with fade
            nvl clear
            window show
            n "Apparently Remy hadn't approved of my unwillingness to be his slave."
            n "Did he really think I wanted to spend my free time doing his work for him?"
            n "Thanks, but no thanks, buddy."
            window hide
            nvl clear

            $ remystatus = "bad"

            $ remyscenesfinished = 1

            if chapter4unplayed == False:

                jump chapter4chars

            elif chapter3unplayed == False:

                jump chapter3chars

            elif chapter2unplayed == False:

                jump chapter2chars
            else:


                jump chapter1chars

elif remyanswers == 0:

    $ mp.remybooks = 0
    $ mp.save()

    show remy look with dissolve
    Ry "Sorry to disappoint you, but it seems not a single book is in the right place."
    menu:
        "Let me try again.":
            $ remymood -= 1
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "Alright, I'll come back in a bit."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            jump dwtd_r1_bookshelfcrush_init
        "This is the best I can do.":

            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "I see. Let me fix that up for you, then."
            play sound "fx/booksort.wav"
            $ renpy.pause (3.0)
            show remy smile with dissolve
            Ry "There, that should be it."
            show remy normal with dissolve
            jump remycont
        "[[Give up and leave.]":

            c "I give up. This is stupid and you're stupid for making me do your work for you."
            Ry "Well, it's not like I'm forcing you to stay here. You can see yourself out, if you can still find the exit."
            stop music fadeout 1.0
            scene black with fade
            nvl clear
            window show
            n "Apparently Remy hadn't approved of my unwillingness to be his slave."
            n "Did he really think I wanted to spend my free time doing his work for him?"
            n "Thanks, but no thanks, buddy."
            window hide
            nvl clear

            $ remystatus = "bad"

            $ remyscenesfinished = 1

            if chapter4unplayed == False:

                jump chapter4chars

            elif chapter3unplayed == False:

                jump chapter3chars

            elif chapter2unplayed == False:

                jump chapter2chars
            else:


                jump chapter1chars
else:

    show remy look with dissolve

    $ mp.remybooks = remyanswers
    $ mp.save()

    Ry "Sorry to disappoint you, but it seems only [remyanswers] books are in the right place."
    menu:
        "Let me try again.":
            $ remymood -= 1
            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "Alright, I'll come back in a bit."
            show remy normal flip
            $ renpy.pause (0.3)
            hide remy with easeoutright
            jump dwtd_r1_bookshelfcrush_init
        "This is the best I can do.":

            $ renpy.pause (0.5)
            show remy normal with dissolve
            Ry "I see. Let me fix that up for you, then."
            play sound "fx/booksort.wav"
            $ renpy.pause (3.0)
            show remy smile with dissolve
            Ry "There, that should be it."
            show remy normal with dissolve
            jump remycont
        "[[Give up and leave.]":

            c "I give up. This is stupid and you're stupid for making me do your work for you."
            Ry "Well, it's not like I'm forcing you to stay here. You can see yourself out, if you can still find the exit."
            stop music fadeout 1.0
            scene black with fade
            nvl clear
            window show
            n "Apparently Remy hadn't approved of my unwillingness to be his slave."
            n "Did he really think I wanted to spend my free time doing his work for him?"
            n "Thanks, but no thanks, buddy."
            window hide
            nvl clear

            $ remystatus = "bad"

            $ remyscenesfinished = 1

            if chapter4unplayed == False:

                jump chapter4chars

            elif chapter3unplayed == False:

                jump chapter3chars

            elif chapter2unplayed == False:

                jump chapter2chars
            else:


                jump chapter1chars