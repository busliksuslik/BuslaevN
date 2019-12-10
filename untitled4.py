def rounde(num):
    return round(num,1)
def loans(zp):
    zp = zp
    print('после уплаты пенсионной ставки (2%) у вас осталось',rounde(zp - zp*0.02),'€')
    zp = zp - zp*0.02
    print('после уплаты страхования от безработицы (1.6%) у вас осталось',rounde(zp-zp*0.016),'€')
    zp = zp - zp*0.016
    print('после уплаты взноса государственного социального страхования(11%) у вас осталось',rounde(zp-zp*0.11),'€')
    zp = zp - zp*0.11
    if zp*12<=14000:
        zp = zp-6000/12
        mini=6000/12
    elif zp*12>14000 and zp*12<25000:
        mini = rounde(500-0.55555555556*(zp-1200))
        zp-= mini/12
    elif zp*12>25200:
        mini = 0
        zp = zp
    print(mini,'размер необлагаемой зарплаты\n',rounde(zp),' столько зарплаты облагается налогом после уплаты страхований')
    if zp*12<20000:
        zp =zp -  (zp*0.20)
        print('после выплаты подоходного налога(20%) у вас осталось',rounde(zp)+ mini,'€')
    elif zp*12>20000 and zp <62800:
        zp =zp - (zp*0.23)
        print('после выплаты подоходного налога(23%) у вас осталось',rounde(zp)+ mini,'€')
    else:
        zp =zp - (zp*0.314)
        print('после выплаты подоходного налога(31,4%) у вас осталось',rounde(zp)+ mini,'€')
    zp = zp+mini
    return round(zp,1)
num_peo = int(input('как многораотающих людей в семье'))
new_zp = 0
spizheno  = 0
alll=0
for i in range(num_peo):
    br_zp= int(input('введите брутто зарплату'))
    new_zp = loans(br_zp)
    alll = alll+new_zp
    spizheno =spizheno+  (br_zp-new_zp)
ch_num = int(input('кол-во детей:'))
print('за первого и второго ребёнка по 60 дальше по 100')
if ch_num >= 3:
    ch_num-=2
    new_zp = new_zp +120 + ch_num*100
    br_zp = new_zp +120 + ch_num*100
elif ch_num>=1 and ch_num<3:
    new_zp = new_zp + ch_num*60
    br_zp = new_zp + ch_num*60
print(round(alll,1),'   ',round(alll*12,1),' ',round(spizheno,1))


