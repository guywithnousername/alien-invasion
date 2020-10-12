import pygame

class Score:
    """
    class for showing the score
    """
    def __init__(self,aigame,msg):
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.text = self.font.render(msg,True,(0,255,0),None)
        self.rect = self.text.get_rect()
        self.rect.center = 1583,60

    def show(self,msg):
        self.text = self.font.render(msg,True,(0,255,0),None)
        self.screen.blit(self.text,self.rect)