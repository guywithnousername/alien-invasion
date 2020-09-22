import pathlib
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

  def __init__(self, aigame):
    super().__init__()
    path = pathlib.Path(__file__).parent.absolute()
    self.screen= aigame.screen
    self.image = pygame.image.load(str(path) + '/images/alien.bmp')
    self.rect = self.image.get_rect()
    self.setting = aigame.settings
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    self.x = float(self.rect.x)

  def check_edges(self):
    screen_rect = self.screen.get_rect()
    if self.rect.right >= screen_rect.right or self.rect.left <= 0:
      return True


  def update(self):
    self.x += (self.setting.alien_speed * self.setting.direction)
    self.rect.x = self.x

class blueAlien(Alien):

  def __init__(self, aigame):
    super().__init__(aigame)
    path = pathlib.Path(__file__).parent.absolute()
    self.image = pygame.image.load(str(path) + '/images/blue_alien.bmp')