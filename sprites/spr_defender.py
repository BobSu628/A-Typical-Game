from sprites.spr_parent import SprPar


class SprDefender(SprPar):
    def __init__(self, pos):
        super().__init__(pos,
                         ["resources/defender.png"])
