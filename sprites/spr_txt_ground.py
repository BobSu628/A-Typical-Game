from sprites.spr_parent import SprPar


class SprTxtGround(SprPar):
    def __init__(self, pos):
        super().__init__(pos,
                         ["resources/txt_ground.png"])
