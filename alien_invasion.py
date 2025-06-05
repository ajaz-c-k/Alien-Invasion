import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
     """Overall class to manage game assets and behavior."""
     def __init__(self):
          """Initialize the game, and create game resources."""
          pygame.init()
          self.settings = Settings()
          self.screen = pygame.display.set_mode(
               (self.settings.screen_width, self.settings.screen_height)
          )
          pygame.display.set_caption("Alien Invasion")
          self.ship = Ship(self)

     def run_game(self):
          """Start the main loop for the game."""
          while True:
               self._check_events()
               self._update_screen()
               self.ship.update()

     def _check_events(self):
          """Respond to key presses and mouse events."""
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    sys.exit()
               elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                         self.ship.moving_right=True
               elif event.type==pygame.KEYUP:
                    if event.key==pygame.K_RIGHT:
                         self.ship.moving_right=False

     def _update_screen(self):
          """Update the images on the screen and flip to the new screen."""
          self.screen.fill(self.settings.bg_color)
          self.ship.blitme()
          pygame.display.flip()
     

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
