"""
Author: Jakub Kupka
"""

import random

from oddelovac import oddelovac

def hlavni():
    spust_hru()

def spust_hru():
    print(f"""Hi there!
{oddelovac}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{oddelovac}""")
    prubeh_kola()

def prubeh_kola():
    """
    vloženi zadaní od hrače, počítaní kol a
    konečné vyhodnoceni
    """
    hra_probiha = True
    pocet_pokusu = 0
    hadane_cislo = generovani_cisla()
    while hra_probiha is True:
        hadani = input(">>> ")
        pocet_pokusu += 1
        if kontrola_hadani(hadani) == True:
            hra_probiha = vyhodnoceni_hry(
                    hadane_cislo, hadani,
                    hra_probiha, pocet_pokusu)

def generovani_cisla() -> list:
    """
    generuje čtyřmístné číslo bez nuly na
    začátku a bez duplicit
    """
    unikatni = []
    while len(unikatni) < 4:
        navrh = random.randint(0, 9)
        if navrh not in unikatni:
            unikatni.append(navrh)
            if unikatni[0] == 0:
                unikatni.pop(0)
    return unikatni

def kontrola_hadani(hadani: str) -> bool:
    """
    kontrola čísla z hlediska: počtu znaků,
    pouze číslo, duplicity, počáteční nula
    """
    kontrola_vstupu = True
    if len(hadani) != 4 or not hadani.isnumeric():
        print("You are supposed to enter only 4 digit number")
        kontrola_vstupu = False
    elif int(hadani[0]) == 0:
        print("You are not allowed to enter 0 as a first number")
        kontrola_vstupu = False
    elif hadani:
        for cislo in hadani:
            if hadani.count(cislo) > 1:
                print("You are not allowed to enter any number with duplicates")
                kontrola_vstupu = False
                break
    return kontrola_vstupu

def vyhodnoceni_hry(hadane_cislo: list, hadani: str,
        hra_probiha: bool, pocet_pokusu: int) -> bool:
    """
    zjištění shodných čísel, vyhodnocení a
    oznamení
    """
    bulls = 0
    cows = 0
    hadani_prevod = list(map(int,hadani))
    if hadani_prevod == hadane_cislo:
        hra_probiha = False
        print(f"""Correct, you've guessed the right number
in {pocet_pokusu} guesses!
{oddelovac}
That's {slovni_hodnoceni(pocet_pokusu)}""")
        quit()
    for index, cislo in enumerate(hadane_cislo):
        if cislo in hadani_prevod and \
                cislo == hadani_prevod[index]:
            bulls += 1
            continue
        elif cislo in hadani_prevod and \
                cislo != hadani_prevod[index]:
            cows += 1
    print(f"""{vyhodnoceni_cisla_pro_bulls(bulls)} {bulls}, {vyhodnoceni_cisla_pro_cows(cows)} {cows}
{oddelovac}""")
# nevím jak kontroluješ, ale řadek 97 jsem Ti tady nechal
    print(hadane_cislo, hadani_prevod)
    return hra_probiha

def vyhodnoceni_cisla_pro_bulls(bulls: int) -> str:
    vysledek_pro_bulls = bulls
    if bulls <= 1:
        vysledek_pro_bulls = "bull"
    else:
        vysledek_pro_bulls = "bulls"
    return vysledek_pro_bulls

def vyhodnoceni_cisla_pro_cows(cows: int) -> str:
    if cows <= 1:
        vysledek_pro_cows = "cow"
    else:
        vysledek_pro_cows = "cows"
    return vysledek_pro_cows

def slovni_hodnoceni(pocet_pokusu: int) -> str:
    if pocet_pokusu <= 4:
        vysledek_hodnoceni = "amazing"
    elif pocet_pokusu <= 10:
        vysledek_hodnoceni = "avarage"
    else:
        vysledek_hodnoceni = "not so good"
    return vysledek_hodnoceni

hlavni()


# Otázky:
# 1. je nějaká cesta abych se vyhnul v řádku 42 použití druhého if ve while?
# Případně, je to takto akceptovatelné?
# 2. jak lze zalomit text na řádcích 61 a 90. Zkoušel jsem něco podle PEP-8,
# ale u řádku 61 mi Pycharm nabízí další úvozovky na novém řádku, což pravděpodbně
# nebude akceptovatelné podle PEP-8 (alespoň jsem tam tohle řešení nenašel). Na řádku 90
# si nejsem jistý jak s takto formatovaným textem zacházet a zalomit jej.
# 3. Zkoušel jsem podle externích zdrojů vložit časoměřič, ale nedařilo se mi. Mohl bych
# poprosit o ukázku na tomto příkladu? Díky, Kuba