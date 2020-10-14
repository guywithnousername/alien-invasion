import pygame
from pygame.sprite import Sprite
import pygame.font
class Wall(Sprite):
    def __init__(self,aigame,x):
        self.setting = aigame.settings
        self.wall_width = 20
        self.screen = aigame.screen
        self.color = (200,255,0)
        self.rect = pygame.Rect(x,(self.setting.height - 125),self.wall_width,10)

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Text:
    """
    class for showing the score
    """
    def __init__(self,aigame,msg,y):
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.text = self.font.render(msg,True,(0,255,0),None)
        self.rect = self.text.get_rect()
        self.rect.center = 1500,y

    def show(self,msg):
        self.text = self.font.render(msg,True,(0,255,0),None)
        self.screen.blit(self.text,self.rect)