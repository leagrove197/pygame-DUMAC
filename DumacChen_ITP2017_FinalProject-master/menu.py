from pygame import *    #import  the pygame with *
import sys              #import sys so you can quit the game
import pygame           #import pygame because we are making pygame...

def menu_screen(Button,run_game):       #define menu_screen and inherit the Button class and run_game to this menu_screen
    #make the screen for menu
    display.set_caption("SPACE COW")        #display the title for the game in the main menu
    screen = pygame.display.set_mode((800, 600))        #set the resolution width and height for the game
    #object button for quit and start
    start_button = Button("start button.png")     #summon the start button picture and consider it as the start_button
    quit_button = Button("quit button.png")     #summon the quic button picture and consider it as the quit_button
    #image for the menu's backgound
    bg_image=pygame.image.load("asteroid_wall.jpg")     #summon the asteroid_wall picture and consider it as the bg_image or background for the main menu
    bg_image=pygame.transform.scale(bg_image, (800, 600))   #set the resolution for the background the same as the game resolution so it fits perfectlyyyy


    pygame.init()       #initialized all imported pygame modules

    while True:         #make a while loop for the main menu
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #make rect_start variable which is  a draw.rect black colored and set the size
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))  #make rect_quit variable which is  a draw.rect black colored and set the size
        screen.blit(bg_image,(0,0)) #call the background image 0,0

        screen.blit(start_button.button,(250,200))  #call the start button image to the screen and set the size 250,200
        screen.blit(quit_button.button,(250,300))   #call the quit button image to the screen and set the size to 250,300

        ev=event.wait()     #pause the program for an amount of time and consider it as ev variable

        if ev.type == MOUSEBUTTONDOWN: #make loop for clicking the mouse button
            if rect_start.collidepoint(mouse.get_pos()):    #if you click on the start button,
                run_game()                                      #it call the run_game, the program will run the game so you can play
            if rect_quit.collidepoint(mouse.get_pos()):     #if you click on the quit button.
                sys.exit()                                         #the pygame will be closed

        if ev.type == QUIT:         #if you click the quit which is the redbutton on top left (if you use macbook)
            sys.exit()                  #the pygame will be closed

        display.update()        #then the display will be update by the button that you choose

def pause_menu(Button,run_game):    #define the pause menu and inherit the Button class and run_game so you can continue playing in the pause menu
    #pause_menu
    #make the screen display
    display.set_caption("SPACE COW")    #make the title even in the pause menu
    screen = pygame.display.set_mode((800, 600))    #pause menu resolution is 800, 600. the same as before

    # object button for quit and start
    start_button = Button("quit button.png")    #summon the quit button image an consider it as the start_button
    return_button = Button("pause button.png")  #summon the pause button image and consider it as the return_button

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")   #summon the asteroid_wall image and consider is as the bg_image
    bg_image = pygame.transform.scale(bg_image, (800, 600)) #make the resolotion fits for the pause menu game. the same as the main menu


    pygame.init()           #initialize all imported pygame modules
    paused=True #pause True so it pause the game
    while paused:   #make a loop while the game is paused
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #make rect_start variable which is  a draw.rect black colored and set the position
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))    #make rect_return variable which is  a draw.rect black colored and set the position
        screen.blit(bg_image, (0, 0))   #call the background image 0,0

        screen.blit(start_button.button, (250, 200))    #call the start button image to the screen and set the size 250,200
        screen.blit(return_button.button, (250, 300))   #call the return button image to the screen and set the size 250,300

        ev = event.wait()               #pause the program for an amount of time and consider it as ev variable

        if ev.type == MOUSEBUTTONDOWN:      #make loop for clicking the mouse button
            if rect_start.collidepoint(mouse.get_pos()):     #if you click on the rect_start which is a quit button image,
                menu_screen(Button,run_game)                     #will go to main menu screen and summon the button class and run_game so you can play again
            if rect_return.collidepoint(mouse.get_pos()):   #if you click the rect_return which is a return button image,
                paused = False                              #it will break the pause by turning the True into False

        if ev.type == QUIT:         #if you quit the game it will close the program
            sys.exit()


        display.update()    #update the display

def lose_menu(Button,run_game,score): #define the lose_menu, everytime you lose, the program will go to this lose menu and call the Button class, run_game so you can play again, and score so you can see your score when you lose
    #make the screen for menu
    display.set_caption("SPACE COW")    #title
    screen = pygame.display.set_mode((800, 600))    #set the display resolution
    font=pygame.font.SysFont("",130) #put a text in 130 fontsize
    text=font.render("YOU DIED",True,(255,0,0))  #put YOU DIED text in red color
    font2=pygame.font.SysFont("",50)
    text2=font2.render("Try Again?",True,(90,255,90))
    score_text=font2.render("score:"+str(score),True,(90,255,90))  #put the score in white color + your total score in the lose menu

    # object button for quit and start
    start_button = Button("start button.png")   #summon the start button image and consider it as start_button
    quit_button = Button("quit button.png")     #summon the quit button image and consider it as quit_button

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")       #summon the background image
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    pygame.init()   #initialized all imported modules

    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #make rect_start variable which is  a draw.rect black colored and set the position
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))  #make rect_quit variable which is  a draw.rect black colored and set the position
        screen.blit(bg_image, (0, 0))       #call the background image 0,0
        screen.blit(text,(200,10))              #call the text "YOU DIED" in 200,10 position x y
        screen.blit(start_button.button, (250, 200))    #call the start button image in 250, 200 position x y
        screen.blit(quit_button.button, (250, 300))     #call the quit button image in 250, 300 position x y
        screen.blit(score_text,(200,400))               #call the score text in 200, 400 position x y
        screen.blit(text2,(330,100))

        ev = event.wait()       #pause the program for an amount of time and consider it as ev variable

        if ev.type == MOUSEBUTTONDOWN:  #if you click the mouse
            if rect_start.collidepoint(mouse.get_pos()):    #if you click the start button, then you play again
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()): #if you click the quit button, then you exit the game
                sys.exit()

        if ev.type == QUIT:     #same as before
            sys.exit()

        display.update()    #display update
