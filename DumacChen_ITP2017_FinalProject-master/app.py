import menu     #first import menu
import random    #import random to and we can do what we want with random such as random.randint or .sleep

from classes import *   #we import the classes file to this file with *


#I editted for the title,jet, and text when you lose and add comment for this dumacchen code

def run_game():             #define the run_game
    #game play interface
    screen = pygame.display.set_mode((800, 600))    #this is for the screen width and height
    display.set_caption("SPACE COW")                #set the title for the gam


    scores = 0                          #set the current score when you start the game which is Zero
    theClock = pygame.time.Clock()  #create an object to help track time
    bg_image = Star_bg("star.gif")          #to call the star picture into the game


    x = 0
    y = 0
    x1 = bg_image.width
    y1 = 0                              #make the coordinate of moving background

    pygame.init()                   #initialize all imported pygame modules



    cow1 = Cow(screen)
    Cow_sprites = Group(cow1)       #creating a jet


    asteroid_group = Group()        #create asteroid object group


    bullets = Group()               #create bullets object Group



    Fps = 120
    asteroid_timer = pygame.time.get_ticks()        #get the time in milliseconds for the asteroid_timer
    while True:                                     #make a while loop
        theClock.tick(Fps)                  #sets up how fast game should run or how often while loop should update itself, run through itself.
        Fps += 0.01         #game phase goes faster after every frame



        x -= 5
        x1 -= 5
        bg_image.draw(screen,x,y)
        bg_image.draw(screen,x1, y1)
        if x < -bg_image.width:
            x = 0
        if x1 < 0:                           #spawn the asteroid from the right
            x1 = bg_image.width


        font=pygame.font.SysFont("",36)     #input the score in 36fontsize
        score_board=font.render("score:"+str(scores),True,(255,255,255))    #to input the score inside the game in white color and add "score:" before it

        screen.blit(score_board,(10,550))           # update refered to the word's method



        Cow_sprites.draw(screen)            #put the space cow inside the screen game

        bullets.draw(screen)                #put the bullets inside the screen game

        asteroid_group.draw(screen)         #put the asteroid inside the screen game
        display.update()                #update cow  and screen view


        event.get()                 #summon and get the event from other file


        #moving the cow according to key pressed
        key = pygame.key.get_pressed()              #make key variable for what hotkey we will press while playing the game
        if key[K_LEFT] and cow1.rect.x>0:           #if you press left key, and the cow is not over the left screen which is x = 0 in the screen width, the cow will move to the left
            cow1.moveleft()

        if key[K_RIGHT] and cow1.rect.x<=550:       #if you press right key, and the cow is not over the right screen which is x = 700 in the screen width because the half of the cow picture is 100 width,
            cow1.moveright()                                # then the cow will move to the right

        if key[K_DOWN] and cow1.rect.y<=450:        #if you press down key, and the cow is not over the bottom screen which is y=500, the cow will move down
            cow1.movedown()

        if key[K_UP] and cow1.rect.y>0:             #if you press up key, and the cow is no over the top screen which is y = 0, the cow will move up
            cow1.moveup()

        if key[K_SPACE] and len(bullets) <= cow1.firerates+(scores/4000):   #if you press space and total of the bullet in game game is not bigger than the cow firerate + score/4000
            bullet = Bullet(screen, cow1.rect.x+150, cow1.rect.y+42)     #set the bullet spawn place when you press space
            bullets.add(bullet)                     #add the bullet spawn place to the bullets
            pygame.mixer.music.load("LaserBlast.wav")      #to add the sound everytime you shot the bullet
            pygame.mixer.music.play()                       #to play the sound

        if key[K_ESCAPE]:                           #if you press escape key, it will go to main menu screen and call the Button class and run_game so you can run the game again
            menu.menu_screen(Button,run_game)

        if key[K_p]:                            #if you press p key, it will go to pause menu screen and call the Button class and run_game so you can run the game again
            menu.pause_menu(Button,run_game)


        #generate asteroid randomly
        if pygame.time.get_ticks() - asteroid_timer >= 200: #if the millisecond time - the asteroid timer is bigger or equal to 200
            asteroid = Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20))    #make variable asteroid and set the spawn place which is random by using random.randint
            asteroid_group.add(asteroid)    #add the variable asteroid to the asteroid_group
            asteroid_timer = pygame.time.get_ticks()    #get the time in milliseconds for the asteroid_timer

        #update the movement of asteroid
        for asteroid in asteroid_group: #make asteroid loop in the asteroid_group
            asteroid.movement()         #movement for the asteroid
            if asteroid.rect.right <= 0:        #if the asteroid goes beyond the left screen
                asteroid_group.remove(asteroid) #the asteroid will be removed
            if groupcollide(Cow_sprites,asteroid_group,dokilla=True,dokillb=True):#collition check
                menu.lose_menu(Button,run_game,scores)  #if the asteroid touch your space cow, the game will go to the lose menu and call Button class, run_game to play again, and scores to reveal your score

        #update bullet movement on screen
        for bullet in bullets:      #make bullet loop in the bullets(variable from classes file)
            bullet.movement()       #movement for the bullet
            if bullet.rect.left > 800:  #if the bullet goes beyond the right screen, the bullet will be removed
                bullets.remove(bullet)
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):  #collition check
                scores += 100   #if the bullet touch the asteroid, your score will be up by 100

menu.menu_screen(Button,run_game)   #to run the game , go to main menu first so we call the Button class and run_game to play the game
