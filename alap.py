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
        print(f"A random ember: {nev[i]}, BMI-je {x}, életkora pedig: {kor[i]}")
        ell(x, nev[i], mag[i], suly[i], kor[i])
        intake(x, nev[i], mag[i], suly[i], kor[i])
    else:
        x = round((suly / ((mag / 100) ** 2)), 1)
        print(f"Az általad válaszott ember: {nev}, BMI-je {x}, életkora pedig: {kor}")
        ell(x, nev)
        intake(x, nev, mag, suly, kor)
    
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
    ker = input("Kinek a BMI-jét szeretnéd tudni?: ")
    os.system("cls")
    i = 0
    while i < n and nev[i] != ker:
        i = i + 1
    if(i < n):
        magas, sulya, neve, kora = mag[i],suly[i],nev[i], kor[i]
        bmi(magas, sulya, neve,kora, random = False)
    else:
        print("Nem található")

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
    n = len(mag)
    for i in range(n):
        for j in range(n-i-1):
            if suly[j] > suly[j+1]:
                mag[j], mag[j+1] = mag[j+1], mag[j]
                nev[j], nev[j+1] = nev[j+1], nev[j]
                suly[j], suly[j+1] = suly[j+1], suly[j]
                kor[j], kor[j+1] = kor[j+1], kor[j]
            
def main():
    mag, suly, nev, kor = [], [], [], []
    os.system("cls")
    x = input("lista 1 vagy 2?: ")
    os.system("cls")
    
    while x != "1" and x != "2":
        os.system("cls")
        x = input("lista 1 vagy 2?: ")
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
        
main()

#test2
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