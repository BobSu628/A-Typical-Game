import pygame


# load image
def load_image(name):
    image = pygame.image.load(name)
    return image


# colors
white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 0, 0)
light_red = (255, 0, 0)

green = (0, 200, 0)
light_green = (0, 255, 0)

blue = (0, 0, 200)
light_blue = (0, 0, 255)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

orange = (209, 74, 12)
grey = (150, 147, 145)

# screen size
display_width = 1000
display_height = 800
scr_len = 700

# fps
FPS = 30
