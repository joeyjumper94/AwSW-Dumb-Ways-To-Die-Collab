# AwSW Dumb Ways to Die Mod

Publicly available core methods:

+ `call screen dwtd_qte("QTE_ACTION")` - Use to display a button the player must click within a certain amount of time. Second argument can be a floating point number of seconds, default 1.0.
+ `if not dwtd.check_keypoint("KEYPOINT"):` - If this `if` statement triggers, the player is trying to cheese a Hardcore save. Force their death, maybe with a message from system.
    + KEYPOINT argument values. Give the keypoint that happened most recently before your scene, e.g. `'C1_CHARACTER_SELECT'` for a death in Remy1.
        + `'C1'` - Literally just started the game.
        + `'C1_FOUND_LEMON'` - Found the lemon in the pantry
        + `'C1_CHARACTER_SELECT'` - Made it to choosing a character in Chapter 1
        + `'C2'` - Made it to Chapter 2 title card
        + `'C2_CHARACTER_SELECT'` - Made it to choosing a character in Chapter 2
        + `'C3'` - Made it to Chapter 3 title card
        + `'C3_CHARACTER_SELECT'` - Made it to choosing a character in Chapter 3
        + `'C4'` - Made it to Chapter 4 title card
        + `'C4_CHARACTER_SELECT'` - Made it to choosing a character in Chapter 4
        + `'C5'` - Made it to Chapter 5 title card
+ `show dwtd_youdied_text` - Display the "You Died" comic sans text to tell the player what the hell's going on.
+ `dwtd.deathsound(sound_number,sound_playtime)` - Play a sound, often done while showing the "You Died" text, for tonal consistency.
    + `sound_number` - How many "booms" in the sound. No consistent direction.
    + `sound_playtime` - Fadeout time of the booms, as they're almost universally too long. It's recommended to follow this statement with `renpy.pause()` of equivalent time to let things really sink in for the player.
+ `call dwtd_youdied("Name of death","CAUSE OF DEATH")` - End of a death path. Displays `"CAUSE OF DEATH"` as read by system, then opens a menu screen to load, mainmenu, or quit.
