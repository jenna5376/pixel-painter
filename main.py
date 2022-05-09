#reference: https://www.youtube.com/watch?v=N20eXcfyQ_4&t=209s

""" what did i learn
trial and error system
import asterisk -> all methods vars imported so u dont need to prefix them
good way of oraganizing vars -> capitalize constants, lower changing vars
pass null code, good for testing code (PASS)
recursive func
"""

#import 
from pygame import PixelArray
from utils import * 
import sys

sys.setrecursionlimit(2000)

brush_img = pygame.image.load("utils/assets/brush.png")
eraser_img = pygame.image.load("utils/assets/eraser.png")
fill_img = pygame.image.load("utils/assets/fill.png")
picker_img = pygame.image.load("utils/assets/picker.png")
grid_img = pygame.image.load("utils/assets/grid.png")
clear_img = pygame.image.load("utils/assets/clear.png")
save_img = pygame.image.load("utils/assets/save.png")


icons = [brush_img,eraser_img,fill_img,picker_img,grid_img,clear_img,save_img]

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pixel Painter")

user_text_input = ""

drawing = pygame.Surface.subsurface(WIN,(0,0,WIDTH,HEIGHT-TOOLBAR_HEIGHT))

run = True
#fps sets speed
clock = pygame.time.Clock()
drawing_color = BLACK

colors = [
    RED,ORANGE,YELLOW,GREEN,BLUE,INDIGO,PURPLE,
    RED2,ORANGE2,YELLOW2,GREEN2,BLUE2,INDIGO2,PURPLE2,
    BLACK,GREY,GREY2,WHITE,BROWN,BROWN2,BROWN3]
buttons = []


#tool size buttons
buttons.append(Button(320,button_y,button_size*2,button_size,WHITE,"1",WHITE))
buttons.append(Button(320,button_y2,button_size*2,button_size,WHITE,"2",WHITE))
buttons.append(Button(320,button_y3,button_size*2,button_size,WHITE,"3",WHITE))


buttons.append(Button(405,button_y3,75,button_size,WHITE,"INPUT",WHITE))
#brush,erase,fill,color picker,grid,clear
tools = ["B","E","F","P","G","C"]

buttons.append(Button(485,button_y3,button_size,button_size,WHITE,"S",WHITE))

color_picker = False
fill_tool = False

tool_size = 1

#old color -> color at row col

def init_grid(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)
    return grid

grid = init_grid(ROWS,COLS,BG_COLOR)

