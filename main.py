import pygame
import os


class ball(object):
    def __init__(self):
        """ The constructor of the class """
        pygame.sprite.Sprite.__init__(self)

        ball.image = pygame.image.load("PinHeadLarry.png")
        
        self.image = pygame.transform.scale(self.image,(50,50))

        self.x = 20
        self.y = 30
        self.x_velocity = 1
        self.y_velocity = 1
        
    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image, (self.x, self.y))

    def bounce(self,screen_width,screen_height, collider):
        self.x += self.x_velocity
        self.y += self.y_velocity

        #IF ball reaches Top
        if(self.y <= 0):
          self.y_velocity = 2 
        #IF ball reaches Bottom
        if(self.y >= screen_height-50):
          self.y_velocity = -2
        #IF ball reaches Right
        if(self.x >= screen_width-50 or collider):
          self.x_velocity = -3
        #If ball reaches Left
        if( self.x <= 0):
          self.x_velocity = 3

class paddle(object):
    def __init__(self):
        """ The constructor of the class """
        pygame.sprite.Sprite.__init__(self)

        paddle.image = pygame.image.load("PinHeadLarry.png")
        
        self.image = pygame.transform.scale(self.image,(20,100))

        self.x = 700
        self.y = 30
        
    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image, (700, self.y))
    def move(self):
      pos = pygame.mouse.get_pos()

      #self.x = pos[0]
      self.y= pos[1]

    def hit(self, obj): #Returns True of False depending if fully triggered. 

      if(obj.x+25 >= self.x and obj.x+25 <= self.x+20 ):

        if(obj.y+25 >= self.y and obj.y+25 <= self.y+100):

          print("True")
          return True
        else:
          return False
      else:
        return False



pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

Patty = ball()
Paddle = paddle()
clock = pygame.time.Clock()

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    screen.fill((255,255,255))
    Patty.draw(screen)
    Paddle.draw(screen)
    Paddle.move()
    Patty.bounce(screen_width,screen_height,Paddle.hit(Patty))
    pygame.display.update() # update the screen

    clock.tick(60)