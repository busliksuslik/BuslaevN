import pygame, random, math

class Car():
    width = 20
    height = 50
    def __init__(self,surface,color):
        self.surf = surface 
        self.color = color
        self.x = surface.get_width()//2 - Car.width//2 
        self.y = surface.get_height()
        self.motion_l = False
        self.motion_r = False
        self.time = 0
        self.speedy = 1
    def drive(self): 
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, Car.width, Car.height)) 
        self.y -= self.speedy 
        if self.y < -Car.height: 
            self.y = H
            self.time +=1
            self.speedy = round(1/(0.1+math.exp(-self.time)))
            return True
            
    def drivel(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, Car.width, Car.height)) 
        if self.x > 0 : 
            self.x -= 3
    def driver(self):
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, Car.width, Car.height)) 
        if  self.x < self.surf.get_width() - Car.width: 
            self.x += 3
    def dmg(self):
        self.y = H
class Obstacle():
    width = 20
    height = 20
    def __init__(self,surface,color):
        self.surf = surface 
        self.color = color
        self.x = random.randint(0,surface.get_width()- 20)
        self.y = random.randint(0,surface.get_height()-100)
    def draw(self): 
        pygame.draw.rect(self.surf, self.color, (self.x, self.y, Obstacle.width, Obstacle.height)) 
    def cord(self):
        return(self.x,self.y)
    def new(self):
        self.x = random.randint(0,self.surf.get_width()- 20)
        self.y = random.randint(0,self.surf.get_height()-100)
        
 
FPS = 60
W = 600  # ширина экрана
H = 800  # высота экрана
PL1 = 0
PL2 = 0
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
BLACK = (0,0,0)
 
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

surf_left = pygame.Surface((W//2, H)) 
surf_left.fill(WHITE)
surf_right = pygame.Surface((W//2, H))

sc.blit(surf_left, (0, 0)) 
sc.blit(surf_right, (W//2, 0))

car_left = Car(surf_left, BLACK) 
car_right = Car(surf_right, WHITE)
obs_left = Obstacle(surf_left, BLACK) 
obs_right = Obstacle(surf_right, WHITE)

f1 = pygame.font.SysFont('arial', 36)
text1 = f1.render('PLAYER 1   '+str(PL1), 1, WHITE)

f2 = pygame.font.SysFont('arial', 36)
text2 = f2.render('PLAYER 2   '+str(PL2), 1, BLACK)


 
while True:
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                car_right.motion_l = True
            elif i.key == pygame.K_RIGHT:
                car_right.motion_r = True
            elif i.key == pygame.K_a:
                car_left.motion_l = True
            elif i.key == pygame.K_d:
                car_left.motion_r = True
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT:
                car_right.motion_l = False
            elif i.key == pygame.K_RIGHT:
                car_right.motion_r = False
            elif i.key == pygame.K_a:
                car_left.motion_l = False
            elif i.key == pygame.K_d:
                car_left.motion_r = False
    if car_right.y < obs_right.y and car_right.x < obs_right.x+20 and car_right.x > obs_right.x - 20 and car_right.y > obs_right.y-20:
        PL1+=1
        car_right.dmg()
        obs_right.new()
    if car_left.y < obs_left.y and car_left.x < obs_left.x+20 and car_left.x > obs_left.x - 20 and car_left.y > obs_left.y-20:
        PL2+=1
        car_left.dmg()
        obs_right.new()
                
    surf_right.fill(BLACK)
    surf_left.fill(WHITE)

    if car_left.motion_l:
        car_left.drivel()
    elif car_left.motion_r:
        car_left.driver()
    if car_right.motion_l:
        car_right.drivel()
    elif car_right.motion_r:
        car_right.driver()
    A = car_left.drive()
    if A:
        obs_left.new()
    A = car_right.drive() 
    if A:
        obs_right.new()
    obs_left.draw()
    obs_right.draw()
    sc.blit(surf_right, (W//2, 0))
    sc.blit(surf_left, (0, 0))
    text1 = f1.render('PLAYER 2   '+str(PL2), 1, WHITE)
    text2 = f2.render('PLAYER 1   '+str(PL1), 1, BLACK)
    sc.blit(text1, (W//2, 0))
    sc.blit(text2, (0, 0))
    pygame.display.update()
 
    clock.tick(FPS)