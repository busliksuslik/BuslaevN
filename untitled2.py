a = int(input())
try:
    b= 100/a
except ZeroDivisionError:
    b=0
else:
    b = 100/a
finally:
    print(b)