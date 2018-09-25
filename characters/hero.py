import pygame
from characters import char_parent
from sprites import spr_hero


class Hero(char_parent.ChrPar):
    cat = "Human"
    hostile = False

    def __init__(self, pos):
        self.sprite = spr_hero.SprHero(pos)
        self.ap = 800
        self.dp = 500
        self.max_hp = 10000
        super().__init__(pos)
