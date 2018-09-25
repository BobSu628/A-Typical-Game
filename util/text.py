import pygame
import cfg


class Text:

    def __init__(self, text, color, size, style):
        self.text = text
        self.color = color
        self.size = size
        self.font = pygame.font.SysFont(style, size)
        self.surface = []
        self.rect = []

        self.split_text = text.split("\n")
        for i in range(0, len(self.split_text)):
            self.surface.append(self.font.render(self.split_text[i], True, color))
            self.rect.append(self.surface[i].get_rect())

    def get_surface(self):
        return self.surface, self.rect

    def display_to_screen(self, display, y_displace=0, gap=40, align="center", padding=50):
        for i in range(0, len(self.split_text)):
            rect = self.rect[i]
            if align == "center":
                rect.center = (cfg.display_width / 2), y_displace + gap*i
            elif align == "left":
                rect.midleft = padding, y_displace + gap*i
            display.blit(self.surface[i], rect)

    def display_to_button(self, display, x, y, width, height, gap=40):
        for i in range(0, len(self.split_text)):
            rect = self.rect[i]
            rect.center = ((x + (width / 2)), y + (height / 2) + gap*i)
            display.blit(self.surface[i], rect)
