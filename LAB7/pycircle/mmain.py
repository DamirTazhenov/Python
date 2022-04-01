import pygame

pygame.init()

resolution = (800,600)
xchange,ychange = 400,300
clock = pygame.time.Clock()

mscreen = pygame.display.set_mode(resolution)
done = False

while not done:
    for event in pygame.event.get(): #this empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
        if event.type == pygame.QUIT: #click on close bottom on the window
            done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if xchange > 775:
                    pass
                else:
                    xchange = xchange + 20
            elif event.key == pygame.K_LEFT:
                if xchange <25:
                    pass
                else:
                    xchange = xchange - 20
            elif event.key == pygame.K_DOWN:
                if ychange >575:
                    pass
                else:
                    ychange = ychange + 20
            elif event.key == pygame.K_UP:
                if ychange <25:
                    pass
                else:
                    ychange = ychange - 20

    mscreen.fill((255,255,255))
    
    #circle = pygame.draw.circle

    pygame.draw.circle(mscreen, (1,1,1),(xchange,ychange), 25)    

    clock.tick(60)
    pygame.display.update()
    