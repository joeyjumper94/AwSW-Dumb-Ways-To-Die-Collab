init:
    find label seccont
    search say "Getting ready, I noticed something lying on the table. It was the note Remy had left for me in case I needed anything. Along with his own home phone and work number, there were also some numbers for delivery of food and other necessities, as well as emergency and even janitorial services. He had certainly thought of everything, even though I now had to wonder what a dragon plumber might look like." as plumber
    search python
    callto label dwtd_dontslip from plumber return here

label dwtd_dontslip:
    play sound "fx/door/doorbell.wav"
    nvl clear
    n "My musings were interrupted when the doorbel rang. When I stood to walk to the door--{w=1.0}"
    window hide
    nvl clear

    call screen dwtd_qte("Don't trip!")
    if not _return:
        $ renpy.pop_call()
        play sound "fx/impact3.ogg"
        scene black with None
        m "I tripped on my way to the door, falling hard and face-first onto the floor."
        m "That was the last thing I felt."
        $ renpy.pause (1.0)
        scene o at Pan((0,250), (0,250), 0.1) with dissolveslow
        show sebastian shy b flip at left with easeinleft
        Sb "Ambassador, are you alright?"
        show sebastian drop b flip with dissolve
        $ renpy.pause (0.8)
        Sb "I am so fired for this..."
        scene black with dissolvemed
        call dwtd_youdied("You tripped on the way to the door and cracked your skull open on the apartment floor.")

    m "When I opened the door, I was met by another dragon."
    play sound "fx/door/handle.wav"

    return