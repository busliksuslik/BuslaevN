import pygame
pygame.init()
 
 
def turning(car_surf,degrees):
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
        car_surf = pygame.transform.rotate(car_surf, degrees)
        sc.blit(car_surf, car_rect)
        pygame.display.update()
 
FPS = 60
SCREEN_SIZE = WIN_WIDTH, WIN_HEIGHT = 800, 800
BLACK = (0, 0, 0)
UP = 0
DOWN = 180
RIGHT = -90
LEFT = 90
 
sc = pygame.display.set_mode(SCREEN_SIZE)
sc.fill((255,192,203))
clock = pygame.time.Clock()
 
car_surf = pygame.image.load('car.png')
car_rect = car_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))  
sc.blit(car_surf, car_rect)
 
pygame.display.update()
while 1:
    sc.fill((255,192,203))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        turning(car_surf,UP)
        car_rect.y -= 3
    elif keys[pygame.K_DOWN]:
        turning(car_surf,DOWN)
        car_rect.y += 3
    elif keys[pygame.K_RIGHT]:
        turning(car_surf,RIGHT)
        car_rect.x += 3
    elif keys[pygame.K_LEFT]:
        turning(car_surf,LEFT)
        car_rect.x -= 3

 
    clock.tick(FPS)