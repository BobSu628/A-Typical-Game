import pygame
from characters import char_parent
from sprites import spr_defender


class Defender(char_parent.ChrPar):
    cat = "Human"
    hostile = False

    def __init__(self, pos):
        self.sprite = spr_defender.SprDefender(pos)
        self.max_hp = 2000
        self.ap = 100
        self.dp = 500
        super().__init__(pos)
