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
                self.thic = r.choice([1,2,3])
                self.len = r.random()*20 + 10
                
        def fall(self):
                self.y += self.yspeed
                self.yspeed += 0.095
                
                if self.y > scr_height:
                        self.y = r.random()*200-300
                        self.yspeed = r.random()*3+4
                
        def show(self):
                line = pygame.Surface((self.thic,self.len),pygame.SRCALPHA)
                line.fill((138,43,226,r.random()*200+55))
                screen.blit(line,(self.x,self.y))
                
                
#######################################################     

def setup():
        global screen
        global text, textRect
        screen = pygame.display.set_mode((scr_width,scr_height))
        screen.fill((230,230,250,0))
        
        
        for i in range(500) :
                d.append(Drop())
        
        # For Text        
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('PURPLE RAIN', True, (138,43,226,0), (230,230,250))#(230,230,250)
        textRect = text.get_rect()
        textRect.center = (scr_width // 2,scr_height // 2)
        
def draw():
        surf = pygame.Surface((scr_width,scr_height),pygame.SRCALPHA)
        surf.fill((230,230,250))
        screen.blit(surf,(0,0))
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
