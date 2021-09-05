init:
    find label sebastianskip

    search menu "It's pretty cold."
    branch "It's pretty cold.":
        search say "I suppose it takes some getting used to." as dwtd_xseb_freeze_linknode # ideally I wish I could insert text directly after the menu, without replacing the menu option
        search say "I could warm you up." 
        callto label dwtd_xseb_freeze_complaint from dwtd_xseb_freeze_linknode return here

        search menu "No, thank you."
        change "No, thank you." to inaccessible
        add option "No, thank you." to dwtd_xseb_freeze_rejection

label dwtd_xseb_test:
    m "Hello world!"

    Sb "Hi."
    return

label dwtd_xseb_freeze_complaint:
    c "It's freezing, actually. In town it wasn't this bad."
    Sb "Well, that's how it is up here."
    c "I guess so. I just hope I have all my extremities by the morning."
    # Sb "I could warm you up."
    # c "Not sure it would be safe to keep a fire burning overnight."
    # Sb "You're right, but I wasn't talking about that."
    # c "I see..."
    # Sb "Either way, the only blanket I can offer is myself."
    # menu:
    #     "I'll take it.": 
    #     "No, thank you.": 
    return


label dwtd_xseb_freeze_rejection:
    $ dwtd.will_die()
    $ renpy.pop_call()

    # expressions don't show because scene is black already
    Sb disapproval "Really? Aren't you worried about your health?"
    c "Eh, I'm good."
    Sb "Well, okay, have it your way. No scales off my snout if you freeze to death."
    c "Hey, nothing against you in particular, it's just..."
    Sb normal "..."
    c "...you're a guy."
    Sb disapproval "Is that it? Huh, must be a human thing."
    c "I wouldn't be comfortable with it, that's all."
    Sb normal "Well, good night then."
    c "Good night, Sebastian."

    scene black ((0,0,0,0), 2.0, dist=50)
    $ renpy.pause(2.0)
    $ dwtd.deathsound(5) 
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause (4.0)
    call dwtd_youdied("Frozen", "You had a very uncomfortable night, and then froze to death.")
