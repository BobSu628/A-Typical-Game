import pygame
from characters import char_parent
from sprites import spr_boss


class Boss(char_parent.ChrPar):
    cat = "King"

    def __init__(self, pos):
        self.sprite = spr_boss.SprBoss(pos)
        self.max_hp = 10000
        self.ap = 5000
        self.dp = 2500
        super().__init__(pos)
