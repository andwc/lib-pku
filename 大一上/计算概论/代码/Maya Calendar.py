num=int(input())
print(num)
haab={'pop':0,'no':20,'zip':40,'zotz':60,'tzec':80,'xul':100,'yoxkin':120,'mol':140,'chen':160,'yax':180,'zac':200,'ceh':220,'mac':240,'kankin':260,'muan':280,'pax':300,'koyab':320,'cumhu':340,'uayet':360}
tzolkin={1:'imix',2:'ik',3:'akbal',4:'kan',5:'chicchan',6:'cimi',7:'manik',8:'lamat',9:'muluk',10:'ok',11:'chuen',12:'eb',13:'ben',14:'ix',15:'mem',16:'cib',17:'caban',18:'eznab',19:'canac',20:'ahau'}
day=0
for i in range(num):
    shuru=input().split()
    day=int(shuru[0][:len(shuru[0])-1])+haab.get(shuru[1])+365*int(shuru[2])
    #print(day)
    year=day//260
    day%=260
    day+=1
    month=day%13
    if month==0:
        month=13
    day%=20
    if day==0:
        day=20
    print(month,tzolkin.get(day),year)