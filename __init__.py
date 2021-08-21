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
        pass