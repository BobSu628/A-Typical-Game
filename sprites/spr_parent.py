import pygame


class SprPar(pygame.sprite.Sprite):

    def __init__(self, pos, images):
        self.x = pos[1]
        self.y = pos[0]
        self.ani_speed_init = 30
        self.ani_speed = self.ani_speed_init
        self.ani = images
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])
        self.update()

    def update(self):
        self.ani_speed -= 1
        if self.ani_speed == 0:
            self.img = pygame.image.load(self.ani[self.ani_pos])
            self.ani_speed = self.ani_speed_init
            if self.ani_pos == self.ani_max:
                self.ani_pos = 0
            else:
                self.ani_pos += 1

    def draw(self, pos, display):
        self.x = pos[1]
        self.y = pos[0]
        display.blit(self.img, (self.x, self.y))
        self.update()

