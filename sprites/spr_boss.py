from sprites.spr_parent import SprPar


class SprBoss(SprPar):
    def __init__(self, pos):
        super().__init__(pos,
                         ["resources/boss.png"])
