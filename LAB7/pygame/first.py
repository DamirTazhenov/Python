from time import time
from webbrowser import get
import pygame
import os
import math
from datetime import datetime

resolution = width, height = 800,800
half_width, half_height = width // 2, height // 2

image_gallery = {}

def blit_Rotate(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)

def get_image(path):
    global image_gallery
    image = image_gallery.get(path)
    if image == None:
        canonic_path = u'LAB7/pygame/'+path #path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonic_path).convert_alpha()
        image_gallery[path] = image
    return(image)

angle = 0

pygame.init()

mainscreen = pygame.display.set_mode(resolution)
done = False
clock = pygame.time.Clock()

font = pygame.font.SysFont('Verdana', 30)

start_position = (0,0)


while not done:
    for event in pygame.event.get(): #this empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.
        if event.type == pygame.QUIT: #click on close bottom on the window
            done = True
    
    mainscreen.fill([1,1,1])

    clock_surface = get_image('clocks.png').convert_alpha()
    seconds = get_image('seconds.png').convert_alpha()
    minutes = get_image('minutes.png').convert_alpha()

    mainscreen.blit(clock_surface, start_position)

    timenow = datetime.now()
    minutess, secondss = timenow.minute, timenow.second
    minute_grad, seconds_grad = minutess * 6, secondss * 6

    time_render = font.render(f'{timenow:%H:%M:%S}', True, pygame.Color('white'), pygame.Color('black'))
    mainscreen.blit(time_render, (0,0))

    
    blit_Rotate(mainscreen, minutes, start_position, -minute_grad)
    blit_Rotate(mainscreen, seconds, start_position, -seconds_grad)

    pygame.display.flip()
    clock.tick(60)
    
    