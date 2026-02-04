import pygame
import random
import os
from pygame.locals import *

pygame.init()

script_path = os.path.abspath(__file__)
dir_name = os.path.dirname(script_path)

canvas = pygame.display.set_mode([500,570])

pygame.display.set_caption('snake game')
pygame.display.set_icon(pygame.image.load(dir_name+'/icon.png'))

bg = pygame.image.load(dir_name + '/background.png')
bg_new = pygame.transform.scale(bg,(500,570))

def grid_normal():
    for i in range(0,525,25):
        pygame.draw.line(canvas,'yellow',[0,i],[500,i],3)
        pygame.draw.line(canvas,'yellow',[i,0],[i,500],3)

def grid_dhiraj():
    pygame.draw.rect(canvas,'grey',[0,0,174,25],0)
    pygame.draw.rect(canvas,'grey',[0,0,25,174],0)
    pygame.draw.rect(canvas,'grey',[331,0,174,25],0)
    pygame.draw.rect(canvas,'grey',[480,0,25,174],0)
    pygame.draw.rect(canvas,'grey',[480,331,25,174],0)
    pygame.draw.rect(canvas,'grey',[331,480,174,25],0)
    pygame.draw.rect(canvas,'grey',[0,331,25,174],0)
    pygame.draw.rect(canvas,'grey',[0,480,174,25],0)

def grid_vedant():
    pygame.draw.rect(canvas,[100,100,100],[0,20,500,500],25)

def score(sc,mode,gc):
    if mode == 'dhiraj':
        color = 'yellow'
    elif mode == 'vedant':
        color = [0,18,154]
    font = pygame.font.SysFont('freesansbold',40)
    pygame.draw.rect(canvas,'black',[0,524,500,45],0)
    pp = font.render(f'score : ' + str(sc+gc),True,color)
    textRect = pp.get_rect()
    textRect.center = (250,545)
    canvas.blit(pp,textRect)
    pass

def snake_head(direction,x,y,mode):
    if mode == 'dhiraj':
        color = 'green'
        a = 0
    if mode == 'vedant':
        color = 'white'
        a = 20
    pygame.draw.rect(canvas,color,[(x-1)*25+2,(y-1)*25+2+a,25,25])
    if direction == 'left':
        pygame.draw.rect(canvas,'red',[(x-1)*25+2+3,(y-1)*25+2+a+5,6,6])
        pygame.draw.rect(canvas,'red',[(x-1)*25+2+3,(y-1)*25+2+15+a,6,6])
    elif direction == 'right':
        pygame.draw.rect(canvas,'red',[(x)*25-11,(y-1)*25+6+a,6,6])
        pygame.draw.rect(canvas,'red',[(x)*25-11,(y-1)*25+17+a,6,6])
    elif direction == 'up':
        pygame.draw.rect(canvas,'red',[(x-1)*25+7,(y-1)*25+5+a,6,6])
        pygame.draw.rect(canvas,'red',[(x-1)*25+17,(y-1)*25+5+a,6,6])
    elif direction == 'down':
        pygame.draw.rect(canvas,'red',[(x-1)*25+7,(y-1)*25+15+a,6,6])
        pygame.draw.rect(canvas,'red',[(x-1)*25+17,(y-1)*25+15+a,6,6])
    
def body(l,x,y,direction,c,d,mode):
    ''' x,y = coordinate of head '''
    ''' direction = direction oh head '''
    ''' l = list of coordinates from where head has moved'''
    snake_head(direction,x,y,mode)
    if mode == 'dhiraj':
        color = 'green'
    if mode == 'vedant':
        color = 'white'
    for (a,b) in l:
        if mode == 'dhiraj':
            pygame.draw.rect(canvas,color,[(a-1)*25+2,(b-1)*25+2,25,25])  
        if mode == 'vedant':
            pygame.draw.rect(canvas,color,[(a-1)*25+2,(b-1)*25+22,25,25]) 
    if (c,d) != 0 and mode == 'dhiraj':
        pygame.draw.rect(canvas,'black',[(c-1)*25+2,(d-1)*25+2,25,25])  
    if (c,d) != 0 and mode == 'vedant':
        pygame.draw.rect(canvas,'black',[(c-1)*25+2,(d-1)*25+22,25,25])
    pass

def collision_of_snake_vedant(l,x,y):
    if (x,y) in l or x <= 1 or y <= 1 or x >= 20 or y >= 20:
        return True
    else:
        return False    

