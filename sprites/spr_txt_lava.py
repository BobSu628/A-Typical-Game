from sprites.spr_parent import SprPar


class SprTxtLava(SprPar):
    def __init__(self, pos):
        super().__init__(pos,
                         ["resources/txt_lava.png"])
