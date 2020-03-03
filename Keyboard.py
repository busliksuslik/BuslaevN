import pygame
 
FPS = 60
W = 400 
H = 400  
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
 

x = W // 2
y = H // 2
r = 50
 
motion = STOP
 
while 1:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, BLUE, (x, y), r)
 
    pygame.display.update()
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT or i.key == pygame.K_a:
                motion = LEFT
            elif i.key == pygame.K_RIGHT or i.key == pygame.K_d:
                motion = RIGHT
            elif i.key == pygame.K_UP or i.key == pygame.K_w:
                motion = UP
            elif i.key == pygame.K_DOWN or i.key == pygame.K_s:
                motion = DOWN
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN ,pygame.K_a , pygame.K_d,pygame.K_w , pygame.K_s]:
                motion = STOP

 
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