import pygame
import random
import os
from pygame.locals import *
pygame.init()
script_path = os.path.abspath(__file__)
dir_name = os.path.dirname(script_path)
canvas = pygame.display.set_mode([500,550])
pygame.display.set_caption('snake game')
pygame.display.set_icon(pygame.image.load(dir_name+'/icon.png'))

def grid():
    try:
        for i in range(0,525,25):
            pygame.draw.line(canvas,'yellow',[0,i],[500,i],3)
            pygame.draw.line(canvas,'yellow',[i,0],[i,500],3)
    except:
        print("grid error")

def snake_head(direction,x,y):
    try:
        pygame.draw.rect(canvas,'green',[(x-1)*25+2,(y-1)*25+2,22,22])
        if direction == 'left':
            pygame.draw.rect(canvas,'red',[(x-1)*25+2+3,(y-1)*25+2+3,6,6])
            pygame.draw.rect(canvas,'red',[(x-1)*25+2+3,(y-1)*25+2+13,6,6])
        elif direction == 'right':
            pygame.draw.rect(canvas,'red',[(x)*25-11,(y-1)*25+4,6,6])
            pygame.draw.rect(canvas,'red',[(x)*25-11,(y-1)*25+15,6,6])
        elif direction == 'up':
            pygame.draw.rect(canvas,'red',[(x-1)*25+5,(y-1)*25+5,6,6])
            pygame.draw.rect(canvas,'red',[(x-1)*25+15,(y-1)*25+5,6,6])
        elif direction == 'down':
            pygame.draw.rect(canvas,'red',[(x-1)*25+5,(y-1)*25+15,6,6])
            pygame.draw.rect(canvas,'red',[(x-1)*25+15,(y-1)*25+15,6,6])
    except:
        print('snake head error')

def apple(x,y):
    canvas.blit(image,[(x-1)*25-1,(y-1)*25-2])

def body(l,x,y,direction,c,d):
    ''' x,y = coordinate of head '''
    ''' direction = direction oh head '''
    ''' l = list of coordinates from where head has moved'''
    snake_head(direction,x,y)
    for (a,b) in l:
        pygame.draw.rect(canvas,'green',[(a-1)*25+2,(b-1)*25+2,22,22])  
    if (c,d) != 0:
        pygame.draw.rect(canvas,'black',[(c-1)*25+2,(d-1)*25+2,22,22])  
    pass

def collision_of_snake(l,x,y):
    if (x,y) in l or x <= 0 or y <= 0 or x >= 21 or y >= 21:
        return True
    else:
        return False    

def location_of_apple(l):
    while True:
        x, y = random.randint(1, 20), random.randint(1, 20)
        if (x, y) not in l:
            return (x,y)

timer = pygame.time.Clock() 
image = pygame.image.load(dir_name+'/apple.png')
pygame.Surface.set_colorkey (image, [255,255,255])
running = True
l = []
(a_x,a_y) = location_of_apple(l)
(x,y) = (1,1)
size = 1
direction = 'right'
RUNNING = pygame.USEREVENT + 1
pygame.time.set_timer(RUNNING, 200) 
(c,d) = (0,0)

font = pygame.font.SysFont('freesansbold',40)
sc = font.render(f'score : {len(l)}',True,'yellow')
textRect = sc.get_rect()
textRect.center = (250,525)

while running:
    grid()
    apple(a_x,a_y)
    canvas.blit(sc,textRect)
    if collision_of_snake(l,x,y) == True:
        print("Collision")
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'
        if event.type == RUNNING:
            body(l,x,y,direction,c,d)
            if (x,y) == (a_x,a_y):
                (a_x,a_y) = location_of_apple(l)
                if direction == 'right':
                    l.append((x,y))
                    x+=1
                    (c,d) = l[0]
                elif direction == 'left':
                    l.append((x,y))
                    x-=1
                    (c,d) = l[0]
                elif direction == 'up':
                    l.append((x,y))
                    y-=1
                    (c,d) = l[0]
                elif direction == 'down':
                    l.append((x,y))
                    y+=1
                    (c,d) = l[0]
            if direction == 'right':
                l.append((x,y))
                x+=1
                (c,d) = l[0]
                del(l[0])
            elif direction == 'left':
                l.append((x,y))
                x-=1
                (c,d) = l[0]
                del(l[0])
            elif direction == 'up':
                l.append((x,y))
                y-=1
                (c,d) = l[0]
                del(l[0])
            elif direction == 'down':
                l.append((x,y))
                y+=1
                (c,d) = l[0]
                del(l[0])
    pygame.display.update()
print("Score is : "+ str(len(l)))
print("GAME OVER")