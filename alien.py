import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

  def __init__(self,aigame):
    super().__init__()
    self.screen= aigame.screen
    self.image = pygame.image.load('games/images/alien.bmp')
    self.rect = self.image.get_rect()

    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    self.x = float(self.rect.x)
    