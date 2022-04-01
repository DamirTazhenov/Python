import pygame
pygame.init()
screen = pygame.display.set_mode((400,500)) 
done = False
is_blue = True

while not done:
    for event in pygame.event.get(): #this empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
        if event.type == pygame.QUIT: #click on close bottom on the window
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255,100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(30,30,100,100))
    pygame.display.flip() #this call is required in order for any updates that you make to the game screen to become visible.
