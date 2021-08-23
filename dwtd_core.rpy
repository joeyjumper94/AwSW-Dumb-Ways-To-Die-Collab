label dwtd_youdied(cause_of_death="Who knows how you died, but for me it was entertaining."):
    if dwtd.hardcore == True:
        $ persistent.dwtd_keypoint = dwtd.keypoint_enum["RESET"]
    play sound "fx/system3.wav"
    s "[cause_of_death]"
    play sound "fx/system3.wav"
    call screen dwtd_youdied_options_screen

    $ MainMenu(confirm=False)()

image dwtd_youdied_text = "image/ui/youdied.png"

screen dwtd_youdied_options_screen tag smallscreen:
    modal True
    window id "dwtd_youdied" at popup:
        style "smallwindow"
        hbox:
            spacing 30
            textbutton "Load" action ShowMenu("load")
            textbutton "Main Menu" action MainMenu(confirm=False)
            textbutton "Quit" action Quit()

screen dwtd_qte(qte_action,qte_time=1.0):
    timer qte_time action Return(False)
    modal True
    window id "qte":
        textbutton qte_action action Return(True) at top