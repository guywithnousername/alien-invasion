import sys
import time
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class Game:
  def __init__(self):
    pygame.init()
    self.settings=Settings()
    self.screen=pygame.display.set_mode((self.settings.width,self.settings.height))
    pygame.display.set_caption('Aliens!')
    self.player = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens= pygame.sprite.Group()

    self.create_aliens()

  def run(self):
    while True:
      self.check()
      self.update_screen()
      self.player.update()
      self.update_bullets()

      for bullet in self.bullets.copy():
        if bullet.rect.top <= 0:
          time.sleep(0.05)
          self.bullets.remove(bullet)

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
    if len(self.bullets) < self.settings.most_bullets:
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
    self.aliens.draw(self.screen)
  
  def update_bullets(self):
    self.bullets.update()

  def create_aliens(self):
    alien = Alien(self)
    self.aliens.add(alien)
if __name__ =='__main__':
  ai=Game()
  ai.run()