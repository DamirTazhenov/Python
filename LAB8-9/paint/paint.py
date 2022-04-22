import random
import pygame
import math

colors = {
    'red' : (255, 0, 0),
    'blue' : (0, 0, 255),
    'green' : (0, 255, 0),
    'black': (0,0,0),
    'white' : (255, 255, 255),
    'purple' : (255, 0, 255),
    'brown' : (150, 75, 0),
    'olive' : (128, 128, 0),
    'sky blue' : (0, 255, 255),
}

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Paint')
screen.fill(colors['black'])
base = pygame.Surface((800, 600))

draw_on = False

pos_last = (0, 0)

color = colors['green']
figure = 'pen'

def Rect_pos(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN: # for changing
            if event.key == pygame.K_8: #colors on buttons  1 - 8
                color = colors['blue']
            if event.key == pygame.K_1:
                color = colors['green']
            if event.key == pygame.K_2:
                color = colors['red']
            if event.key == pygame.K_3:
                color = colors['white']
            if event.key == pygame.K_4:
                color = colors['olive']
            if event.key == pygame.K_5:
                color = colors['brown']
            if event.key == pygame.K_6:
                color = colors['purple']
            if event.key == pygame.K_7:
                color = colors['sky blue']
            if event.key == pygame.K_p:
                figure = 'pen'
            if event.key == pygame.K_c:
                figure = 'circle'
            if event.key == pygame.K_k:
                figure = 'rectangle'
            if event.key == pygame.K_e:
                figure = 'erase'
            if event.key == pygame.K_s:
                figure = 'square'
            if event.key == pygame.K_t:
                figure = 'right triangle'
            if event.key == pygame.K_q:
                figure = 'equilateral triangle'
            if event.key == pygame.K_h:
                figure = 'rhombus'
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw_on = True
            pos_last = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            draw_on = False
            base.blit(screen, (0, 0))
        if event.type == pygame.MOUSEMOTION: # functions for figures
            if draw_on == True:
                if figure == 'circle':
                    screen.blit(base, (0, 0))
                    pygame.draw.circle(screen, color, (pos_last[0], pos_last[1]), int(math.sqrt((event.pos[0] - pos_last[0]) ** 2 + (event.pos[1] - pos_last[1]) ** 2)))
                if figure == 'rectangle':
                    screen.blit(base, (0, 0))
                    a = Rect_pos(pos_last[0], pos_last[1], event.pos[0], event.pos[1])
                    pygame.draw.rect(screen, color, pygame.Rect(a))
                if figure == 'pen':
                    pygame.draw.line(screen, color, [pos_last[0], pos_last[1]], [event.pos[0], event.pos[1]], 5)
                    pos_last = event.pos
                if figure == 'erase':
                    pygame.draw.circle(screen, color['black'], (event.pos[0], event.pos[1]), 9)
                if figure == 'square':
                    screen.blit(base, (0, 0))
                    a = Rect_pos(pos_last[1], pos_last[1], event.pos[1], event.pos[1])
                    pygame.draw.rect(screen, color, pygame.Rect(a))
                if figure == 'right triangle':
                    screen.blit(base, (0, 0))
                    pygame.draw.polygon(screen, color, [(pos_last[0], pos_last[1] + event.pos[0]), (pos_last[0], pos_last[1]), (pos_last[0] + 2 * event.pos[0], pos_last[1])])
                if figure == 'equilateral triangle':
                    screen.blit(base, (0, 0))
                    pygame.draw.polygon(screen, color, [(pos_last[0] - event.pos[0], pos_last[0] + event.pos[0]), (pos_last[0] + event.pos[0], pos_last[0] + event.pos[0]), (pos_last[0], pos_last[0] - event.pos[0])])
                if figure == 'rhombus':
                    pos1 = (pos_last[0] / 2, pos_last[1] / 2 - event.pos[0] / 2)
                    pos2 = (pos1[0] - event.pos[1] / 2, pos1[1] + event.pos[0] / 2)
                    pos3 = (pos1[0], pos1[1] + event.pos[0])
                    pos4 = (pos2[0] + event.pos[1], pos2[1])
                    points = [pos1, pos2, pos3, pos4]
                    screen.blit(base, (0, 0))
                    pygame.draw.polygon(screen, color, points)
    pygame.display.flip()
pygame.quit()