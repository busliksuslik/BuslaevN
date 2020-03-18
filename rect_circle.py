import pygame

 
FPS = 60
SCREEN_SIZE = WIN_WIDTH, WIN_HEIGHT = 400, 400
COLOR2 = (0, 167, 79)
COLOR1 = (125, 1, 164)
FON = (91, 78, 0)
rect_width = WIN_WIDTH // 2
rect_height = WIN_HEIGHT // 2


pygame.init()
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode(SCREEN_SIZE)
sc.fill(FON)
 
rect_1 = pygame.Rect((0, 0), (rect_width, rect_height))
rect_2 = pygame.Rect((rect_width, 0), (rect_width, rect_height))
rect_3 = pygame.Rect((rect_width, rect_height), (rect_width, rect_height))
rect_4 = pygame.Rect((0, rect_height), (rect_width, rect_height))
 
surf_1 = pygame.Surface((rect_width, rect_height))
surf_2 = pygame.Surface((rect_width, rect_height))
surf_3 = pygame.Surface((rect_width, rect_height))
surf_4 = pygame.Surface((rect_width, rect_height))
 
surf_1.fill(FON)
surf_2.fill(FON)
surf_3.fill(FON)
surf_4.fill(FON)
 
sc.blit(surf_1, rect_1)
sc.blit(surf_2, rect_2)
sc.blit(surf_3, rect_3)
sc.blit(surf_4, rect_4)
 
circle_update = (rect_1, rect_2, rect_3, rect_4)

CIRCLE_COLOR = COLOR1
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_1:
                circle_update = (rect_1, rect_3)
            elif i.key == pygame.K_2:
                circle_update = (rect_2, rect_4)
            elif i.key == pygame.K_0:
                circle_update = (rect_1, rect_2, rect_3, rect_4)
 
    if True:
        if CIRCLE_COLOR == COLOR1:
            CIRCLE_COLOR = COLOR2
        elif CIRCLE_COLOR == COLOR2:
            CIRCLE_COLOR = COLOR1
        pygame.draw.circle(sc, CIRCLE_COLOR, (WIN_WIDTH // 2, WIN_HEIGHT // 2), 100)
        pygame.display.update(circle_update)
        pygame.time.delay(500)
 
    clock.tick(FPS)