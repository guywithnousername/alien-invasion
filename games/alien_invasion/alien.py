import pathlib
import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):

  def __init__(self, aigame):
    super().__init__()
    path = pathlib.Path(__file__).parent.absolute() # get file path
    self.image = pygame.image.load(str(path) + '/images/alien.bmp') #get location of the alien image
    self.screen= aigame.screen
    self.rect = self.image.get_rect()
    self.setting = aigame.settings
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    self.x = float(self.rect.x)

  def check_edges(self): #check if touching edge
    screen_rect = self.screen.get_rect()
    if self.rect.right >= screen_rect.right or self.rect.left <= 0:
      return True


  def update(self): #move the alien
    self.x += (self.setting.alien_speed * self.setting.direction)
    self.rect.x = self.x

  def randomize(self):
    randomx= random.randint(-20,20)
    randomy= random.randint(-10,10)
    self.x += randomx
    self.rect.y += randomy
    self.rect.x = self.x

class blueAlien(Alien):

  def __init__(self, aigame):
    super().__init__(aigame)
    path = pathlib.Path(__file__).parent.absolute()
    self.image = pygame.image.load(str(path) + '/images/blue_alien.bmp')
    self.y = float(self.rect.y)

  def update(self):
    self.y += self.setting.blue_alien_speed
    self.rect.y = self.y
  
  def check_edges(self):
    screen_rect = self.screen.get_rect()
    if self.y <= screen_rect.bottom:
      return True
