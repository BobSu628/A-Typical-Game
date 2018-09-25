from textures import texture_parent
from sprites import spr_txt_lava


class Lava(texture_parent.TxtPar):
    canWalkOn = False

    def __init__(self, pos):
        super().__init__(pos)
        self.sprite = spr_txt_lava.SprTxtLava(pos)

    def getName(self):
        return "lava"

