import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
     """Overall class to manage game assets and behavior."""
     def __init__(self):
          """Initialize the game, and create game resources."""
          pygame.init()
          self.settings = Settings()
          self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
          self.settings.screen_width=self.screen.get_rect().width
          self.settings.screen_height=self.screen.get_rect().height
          
          pygame.display.set_caption("Alien Invasion")
          self.ship = Ship(self)
          self.bullets=pygame.sprite.Group()
          self.aliens=pygame.sprite.Group()

          self._create_fleet()

     def run_game(self):
          """Start the main loop for the game."""
          while True:
               self._check_events()
               self._update_bullets()
               self.ship.update()
               self._update_screen()

     def _check_events(self):
          """Respond to key presses and mouse events."""
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    sys.exit()
               elif event.type==pygame.KEYDOWN:
                    self._check_keydown_events(event)
               elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

               
     

     def _check_keydown_events(self,event):
          """Responds to key presses"""
          if event.key==pygame.K_RIGHT:
               self.ship.moving_right=True
          elif event.key==pygame.K_LEFT:
               self.ship.moving_left=True
          elif event.key==pygame.K_q:
               sys.exit()
          elif event.key==pygame.K_SPACE:
               self._fire_bullet()
                    

     def _check_keyup_events(self,event):
          """Responds to key releases"""
          if event.key==pygame.K_RIGHT:
               self.ship.moving_right=False
          elif event.key==pygame.K_LEFT:
               self.ship.moving_left=False
          
          elif event.key==pygame.K_q:
               sys.exit()
          
     
     def _fire_bullet(self):
          """create a new bullet and add it in bullet group"""
          if len(self.bullets)<self.settings.bullets_allowed:
               new_bullet=Bullet(self)
               self.bullets.add(new_bullet)


     def _create_fleet(self):
          """create the fleet of aliens"""
          #make an alien

          alien=Alien(self)
          self.aliens.add(alien)
     
     def _update_bullets(self):
          """update position of bullets and get rid of old bullets"""
          #update bullet position
          self.bullets.update()

          #get rid of bullets that have been disappered.
          for bullet in self.bullets.copy():
               if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)

                    
     def _update_screen(self):
          """Update the images on the screen and flip to the new screen."""
          self.screen.fill(self.settings.bg_color)
          self.ship.blitme()
          for bullet in self.bullets.sprites():
               bullet.draw_bullet()
          self.aliens.draw(self.screen)
          pygame.display.flip()
     

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
