import renpy
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    @staticmethod
    def mod_info():
        return ("Dumb Ways To Die", "v0.0", "Many", False)

    @staticmethod
    def mod_load():
        pass

    @staticmethod
    def mod_complete():
        skip_menus = (node for node in renpy.game.script.all_stmts if isinstance(node, renpy.ast.Menu) and node.items[0][0] == "Yes. I want to skip ahead.")
        for node in skip_menus:
            no_block = None
            for i,option in enumerate(node.items):
                node.items[i] = (option[0], 'not dwtd.hardcore' if option[1] == 'True' else option[1]+' and not dwtd.hardcore', option[2])
                if option[0] == "No. Don't skip ahead.":
                    no_block = option[2]
            if not no_block:
                renpy.error(node, "has \"Yes. I want to skip ahead.\" but not \"No. Don't skip ahead.\"")
            node.items.append(("There is no skipping in a \"Hardcore\" timeline.", 'dwtd.hardcore', no_block))