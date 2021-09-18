# AwSW Dumb Ways to Die Mod

Publicly available core methods:

+ `call screen dwtd_qte("QTE_ACTION")` - Use to display a button the player must click within a certain amount of time. Second argument can be a floating point number of seconds, default 1.0.
+ `if not dwtd.check_keypoint():` - If this `if` statement triggers, the player is trying to cheese a Hardcore save. Force their death, maybe with a message from system.
+ `show dwtd_youdied_text` - Display the "You Died" comic sans text to tell the player what the hell's going on.
+ `dwtd.deathsound(sound_number,sound_playtime)` - Play a sound, often done while showing the "You Died" text, for tonal consistency.
    + `sound_number` - How many "booms" in the sound. No consistent direction.
    + `sound_playtime` - Fadeout time of the booms, as they're almost universally too long. It's recommended to follow this statement with `renpy.pause()` of equivalent time to let things really sink in for the player.
+ `call dwtd_youdied("Name of death","CAUSE OF DEATH")` - End of a death path. Displays `"CAUSE OF DEATH"` as read by system, then opens a menu screen to load, mainmenu, or quit.
