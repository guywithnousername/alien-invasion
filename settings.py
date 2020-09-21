import random
class Settings:
  def __init__(self):
    self.width=1000
    self.height=700
    self.bg_color = (230,230,230)
    self.speed = 3.0
    self.bullet_speed = 5.0
    self.bullet_width = 15
    self.bullet_height = 10
    self.bullet_color = (47, 255, 0)
    choices = (1,2,3)
    self.most_bullets = random.choice(choices)