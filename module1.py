import random

valikud = ["kivi", "käärid", "paber"]


while True:
    print("\n1. Alustada mängu")
    print("2. Lõpetada mängu")
    valik = input("Sisesta number (1-2): ")

    if valik == "1":
        print("Vali oma käik:")
        print("1. kivi")
        print("2. käärid")
        print("3. paber")
        
        try:
            kasutaja_valik = int(input("Sisesta number (1-3): ")) - 1
            if kasutaja_valik < 0 or kasutaja_valik > 2:
                print("Vale valik! Palun sisesta number 1-3.")
                continue
        except ValueError:
            print("Vale sisend! Palun sisesta number 1-3.")
            continue

        comp_valik = random.randint(0, 2)
        
        print(f"Sinu valik: {valikud[kasutaja_valik]}")
        print(f"Arvuti valik: {valikud[comp_valik]}")

        if kasutaja_valik == comp_valik:
            print("Viik!")
        elif (kasutaja_valik - comp_valik) % 3 == 1:
            print("Sa võitsid!")
        else:
            print("Arvuti võitis!")

    elif valik == "2":
        print("Mäng lõpetatud.")
        break
    else:
        print("Vale valik! Palun sisesta 1 või 2.")