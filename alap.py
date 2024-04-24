from random import *
import os

def olvas(filenev, mag, suly, nev, kor):
    f = open(f"{filenev}", "r", encoding="UTF-8")
    sor = f.readline().strip()
    while sor != "":
        y = sor.split("; ")
        mag.append(int(y[0]))
        suly.append(int(y[1]))
        nev.append(y[2])
        kor.append(int(y[3]))
        sor = f.readline().strip()
    f.close()

def bmi(mag, suly, nev,kor, random = False):
    if random == True:
        i = randint(0, len(mag))
        x = round((suly[i] / ((mag[i] / 100) ** 2)), 1)
        if nev[i] != "Gabó":
            print(f"A random ember: {nev[i]}, BMI-je {x}, életkora pedig: {kor[i]}")
            ell(x, nev[i])
            intake(x, nev[i], mag[i], suly[i], kor[i])
        else:
            os.system("start microsoft-edge:https://www.ritafoldi.hu/a-fogyas-alapjai-hogyan-mit-mikor-es-mennyit/")
    else:
        if nev != "Gabó":
            x = round((suly / ((mag / 100) ** 2)), 1)
            print(f"Az általad válaszott ember: {nev}, BMI-je {x}, életkora pedig: {kor}")
            ell(x, nev)
            intake(x, nev, mag, suly, kor)
        else:
            os.system("start microsoft-edge:https://www.ritafoldi.hu/a-fogyas-alapjai-hogyan-mit-mikor-es-mennyit/")
    
def ell(rate, nev):
    if rate < 18.5:
        print(nev, "alacsony testsúlyú")
    elif rate < 24.9:
        print(nev, "normális testsúlyú")
    elif rate < 29.9:
        print(nev, "túlsúlyos")
    else:
        print(nev, "elhízott")
        
def dontes(nev):
    n = len(nev)
    ker = input("Kinek a BMI-jét szeretnéd tudni?: ").capitalize()
    os.system("cls")
    i = 0
    while i < n and nev[i] != ker:
        i += 1
    if(i < n):
        return i
    else:
        return -1

def intake(bmi, neve, mag, suly, kor):
    normal, n, kg, nap = 24.9, [1.2, 1.375, 1.55, 1.725, 1.9], 7700, 55
    szam = 0
    for i in range(len(n)):
        szam += n[i]
    akt = szam / len(n)
    bmr = 66.47 + (13.75 * suly) + (5.003 * mag) - (6.755 * kor)
    okal = bmr * akt
    new = (normal / bmi) * suly
    total = (suly - new) * kg
    dkal = total / nap
    kal = okal - dkal
    #Az aktivitási szint az n, ezáltal mindig változni fog, hogy mennyi kalória kell, erőltetett diéta kalória számai találhatóak itt
    print(f"A normális BMI szint eléréséhez ennyi kalóriát kell elfogyasztani 1 nap {neve}-nak/nek: {abs(round(kal))}, és elérni kívánt súlya kb. {round(new, 1)}kg")

def csere(mag, nev, suly, kor, j):
    mag[j], mag[j+1] = mag[j+1], mag[j]
    nev[j], nev[j+1] = nev[j+1], nev[j]
    suly[j], suly[j+1] = suly[j+1], suly[j]
    kor[j], kor[j+1] = kor[j+1], kor[j]

def bubble(mag, suly, nev, kor):
    x = input("Csökkenő vagy növekvő sorrend? (súly alapján): ")
    n = len(mag)
    for i in range(n):
        if x == "csökkenő":
            for j in range(n-i-1):
                if suly[j] < suly[j+1]:
                    csere(mag, nev, suly, kor, j)
        else:
            for j in range(n-i-1):
                if suly[j] > suly[j+1]:
                    csere(mag, nev, suly, kor, j)
    return suly,mag, nev, kor

def ujfajl(mag, suly, nev, kor):
    fw = open("Rendezett.txt", "w", encoding="UTF-8")
    for i in range(len(mag)):
       fw.write(f"{mag[i]}, {suly[i]}, {nev[i]}, {kor[i]}\n")
    fw.close()

