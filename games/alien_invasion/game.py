'''the main file, which does everything'''
import sys
import pathlib
import time
import pygame
import random
from time import sleep
#import all the other files 
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien , blueAlien
from wall import Wall
class Game:
  def __init__(self):
    #make the screen
    pygame.init()
    self.settings=Settings()
    self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    self.settings.width = self.screen.get_rect().width
    self.settings.height = self.screen.get_rect().height
    pygame.display.set_caption('Aliens!')
    #create the other sprites' instances
    #also add groups of sprites
    self.player = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens= pygame.sprite.Group()
    self.walls = pygame.sprite.Group()
    self.create_aliens()
    self.make_walls()
    #define a sound
    if self.settings.sound_on:
      path = pathlib.Path(__file__).parent.absolute()
      self.shoot = pygame.mixer.Sound(str(path) + '/shoot.ogg')
      self.shoot.set_volume(0.3)
      self.explode = pygame.mixer.Sound(str(path) + '/explosion.ogg')
      self.explode.set_volume(0.45)
    #set some variables
    self.score=0
    

  def run(self):
    '''mainloop'''
    #run the game 
    while True:
      self.check()
      
      self.player.update()
      self.update_bullets()
      self.update_aliens()
      #check if bullets are touching the top of the screen
      for bullet in self.bullets.copy():
        if bullet.rect.top <= 0:
          time.sleep(0.05)
          self.bullets.remove(bullet)
      self.update_screen()

  def keydown(self, event):
    #check when a key is down
    if event.key == pygame.K_RIGHT:
      self.player.right=True
    if event.key == pygame.K_LEFT:
      self.player.left=True
    elif event.key == pygame.K_q or event.key == pygame.K_w:
      raise SystemError
    elif event.key == pygame.K_SPACE:
      self.fire_bullet()

  def keyup(self, event):
    #check when a key is up
    if event.key == pygame.K_RIGHT:
      self.player.right = False
    if event.key == pygame.K_LEFT:
      self.player.left = False
  
  def fire_bullet(self):
    '''fire a bullet'''
    if len(self.bullets) < self.settings.most_bullets: #check if the number of bullets is less than the limit
      #add a bullet
      if self.settings.sound_on:
        self.shoot.play()
      new_bullet= Bullet(self)
      self.bullets.add(new_bullet)

  def check(self):
    '''check keys'''
    for event in pygame.event.get():
      #check if the window's red button is pressed
      if event.type == pygame.QUIT:
        raise SystemError
      #check keydown events
      elif event.type == pygame.KEYDOWN:
        self.keydown(event)
       #check keyup events
      elif event.type == pygame.KEYUP:
        self.keyup(event)
    if len(self.walls ) == 0:
      print('you lose!')
      raise SystemError
  
  def update_screen(self):
    #change the screen so characters move
    self.screen.fill(self.settings.bg_color)
    self.player.show()
    for bullet in self.bullets.sprites():
      bullet.bullet()
    self.aliens.draw(self.screen)
    self.draw_walls()
    #show the screen
    pygame.display.flip()
  
  def update_bullets(self):
    self.bullets.update() #make all the bullets update
    number_aliens = len(self.aliens)# get the number of aliens
    for bullet in self.bullets.sprites():
      # make bulllets who collide with aliens disappear
      alien = pygame.sprite.spritecollideany(bullet,self.aliens)
      if alien is not None:
        self.aliens.remove(alien)
        self.explode.play()
        self.bullets.remove(bullet)
        break
      wall = pygame.sprite.spritecollideany(bullet,self.walls)
      if wall is not None:
        self.walls.remove(wall)
        self.bullets.remove(bullet)
        break
    number_aliens2 = len(self.aliens)# get the number of aliens after some are destroyed by bullets
    if number_aliens2 < number_aliens: # if a alien is destroyed,change the score
      self.score += number_aliens - number_aliens2
      print(self.score)

  def create_aliens(self):
    '''make all the aliens'''
    alien1 = Alien(self)
    alien_width, alien_height = alien1.rect.size
    available_width_x = self.settings.width - (2 * alien_width)
    number_aliens_x = available_width_x // (2 * alien_width)

    ship_height = self.player.rect.height
    available_width_y = (self.settings.height - (3 * alien_height) - ship_height)
    number_rows = available_width_y // (2 * alien_height)
    for rowNumber in range(number_rows):
      for alienNumber in range(number_aliens_x):
        self.make_alien(alienNumber,rowNumber)
      
  def make_alien(self,alien_Number,row_number):
    '''make a single alien'''
    alien = Alien(self)
    alien_width,alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * alien_Number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    self.aliens.add(alien)

  def update_aliens(self):
    '''make all the aliens move'''
    self.aliens.update()

    self.check_fleet_edges()
    for a in self.aliens:
      wall = pygame.sprite.spritecollideany(a,self.walls)
      if wall is not None:
        self.walls.remove(wall)
        choice = (0,1)
        random.choice(choice)
        if choice == 1:
          self.aliens.remove(a)  
  def check_fleet_edges(self):
    '''see if the aliens have touched the edge'''
    for alien in self.aliens.sprites():
      if alien.check_edges():
        self.change_direction()
        break

  def change_direction(self):
    '''change the direction of the fleet'''
    for alien in self.aliens.sprites():
      alien.rect.y += self.settings.drop_speed
    self.settings.direction *= -1

  def draw_walls(self):
    for w in self.walls.sprites():
      w.update()

  def make_walls(self):
    self.test_wall = Wall(self,0)
    avail_width_x = self.settings.width - self.test_wall.wall_width
    number_walls_x = avail_width_x // self.test_wall.wall_width
    for x in range(number_walls_x):
      self.make_wall(x)

  def make_wall(self,X):
    x = (self.test_wall.wall_width + 2 * X)
    wall = Wall(self,x)
    self.walls.add(wall)



  
if __name__ =='__main__':
  ai=Game() #initialize
  ai.run() #run
