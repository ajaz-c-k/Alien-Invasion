import pygame
from pygame.sprite import Sprite

class Ship(Sprite):   # ✅ Fix: inherit from Sprite
    def __init__(self, ai_game):
        """Initialise the Ship and its starting position."""
        super().__init__()  # ✅ Correctly call Sprite initializer
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Store the decimal value of ship in the horizontal position
        self.x = float(self.rect.x)

        # Start each new ship at the center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
