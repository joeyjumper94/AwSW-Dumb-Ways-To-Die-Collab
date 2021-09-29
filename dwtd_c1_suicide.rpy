init python:
    def dwtd_c1_suicide_link(ml):
        for l in ['quest2','quest3','quest5']:
            ml.find_label(l).hook_to('dwtd_c1_suicide',condition='suicide >= 2',return_link=False)
        
        ml.find_label('quest1') \
            .hook_to('dwtd_c1_suicide_quest1_check')

        ml.find_label('quest2') \
            .hook_to('dwtd_c1_suicide_quest2_suicideforcecheck') \
            .search_menu("It tells us that it was suicide.") \
            .branch() \
            .search_if() \
            .link_from('dwtd_c1_suicide_quest2_suicideforcecheck_failed')
        
        ml.find_label('quest3') \
            .hook_to('dwtd_c1_suicide_quest3_suicideforcecheck') \
            .search_menu("He wouldn't, because this was clearly a suicide.") \
            .branch() \
            .search_if() \
            .link_from('dwtd_c1_suicide_quest3_suicideforcecheck_failed')
        
        ml.find_label('quest5') \
            .hook_to('dwtd_c1_suicide_quest5_suicideforcecheck') \
            .search_menu("He committed suicide.") \
            .branch() \
            .search_if() \
            .link_from('dwtd_c1_suicide_quest5_suicideforcecheck_failed')

    dwtd_c1_suicide_link(magmalink())

label dwtd_c1_suicide_quest1_check:
    if dwtd.check_keypoint():
        jump dwtd_c1_suicide_quest1_check_return
    play sound "fx/system3.wav"
    s "You can't reload to fix a \"Hardcore\" timeline. You have far too overactive an imagination."
    if wrong3:
        c "Based on the number and shape of the wounds, I'd say it was a suicide."
        Br "No way."
        python:
            answers -= 2
            suicide += 1
            wrong3 = False
    c "They are clean cuts, like from a knife or another sharp instrument."
    Br "That is true, but why does this matter?"
    c "It tells us that it was a suicide."
    Br "I thought we ruled that one out already."
    jump dwtd_c1_suicide

label dwtd_c1_suicide_quest2_suicideforcecheck:
    if dwtd.check_keypoint() or not wrong6:
        jump dwtd_c1_suicide_quest2_suicideforcecheck_return
    play sound "fx/system3.wav"
    s "You can't reload to fix a \"Hardcore\" timeline. You have far too overactive an imagination."
    c "It tells us that it was suicide."
    jump dwtd_c1_suicide_quest2_suicideforcecheck_failed

label dwtd_c1_suicide_quest3_suicideforcecheck:
    if dwtd.check_keypoint() or not wrong10:
        jump dwtd_c1_suicide_quest3_suicideforcecheck_return
    play sound "fx/system3.wav"
    s "You can't reload to fix a \"Hardcore\" timeline. You have far too overactive an imagination."
    c "He wouldn't, because this was clearly a suicide."
    jump dwtd_c1_suicide_quest3_suicideforcecheck_failed

label dwtd_c1_suicide_quest5_suicideforcecheck:
    if dwtd.check_keypoint() or not wrong18:
        jump dwtd_c1_suicide_quest5_suicideforcecheck_return
    play sound "fx/system3.wav"
    s "You can't reload to fix a \"Hardcore\" timeline. You have far too overactive an imagination."
    c "He committed suicide."
    jump dwtd_c1_suicide_quest5_suicideforcecheck_failed

    



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
        "Religion.":
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
    c "Actually, could you show us slashing at your own wing with that knife? Held with your foot?"
    show bryce brow b
    show adine sad b flip
    with dissolve
    Ad "W- What?"
    show adine at Position(xanchor='center',xpos=0.0) with ease
    m "Adine backed away a few steps, leaving the knife on the ground."
    Br stern b "Okay, that's enough, [player_name]. You can't ask her to risk hurting herself to prove your point."
    Br brow b "Besides. Now that you explain it that way, we'd expect to find blood on the victim's feet. We don't."
    c "No, no. You saw how little blood there was in the wing cuts. Here."
    m "I began balancing on one foot, struggling to take off my shoe and expose my other foot."
    Br stern b "Careful!"
    m "Reaching over with my bare foot, I picked up the knife by the handle between my big and index toes."
    c "We can already see fliers have no problem picking up and manipulating things with their feet, right? Even flying and landing with objects held."
    m "I stuck my arm out like a sheet hung from it, pretending it was a wing. Then, I lifted my leg to swipe the knife through the imaginary wing membrane. The knife skittered from between my toes when I stumbled to catch my balance, but my point had been made."
    c "My legs are {i}less{/i} articulate than a flier's. And {i}I{/i} could replicate that damage, if I had wings."
    Ad think b flip "{size=-8}What are you even talking about? Why would someone do that?{/size}"
    Br brow b "And the chest and neck injuries?"
    m "I held up three fingers on one hand, folding in my thumb and pinkie."
    c "Roughly equivalent to a flier hand, right?"
    m "Picking up the knife between my index and middle fingers, I twisted my hand, flicking the handle against my palm until I had it gripped around the right way."
    c "And then,"
    m "I swiped the blade of the knife in the space over my chest."
    c "Q.E.D."
    show adine sad b flip with dissolve
    $ renpy.pause(0.8)
    Ad disappoint b flip "Um."
    $ renpy.pause(0.5)
    Ad think b flip "You can't make those motions with wings. Your elbow was out too far."
    m "I stared at her."
    Ad sad b flip "You can't get further than... this?"
    c "Oh, so lower."
    show adine think b flip with dissolve
    m "I repeated the chest slashing motions, now from the lower angle."
    show bryce stern b with dissolve
    m "Bryce shook his head."
    Br "That doesn't work. Now the angle of the cuts are too low, and you can't reach your neck."
    c "Yes I can. If I tug in my shoulder like thi--"
    play sound "fx/slice.ogg"
    show adine sad b flip
    show bryce angry b
    with fadequick
    $ renpy.pause(0.5)
    c "Urk"
    Br "[player_name]!"
    show bryce stern b at center
    show adine think b
    with fadequick
    Br "Just don't--"
    scene black with dissolve
    play sound "fx/impact3.ogg"
    $ renpy.pause(2.0)
    $ dwtd.deathsound(5)
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause(4.0)
    call dwtd_youdied("Clearly Suicide","That was a very direct demonstration you gave.")