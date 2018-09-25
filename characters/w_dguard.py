import pygame
from characters import char_parent
from sprites import spr_w_dguard


class DemonguardWarrior(char_parent.ChrPar):
    cat = "Demonguard"

    def __init__(self, pos):
        self.sprite = spr_w_dguard.SprDemonguardWarrior(pos)
        self.max_hp = 1500
        self.ap = 1000
        self.dp = 500
        super().__init__(pos)
