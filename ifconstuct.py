#1
a= int(input())
b= int(input())
if a>b:
    print(b)
else:
    print(a)
#2
a= int(input())
if a>0:
    print('1')
elif a<0:
    print('-1')
else:
    print('0')
#3
x1= int(input('координата х для 1 клетки '))
y1= int(input('координата у для 1 клетки '))
x2= int(input('координата х для 2 клетки '))
y2= int(input('координата у для 2 клетки '))
if ((x1%2==y1%2)and(y1%2==y2%2)):
    print('yes')
else:
    print('no')
#4
a = int(input())
b = False
if a%4==0:
    b=True
if a%100 ==0:
    b=False
if a%400 == 0:
    b=True
if b == True:
    print('Високосный')
else:
    print('не високосный')
#5
a= int(input())
b= int(input())
c =int(input())
if (a<=b)and (a<=c):
    print(a)
elif (b<=a)and(b<=c):
    print(b)
elif (c<=a)and(c<=b):
    print(c)
#6
a= int(input())
b= int(input())
c =int(input())
if (a==b)and(a==c):
    print('3')
elif ((a==b)or(a==c)or(b==c)):
    print('2')
else:
    print('0')
#7
x1= int(input('координата х для 1 клетки '))
y1= int(input('координата у для 1 клетки '))
x2= int(input('координата х для 2 клетки '))
y2= int(input('координата у для 2 клетки '))
if x1==x2 or y1==y2 :
    print('yes')
else:
    print('no')
#8
x1= int(input('координата х для 1 клетки '))
y1= int(input('координата у для 1 клетки '))
x2= int(input('координата х для 2 клетки '))
y2= int(input('координата у для 2 клетки '))
if (x1==x2+1)or(x1==x2-1)and(y1==y2+1)or(y1==y2-1):
    print('yes')
else:
    print('no')
#9
import math
x1= int(input('координата х для 1 клетки '))
y1= int(input('координата у для 1 клетки '))
x2= int(input('координата х для 2 клетки '))
y2= int(input('координата у для 2 клетки '))
if abs(x1-x2)==abs(y1-y2):
    print('yes')
else:
    print('no')
#10
x1= int(input('координата х для 1 клетки '))
y1= int(input('координата у для 1 клетки '))
x2= int(input('координата х для 2 клетки '))
y2= int(input('координата у для 2 клетки '))
if (x1==x2 or y1==y2) or (x1-x2==y1-y2) :
    print('yes')
else:
    print('no')
#11
x1= int(input('координата х для 1 клетки '))
y1= int(input('координата у для 1 клетки '))
x2= int(input('координата х для 2 клетки '))
y2= int(input('координата у для 2 клетки '))
if  (x2-x1==2) and (y2-y1==1) or (x2-x1==-2) and (y2-y1==-1) or (y2-y1==2) and (x2-x1==1) or (y2-y1==-2) and (x2-x1==-1) :
    print('yes')
else:
    print('no')
#12
n = int(input())
m = int(input())
k= int(input())
vib = False
for i in range(1,m):
    if k== i*n:
        vib=True
for i in range(1,n):
    if k == i*m:
        vib=True
if vib == True:
    print('Yes')
else:
    print('No')
#312
N = int(input())
M = int(input())
x = int(input())
y = int(input())
if x<=N//2 and y<=M//2:
    if x<y:
        print(x)
    else:
        print(y)
elif x>N//2 and y<M//2:
    if (N-x)<y:
        print(N-x)
    else:
        print(y)
elif x>N//2 and y>M//2:
    if N-x<M-y:
        print(N-x)
    else:
        print(M-y)
elif x<N//2 and y>M//2:
    if x<M-y:
        print(x)
    else:
        print(M-y)        
        























