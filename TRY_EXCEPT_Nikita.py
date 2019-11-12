#1
err=True
while err==True: #цикл для введения нач.суммы
    try:
        summ = int(input('сумма'))
    except ValueError: # ошибка формата (если введены буквы)
        print('недопустимый формат')
    else:
        err=False #если ошибок нет идём дальше
err=True
while err==True:#цикл для введения кол-ва лет
   try:
       years = int(input('года'))
   except ValueError:# ошибка формата (если введены буквы)
        print('недопустимый формат')
   else:
        err=False#если ошибок нет идём дальше
err=True
while err == True:#цикл для введения процентной ставки
    try:
        percent = int(input('процентная ставка'))
    except ValueError:# ошибка формата (если введены буквы)
        print('недопустимый формат')
    else:
        err = False#если ошибок нет идём дальше
try:                               #здесь пояснение
    end = summ*(1+percent/100)     #тип int поддерживает огромные числа, a float нет
except OverflowError:              #тут проверка будет ли float умещатся
    print('Слишком большие числа') #
else:#если ошибок нет идём дальше
    for i in range(1,years+1):
            end = summ*(1+percent/100)**i
            print(i,'год ',round(end,2))
    print('прибыль: ', round(end,2))
#2
a = int(input()) #ввод делителя
try: 
    b= 100/a #делим 100 на а
except ZeroDivisionError: # if a==0:
    b=0
else:
    b = 100/a
finally:# сдесь просто ради того чтобы вставить, если убрать finally ничего не изменится
    print(b)