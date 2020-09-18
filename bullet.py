import pygame
from pygame.sprite import Sprite

class Bullet(Sprite,game):
  super.__init__()
  self.screen = game.screen
  self.settings = ai_game.settings
  self.color = self.settings.bullet_color

  self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
  self.rect.midtop= game.ship.rect.midtop

  self.y = float(self.rect.y)