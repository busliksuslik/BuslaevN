err=True
while err==True:
    try:
        summ = int(input('сумма'))
    except ValueError:
        print('недопустимый формат')
    else:
        err=False
err=True
while err==True:
   try:
       years = int(input('года'))
   except ValueError:
        print('недопустимый формат')
   else:
        err=False
err=True
while err == True:
    try:
        percent = int(input('процентная ставка'))
    except ValueError:
        print('недопустимый формат')
    else:
        err = False
try:
    end = summ*(1+percent/100)
except OverflowError:
    print('Слишком большие числа')
else:
    for i in range(1,years+1):
        try:
            end = summ*(1+percent/100)**i
        except OverflowError:
            print('Слишком большие числа')
        else:
            print(i,'год ',round(end,2))
if err==True:
    print('прибыль: ', round(end,2))