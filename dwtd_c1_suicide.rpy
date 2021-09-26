init python:
    def dwtd_c1_suicide_link(ml):
        for l in ['quest2','quest3','quest5']:
            ml.find_label(l).hook_to('dwtd_c1_suicide',condition='suicide >= 2',return_link=False)
    dwtd_c1_suicide_link(magmalink())

label dwtd_c1_suicide:
    python:
        dwtd.will_die()
        wrong1 = True
        wrong2 = True
        wrong3 = True
        wrong4 = True
    c "Excuse me? No we haven't."
    c "Do I really have to spell it out for you?"
    Br stern b "You can't be serious."
    c "Oh, I'm serious. I've seen this kind of thing before on cop dramas. This is totally a suicide, and I can prove it."
    Br stern b "This I have got to see."
    stop music fadeout 1.0
    $ renpy.pause (0.8)
    Br brow b "Wait, where are you going?"
    
    scene town6 with fade

    play music "mx/basicguitar.ogg"

    show bryce normal b with dissolve
    show bryce at right with ease
    m "I crossed the street, over to where Adine, the waitress from the café, sat huddled in the shade. She shrank back a little as I approached."
    hide bryce with easeoutright
    show adine disappoint b flip at left with easeinleft
    Ad "I- You're coming over to talk to me?"
    c "I just need some help explaining something to Bryce over there. The café you work at is near here, right?"
    Ad think b flip "Yes..."
    c "Could you go get me a knife? Uh, one of the larger ones? Curved, with a pointy tip?"
    Ad sad b flip "Why do you need something like that?"
    # c "I'm going to need a knife to cut my way through the crowd of people." # Copilot, what?
    c "It's just a prop to explain something. Don't worry about it."
    Ad think b "If you say so."
    hide adine with easeoutleft
    play sound "fx/takeoff.ogg"
    show bryce brow b with easeinright
    Br stern b "This had better be good."
    c "Oh, it will be."
    Br brow b "How about you start explaining the reasoning here. Why did he commit suicide?"

label dwtd_c1_suicide_menu1:
    menu:
        c "Because..."
        "Gum disease." if wrong1:
            c "It was a suicide over his gum disease medical bills. You saw all the blood on his muzzle earlier, around his mouth."
            Br brow b "What kind of world do you live in where that makes sense?"
            c "Well, an unregulated medical insurance industry--"
            Br stern b "That was rhetorical. Our world isn't like that."
            $ wrong1 = False
            jump dwtd_c1_suicide_menu1
        "Stress." if wrong2:
            c "He was probably under a lot of stress from his job. Flying everywhere at all hours of the day?"
            Br brow b "That's what fliers do."
            Br stern b "Very few of them commit suicide over it. Fewer still do so in rural environments like this."
            c "So you're saying it is possible."
            Br "I'm saying your theory needs work to be remotely plausible."
            $ wrong2 = False
            jump dwtd_c1_suicide_menu1
        "Religion":
            pass
    c "Think about the situation this poor guy's in. Humans have just shown up in his world. Your people worship us, right?"
    Br brow b "More or less."
    c "So he's looking at our arrival like some kind of messianic arrival or apocalyptic omen. Now the cuts on his wings -- they're vertical, through the membrane, along the spines. That looks painful. Why?"
    Br stern b "He was defending himself from someone slashing at him."
    # c "That's right. He's been attacked by someone." # That's true Copilot, but not what the player character is saying here.
    c "No, no, no. All the cuts are {i}with the spines.{/i}{w=0.5} I think it was something ritualistic."
    Br brow b "Ritualistic suicide?"
    Br stern b "He did it in the middle of the street, some time well after midnight. What circumstances would lead to his ritual occurring here? Assuming that's even what this is."

label dwtd_c1_suicide_menu2:
    menu:
        c "He killed himself here because..."
        "Nothing." if wrong3:
            c "He just decided this was the best time and place to end his life."
            Br "That's ridiculous."
            Br "Nobody throws their life away without some sort of reason."
            $ wrong3 = False
            jump dwtd_c1_suicide_menu2
        "Gum disease pain." if wrong4:
            c "That blood around his muzzle? He had gum disease. The pain was just abruptly too much to bear."
            if wrong1 == False:
                Br "We definitely ruled that one out already."
            Br brow b "We have forensics checking that blood, but I highly doubt it's going to come back as his."
            Br stern b "For now, assume he doesn't have gum disease."
            $ wrong4 = False
            jump dwtd_c1_suicide_menu2
        "Reza.":
            pass
    c "He saw Reza, and attacked him. He got a taste of human blood and thought that would lead to his ascension."
    c "Then Reza took the knife and ran, thinking he could use it to defend himself."
    $ renpy.pause (0.8)
    Br brow b "..."
    Br "My working theory is that Reza was the attacker, and the blood on his muzzle is explained by fighting back. But I can't completely rule out what you're saying."
    Br stern b "{i}If{/i} the victim here could make the motions you're implying he made with the knife."
    c "If he attacked Reza, then Reza is the victim."
    Br "Let's not confuse terminology now."
    show bryce at right with ease
    play sound "fx/landing.ogg"
    $ renpy.pause (2.0)
    show adine think b flip at left with easeinleft
    m "Adine landed, knife gripped by one of her feet.{w=0.6} Before she passed it to what could be described as a hand for her, I spoke up."
    c "Actually, could you show us slashing at your wing with that knife?"