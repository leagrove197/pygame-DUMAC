from pygame import *       #import the pygame with *
from pygame.sprite import * #import the sprite also

class Cow(Sprite):      #create class Cow and inherit the Sprite inside the Cow
    #initialize the Cow

    def __init__(self, screen): #define initialize  and put the screen inside
        Sprite.__init__(self)
        #initialize the Cow
        self.image = image.load("cooow.png")    #load the Cow image
        self.image = pygame.transform.scale(self.image, (140, 100))   #set the size of the cow image
        self.rect = self.image.get_rect()   #get rectangle for the image
        self.rect.x = 10    #rect x = 10
        self.rect.y = 50    #rect y = 50
        self.screen = screen    #initiate screen
        self.move_speed = 20    #set the movement for the cow
        #bullet
        self.firerates = 2  #set the bullet attack speed

    def moveleft(self):             #define moveleft
        self.rect.x -= self.move_speed  #setting so the cow can move to the left
        display.flip()

    def moveright(self):
        self.rect.x += self.move_speed  #setting so the cow can move to the right
        display.flip()

    def moveup(self):
        self.rect.y -= self.move_speed  #setting so the cow can move to the top
        display.flip()

    def movedown(self):
        self.rect.y += self.move_speed  #setting so the cow can move to the bottom
        display.flip()





class Star_bg:  #create Star_bg class for the background while playing the game
    #resourse of the backgound setting
    def __init__(self,background):          #define initialize and put the background inside
        self.background=image.load(background)  #to load the background image
        self.background=pygame.transform.scale(self.background,(800,600))   #to set the size of the background so it fits perfectly with the game resolution
        self.background_size=self.background.get_size() #get the background size
        self.background_rect=self.background.get_rect() #get the background rectangle
        self.width,self.height=self.background_size #the width and height will follows the size of the background
    def draw(self,screen,x,y):      #define draw and put screen, x , y inside
        screen.blit(self.background,(x,y))  #call the background picture so it will appear in the game

class Bullet(Sprite):   #create a Bullet class and inherit the Sprite
    def __init__(self,screen, startx, starty):  #define initialize and put the screen, startx, starty
        Sprite. __init__(self)      #super class Sprite
        self.startx = startx       #initiate startx
        self.starty = starty        #initiate starty

        self.speedx = 20            #speed of the background in x to move, x is horizontal

        self.image = pygame.image.load("bullets.png")   #load the bullets image
        self.image = pygame.transform.scale(self.image,(100,100)) #set the size of the bullet image
        self.rect=self.image.get_rect() #get rectangle for the image
        self.rect.left = startx    #set the rect left = startx. x is horizontal
        self.rect.top = starty      #set the rect top = starty.  y is vertical
        self.rect.center = (startx,starty)  #set the rect center = (startx , starty) . so it will be at center
        self.screen = screen    #initiate screen
    def movement(self):
        # self.screen.blit(self.image,[self.startx,self.starty])
        self.rect.left += self.speedx   #to add the movement speed for the cow

class Asteroid(Sprite):     #create Asteroid class and inherit Sprite
    #initialize the Asteroid
    def __init__(self, screen, width, height, speedx, startx, starty):  #define initialize and put screen, width, height, speedx, startx, starty inside
        Sprite.__init__(self)   #super class initiate
        self.startx = startx    #initiate startx
        self.starty = starty    #initiate starty

        self.speedx = speedx    #set the speed for the asteroid, we set it like that because the movement speed of the asteroid is different from each other

        self.image = pygame.image.load("meteor.png")    #load the meteor image
        self.image = pygame.transform.scale(self.image, (width, height))    #set the size of the image
        self.rect = self.image.get_rect()       #get rectangle for the image
        self.rect.left = startx         #set the rect left = startx
        self.rect.top = starty          #set the rect top = starty
        self.screen = screen            #initiate screen

    def movement(self):     #define movement
        #method to move the Asteoid
        self.rect.left -= self.speedx   #set the movement for the asteorid, we use - because the asteroid goes to the left in x


class Button(Sprite):           #create Button class and inherit Sprite
    #initialize the button
    def __init__(self,image):   #define initialize and put image
        Sprite. __init__(self)      #super intialize sprite
        self.button=pygame.image.load(image)    #load the button image
        self.button=pygame.transform.scale(self.button,(300,150))   #set the size for all of the button that we want to click to Return, Start, and Quit
