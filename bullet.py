import pygame
from pygame.sprite import Sprite
import pathlib

class Bullet(Sprite):
  def __init__(self,ai_game):
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    path = pathlib.Path(__file__).parent.absolute()
    self.color = self.settings.bullet_color
    self.image = pygame.image.load(f"{str(path)}/images/bullet.png")
    self.rect = self.image.get_rect() #set a rect (doesn't draw anything)
    self.rect.midtop= ai_game.player.rect.midtop #go to player
    self.y = float(self.rect.y)
  
  def update(self): #make the bullet go upwards
    self.y -= self.settings.bullet_speed
    self.rect.y = self.y

  def bullet(self): #draw the bullet
    self.screen.blit(self.image,self.rect)