def legelhizotabb(hizas, nev):
    n = len(hizas)
    max = hizas[0]
    for i in range(1, n):
        if hizas[i] < max:
            max = i
    print("Legelhízotabb ember az osztályban:", nev[i])
            
def fullbmi(mag, suly, nev):
    elhizottnev = []
    elhizottsuly = []
    szamos = 0
    szamos2 = 0
    for i in range(len(mag)):
        szamos2 += 1
        x = round((suly[i] / ((mag[i] / 100) ** 2)), 1)
        if x > 29.9:
            szamos += 1
            elhizottnev.append(nev[szamos2])
            elhizottsuly.append(int(x))
    print("Ennyi elhízott ember van az osztályba:", szamos)
    legelhizotabb(elhizottsuly, elhizottnev)

def hozzairas(filenev):
    fa = open(f"{filenev}", "a", encoding="UTF-8")
    x = int(input("Magasság (magasabb mint 50 cm): "))
    while x < 50:
        os.system("cls")
        x = int(input("Magasság (magasabb mint 50 cm): "))
        os.system("cls")
    fa.write(f"\n{x}")

    x = int(input("Súly (több mint 20 kg): "))
    while x < 20:
        os.system("cls")
        x = int(input("Súly (több mint 20 kg): "))
        os.system("cls")
    fa.write(f"; {x}")

    x = input("Név (hosszabb 2 betűnél): ")
    while len(x) <= 2:
        os.system("cls")
        x = input("Név (hosszabb 2 betűnél): ")
        os.system("cls")
    fa.write(f"; {x}")

    x = int(input("Életkor (legalább 10 év): "))
    while x < 10:
        os.system("cls")
        x = int(input("Életkor (legalább 10 év): "))
        os.system("cls")
    fa.write(f"; {x}\n")
    fa.close()

