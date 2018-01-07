import pygame
import time 
from random import *

'''
IMPORTANT
pygames.init() is always the first thing you do. No matter what, No exceptions.  
'''
pygame.init()

#colors
black = (0,0,0)
white = (255,255,255)
sunset = (253,72,47)
greenYellow = (184, 255, 0)
brightBlue = (47,228, 253)
orange = (255,113,0)
yellow = (255, 236, 0)
purple = (252, 67, 255)

colorChoices = [greenYellow,brightBlue, orange, yellow, purple]

surfaceWidth = 800
surfaceHeight = 500
roofOfWindow = 0

imageHeight = 128
imageWidth = 128

surface = pygame.display.set_mode((surfaceWidth,surfaceHeight)) #set_mode(resolution) 
pygame.display.set_caption('Flappy Pidgey') #Title on window
clock = pygame.time.Clock() #FPS tracker


'''
Make sure the asset is in the same folder as the script.
Otherwise, make sure you type the path to the asset.  
'''
img = pygame.image.load('pidgey.png')


#####Functions####
def score(count):
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Score: "+str(count),True, white)
    surface.blit(text, [0,0])

def block(x_block, y_block, block_width, block_height, gap,colorChoice):
    #(where do we draw it, what color do we want, what are the dimensions) 
    pygame.draw.rect(surface,colorChoice,[x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface,colorChoice,[x_block, y_block + block_height + gap, block_width, surfaceHeight])
    

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP,pygame.QUIT ]):
        if event.type is pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key
    return None

def makeTextObjs(text,font):
    textSurface = font.render(text, True,sunset) #asks for text and anti aliasing
    return textSurface, textSurface.get_rect() 
    
def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    largeText = pygame.font.Font('freesansbold.ttf',150)

    titleTextSurf,titleTextRect = makeTextObjs(text,largeText)
    titleTextRect.center = surfaceWidth/2, (surfaceHeight/2)
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf,typTextRect = makeTextObjs('Press f to try again',smallText)
    typTextRect.center = surfaceWidth/2, ((surfaceHeight/2)+100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1) #Will cease input so that if the user hit a key by accident the message will still show. 

    while replay_or_quit == None: #while replay or quit is nothing
        clock.tick()

    #while that replay or quit is alive the main function will never run
    #this is designed to be a restart function
    main() 
    
def gameOver():
    msgSurface('Kaboom')

def pidgey(x,y,image):
    surface.blit(img,(x,y))

def main():
    
    x=150 #where pidgey starts on x axis
    y=200  #where pidgey starts on y axis
    
    y_move = 0
    x_block = surfaceWidth
    y_block = 0

    blockColor = colorChoices[randrange(0,len(colorChoices))]
    
    block_width = 75
    block_height = randint(0,(surfaceHeight/2))
    gap = imageHeight * 3
    block_move = 10
    
    game_over = False #Boolean to infinitely loop the game

    current_score = 0

    while not game_over:
        for event in pygame.event.get():
             if event.type == pygame.QUIT: #usually QUIT means you exit the window
                 pygame.quit()
                 quit()
 
             if event.type == pygame.KEYDOWN: #down arrow key
                 if event.key == pygame.K_UP:
                     y_move = -7

             if event.type == pygame.KEYUP: #up arrow key
                 if event.key == pygame.K_UP:
                     y_move = 7

        y += y_move #y=y+y_move , this is the up and down movement of pidgey
         
        surface.fill(black) #repaints background to black
        pidgey(x,y,img) #repaints your character over the black bg
        score(current_score) #updates scoreboard
        block(x_block,y_block,block_width,block_height,gap,blockColor) #draws in the block
        x_block -= block_move #moves blocks

        if y > surfaceHeight- 40 or y < roofOfWindow: #zone where your character dies
            gameOver()

        if x_block < (-1*block_width): #if block moves off the screen
            x_block = surfaceWidth #resets block location to the right side of screen
            block_height = randint(0,(surfaceHeight/2))
            blockColor = colorChoices[randrange(0,len(colorChoices))]
            current_score += 1

        if x + imageWidth > x_block : #checks for collision
            if x < x_block+ block_width:
                #print("possibly inside the boundaries of x")
                if y < block_height:
                    #print("y crossover upper.")
                    if x - imageWidth < block_width + x_block:
                        #print("gameOver hit upper")
                        gameOver()
                        
        if x + imageWidth > x_block: #checks for collisions on the bottom block
            #print ('x crossover')
            if y + imageHeight > block_height + gap:
                #print ('Y crossover lower')
                if x < block_width + x_block:
                    #print('GameOver lower')
                    gameOver()
                    
        '''
        #For some reason this code doesn't work
        if x < x_block and x > x_block - block_move:
            print('score')
            current_score += 1
        '''    

        #Increasingn difficulty
        if 3 <= current_score < 5:
            block_move = 15
            gap = imageHeight *2.6

        if 5 <= current_score < 7:
            block_move = 20
            gap = imageHeight *2.3

        if 7 <= current_score <10:
            block_move = 25
            gap = imageHeight * 2

        if 10 <= current_score < 13:
            block_move = 30
            gap = imageHeight *1.6

        if 10 <= current_score < 15:
            block_move = 35
            gap = imageHeight *1.3

        if 17 < current_score:
            block_move = 35
            gap = imageHeight *1.3
                                           
        #.flip() will update the ENTIRE window (inefficient)
        #.update() will only update the parameter (efficient)
        pygame.display.update()   
        
        clock.tick(60) # you frames per second (FPS)
        
    #end of while loop
        
##################

main()
pygame.quit()
quit()

#END
 
