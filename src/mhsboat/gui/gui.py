import pygame

pygame.init()

### VARIABLES
boat = pygame.Rect((100, 250, 100, 50))
screen_Width = 800;
screen_Height = 600;
backGround = (125, 125, 255)
boatColor = (0,0,255)

run = True;
screen = pygame.display.set_mode((screen_Width, screen_Height))

###Initialize and runs events when needed
while run:
    
    ### Fills screen with water and draws the boat
    screen.fill(backGround)
    pygame.draw.rect(screen, boatColor, boat)



    ### Grabs event, if closed, then stops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()