def draw_grid(win,grid):
    
    #gives element index
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            #position x, y, pixel size
            pygame.draw.rect(win,pixel,(j*PIXEL_SIZE,i*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    
    if DRAW_GRID_LINES:
        for i in range(ROWS+1):
            #start and end of line
            pygame.draw.line(win,BLACK,(0,i*PIXEL_SIZE),(WIDTH,i*PIXEL_SIZE))
        for j in range(COLS+1):
            pygame.draw.line(win,BLACK,(j*PIXEL_SIZE,0),(j*PIXEL_SIZE,HEIGHT-TOOLBAR_HEIGHT))

def draw(win,grid,buttons,user_text_input):
    
    win.fill(BG_COLOR)
    draw_grid(win,grid)
    
    #COLOR BASE
    pygame.draw.rect(win,GREY3,(0,HEIGHT-TOOLBAR_HEIGHT,WIDTH,TOOLBAR_HEIGHT))

    for button in buttons:
        button.draw(win)

    #tool size icons
    tool_size_icon_width = 55

    pygame.draw.rect(win,GREY4,(322,button_y + 15, PIXEL_SIZE+tool_size_icon_width,5))
    pygame.draw.rect(win,GREY4,(322,button_y2 + 12, PIXEL_SIZE+tool_size_icon_width, 10))
    pygame.draw.rect(win,GREY4,(322,button_y3 + 10, PIXEL_SIZE+tool_size_icon_width, 15))
    
    font = get_font(18)

    #user input box

    user_text = font.render(user_text_input,True,GREY4)
    win.blit(user_text,[413,button_y3+11])
    
    font = get_font(20)
    color_label = font.render("color",1,GREY4)
    size_label = font.render("size",1,GREY4)
    tool_label = font.render("tool",1,GREY4)

    #clabels
    win.blit(color_label,(30+120,button_y-20,300,300))
    win.blit(size_label,(320+20,button_y-20,300,300))
    win.blit(tool_label,(405+42,button_y-20,300,300))

    if user_text_input == "":
        input_label = font.render("file name",1,GREY2)
        win.blit(input_label,(413,button_y3+11,412,button_y3+22))

    for i in range(6):
        if i<3:
            win.blit(icons[i],(407+i*40,button_y+3))
        else:
            win.blit(icons[i],(408+i*40-(40*3),button_y2+3))

    win.blit(icons[6],(488,button_y3+3))
    pygame.display.update()


def get_row_col_from_pos(pos):
    x,y = pos

    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    #make sure mouse is in drawable area
    if row >= ROWS:
        raise IndexError

    return row, col


def fill(grid,row,col,old_color,new_color):
    
    if row < 0 or row > ROWS-1 or col < 0 or col > COLS-1:
        return
    if grid[row][col] != old_color:
        return   
    
    grid[row][col] = new_color
    
    fill(grid,row+1,col,old_color,new_color)
    fill(grid,row-1,col,old_color,new_color)
    fill(grid,row,col+1,old_color,new_color)
    fill(grid,row,col-1,old_color,new_color)


#color buttons
for i in range(21):
    if i <7:
        buttons.append(Button(30+40*i,button_y,button_size,button_size,colors[i]))
    elif i <14:
        buttons.append(Button(30+40*i-(7*40),button_y2,button_size,button_size,colors[i]))
    else:
        buttons.append(Button(30+40*i-(14*40),button_y3,button_size,button_size,colors[i]))       

#tool buttons
for i in range(6):
    if i<3:
        buttons.append(Button(405+i*40,button_y,button_size,button_size,WHITE,tools[i],WHITE))
    else:
        buttons.append(Button(405+i*40-(3*40),button_y2,button_size,button_size,WHITE,tools[i],WHITE))


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN and typing == True:
            if event.key == pygame.K_BACKSPACE:
                user_text_input = user_text_input[0:-1]
            else:
                if len(user_text_input)<8:
                    user_text_input += event.unicode
        else:
            pygame.draw.line(WIN,BLACK,(440,button_y3),(440,button_y3+10))

        if pygame.mouse.get_pressed()[0]:
            button.outline = WHITE
            #get x y position of mouse
            pos = pygame.mouse.get_pos()


            try:
                row,col = get_row_col_from_pos(pos)
                

                if color_picker == False and fill_tool == False:
                    grid[row][col] = drawing_color
                    if tool_size >= 2:
                        grid[row+1][col] = drawing_color
                        grid[row][col+1] = drawing_color
                        grid[row+1][col+1] = drawing_color

                    if tool_size >= 3:
                        grid[row+2][col] = drawing_color
                        grid[row+2][col+1] = drawing_color
                        grid[row][col+2] = drawing_color
                        grid[row+1][col+2] = drawing_color
                        grid[row+2][col+2] = drawing_color                    
                elif fill_tool == True:
                    old_color = grid[row][col]
                    new_color = drawing_color
                    fill(grid,row,col,old_color,new_color)
                    fill_tool = False
                elif color_picker == True:
                    drawing_color = grid[row][col]
                    color_picker = False

            except IndexError:
                
                for button in buttons: 

                    if not button.clicked(pos):
                        
                        continue
                    button.outline = BLUE3

                    if button.text == "1":
                        tool_size = 1
                    elif button.text == "2":
                        tool_size = 2
                    elif button.text == "3":
                        tool_size = 3
                    elif button.text == "B":
                        drawing_color = last_color
                    elif button.text == "E":
                        drawing_color = WHITE
                    elif button.text == "F":
                        fill_tool = True
                    elif button.text == "P":
                        color_picker = True
                    elif button.text == "G":
                        if DRAW_GRID_LINES == False:
                            DRAW_GRID_LINES = True
                        else:
                            DRAW_GRID_LINES = False
                    elif button.text == "C":
                        grid = init_grid(ROWS,COLS,BG_COLOR)
                        drawing_color = last_color
                    elif button.text == "S":
                        pygame.image.save(drawing, "drawings/"+user_text_input + ".png")
                    else:
                        drawing_color = button.color
                        last_color = drawing_color
 
                    if button.text == "INPUT":
                        typing = True
                    else:
                        typing = False
                    break
    draw(WIN,grid,buttons,user_text_input)

pygame.quit()
