'''the file used to manage the aliens'''
import pathlib
import pygame as pg
from settings import Settings
import os
class Ship:
  def __init__(self,aigame):
    #set all of the variables for the ship
    path = pathlib.Path(__file__).parent.absolute()
    self.screen=aigame.screen
    self.screen_rect = aigame.screen.get_rect()
    self.image= pg.image.load(str(path) + '/images/rocketShip.bmp')
    self.rect=self.image.get_rect()
    self.rect.midbottom = self.screen_rect.midbottom
    self.left=False
    self.right=False
    self.sett = aigame.settings

  def show(self):
    #show the ship on the screen
    self.screen.blit(self.image,self.rect)
    
  def update(self):
    #check movement
    if self.right and self.rect.right < self.screen_rect.right:
      self.rect.x += int(self.sett.speed)
    if self.left and self.rect.left > 0:
      self.rect.x -= int(self.sett.speed)
      
   
