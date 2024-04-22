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
        
def dontes(nev, mag, suly,kor):
    n = len(nev)
    ker = input("Kinek a BMI-jét szeretnéd tudni?: ").capitalize()
    os.system("cls")
    i = 0
    while i < n and nev[i] != ker:
        i += 1
    if(i < n):
        magas, sulya, neve, kora = mag[i],suly[i],nev[i], kor[i]
        bmi(magas, sulya, neve,kora, random = False)
    else:
        print("Nem található")
    bubble(mag, suly, nev, kor)

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

def bubble(mag, suly, nev, kor):
    x = input("Csökkenő vagy növekvő sorrend? (súly alapján): ")
    n = len(mag)
    for i in range(n):
        if x == "csökkenő":
            for j in range(n-i-1):
                if suly[j] < suly[j+1]:
                    mag[j], mag[j+1] = mag[j+1], mag[j]
                    nev[j], nev[j+1] = nev[j+1], nev[j]
                    suly[j], suly[j+1] = suly[j+1], suly[j]
                    kor[j], kor[j+1] = kor[j+1], kor[j]
        else:
            for j in range(n-i-1):
                if suly[j] > suly[j+1]:
                    mag[j], mag[j+1] = mag[j+1], mag[j]
                    nev[j], nev[j+1] = nev[j+1], nev[j]
                    suly[j], suly[j+1] = suly[j+1], suly[j]
                    kor[j], kor[j+1] = kor[j+1], kor[j]
    ujfajl(suly,mag, nev, kor)

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
    ok = input("Szeretnéd a programot futtatni, vagy a bmi statisztikát szeretnéd?(y/n): ")
    while ok != "y" and ok != "n":
        os.system("cls")
        ok = input("Szeretnéd megtekinteni a bmi statisztikát?(y/n): ")
        os.system("cls")
    m = os.path.isfile()
    if m == True:
        if ok == "y":
            ...
        else:
            ...
    if m == False:
        if ok == "y":
            print("Nincs még létező file, ezáltal kérem várjon, itt van pár lehetőség zenéhez:")

    os.system("cls")
    print("Ez a program egy osztály adatait és bmi számitásait végzi el. \n")
    b = input("Akarsz-e saját adatokat írni?\nHa nem, akkor megtudod tekinteni az adatokat. (y/n): ")
    os.system("cls")

    while b != "y" and b != "n":
        os.system("cls")
        b = input("Akarsz-e saját adatokat rögzíteni az adattárban?\nHa nem, akkor megtudod tekinteni az adatokat. (y/n): ")
        os.system("cls")
    if b == "y":
        h = input("Melyik fájlba akarsz adatot rögzíteni? (1 vagy 2): ")
        os.system("cls")
        if h == "1":
            hozzairas("lista1.txt")
        elif h == "2":
            hozzairas("lista2.txt")
        else:
            raise ValueError
    elif b == "n":
        os.system("cls")
        x = input("Melyik lista adatait szeretnéd megtekinteni? lista 1 vagy 2?: ")
        os.system("cls")
    
        while x != "1" and x != "2":
            os.system("cls")
            x = input("Melyik lista adatait szeretnéd megtekinteni? lista 1 vagy 2?: ")
            os.system("cls")
        
        if x == "1":
            olvas("lista1.txt", mag, suly, nev, kor)
            os.system("cls")
        else:
            olvas("lista2.txt", mag, suly, nev, kor)

    y = input("Random ember BMI értékét kéred(random), vagy meg akarod nézni a név listát és az alapján dönteni(döntés)?: ")
        
    while y != "random" and y != "döntés":
        os.system("cls")
        y = input("random vagy döntés?: ")
        os.system("cls")
            
    if y == "döntés":
        os.system("cls")
        print(*nev, sep="; ")
        dontes(nev, mag, suly, kor)
    else:
        random = True
        bmi(mag, suly, nev, kor, random)
        bubble(mag, suly, nev, kor)

    fullbmi(mag, suly, nev)    
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