def collision_of_snake_dhiraj(l,x,y):
    if (x,y) in l or ( x <= 7 and y <= 1) or (x >= 14 and y <= 1) or ( x <= 7 and y >= 20) or (x >= 14 and y >= 20) or ( x <= 1 and y <= 7) or (x <= 1 and y >= 14) or ( x >= 20 and y <= 7) or (x >= 20 and y >= 14):
        return True
    else:
        return False 

def apple_draw(x,y,mode):
    if mode == 'vedant':
        color = 'green'
        pygame.draw.rect(canvas,color,[(x-1)*25+4,(y-1)*25+24,22,22])
    if mode == 'dhiraj':
        color = 'red'
        pygame.draw.rect(canvas,color,[(x-1)*25+4,(y-1)*25+4,22,22])

def golden_apple_draw(x,y,color):
    pygame.draw.rect(canvas,color,[(x-1)*25+4,(y-1)*25+24,22,22])
    
def location_of_apple(l,mode):
    if mode == 'vedant':
        b = [(4,4),(17,17),(17,4),(4,17)]
    else:
        b = []
    while True:
        x, y = random.randint(2, 19), random.randint(2, 19)
        if (x, y) not in l :
            if (x,y) not in b:
                return (x,y)
        
def location_of_golden_apple(l):
    b = [(4,4),(17,17),(16,7),(4,17)]
    while True:
        x, y = random.randint(2, 19), random.randint(2, 19)
        if (x, y) not in l:
            if (x,y) not in b:
                return (x,y)

def wormholes():

    pygame.draw.rect(canvas,'grey',[75,95,27,27],3)
    pygame.draw.rect(canvas,'purple',[78,98,21,24])

    pygame.draw.rect(canvas,'grey',[400,95,27,27],3)
    pygame.draw.rect(canvas,'purple',[400,98,24,21])

    pygame.draw.rect(canvas,'grey',[75,420,27,27],3)
    pygame.draw.rect(canvas,'purple',[78,423,24,21])

    pygame.draw.rect(canvas,'grey',[400,420,27,27],3)
    pygame.draw.rect(canvas,'purple',[403,420,21,24])

def timebar(gsc):
    pygame.draw.rect(canvas,'yellow',[0,0,(20-gsc)*25,20])
    pygame.draw.rect(canvas,'black',[(20-gsc)*25,0,gsc*25,20])

Running = True
ON_BOX_VEDANT = pygame.USEREVENT + 1
ON_BOX_DHIRAJ = pygame.USEREVENT + 2
box_dhiraj = pygame.Rect([10,10,160,40])
box_vedant = pygame.Rect([330,10,160,40])
fon = pygame.font.Font('freesansbold.ttf',20)
ved = fon.render("Vedant's Mode",True,[17,52,60])
dhi = fon.render("Dhiraj's Mode",True,[17,52,60])
text_ved = ved.get_rect()
text_dhi = dhi.get_rect()
text_ved.center = [410,30]
text_dhi.center = [90,30]
draw_mode = True

ON_BOX_TOUCH = pygame.USEREVENT + 3
ON_BOX_ARROW = pygame.USEREVENT + 4
box_touch = pygame.Rect([10,520,160,40])
box_arrow = pygame.Rect([330,520,160,40])
arr = fon.render("Touch Mode",True,[17,52,60])
tou = fon.render("Arrow Mode",True,[17,52,60])
text_arr = arr.get_rect()
text_tou = tou.get_rect()
text_arr.center = [90,540]
text_tou.center = [410,540]
draw_cont = True

