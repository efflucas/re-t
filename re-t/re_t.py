import pygame
import sys
from pygame.locals import *

pygame.init() # initialize pygame

# window size

DISP_WIDTH = 400 # 400 pixels
DISP_HEIGHT = 300 # 300 pixels

# load window icon into variable called WINDOW_ICON
WINDOW_ICON = pygame.image.load("test.png")

# create vaiable for window title called WINDOW_TEXT
WINDOW_TEXT = 'Test Software'


DISPLAYSURF = pygame.display.set_mode((DISP_WIDTH, DISP_HEIGHT)) # applies display width and height to variable called DISPLAYSURF
pygame.display.set_caption(WINDOW_TEXT) # applies the text "Test Software" to the window title
pygame.display.set_icon(WINDOW_ICON) # applies test.png as icon in the window title

# color codes

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

class Bubblegum(): # pygame.sprite.Sprite enables the use of pygame-based collision. Enables class to use pygame.spirte.Sprite function
    

    # def __init__ code. applies default values to be used unless stated otherwise
    def __init__(self, image = "test.png", x = DISP_WIDTH / 2, y = DISP_HEIGHT / 2, xspeed = 1, yspeed = 1, direction = 'right'):

        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (15, 15)) # pygame.image.load needs to be used to be able to just use 'image' as variable, scale is used for collision later. 15 is used since sprite is 15x15 pixels
        self.rect = self.image.get_rect() # defines a rectangle on the image (hitbox)
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.direction = direction

        




    def stop_move(self): # code for stopping the sprite from going outside the window when using keyboard controlls

        if self.x > DISP_WIDTH - 15: # 15 is used since image is 15x15 pixels
            self.x -= 1 # move sprite 1 pixels to the left

        elif self.x < 0:
            self.x += 1

        elif self.y > DISP_HEIGHT - 15:
            self.y -= 1

        elif self.y < 0:
            self.y += 1

        


    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect) # code to draw on screen. for this we onyl need the image, x and y coordinates. self.x and self.y has to be sperate

    def collision(self): # collision code
        if self.rect.colliderect(bubblegum2.rect): # checks if bubblegum (1) collides with bubblegum2
            print("Collision")



class Bubblegum2():
    

    # def __init__ code. applies default values to be used unless stated otherwise
    def __init__(self, image = "test2.png", x = DISP_WIDTH / 2, y = DISP_HEIGHT / 2, xspeed = 1, yspeed = 1, direction = 'right'):
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (15, 15)) # pygame.image.load needs to be used to be able to just use 'image' as variable
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.direction = direction
        
        




    def stop_move(self): # code for stopping the sprite from going outside the window when using keyboard controlls

        if self.x > DISP_WIDTH - 15: # 15 is used since image is 15x15 pixels
            self.x -= 1 # move sprite 1 pixels to the left

        elif self.x < 0:
            self.x += 1

        elif self.y > DISP_HEIGHT - 15:
            self.y -= 1

        elif self.y < 0:
            self.y += 1



    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect) # code to draw on screen. for this we onyl need the image, x and y coordinates. self.x and self.y has to be sperated

    def collision(self): # has to be here since an object list is used later on.
        pass 



# append object on screen (aka spawn it)

bubblegum = Bubblegum(xspeed = 0.125, yspeed = 0.125) # if the () has nothing in it the default values will be used
bubblegum2 = Bubblegum2(xspeed = 0.125, yspeed = 0.125) # if the () has nothing in it the default values will be used


# makes a list of objects
objects = []
objects.append(bubblegum) # adds bubblegum to list called objects
objects.append(bubblegum2) # adds bubblegum2 to list called objects


pygame.key.set_repeat(1, 25) # enables pygame to check for multime keypresses. 1 = enabled, other value = interval between

