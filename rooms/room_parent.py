import cfg
import pygame


class RoomPar:
    w = cfg.display_width
    h = cfg.display_height

    def __init__(self):
        self.buttons = []

    def blit(self, display):
        display.fill(cfg.black)

    def handle_event(self, event):
        events = []
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            for button in self.buttons:
                events.append(button.onclick())

        return events
