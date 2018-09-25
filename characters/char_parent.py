class ChrPar:

    cat = "Category"
    hostile = True
    move_speed = 10

    def __init__(self, pos):
        self.dis = (0, 0)
        self.pos = pos
        self.hp = self.max_hp
        self.fr_count = 0

    def set_pos(self, pos):
        self.pos = pos

    def move(self, move):
        self.dis = move

    def moveProcedure(self):
        if self.dis != (0, 0):
            if self.fr_count < 100 / self.move_speed:
                self.pos = (self.pos[0] + self.dis[0] * self.move_speed, self.pos[1] + self.dis[1] * self.move_speed)
                self.fr_count += 1
            else:
                self.dis = (0, 0)
                self.fr_count = 0

    def draw(self, display):

        self.moveProcedure()
        self.sprite.draw(self.pos, display)
