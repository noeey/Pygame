import sys, pygame

from pygame.locals import *


width=1200
height=780

screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('HomeLauncher.png').convert()
dwarf = pygame.transform.scale(pygame.image.load('dwarf.png').convert(),(100,100))

#speed = (0,0)

class Player(pygame.sprite.Sprite) :
   def __init__(self):
       super().__init__()
       self.image = pygame.image.load('door.png')
       self.rect = self.image.get_rect()

moveX = 10
moveY = 10

screen.blit(bg, (0, 0))





pygame.key.set_repeat(10,10)

while 1:


   screen.blit(bg, (0, 0))
#movesprite
   for event in pygame.event.get():
       if event.type== pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
               moveX+=10
           if event.key == pygame.K_LEFT:
               moveX -= 10
           if event.key == pygame.K_UP:
               moveY -= 10
           if event.key == pygame.K_DOWN:
               moveY += 10



       if event.type ==QUIT:
           pygame.quit()
           sys.exit()
   screen.blit(dwarf, (moveX, moveY))

   pygame.display.update()
