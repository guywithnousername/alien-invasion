import random
class Settings:
  def __init__(self):
    self.width=1000
    self.height=700
    self.bg_color = (25,25,25)
    self.speed = 3.0
    self.bullet_speed = 5.0
    self.bullet_width = 15
    self.bullet_height = 10
    self.bullet_color = (0, 255, 242)
    choices = (1,2,3)
    self.most_bullets = random.choice(choices)
    self.alien_speed = 1.5
    self.drop_speed = 1
    self.direction = 1 #1 represents right, 2 represents left
    self.bonus_speed = 3.0
    self.bonus_direction = -1 #1 represents right, 2 represents left