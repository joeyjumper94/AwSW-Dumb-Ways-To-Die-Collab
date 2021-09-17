init python:
    def dwtd_remy4_rominterfere_link(ml):
        anna_scorned = '(annadead == False) and (annastatus in ["bad","abandoned"]) and (annascenesfinished > 1)'
        ml.find_label('remy4skip2') \
            .search_if('remystatus == "neutral"') \
            .branch_else() \
            .search_say("You are pretty cute, you know that?") \
            .hook_to('dwtd_remy4_rominterfere_firstsigns', condition=anna_scorned) \
            .search_say("I am serious.") \
            .hook_to('dwtd_remy4_rominterfere_kisscheck', condition=anna_scorned, return_link=False) \
            .search_menu("Kiss him.") \
            .link_from('dwtd_remy4_rominterfere_lastescapemenu') \
            .branch() \
            .first() \
            .link_from('dwtd_remy4_rominterfere_sealthedeal') \
            .search_say("Anyway, it's getting really late, so I should probably get going now.") \
            .hook_to('dwtd_remy4_rominterfere_uhoh', condition=anna_scorned) \


    dwtd_remy4_rominterfere_link(magmalink())

label dwtd_remy4_rominterfere_firstsigns:
    # Coming from "You are pretty cute, you know that?"
    show remy look b with dissolve
    m "Remy slipped over to my couch, taking a seat by lying along most of it. After a moment, I followed him over."
    jump dwtd_remy4_rominterfere_firstsigns_return

label dwtd_remy4_rominterfere_kisscheck:
    # Coming from "I am serious."
    m "He looked at me, hesitating. Then, he leaned forward, his head slowly his head slowly moving closer to my own."
    show remyrom at Pan((580, 326), (350, 0), 8.0) with fade
    $ renpy.pause (6.0)
    if not dwtd.check_keypoint():
        play sound "fx/system3.wav"
        s "Looks like this \"Hardcore\" timeline is broken. The scorn is too strong here."
        jump dwtd_remy4_rominterfere_sealthedeal
    else:
        jump dwtd_remy4_rominterfere_lastescapemenu


label dwtd_remy4_rominterfere_uhoh:
    # Coming from "Anyway, it's getting really late, so I should probably get going now."
    m "He struggled to unfold his legs again from his seated position on the couch."
    $ dwtd.will_die()
    c "You alright there?"
    Ry smile b "It's nothing."
    Ry look b "Just a bit of joint pain I've been having today. I must have slept wrong on something. It wasn't as bad earlier, cleaning the pantry."
    Ry shy b "Mind if I just sit here with you for a few more minutes? I don't want to impose..."
    c "I don't mind at all."
    Ry normal b "Thank you."
    $ renpy.pause(0.8)
    m "Scooching a little closer on the couch, I hugged Remy. He leaned into me, and we stayed just like that for a minute, maybe two."
    stop music fadeout 5.0
    m "Then I found his body heat starting to be a little too much."
    # m "I was going to get up, but I couldn't." # Not quite yet, Copilot. Jeepers.
    Ry shy b "Is something wrong?"
    c "Sorry, just a little hot in here."
    Ry "I- I see. If you would prefer I go..."
    c "No, no that's not what I mean."
    play music "mx/threat.ogg" fadein 0.5
    m "My ability to form coherent corrections was cut off as a dull pain in my gut began to throb. I struggled to my feet, already a little unsteady."
    Ry look b "[player_name]? Are you alright?"
    c "N- No."
    m "The stinging was quickly working its way up my throat, and something else wasn't far behind. I lurched for the restroom and the porcelain throne within."
    scene bath with wiperight
    $ renpy.pause (0.5)
    m "I barely got the first heave inside the bowl."
    show remy sad b flip at left with easeinleft
    m "Remy was at my side a moment later, despite limping in after me, clearly still suffering his joint pain."
    Ry "[player_name]? Should I call someone?"
    m "Any attempt at a reply by me was interrupted by my second heave."
    Ry "I- I'm calling a doctor to check on you. Just hold on."
    m "I gave him a nod while struggling to keep my grip on the toilet bowl. Already I was feeling stiff and foggy, despite my heart beating a mile a minute."
    m "Chills ran up and down my arms, neck, and head. My shirt collar felt damp."
    hide remy with easeoutright
    $ renpy.pause (1.5)
    Ry sad b "I'm at [player_name]'s apartment. They just abruptly became violently ill. Vomiting, clammy scal-- ah, skin."
    Ry sad b "I- I don't know! We--"
    Ry shy b "We had just kissed. I didn't think that would have any negative impact. I- I didn't think, I--"
    Ry sad b "The bathroom.{w=0.5} I've opened the front door.{w=0.5} Yes, thank you. I- I need to go back in there."
    $ renpy.pause (0.5)
    show remy sad b flip at left with easeinleft
    Ry "Just hold on. Help is coming."
    m "I was still trying to get up, but I couldn't." # Now you can, Copilot. Thanks.
    Ry "I'm sorry. I didn't mean to hurt you." # Ooh, wow, nice Copilot.
    show remy look b flip with fadequick
    Ry "I didn't think my saliva would affect you so much. If- If it was food from the cart, that would have affected you earlier, I..."
    Ry "Unless it was something in the lipstick."
    show remy shy b flip with fadequick
    Ry "Anna's substitution? I had thought--"
    m "It didn't matter what he thought now. My stiffening body could no longer keep my position bent over the toilet."
    scene black with dissolvemed
    play sound "fx/impact.wav"
    m "My head struck the tiled wall on the way down, the sharp spike of pain forcing my eyes closed."
    Ry sad b "[player_name]!"
    Ry sad b "No. No, stay with me."
    m "I couldn't open my eyes again, couldn't move. Even my chest was tightening."
    Ry shy b "P- Please don't--"
    Ry sad b "I can't. N- Not again. Please, [player_name], just hold on..."
    stop music fadeout 6.0
    m "I couldn't hold on. I couldn't breathe. I couldn't even move to return his touch one last time as he shook my shoulder."
    $ renpy.pause (2.0)
    $ dwtd.deathsound(2)
    show dwtd_youdied_text at top with easeintop
    $ renpy.pause(4.0)
    call dwtd_youdied("Romantic Interference","I suppose this is what happens when you scorn the lady with control over most chemical supplies in town, then date someone she hates.")