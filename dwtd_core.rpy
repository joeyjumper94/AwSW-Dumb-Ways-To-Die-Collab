label dwtd_youdied(cause_of_death="Who knows how you died, but for me it was entertaining."):
    if dwtd.hardcore == True:
        $ persistent.dwtd_keypoint = dwtd.keypoint_enum["RESET"]

    play sound "fx/system3.wav"
    s "You died."
    play sound "fx/system3.wav"
    s "[cause_of_death]"
    play sound "fx/system3.wav"
    s "There's nothing else for you here."
    play sound "fx/system3.wav"
    s "Prepare to return to the main menu."
    $ renpy.pause (0.8)
    play sound "fx/system3.wav"
    s "Loser."

    $ renpy.pop_call()
    return

screen dwtd_qte(qte_action,qte_time=1.0):
    timer qte_time action Return(False)
    modal True
    window id "qte":
        textbutton qte_action action Return(True) at top