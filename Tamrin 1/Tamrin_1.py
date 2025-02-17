saat = int(input("sara khanom saat ra vared kon :"))

if 0 <= saat < 6:
    print("نیمه شب بخیر")
elif 6 <= saat < 12:
    print("صبح بخیر")
elif 12<= saat < 18:
    print("بعد از ظهر بخیر")
elif 18<= saat < 24:
    print("شب بخیر")
else :
    print("sara khanom, lotfan saat beyn 0 ta 24 ra vared konid")