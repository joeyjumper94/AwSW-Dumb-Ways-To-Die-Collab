init python:
    def dwtd_c4_reza_hideout_link(ml):
        ml.find_label("didit")\
            .search_say("We slowly made our way to the front door. I took a deep breath and tried to prepare myself for the possibility of facing Reza. The tense scenarios and things I could say to him rushed through my head as I pressed down on the door handle.")\
            .hook_to("dwtd_c4_reza_hideout")\
            .search_say("When I looked down to the source of the noise, I saw a taut wire through the gap in the door, hovering over the floor of the entryway.")\
            .link_from("dwtd_c4_reza_hideout_end")
    dwtd_c4_reza_hideout_link(magmalink())

label dwtd_c4_reza_hideout:
    if dwtd.check_keypoint():
        call screen dwtd_qte("open the door cautiously.")
    else:
        play sound "fx/system3.wav"
        s "This timeline is hardcore, pal. You can't reload to fix this."
        $ _return = False
    if not _return:
        $ dwtd.will_die()
        stop music
        play sound "fx/explosion.ogg"
        scene explosion with Shake((0, 0, 0, 0), 3.0, dist=30)
        $ renpy.pause (3.0)
        $ dwtd.deathsound(5)
        show dwtd_youdied_text at top with easeintop
        $ renpy.pause (4.0)
        call dwtd_youdied("Shower Slip", "You cracked your skull open in the shower and died. {w}Think about how Adine feels...")
    m "The door inched open with a creak, but I noticed a slight resistance and a strange sound that suddenly made me hesitate."
    play sound "fx/door/door_open.wav"
    queue sound "fx/wire.ogg"
    show tripwire at Pan((300,0),(500, 608),8.0) with fade
    $ renpy.pause 8.5
    jump dwtd_c4_reza_hideout_end