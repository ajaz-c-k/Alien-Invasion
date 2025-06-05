import pygame

class Ship:

    def __init__(self,ai_game):
        """Initialise the Ship and its strating position"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        #start each new ship at the centre of screen
        self.rect.midbottom=self.screen_rect.midbottom

        #Movement flag
        self.moving_right=False

    def update(self):
        """Update the ship's position based on the movemnet flag."""
        if self.moving_right:
            self.rect.x+=1

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)