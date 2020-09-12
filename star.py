import pygame
import random
from pygame.sprite import Sprite
class Star(Sprite):
  def __init__(self,aigame):
    super().__init__()
    self.screen = self.aigame
    self.settings = aigame.settings
    self.star = pygame.image.load('star.bmp')
    self.rect = self.star.get_rect()
    self.rect.midtop = 0
    self.y = float(self.rect.y)
  def update(self):
    self.y += 5
    self.rect.y = self.y