# main pygame loop
while True:

    DISPLAYSURF.fill(WHITE)



    
    for o in objects: # evvery class in the objects list will be applied here.
        o.draw()
        o.stop_move()
        o.collision() # currently only in bubblegum (1) calss
   



    # pygame event code
    for event in pygame.event.get(): # event.get will look for any type of input (not limtied to keyboard)

        # quit code
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # code for keyboard checking
        if event.type == pygame.KEYDOWN:

            # move code for player 1
            # left code
            if event.key == pygame.K_LEFT:
                bubblegum.rect.centerx -= 1 # if left key is pressed remove 1 from bubblegum x var
                print('K_LEFT  :   bubblegum.x = {0}     bubblegum.y = {1}'.format(bubblegum.x, bubblegum.y))
                
            elif event.key == pygame.K_UP:
                bubblegum.rect.centery -= 1 # if up key is pressed remove 1 from bublegum y var
                print('K_UP    :   bubblegum.x = {0}     bubblegum.y = {1}'.format(bubblegum.x, bubblegum.y))
                
                    
            elif event.key == pygame.K_DOWN:
                bubblegum.rect.centery += 1 # if down key is pressed add 1 to bubblegum y var
                print('K_DOWN  :   bubblegum.x = {0}     bubblegum.y = {1}'.format(bubblegum.x, bubblegum.y))

            elif event.key == pygame.K_RIGHT:
                bubblegum.rect.centerx += 1 # if right key is pressed add 1 to bubblegum x var
                print('K_RIGHT :   bubblegum.x = {0}     bubblegum.y = {1}'.format(bubblegum.x, bubblegum.y))



            # code for moving faster
            if event.key == pygame.K_j:
                bubblegum.rect.centerx -= 5 # if left key is pressed remove 5 from bubblegum x var
                print('K_j     :   bubblegum.x = {0}     bubblegum.y = {1}'.format(bubblegum.x, bubblegum.y))
                
            elif event.key == pygame.K_i:
                bubblegum.rect.centery -= 5 # if up key is pressed remove 5 from bublegum y var
                print('K_i     :   bubblegum.x = {0}     bubblegum.y = {1}'.format(bubblegum.x, bubblegum.y))
                
                    
            elif event.key == pygame.K_k:
                bubblegum.rect.centery += 5 # if down key is pressed add 5 to bubblegum y var
                print('K_k     :   bubblegum.x = {0}     bubblegum.y = {1}'.format(bubblegum.x, bubblegum.y))

            elif event.key == pygame.K_l:
                bubblegum.rect.centerx += 5 # if right key is pressed add 5 to bubblegum x var
                print('K_l     :   bubblegum.x = {0}     bubblegum.y = {1}'.format(bubblegum.x, bubblegum.y))










            # move code for player 2
            # left code
            if event.key == pygame.K_a:
                bubblegum2.rect.centerx -= 1 # if left key is pressed remove 1 from bubblegum x var
                print('K_a     :   bubblegum2.x = {0}     bubblegum2.y = {1}'.format(bubblegum2.x, bubblegum2.y))
                
            elif event.key == pygame.K_w:
                bubblegum2.rect.centery -= 1 # if up key is pressed remove 1 from bublegum y var
                print('K_w     :   bubblegum2.x = {0}     bubblegum2.y = {1}'.format(bubblegum2.x, bubblegum2.y))
                
                    
            elif event.key == pygame.K_s:
                bubblegum2.rect.centery += 1 # if down key is pressed add 1 to bubblegum y var
                print('K_s     :   bubblegum2.x = {0}     bubblegum2.y = {1}'.format(bubblegum2.x, bubblegum2.y))

            elif event.key == pygame.K_d:
                bubblegum2.rect.centerx += 1 # if right key is pressed add 1 to bubblegum x var
                print('K_d     :   bubblegum2.x = {0}     bubblegum2.y = {1}'.format(bubblegum2.x, bubblegum2.y))



            # code for quitting
            if event.key == pygame.K_x:
                pygame.quit()
                sys.exit()
            



        



    # update display
    pygame.display.update()



