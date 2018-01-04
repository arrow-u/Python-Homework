import pygame

'''
IMPORTANT
pygames.init() is always the first thing you do. No matter what, No exceptions.  
'''
pygame.init()


#set_mode(resolution) 
surface = pygame.display.set_mode((800,400))

pygame.display.set_caption('Helicopter')

#FPS tracker
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
         if event.type == pygame.QUIT: #usually QUIT means you exit the window
             game_over=True

    #.flip() will update the ENTIRE window (inefficient)
    #.update() will only update the parameter (efficient)
    pygame.display.update()

    #Basically your FPS
    clock.tick(60)

pygame.quit()
quit() 
 
