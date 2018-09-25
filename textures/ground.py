import pygame
from textures import texture_parent
from sprites import spr_txt_ground
import cfg


class Ground(texture_parent.TxtPar):
    def __init__(self, pos):
        super().__init__(pos)
        self.sprite = spr_txt_ground.SprTxtGround(pos)

    def getName(self):
        return "ground"