def main():
    mag, suly, nev, kor = [], [], [], []
    os.system("cls")
    print("Ez a program egy osztály adatait és bmi számitásait végzi el. \n")
    ok = input("Szeretnéd megtekinteni a bmi statisztikát, vagy programot akarod futtatni?(y/n): ")

    while ok != "y" and ok != "n":
        os.system("cls")
        ok = input("Szeretnéd megtekinteni a bmi statisztikát, vagy programot akarod futtatni?(y/n): ")
        os.system("cls")
    m = False

    try:
        f = open("statisztika.txt", "r", encoding="UTF-8")
        sor = f.readline().strip()
        while sor != "":
            k = sor.split()
            if k[0] != "":
                m = True
        f.close()
    except:
        m == False

    if m == True:
        if ok == "y":
            print("Jó ez")
        else:
            os.system("cls")
            print("Rendben, itt a program:")

    elif m == False:
        if ok == "y":
            l = input("Nincs még létező file, ezáltal kérem várjon, itt van pár lehetőség várakozási muzsikához:\n1. Justice\n2. Vibe\n")
            while l != "1" and l != "2":
                os.system("cls")
                l = input("Csak 1est és 2est fogadunk el, kérem írja újra: ")
                os.system("cls")
            if l == "1":
                os.system("start microsoft-edge:https://www.youtube.com/watch?v=YFcM7BntI0M")
            else:
                os.system("start microsoft-edge:https://www.youtube.com/watch?v=vlLgvQErn6o")
        else:
            os.system("cls")
            print("Rendben, itt a program:")

    os.system("cls")
    print("Ez a program egy osztály adatait és bmi számitásait végzi el. \n")
    b = input("Akarsz-e saját adatokat rögzíteni?\nHa nem, akkor megtudod tekinteni az adatokat. (y/n): ")
    os.system("cls")

    while b != "y" and b != "n":
        os.system("cls")
        b = input("Nem nehéz ez. Ott a mondat végen mit kell beirni.\nAkarsz-e saját adatokat rögzíteni az adattárban?\nHa nem, akkor megtudod tekinteni az adatokat. (y/n): ")
        os.system("cls")

    if b == "y":
        h = input("Melyik fájlba akarsz adatot rögzíteni? (A vagy B): ")
        os.system("cls")
        while h != "A" and h != "B":
            os.system("cls")
            h = input("Úgy látszik nem volt elég egyértelmű. Probáljuk meg újra.\nMelyik fájlba akarsz adatot rögzíteni? (A vagy B): ")
            os.system("cls")
        if b == "A":
            hozzairas("lista1.txt")
        else:
            hozzairas("lista2.txt")

    elif b == "n":
        os.system("cls")
        x = input("Melyik osztály adatait szeretnéd megtekinteni? A osztály vagy B osztály?: ")
        os.system("cls")
    
        while x != "A" and x != "B":
            os.system("cls")
            x = input("Megint nem sikerült értelmezni a szöveget.\nTehát probáljuk meg még egyszer;\nMelyik osztály adatait szeretnéd megtekinteni? A osztály vagy B osztály?: ")
            os.system("cls")
        
        if x == "A":
            olvas("lista1.txt", mag, suly, nev, kor)
        else:
            olvas("lista2.txt", mag, suly, nev, kor)

    döntés = input("Random ember BMI értékét kéred (random), vagy meg akarod nézni a név listát és az alapján dönteni (döntés)?: ")
        
    while döntés != "random" and döntés != "döntés":
        os.system("cls")
        döntés = input("Probáljuk meg még egyszer. Tehát random VAGY döntés? Nincs más opció: ")
        os.system("cls")
            
    if döntés == "döntés":
        os.system("cls")
        print(*nev, sep="; ")
        print()
        d = dontes(nev)
        while d == -1:
            print("Nem található ilyen név. Probáld újra.")
            print()
            print(*nev, sep="; ")
            print()
            d = dontes(nev)
        bmi(mag[d], suly[d], nev[d], kor[d])
    
    else:
        bmi(mag, suly, nev, kor, random == True)
        bubble(mag, suly, nev, kor)
    
    buborek = input("Szeretnéd súly szerint növekvő vagy csökkenő sorrendbe rendezni az osztályt? (y/n): ")
    while buborek != "y" and buborek != "n":
        os.system("cls")
        buborek = input("Na akkor még egyszer.\nSzeretnéd súly szerint növekvő vagy csökkenő sorrendbe rendezni az osztályt? (y/n): ")
        os.system("cls")
    if buborek == "y":
        bubble(mag, suly, nev, kor)
        ujfajl(suly, mag, nev, kor)
    else:
        print("Hát akkor ugorjunk a végére.")
        os.system("cls")

    dontes2 = input("Szeretnéd megtekinteni a legelhízottabb személyt az osztályban? (y/n): ")
    while dontes2 != "y" and dontes2 != "n":
        os.system("cls")
        dontes2 = input("Na ez nem sikerült.\nSzeretnéd megtekinteni a legelhízottabb személyt az osztályban? (y/n): ")
        os.system("cls")
    if dontes2 == "y":
        fullbmi(mag, suly, nev)
        print()
        print("Úgy látszik vége a kódnak, nem bántunk már meg több embert ma.")   
main()

#Katy Perry - Firework
#You just gotta ignite the light
#And let it shine
#Just own the night
#Like the Fourth of July

#Cause baby, you're a firework
#Come on, show 'em what you're worth
#Make 'em go, "Oh, oh, oh"
#As you shoot across the sky
#Baby, you're a firework
#Come on, let your colors burst
#Make 'em go, "Oh, oh, oh"
#You're gonna leave 'em all in awe, awe, awe

#Katy Perry - Hot n Cold
# Cause you're hot then you're cold
# You're yes then you're no
# You're in then you're out
# You're up then you're down
# You're wrong when it's right
# It's black and it's white
# We fight, we break up
# We kiss, we make up
# (You) You don't really want to stay, no
# (You) But you don't really want to go
# You're hot then you're cold
# You're yes then you're no
# You're in then you're out
# You're up then you're down