from rooms import lvl_parent
from textures import ground, lava
from characters import *


class LvlPrologue(lvl_parent.LvlPar):

    def __init__(self):
        self.hero_pos = (6, 3)
        self.len = 7
        super().__init__()

    def init_map(self):
        # init texture
        for i in range(0, self.len):
            self.grid[0][i] = lava.Lava(self.pos(0, i))
            if i != 3:
                self.grid[1][i] = lava.Lava(self.pos(1, i))
                self.grid[6][i] = lava.Lava(self.pos(6, i))
            else:
                self.grid[1][i] = ground.Ground(self.pos(1, i))
                self.grid[6][i] = ground.Ground(self.pos(6, i))
            if i == 0 or i == 6:
                self.grid[2][i] = lava.Lava(self.pos(2, i))
                self.grid[3][i] = lava.Lava(self.pos(3, i))
            else:
                self.grid[2][i] = ground.Ground(self.pos(2, i))
                self.grid[3][i] = ground.Ground(self.pos(3, i))
            if i == 0 or i == 1 or i == 5 or i == 6:
                self.grid[4][i] = lava.Lava(self.pos(4, i))
                self.grid[5][i] = lava.Lava(self.pos(5, i))
            else:
                self.grid[4][i] = ground.Ground(self.pos(4, i))
                self.grid[5][i] = ground.Ground(self.pos(5, i))

    def init_level(self):

        # self.grid[1][3].setObj(m_dguard.DemonguardMage(self.pos(1, 3)))
        self.grid[2][2].setObj(m_dguard.DemonguardMage(self.pos(2, 2)))
        self.grid[2][5].setObj(m_dguard.DemonguardMage(self.pos(2, 5)))
        self.grid[3][3].setObj(w_dguard.DemonguardWarrior(self.pos(3, 3)))
        self.grid[2][3].setObj(boss.Boss(self.pos(2, 3)))
        self.grid[5][2].setObj(soldier.Soldier(self.pos(5, 2)))
        # self.grid[5][4].setObj(soldier.Soldier(self.pos(5, 4)))
        self.grid[4][3].setObj(defender.Defender(self.pos(4, 3)))
        self.grid[6][3].setObj(self.hero)



