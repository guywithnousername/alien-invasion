'''the file which stores all the settings for the game'''
import random
class Settings:
  """
  the class where the settings are
  """
  def __init__(self):
    #screen settings
    self.width=1075
    self.height=700
    self.actualw=1000
    self.actualh=700
    self.bg_color = (0,12,24)
    #ship settings
    self.speed = 3.0
    #bullet settings
    self.bullet_speed = 5.0
    self.most_bullets = 3
    #alien settings
    #normal alien settings
    self.alien_speed = 2.5
    self.drop_speed = 3.1
    self.most_lives = 1
    self.direction = 1 #1 represents right, 2 represents left
    #blue alien settings
    self.blue_alien_speed = 3.0 #not added
    #sound settings
    self.sound_on = True
    self.volume = 0.6
  def increment(self):
    self.most_lives += 1