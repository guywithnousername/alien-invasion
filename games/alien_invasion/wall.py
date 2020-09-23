import pygame
from pygame.sprite import Sprite
class Wall(Sprite):
    def __init__(self,aigame):
        self.screen = aigame.screen
        self.color = (0,255,0)
        self.rect = pygame.Rect(50,50,10,10)
        print(self.rect)
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
