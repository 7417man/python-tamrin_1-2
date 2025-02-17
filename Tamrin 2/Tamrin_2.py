import datetime

entekhab = input("( A / B ) halat vared kardan saat khod ra vared konid :")

if entekhab == "A":
    saat = int(input("saat ra vared konid :"))
    while 0 > saat or 24 < saat:
        print("lotfan dar vared kardan saat deght kon")
        saat = int(input("lotfan saat ra vared konid :"))
        
elif entekhab == "B":
    saat = datetime.datetime.now().hour
if 0 <= saat < 6:
    print("نیمه شب بخیر")
elif 6 <= saat < 12:
    print("صبح بخیر")
elif 12<= saat < 18:
    print("بعد از ظهر بخیر")
elif 18<= saat < 24:
    print("شب بخیر")
