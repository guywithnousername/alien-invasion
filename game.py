import sys
from star import Star
import pygame
from settings import Settings
from ship import Ship
class game:
  def __init__(self):
    pygame.init()
    self.settings=Settings()
    self.screen=pygame.display.set_mode((self.settings.width,self.settings.height))
    pygame.display.set_caption('Aliens!')
    self.player = Ship(self)
    self.stars = pygame.sprite.Group()

  def run(self):
    while True:
      self.check()
      self.update_screen()
      self.player.update()
      self.stars.update()

  def keydown(self, event):
    if event.key == pygame.K_RIGHT:
      self.player.right=True
    if event.key == pygame.K_LEFT:
      self.player.left=True
    elif event.key == pygame.K_q:
      exit()

  def keyup(self, event):
    if event.key == pygame.K_RIGHT:
      self.player.right = False
    if event.key == pygame.K_LEFT:
      self.player.left = False

  def check(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit()
      elif event.type == pygame.KEYDOWN:
        self.keydown(event)
      elif event.type == pygame.KEYUP:
        self.keyup(event)
  def star(self):
    draw_star()
  

  def update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.player.show()
    pygame.display.flip() 
  
  

if __name__ =='__main__':
  ai=game()
  star()
  ai.run()
