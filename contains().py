import pygame
 
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
 
pygame.init()

sc = pygame.display.set_mode((400, 300))
sc.fill(WHITE)

pygame.display.update()

rect1 = pygame.Rect((0, 0, 100, 100))
rect2 = pygame.Rect((150 ,150 , 30, 30))

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Какая-то надпись', 1, (180, 0, 0))

surf1 = pygame.Surface((100, 100))
surf1.fill(RED)  
surf2 = pygame.Surface((30, 30))
surf2.fill(BLUE)

collide = False
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN and rect2.collidepoint(pygame.mouse.get_pos()):
            collide = True
        elif i.type == pygame.MOUSEBUTTONUP:
            collide = False
        if collide:
            pos = pygame.mouse.get_pos()
            x = pos[0]-15-rect2[0]
            y = pos[1]-15-rect2[1]
            rect2.move_ip(x,y)   
 
    sc.fill(WHITE)
    
    sc.blit(surf1,rect1)
    sc.blit(surf2,rect2)
    if rect1.contains(rect2):
        sc.blit(text1,(100,100))
 
    pygame.display.update()
 
    pygame.time.delay(20)