while Running :
    canvas.blit(bg_new,[0,0])

    pygame.draw.rect(canvas, [17,52,60], box_dhiraj,3,20) 
    pygame.draw.rect(canvas, [17,52,60], box_vedant,3,20)
    if draw_mode == False and mode == 'vedant':
        pygame.draw.rect(canvas,[55,126,71],[333,13,154,34],0,20)
    elif draw_mode == False and mode == 'dhiraj':
        pygame.draw.rect(canvas,[55,126,71],[13,13,154,34],0,20)
    canvas.blit(ved,text_ved)
    canvas.blit(dhi,text_dhi)

    pygame.draw.rect(canvas, [17,52,60], box_touch,3,20) 
    pygame.draw.rect(canvas, [17,52,60], box_arrow,3,20)
    if draw_cont == False and cont == 'arrow':
        pygame.draw.rect(canvas,[55,126,71],[333,523,154,34],0,20)
    elif draw_cont == False and cont == 'touch':
        pygame.draw.rect(canvas,[55,126,71],[13,523,154,34],0,20)
    canvas.blit(arr,text_arr)
    canvas.blit(tou,text_tou)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()
            quit()
        elif event.type == ON_BOX_VEDANT:
            mode = 'vedant'
            draw_mode = False
        elif event.type == ON_BOX_DHIRAJ:
            mode = 'dhiraj'
            draw_mode = False
        elif event.type == ON_BOX_TOUCH:
            cont = 'touch'
            draw_cont = False
        elif event.type == ON_BOX_ARROW:
            cont = 'arrow'
            draw_cont = False

    if draw_mode == True:
        if box_dhiraj.collidepoint(pygame.mouse.get_pos()): 
            pygame.event.post(pygame.event.Event(ON_BOX_DHIRAJ)) 
        if box_vedant.collidepoint(pygame.mouse.get_pos()): 
            pygame.event.post(pygame.event.Event(ON_BOX_VEDANT)) 
    
    if draw_cont == True:
        if box_arrow.collidepoint(pygame.mouse.get_pos()): 
            pygame.event.post(pygame.event.Event(ON_BOX_ARROW)) 
        if box_touch.collidepoint(pygame.mouse.get_pos()): 
            pygame.event.post(pygame.event.Event(ON_BOX_TOUCH)) 
        
    pygame.display.update()
    if draw_mode == False and draw_cont == False:
        Running = False 
        pygame.quit()

pygame.init()

script_path = os.path.abspath(__file__)
dir_name = os.path.dirname(script_path)
canvas = pygame.display.set_mode([500,570])
pygame.display.set_icon(pygame.image.load(dir_name+'/icon.png'))

running = True

l = []
ap = False
scor = 0
gold_scor = 0
timer = pygame.time.Clock() 
(a_x,a_y) = location_of_apple(l,mode)
direction = 'right'
RUNNING = pygame.USEREVENT + 5
pygame.time.set_timer(RUNNING, 200) 
(c,d) = (0,0)
i = 0
gp = False
gsc = 0

if mode == 'dhiraj':
    (x,y) = (2,2)
    pygame.display.set_caption("Dhiraj's Snake Game")
    while running:
        grid_dhiraj()
        apple_draw(a_x,a_y,'dhiraj')
        score(scor,'dhiraj',gold_scor)
        
        if (x,y) == (a_x,a_y): # eating an apple
            (a_x,a_y) = location_of_apple(l,'dhiraj')
            ap = True
            scor+=1

        if collision_of_snake_dhiraj(l,x,y) == True:
            print("Collision")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if cont == 'arrow':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 'up'
                    elif event.key == pygame.K_DOWN:
                        direction = 'down'
                    elif event.key == pygame.K_LEFT:
                        direction = 'left'
                    elif event.key == pygame.K_RIGHT:
                        direction = 'right'
            if cont == 'touch':
                mx,my = pygame.mouse.get_pos()
                if mx > my and mx+my<520 and my < 520 and my > 20:
                    direction = 'up'
                elif mx < my and mx+my<520 and my < 520 and my > 20:
                    direction = 'left'
                elif mx > my and mx+my>520 and my < 520 and my > 20:
                    direction = 'right'
                elif mx < my and mx+my>520 and my < 520 and my > 20:
                    direction = 'down'

            if event.type == RUNNING:
                body(l,x,y,direction,c,d,'dhiraj')
                if ap == True: # eating an apple
                    ap = False
                    if direction == 'right':
                        l.append((x,y))
                        if x!=20:  
                            x+=1
                        else:
                            x = 1
                        (c,d) = l[0]
                    elif direction == 'left':
                        l.append((x,y))
                        if x!=1:  
                            x-=1
                        else:
                            x = 20
                        (c,d) = l[0]
                    elif direction == 'up':
                        l.append((x,y))
                        if y!=1:  
                            y-=1
                        else:
                            y = 20
                        (c,d) = l[0]
                    elif direction == 'down':
                        l.append((x,y))
                        if y != 20:
                            y+=1
                        else:
                            y = 1
                        (c,d) = l[0]
                else:
                    if direction == 'right':
                        l.append((x,y))
                        if x!=20:  
                            x+=1
                        else:
                            x = 1
                        (c,d) = l[0]
                        del(l[0])
                    elif direction == 'left':
                        l.append((x,y))
                        if x!=1:  
                            x-=1
                        else:
                            x = 20
                        (c,d) = l[0]
                        del(l[0])
                    elif direction == 'up':
                        l.append((x,y))
                        if y!=1:  
                            y-=1
                        else:
                            y = 20
                        (c,d) = l[0]
                        del(l[0])
                    elif direction == 'down':
                        l.append((x,y))
                        if y != 20:
                            y+=1
                        else:
                            y = 1
                        (c,d) = l[0]
                        del(l[0])
        
        pygame.display.update() 

