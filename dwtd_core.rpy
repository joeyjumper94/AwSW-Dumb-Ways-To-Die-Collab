label dwtd_youdied(deathname,cause_of_death="Who knows how you died, but for me it was entertaining."):
    $ dwtd.will_die()
    if not persistent.dwtd_death_set:
        $ persistent.dwtd_death_set = python_set()
    $ persistent.dwtd_death_set.add(deathname)
    play sound "fx/system3.wav"
    s "[cause_of_death]"
    play sound "fx/system3.wav"
    call screen dwtd_youdied_options_screen

    $ MainMenu(confirm=False)()

init python in dwtd:
    def deathsound(sound_number=0, sound_playtime=4.0):
        death_sounds = ["fx/impact2.ogg", "fx/chapter2.ogg", "fx/chapter2.ogg", "fx/chapter3.ogg", "fx/chapter4.ogg", "fx/chapter5.ogg"]
        if not sound_number == 0:
            renpy.music.play(death_sounds[sound_number - 1], loop=False)
            renpy.pause(0.0) #Doesn't play if I don't have this
            renpy.music.stop(fadeout=sound_playtime)

image dwtd_youdied_text = "image/ui/youdied.png"

screen dwtd_youdied_options_screen tag smallscreen:
    modal True
    grid 3 1:
        xanchor 0.5
        xpos 0.5
        ypos 0.9
        spacing 30
        imagebutton idle "image/ui/comicsans_load.png" action ShowMenu("load") at center
        imagebutton idle "image/ui/comicsans_mainmenu.png" action MainMenu(confirm=False) at center
        imagebutton idle "image/ui/comicsans_quit.png" action Quit() at center

screen dwtd_qte(qte_action,qte_time=1.0):
    timer qte_time action Return(False)
    modal True
    window id "qte":
        textbutton qte_action action Return(True) at top