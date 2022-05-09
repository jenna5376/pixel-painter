# capitalized vars mark constants
import pygame
pygame.init()
pygame.font.init()

#available colors

typing = False
RED = (237, 27, 36)
ORANGE = (252, 127, 43)
YELLOW = (254, 242, 0)
GREEN = (25, 177, 77)
BLUE = (0, 163, 232)
INDIGO = (63,71,204)
PURPLE = (164, 72, 161)

RED2 = (254, 174, 201)
ORANGE2 = (255, 201, 13)
YELLOW2 = (239,228,174)
GREEN2 = (181, 229, 29)
BLUE2 = (154, 217, 234)
INDIGO2 = (112,146,191)
PURPLE2 = (199, 191, 230)

BLACK = (0, 0, 0)
GREY = (127,127,127)
GREY2 = (195,195,195)
WHITE = (255, 255, 255)
BROWN = (230,198,183)
BROWN2 = (200,155,130)
BROWN3 = (129,96,79)

FPS = 150
GREY3 = (220,220,220)
GREY4 = (50,50,50)
BLUE3 = (81, 111, 194)


WIDTH,HEIGHT = 550,750

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT-WIDTH

PIXEL_SIZE = WIDTH // ROWS

BG_COLOR = WHITE

DRAW_GRID_LINES = False

button_y = HEIGHT - TOOLBAR_HEIGHT/2-55
button_y2 = button_y + 45
button_y3 = button_y2 + 45
button_size = 35

last_color = BLACK

def get_font(size):
    return pygame.font.SysFont("roboto", size)
