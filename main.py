import pygame
import cfg
from rooms import *


pygame.init()
width = cfg.display_width
height = cfg.display_height
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("ATG")
prev_room = None
room = menu.Menu()
clock = pygame.time.Clock()


def game_quit():
    pygame.quit()
    quit()


def handle_event(event):
    global room, prev_room
    events = room.handle_event(event)
    for event in events:
        if event is not None:
            if event == "play":
                prev_room = room
                room = lvl_prologue.LvlPrologue()
            elif event == "quit":
                game_quit()
            elif event == "menu":
                prev_room = room
                room = menu.Menu()
            elif event == "help":
                prev_room = room
                room = help.Help()
            elif event == "back":
                if prev_room is not None:
                    room = prev_room


def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            else:
                handle_event(event)

        room.blit(gameDisplay)
        pygame.display.update()
        clock.tick(cfg.FPS)
    pygame.quit()
    quit()


# main
game_loop()
