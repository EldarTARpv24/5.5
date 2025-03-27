from random import *

tase = int(input("sisesta tase (1, 2, 3): "))
tase1 = randint(1, 2)
tase2 = randint(1, 4)
tase3 = randint(1, 2)
koikkusimused = 0
oigedv = 0
while True:
    if tase < 1 or tase > 3:
        print("vale arv")
        break
    else:    
        koikkusimused += 1  

    if tase == 1:
        num = randint(1, 10)
        num1 = randint(1, 10)

        if tase2 == 1:
            tasevastus = num - num1
            try:
                vastusinim = int(input(f"{num} - {num1} ="))
                if tasevastus == vastusinim:
                    oigedv += 1  
                    print(" ")
                    print("õige ept")
                    print(" ")
                elif vastusinim == 00:
                    break
                else:
                    print(" ")
                    print("vale, vatke null")
                    print(" ")
            except ValueError:
                print("kirjutage arv")

        elif tase1 == 2:
            tasevastus = num + num1
            try:
                vastusinim = int(input(f"{num} + {num1} ="))
                if tasevastus == vastusinim:
                    oigedv += 1
                    print(" ")
                    print("õige ept")
                    print(" ")
                elif vastusinim == 00:
                    break
                else:
                    print(" ")
                    print("vale, vatke null")
                    print(" ")
            except ValueError:
                print("kirjutage arv")
    elif tase == 2:
        num2 = randint(1, 20)
        num3 = randint(1, 20)
        if tase2 == 1:
            taseotv = num2 - num3
        elif tase2 == 2:
            taseotv = num2 + num3
        elif tase2 == 3:
            taseotv = num2 * num3
        elif tase2 == 4:
            taseotv = num2 / num3
        try:
            vastustase2 = float(input(f"{num2} {['-', '+', '*', '/'][tase2 - 1]} {num3} ="))
            if round(taseotv, 2) == round(vastustase2, 2):
                oigedv += 1
                print(" ")
                print("õige ept")
                print(" ")
            elif vastustase2 == 00:
                break
            else:
                print(" ")
                print("vale, vatke null")
                print(" ")
        except ValueError:
            print("kirjutage arv")
    elif tase == 3:
        num2 = randint(1, 100)
        num3 = randint(1, 100)

        if tase3 == 1:
            taseotv = num2 * num3
        elif tase3 == 2:
            if num3 == 0:
                print(" ")
                print("Ne delite na 0")
                print(" ")
                continue
            taseotv = num2 / num3
        try:
            vastustase2 = float(input(f"{num2} {['*', '/'][tase3 - 1]} {num3} = "))
            if round(taseotv, 2) == round(vastustase2, 2):
                oigedv += 1
                print(" ")
                print("õige ept")
                print(" ")
            elif vastustase2 == 00:
                break
            else:
                print(" ")
                print("vale, vatke null")
                print(" ")
        except ValueError:
            print("kirjutage arv")

if koikkusimused > 0:
    protsenti = (oigedv / (koikkusimused-1)) * 100 
    if protsenti < 60:
        hinne = 2
    elif 60 <= protsenti < 75:
        hinne = 3
    elif 75 <= protsenti < 90:
        hinne = 4
    else:
        hinne = 5

    print(" ")
    koikkusimused-=1 #et ei loeks 00 nagu vastust
    print(f"tulemus: {oigedv}/{koikkusimused} {protsenti}%")
    print(f"hinne: {hinne}")
    print(" ")
else:
    print("test pole sooritatud")
