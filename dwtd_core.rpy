label dwtd_youdied(cause_of_death="Who knows how you died, but for me it was entertaining."):
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
        vbox:
            textbutton qte_action action Return(True) at Position(xpos=0.5)



# init python in dwtd:
#     from Enum import Enum
#     class Keypoint(IntEnum):
#         RESET = -1
#         C1 = 0
#         # C1_MET_SEBASTIAN = 5
#         # C1_MET_REZA = 10
#         # C1_MET_MAVERICK = 15
#         # C1_MET_ANNA = 20
#         # C1_MET_ADINE = 25
#         # C1_MET_VARA = 30
#         C1_FOUND_LEMON = 35
#         # C1_MET_BRYCE = 40
#         # C1_INVESTIGATION_BRYCE_ASKED_FOR_HELP = 45
#         # C1_INVESTIGATION_START = 50
#         # C1_INVESTIGATION_END = 55
#         # C1_CHAR_SELECT = 60
#         C2 = 65
#         # C2_MET_BRYCE = 70
#         # C2_MET_SEBASTIAN = 75
#         # C2_BASEMENT_SURVIVED = 80
#         # C2_INVESTIGATION_START = 85
#         # C2_MET_MAVERICK = 90
#         # C2_CHARACTER_SELECT = 95
#         C3 = 100
#         # C3_MET_BRYCE = 105
#         # C3_MET_EMERA = 110
#         # C3_MET_SEBASTIAN = 115
#         C4 = 120
#         C5 = 125
# No module named enum???

label dwtd_init_keypoints:
    python:
        persistent.dwtd_keypoint = Keypoint.RESET
    python in dwtd:
        keypoints_list = [
            -1, # RESET
            0, # C1
            35, # C1_FOUND_LEMON
            65, # C2
            100, # C3
            120, # C4
            125, # C5
        ]

        def check_keypoint(kpt):
            return persistent.dwtd_keypoint >= kpt

        def set_keypoint(kpt):
            prev_keypoint_idx = keypoints_list.index(kpt)-1
            if prev_keypoint_idx >= 0:
                prev_keypoint = keypoints_list[prev_keypoint_idx]
                if persistent.dwtd_keypoint == prev_keypoint:
                    persistent.dwtd_keypoint = kpt