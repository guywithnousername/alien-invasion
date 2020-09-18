import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
class Game:
  def __init__(self):
    pygame.init()
    self.settings=Settings()
    self.screen=pygame.display.set_mode((self.settings.width,self.settings.height))
    pygame.display.set_caption('Aliens!')
    self.player = Ship(self)
    self.bullets = pygame.sprite.Group()

  def run(self):
    while True:
      self.check()
      self.update_screen()
      self.player.update()
      self.bullets.update()

  def keydown(self, event):
    if event.key == pygame.K_RIGHT:
      self.player.right=True
    if event.key == pygame.K_LEFT:
      self.player.left=True
    elif event.key == pygame.K_q:
      exit()
    elif event.key == pygame.K_SPACE:
      self.fire_bullet()

  def keyup(self, event):
    if event.key == pygame.K_RIGHT:
      self.player.right = False
    if event.key == pygame.K_LEFT:
      self.player.left = False
  
  def fire_bullet(self):
    new_bullet= Bullet(self)
    self.bullets.add(new_bullet)

  def check(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      elif event.type == pygame.KEYDOWN:
        self.keydown(event)
      elif event.type == pygame.KEYUP:
        self.keyup(event)
  
  def update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.player.show()
    for bullet in self.bullets.sprites():
      bullet.bullet()
    pygame.display.flip()
  

if __name__ =='__main__':
  ai=Game()
  ai.run()