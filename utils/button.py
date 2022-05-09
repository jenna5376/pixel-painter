from .settings import *

class Button:
    def __init__(self,x,y,width,height,color, text = None, text_color = GREY4,outline = WHITE):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.outline = outline
        
    def draw(self,win):
        #draws rect color
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
        #adds an outline
        pygame.draw.rect(win,self.outline,(self.x,self.y,self.width,self.height),2)
        if self.text:
            button_font = get_font(15)
            text_surface = button_font.render(self.text,1,self.text_color)
            #centers text
            win.blit(text_surface,(self.x+self.width/2-text_surface.get_width()/2,self.y+self.height/2-text_surface.get_height()/2))
           
    
    def clicked(self,pos):
        x,y = pos

        #return false if mouse isnt in buttons x y range
        if not (x >= self.x and x <= self.x +self.width):
            return False
        if not (y>= self.y and y <= self.y + self.height):
            return False

        return True