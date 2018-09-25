class TxtPar:
    obj = None
    canWalkOn = True
    sprite = None
    pos = None

    def __init__(self, pos):
        self.pos = pos

    def draw(self, display):
        self.sprite.draw(self.pos, display)

    def getName(self):
        return ""

    def setObj(self, o):
        self.obj = o

    def getObj(self):
        return self.obj

    def set_pos(self, pos):
        self.pos = pos

