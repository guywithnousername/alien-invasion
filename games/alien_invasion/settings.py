'''the file which stores all the settings for the game'''
import random
class Settings:
  def __init__(self):
    #screen settings
    self.width=1000
    self.height=700
    self.bg_color = (25,25,25)
    #ship settings
    self.speed = 3.0
    #bullet settings
    self.bullet_speed = 5.0
    self.bullet_width = 15
    self.bullet_height = 10
    self.bullet_color = (0, 255, 242)
    self.most_bullets = 3
    #alien settings
    #yellow alien settings
    self.alien_speed = 1.5
    self.drop_speed = 1
    self.direction = 1 #1 represents right, 2 represents left
    #blue alien settings
    self.blue_alien_speed = 3.0
