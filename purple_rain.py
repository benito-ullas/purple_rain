import pygame
import random as r

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

screen = None
scr_width = 800
scr_height = 600


x = 10
d = []

# Global variable for text
text = None
textRect = None

#######################################################

class Drop:
        def __init__(self):
                self.x = r.random()*scr_width
                self.y = r.random()*200-300
                self.yspeed = r.random()*3+4
                
        def fall(self):
                self.y += self.yspeed
                self.yspeed += 0.095
                
                if self.y > scr_height:
                        self.y = r.random()*200-300
                        self.yspeed = r.random()*3+4
                
        def show(self):
                pygame.draw.line(screen, (138,43,226), (self.x,self.y), (self.x,self.y + r.random()*10+10),r.choice([1,2]))
                
                
#######################################################                

def setup():
        global screen
        global text, textRect
        screen = pygame.display.set_mode((scr_width,scr_height))
        for i in range(500) :
                d.append(Drop())
        
        # For Text        
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('PURPLE RAIN', True, (138,43,226), (230,230,250))
        textRect = text.get_rect()
        textRect.center = (scr_width // 2,scr_height // 2)
        
def draw():
        screen.fill((230,230,250))
        
        #For text
        screen.blit(text, textRect)
 
        for i in range (len(d)):
                d[i].fall()
                d[i].show() 
       
        pygame.display.flip()
        
############################       

setup()
running = True
while running:
        # Quiting program when pygame window is closed
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        draw()
        pygame.display.update()
        fpsClock.tick(fps)
        
############################
