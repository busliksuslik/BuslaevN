import pygame
 
FPS = 60
W = 400  # ширина экрана
H = 400  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"
STOP = "stop"
 
pygame.init()
sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
 
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50
 
motion = STOP
 
while 1:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, BLUE, (x, y), r)
 
    pygame.display.update()
    
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    a,b = pos
    if pressed[0]:
        if round((x-a)**2+(y-b)**2)**(1/2) <= r:
            x,y = pos
            if x > W - 50:
                x = W - 50
                print('BOOM')
            if x < 50:
                x = 50
                print('BOOM')
            if y > H - 50:
                y = H - 50
                print('BOOM')
            if y < 50:
                y = 50
                print('BOOM')
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit() 
            
#        elif i.type == pygame.MOUSEBUTTONDOWN:
#            if i.button == 1:
#                x,y = i.pos
#                if x > W - 50:
#                    x = W - 50
#                if x < 50:
#                    x = 50
#                if y > H - 50:
#                    y = H - 50
#                if y < 50:
#                    y = 50

 
    if motion == LEFT:
        if x >= 50:
            x -= 3
    elif motion == RIGHT:
        if x <= W-50:
            x += 3
    elif motion == UP:
        if y >= 50:
            y -= 3
    elif motion == DOWN:
        if y <= H-50:
            y += 3
        
 
    clock.tick(FPS)