class Dog():
    age = 0
    name = ''
    weight = 0
toyterier = Dog()
toyterier.age = 2
toyterier.name = '3.14159265358979'
toyterier.weight = 2.7182818284590



class Person():
    name = ''
    cellphone = ''
    email = ''
a = Person()
b = Person()
a.name = 'xyz'
b.name = 'abc'
a.cellphone = '2.7182818284590'
a.email = 'fkgjhakgjhera@fkijdfgkoj.jr'
b.cellphone = '2.7182818284590'
b.email = 'fkgjhakgjhera@fkijdfgkoj.jr'





class Bird():
    color = ''
    name = ''
    breed = ''
a = Bird()


class Player():
    name = ''
    force = 0
    xcord = 0
    ycord = 0
a = Player()
    
##############################5 программист не обращается к атрибуту, а просто создаёт новые переменные
##############################6 да
##############################7 у боба не задано имя
class Cat():
    name = ''
    color = ''
    weight = 0
    def meow(self):
        print('мя', end = '')
        print('а',end = '')
        print('у')
a = Cat()
a.color = 'blue'
a.name = '3.1415door'
a.weight = 123**123
a.meow()




class Monster():
    name = ''
    health = 100
    def decrease_health(self,dmg):
        self.health -=dmg
        if self.health<=0:
            print('монстр умер')
a = Monster()
a.decrease_health(100)



class Aadress():
    attribute1 = ''
    attribute2 = ''
    def print_att(self):
        print(self.attribute1)
        print(self.attribute2)
a = Aadress()

import random
class Warrior():
    hp = 100
    dmg = 20
    def damage(self):
        return self.dmg
    def defence(self,a):
        self.hp-=a
        if self.hp<=0:
            return False
        else:
            return True
a = 10
warriors = [Warrior() for i in range(0,a)]
inGame = True
print(len(warriors))
while inGame:
    damPl = random.randint(0,a-1)
    defPl = random.randint(0,a-1)
    while damPl == defPl:
        defPl = random.randint(0,a-1)
    inGame = warriors[defPl].defence(warriors[damPl].damage())
    print(damPl,'юнит атаковал, у юнита ',defPl,'осталось',warriors[defPl].hp)
print('Игрок',damPl,'Убил игрока',defPl)


"генерация случайных чисел"
import random
class Person():
    """родительский класс person. В конструктор берёт принадлежность команде, и создаёт id """
    def __init__(self,a):
        self.id = random.randint(0,100)
        self.comm = a
class Hero(Person):
    """класс герой имеет уровень и солдат, следующих за ним """
    lvl = 0
    solders = []
    def add_solder(self,solder):
        "добавляет солдата к массиву солдата"
        self.solders.append(solder)
    def solders_id(self):
        "выводит id следующих за героем солдат "
        for i in range(len(self.solders)):
            print(self.solders[i].id)
    def lvl_up(self):
        "увеличивает уровень героя на 1"
        self.lvl +=1
    def print_id(self):
        "выводит свой id, а потом id солдат"
        print(self.id)
        self.solders_id()
class Solder(Person):
    "класс солдат может идти за героем"
    def go_with_hero(self,herocom):
        "заставлет идти за героем из заданого массива"
        herocom[0].add_solder(self)
num_comm = 6
comm = [[Hero(i)]for i in range(0,num_comm)]
solders = []
for i in range(20):
    a = random.randint(0,num_comm-1)
    comm[a].append(Solder(a))
t = 0
b = 0
for i in range(num_comm-1):
    if  t<len(comm[i]):
        t = len(comm[i])
        b = i   
comm[b][0].lvl_up()
for i in range(num_comm):
    print(comm[i][0].lvl)
comm[0][1].go_with_hero(comm[0])
comm[0][0].print_id()









        
    

    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
