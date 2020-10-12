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
    self.bg_color = (104,207,248)
    #ship settings
    self.speed = 3.0
    #bullet settings
    self.bullet_speed = 5.0
    self.bullet_width = 15
    self.bullet_height = 10
    self.bullet_color = (76,106,23)
    self.most_bullets = 3
    #alien settings
    #normal alien settings
    self.alien_speed = 2.5
    self.drop_speed = 3
    self.direction = 1 #1 represents right, 2 represents left
    #blue alien settings
    self.blue_alien_speed = 3.0 #not added
    #sound settings
    self.sound_on = True
    self.volume = 0.6