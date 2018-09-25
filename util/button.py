import cfg
import pygame
from util import text


class Button:
    text = ""
    text_style = ""
    x = 0
    y = 0
    w = 0
    h = 0
    text_size = 0
    orig = None
    hover = None
    action = None
    text_color = None

    def __init__(self, text, x, y, width, height, icolor, acolor, text_color=cfg.black, text_size=25, text_style="arial", action=None):
        self.text = text
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.orig = icolor
        self.hover = acolor
        self.text_color = text_color
        self.text_size = text_size
        self.text_style = text_style
        self.action = action

    def draw(self, display):
        cur = pygame.mouse.get_pos()
        if self.x + self.w > cur[0] > self.x and self.y + self.h > cur[1] > self.y:
            pygame.draw.rect(display, self.hover, (self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(display, self.orig, (self.x, self.y, self.w, self.h))

        msg = text.Text(self.text, self.text_color, self.text_size, self.text_style)
        msg.display_to_button(display, self.x, self.y, self.w, self.h, 20)

    def onclick(self):
        click = pygame.mouse.get_pressed()
        cur = pygame.mouse.get_pos()
        if self.x + self.w > cur[0] > self.x and self.y + self.h > cur[1] > self.y and click[0] == 1:
            return self.action
        return None
