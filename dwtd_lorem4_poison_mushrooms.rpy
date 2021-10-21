init python:
    def dwtd_lorem4_poison_mushrooms(ml):
        ( ml.find_label('_call_skiptut_5')
            .search_say("Alright. What would you like on your half?")
            .hook_to('dwtd_lorem4_poison_mushrooms_checkfailed',condition='not dwtd.check_keypoint()',return_link=False)
            .search_menu("Pepperoni.")
            .add_choice("Mushrooms.", jump='dwtd_lorem4_poison_mushrooms_selected')
            .link_behind_from('dwtd_lorem4_poison_mushrooms_selected_end')
            .search_say("Maybe you just haven't had a good pizza to compare it to.")
            .hook_to('dwtd_lorem4_poison_mushrooms_take_effect',condition='renpy.python.store_dicts["store"].get("dwtd_lorem4_poison_mushrooms_selected",False) == True')
        )
    dwtd_lorem4_poison_mushrooms(magmalink())

label dwtd_lorem4_poison_mushrooms_checkfailed:
    play sound "fx/system3.wav"
    s "This is a broken hardcore timeline. Reloading your save can't fix your choices."
    c "Mushrooms."

label dwtd_lorem4_poison_mushrooms_selected:
    $ renpy.pause(0.5)
    $ dwtd_lorem4_poison_mushrooms_selected = True
    Lo "Got it."
    show lorem happy with dissolve
    jump dwtd_lorem4_poison_mushrooms_selected_end

label dwtd_lorem4_poison_mushrooms_take_effect:
    c "Hey, it's still better {nw}"
    play sound "fx/rumble.ogg"
    c "Hey, it's still better {fast}than{cps=*0.3} nothing...{/cps}"
    Lo think "I suppose."
    $ renpy.pause (1.3)
    Lo normal "Hey, are you okay? You look kinda..."
    c "N-No I--"
    m "I stood quickly, which was exactly the wrong thing to do. My gut did a somersault, and after a moment I lost my balance."
    play sound "fx/impact3.ogg"
    scene black with vpunch
    $ renpy.pause(0.3)
    Lo sad "[player_name]!"
    $ renpy.pause(0.8)
    Lo sad "No no no!"
    $ renpy.pause(1.5)
    Lo relieved "Where did Pantolli's get those mushrooms?"
    $ renpy.pause(2.0)
    $ dwtd.deathsound(2)
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause(4.0)
    call dwtd_youdied("Poison Mushrooms", "If you don't trust a company's quality, don't buy risky ingredients from them.")
