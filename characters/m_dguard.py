import pygame
from characters import char_parent
from sprites import spr_m_dguard


class DemonguardMage(char_parent.ChrPar):
    cat = "Demonguard"

    def __init__(self, pos):
        self.sprite = spr_m_dguard.SprDemonguardMage(pos)
        self.max_hp = 1000
        self.ap = 2000
        self.dp = 200
        super().__init__(pos)
