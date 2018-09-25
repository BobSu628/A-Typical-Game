import pygame
from characters import char_parent
from sprites import spr_soldier


class Soldier(char_parent.ChrPar):
    cat = "Human"
    hostile = False

    def __init__(self, pos):
        self.sprite = spr_soldier.SprSoldier(pos)
        self.ap = 100
        self.dp = 50
        self.max_hp = 500
        super().__init__(pos)
