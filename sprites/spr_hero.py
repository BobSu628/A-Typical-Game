from sprites.spr_parent import SprPar


class SprHero(SprPar):
    def __init__(self, pos):
        super().__init__(pos,
                         ["resources/hero.png"])
