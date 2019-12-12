#1
import random
n = 10
m = 10
a = []# создаём нужные переменные
for i in range(n):
    a.append([ random.randint(1,100) for i in range(m)]) #заполняем массив случайными числами
print(a)
max = 0
s = 0
st = 0# создаём нужные переменные
for i in range(n):
    for t in range(m):
        if a[i][t]>max:  # если проверяемый элемент массива больше дествующего максимума 
            s = i        # то проверяемая строка становится действующей 
            st = t       # и проверяемый столбец становиться действующим
            max = a[i][t]# а проверяемиый элемент становиться действующим максимальным
print(s,'  ',st)
#################################
#2
n = 11
a = []# создаём нужные переменные
for i in range(n):
    a.append(["."]*n)#заполняем массив точками
for i in range(n):
    a[i][int(n/2)] ='*'   #меняем средний столбец на *
for i in range(n):
    a[int(n/2)][i]='*'    #меняем среднюю строку на *
for i in range(n):
    for t in range(n):
        if i==t:         #условие для диагонали
            a[i][t]='*'  #меняем диагональ
for i in range(n):       #
    for t in range(n):
        if n - i -1==t:  ##условие для диагонали
            a[i][t]='*'  #меняем диагональ
for i in range(n):       #выводим массив
    print()
    for t in range(n):
        print(a[i][t],end=' ')
################################
#3
n = 10
m = 10
a = []# создаём нужные переменные
for i in range(n):
    a.append(["."]*m)#заполняем массив точками
for i in range(n):
    for t in range(m):
        if i%2==t%2 : # условия для шахматного порядка
            a[i][t]='.'
        else:
            a[i][t]='*'
for i in range(n):#выводим массив
    print()
    for t in range(m):
        print(a[i][t],end=' ')
##################################
#4
n = 11
a = []# создаём нужные переменные
for i in range(n):
    a.append(["."]*n)#заполняем массив точками
for o in range(n):
    for i in range(n):
        for m in range(n):
            if i == m-o or i-o == m:#если точка массива находиться от диагонали на o, то значение заменяется на o+1
                a[i][m] = (o+1)
for i in range(n):#выводим массив
    print()
    for t in range(n):
        print(a[i][t],end=' ')
################################
#5
n = 5
a = []# создаём нужные переменные
for i in range(n):
    a.append(["."]*n)#заполняем массив точками
for i in range(n):
    for t in range(n):#рисуем диагональ
        if i==n-t-1:# условие диагонали
            a[i][t]=1
for i in range(n):
    for t in range(n):
        if i<n-t-1:# условие диагонали
            a[i][t]=0
for i in range(n):
    for t in range(n):
        if i>n-t-1:# условие диагонали
            a[i][t]=2
for i in range(n):#выводим массив
    print()
    for t in range(n):
        print(a[i][t],end=' ')
####################################
#6
def  swap_columns(a, i, j): # ТЗ
    for m in range(len(a)):
        for n in range(len(a[m])): #пробегаем по всем значениям меняем значения местами
            if a[m][n] == i:
                a[m][n]= j
            elif a[m][n] ==j:
                a[m][n]=i
    return a
a = []# создаём нужные переменные
n = int(input())
for i in range(n):
    a.append([int(j) for j in input().split()])#заполняем массив
print(a)
i =int(input())#выбираем какие значения поменять
j =int(input())
swap_columns(a,i,j)
######################################
#7
n= 10
m =11
a = [[m*i+j+1 if i%2==0 else m*(i+1)-j  for j in range(m)]for i in range(n)]
#it's big brain time
#если строка чётная(0,2,4...), то значения идут слева на право, m*i - первое значение строки, m*(i+1) - первое значение следующей строки
#https://www.youtube.com/watch?v=dQw4w9WgXcQ
for i in range(n):#выводим массив
    print()
    for t in range(m):
        print(a[i][t],end=' ')


    