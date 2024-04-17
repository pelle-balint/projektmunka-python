from random import *
import os

def bevisz1(l, l2, l3):
    os.system("cls")
    f = open("igenigen.txt", "r", encoding="UTF-8")
    f.close()
    print('1. lefutott')

def bevisz2(l, l2, l3):
    os.system("cls")
    f = open("igenigen2.txt", "r", encoding="UTF-8")
    f.close()
    print('2. lefutott')

def main():
    list, list2, list3 = [], [], []
    x = int(input("Melyiket kéred? (1 vagy 2): "))
    
    while x != 1 and x != 2:
        os.system("cls")
        print("Még mindig csak 1 vagy 2 az elfogadott")
        x = int(input("Melyiket kéred? (1 vagy 2): "))
        os.system("cls")

    if x == 1:
        bevisz1(list, list2, list3)
        
    else:
        bevisz2(list, list2, list3)

main()