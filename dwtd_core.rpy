label dwtd_youdied(cause_of_death="Who knows how you died, but for me it was entertaining."):
    $ dwtd.will_die()
    play sound "fx/system3.wav"
    s "[cause_of_death]"
    play sound "fx/system3.wav"
    call screen dwtd_youdied_options_screen

    $ MainMenu(confirm=False)()

label dwtd_deathsound(sound_number=0, sound_playtime=4.0): #It is recommended to add a renpy.pause equal to the sound_playtime *after* you show the dwtd_youdied_text
    $ death_sounds = ["fx/impact2.ogg", "fx/chapter2.ogg", "fx/chapter2.ogg", "fx/chapter3.ogg", "fx/chapter4.ogg", "fx/chapter5.ogg"]
    if not sound_number == 0:
        play music death_sounds[sound_number - 1]
        $ renpy.pause (0.1) #Doesn't play if I don't have this
        stop music fadeout sound_playtime
    return

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
    window id "dwtd_youdied" at popup:
        style "smallwindow"
        hbox at center:
            xmaximum 900
            xoffset 50
            xfill False
            xalign 0.5
            spacing 30
            textbutton "Load" action ShowMenu("load")
            textbutton "Main Menu" action MainMenu(confirm=False)
            textbutton "Quit" action Quit()

screen dwtd_qte(qte_action,qte_time=1.0):
    timer qte_time action Return(False)
    modal True
    window id "qte":
        textbutton qte_action action Return(True) at top