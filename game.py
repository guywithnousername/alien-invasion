import sys

import pygame

class game:
  def __init__(self):
    pygame.init()

    self.screen=pygame.displayset_mode((1200,800))
    pygame.display.set_caption('Aliens!')

  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type() == pygame.QUIT:
          sys.exit()
      pygame.display.flip()
if __name__ =='__main__':
  ai=game()
  ai.run_game()
