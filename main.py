import pygame
import os


class ball(object):
    def __init__(self):
        """ The constructor of the class """
        pygame.sprite.Sprite.__init__(self)

        ball.image = pygame.image.load("")
        
        self.image = pygame.transform.scale(self.image,(50,50))

        self.x = 20
        self.y = 30
        self.x_velocity = 1
        self.y_velocity = 1
        
    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image, (self.x, self.y))

    

class paddle(object):
    def __init__(self):
        """ The constructor of the class """
        pygame.sprite.Sprite.__init__(self)

        paddle.image = pygame.image.load("")
        
        self.image = pygame.transform.scale(self.image,(20,100))

        self.x = 700
        self.y = 30
        
    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image, (700, self.y))
   



pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


clock = pygame.time.Clock()

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    screen.fill((255,255,255))
    
    pygame.display.update() # update the screen

    clock.tick(60)