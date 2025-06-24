import pygame

class Ship:

    def __init__(self,ai_game):
        """Initialise the Ship and its strating position"""
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        #store the decimal value of ship in the horizontal position
        self.x=float(self.rect.x)

        #start each new ship at the centre of screen
        self.rect.midbottom=self.screen_rect.midbottom

        #Movement flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """Update the ship's position based on the movemnet flag."""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        
        self.rect.x=self.x

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)