if mode == 'vedant':
    (x,y) = (2,2)
    pygame.display.set_caption("Vedant's Snake Game")
    while running:
        grid_vedant()
        wormholes()
        apple_draw(a_x,a_y,'vedant')
        score(scor,'vedant',gold_scor)
        
        if gp == True:
            timebar(gsc)
            golden_apple_draw(g_x,g_y,'yellow')
        
            if (x,y) == (g_x,g_y): # eating a golden apple
                gp = False
                golden_apple_draw(g_x,g_y,'black')

            if gsc == 20:
                gp = False
                golden_apple_draw(g_x,g_y,'black')
                gsc = 0

        if (x,y) == (a_x,a_y): # eating an apple
            (a_x,a_y) = location_of_apple(l,'vedant')
            if scor%5 == 0:
                (g_x,g_y) = location_of_golden_apple(l)
            if scor % 5 == 0 and scor != 0:
                gp = True
            scor += 1
            ap = True
            
        if collision_of_snake_vedant(l,x,y) == True:
            print("Collision")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if cont == 'arrow':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 'up'
                    elif event.key == pygame.K_DOWN:
                        direction = 'down'
                    elif event.key == pygame.K_LEFT:
                        direction = 'left'
                    elif event.key == pygame.K_RIGHT:
                        direction = 'right'
            if cont == 'touch':
                mx,my = pygame.mouse.get_pos()
                if mx > my and mx+my<520 and my < 520 and my > 20:
                    direction = 'up'
                elif mx < my and mx+my<520 and my < 520 and my > 20:
                    direction = 'left'
                elif mx > my and mx+my>520 and my < 520 and my > 20:
                    direction = 'right'
                elif mx < my and mx+my>520 and my < 520 and my > 20:
                    direction = 'down'

            if event.type == RUNNING:
                if gp == True:
                    gsc += 1
                if gsc != 0:
                    if gp ==False:
                        gold_scor += 20 - gsc
                        gsc = 0
                        timebar(20)
                body(l,x,y,direction,c,d,'vedant')
                if ap == True: # eating an apple
                    ap = False
                    if direction == 'right':
                        l.append((x,y))
                        zeeta = False
                        if x == 17:  
                            if y == 4:
                                zeeta = True
                                (x,y) = (4,17)
                        if zeeta != True:
                            x+=1
                        (c,d) = l[0]
                    elif direction == 'left':
                        l.append((x,y))
                        zeeta = False
                        if x == 4:  
                            if y == 17:
                                zeeta = True
                                (y,x) = (4,17)
                        if zeeta != True:
                            x-=1
                        (c,d) = l[0]
                    elif direction == 'up':
                        l.append((x,y))
                        zeeta = False
                        if x == 4:  
                            if y == 4:
                                zeeta = True
                                (x,y) = (17,17)
                        if zeeta != True:
                            y-=1
                        (c,d) = l[0]
                    elif direction == 'down':
                        l.append((x,y))
                        zeeta = False
                        if x == 17:  
                            if y == 17:
                                zeeta = True
                                (x,y) = (4,4)
                        if zeeta != True:
                            y+=1
                        (c,d) = l[0]
                else:
                    if direction == 'right':
                        l.append((x,y))
                        zeeta = False
                        if x == 17:  
                            if y == 4:
                                zeeta = True
                                (x,y) = (4,17)
                        if zeeta != True:
                            x+=1
                        (c,d) = l[0]
                        del(l[0])
                    elif direction == 'left':
                        l.append((x,y))
                        zeeta = False
                        if x == 4:  
                            if y == 17:
                                zeeta = True
                                (y,x) = (4,17)
                        if zeeta != True:
                            x-=1
                        (c,d) = l[0]
                        del(l[0])
                    elif direction == 'up':
                        l.append((x,y))
                        zeeta = False
                        if x == 4:  
                            if y == 4:
                                zeeta = True
                                (x,y) = (17,17)
                        if zeeta != True:
                            y-=1
                        (c,d) = l[0]
                        del(l[0])
                    elif direction == 'down':
                        l.append((x,y))
                        zeeta = False
                        if x == 17:  
                            if y == 17:
                                zeeta = True
                                (x,y) = (4,4)
                        if zeeta != True:
                            y+=1
                        (c,d) = l[0]
                        del(l[0])
        
        pygame.display.update() 