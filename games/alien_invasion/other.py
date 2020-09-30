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
    def __init__(self,aigame,msg):
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (255,255,0)
        self.font = pygame.font.SysFont(None,48)
        self.rect = (self.screen_rect.right,self.screen_rect.bottom,200,50)
        self.prep(msg)

    def prep(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color)

    def draw(self):
        self.screen.blit(self.msg_image,self.rect)