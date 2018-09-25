from sprites.spr_parent import SprPar


class SprSoldier(SprPar):
    def __init__(self, pos):
        super().__init__(pos,
                         ["resources/soldier.png"])
