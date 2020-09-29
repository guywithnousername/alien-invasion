import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
    def __init__(self,aigame,x):
        self.setting = aigame.settings
        self.wall_width = 20
        self.screen = aigame.screen
        self.color = (200,255,0)
        self.rect = pygame.Rect(x,(self.setting.height - 125),self.wall_width,10)

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect)