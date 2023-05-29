"""Proiect realizat de Banta Maria-Teodora si Bejan Claudia-Monica, 1.1."""

import random

from lista_cuvinte import cuvinte_de_ghicit as lista_cuvinte

def inima():
    print("    **     **")
    print("  **  ** **  **")
    print("**      *     **")
    print("**              **")
    print(" **            **")
    print("  **         **")
    print("     **   **")
    print("       **")
    print("")

cuvant = random.choice(lista_cuvinte).lower()                           #alege cuvant random din lista convertita in litere mici

"""cuvant = 'onomatopee'.lower()"""

cuvant_initial = list(cuvant)                                            #pune cuvantul din lista ales intr-o lista de caractere cu care o sa lucram

"""o _ o _ _ _ o _ e e"""
"""literele sunt lowercase"""
"""avem 3 incercari"""

for index, value in enumerate(cuvant_initial):
    if cuvant_initial[0] != value and cuvant_initial[-1] != value:       #pune "_" in mijlocul cuvantului fara literele de sunt aceleasi cu prima si ultima din cuvant
        cuvant_initial[index] = '_'

incercari = int(input("Scrie numarul de incercari dorit (maxim 6): "))
print(f"Ai la dispozitie {incercari} incercari. Bafta!")
print(" ".join(cuvant_initial))                                          #concatenare " " la cuvantul cu "_"

numar_incercari = 0
set_litere_incercate = set()                                             #creare set cu literele deja incercate

print(" ____")
print(" | ")
print(" |   ")
print("_|_  ")
print("")

while numar_incercari <= incercari:
    litera_incercata = input("Alege o litera: ").lower()
    print(" ")

    if litera_incercata in cuvant_initial:
        print("Litera deja este afisata pe ecran.")
        print(" ")

    if litera_incercata in set_litere_incercate:
        print("Ai mai ales litera asta! Incearca o litera diferita!")
        print(" ")

    elif litera_incercata in cuvant:
        for index, value in enumerate(cuvant):
            if litera_incercata == value:
                cuvant_initial[index] = litera_incercata                 #adauga litera ghicita buna in cuvant
    else:
        if litera_incercata not in set_litere_incercate:
            numar_incercari += 1
        set_litere_incercate.add(litera_incercata)                       #daca nu este litera buna pentru cuvant o pune in setul de litere incercate

#1 incercare
        if incercari ==1:
            if numar_incercari == 1:
                print(f"Ai pierdut! Cuvantul initial era: {cuvant}")
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_ / \ ")
                print(" ")
                break

#2 incercari
        if incercari ==2:
            if numar_incercari == 2:
                print(f"Ai pierdut! Cuvantul initial era: {cuvant}")
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_ / \ ")
                print(" ")
                break

            print(f"Mai ai {2 - numar_incercari} incercari. ")
            print(f"Literele incercate sunt: {','.join(set_litere_incercate)}")

            if 2-numar_incercari == 1:
                print(" ____")
                print(" |  (xx)")
                print(" |   ")
                print("_|_  ")
                print(" ")

#3 incercari
        if incercari ==3:
            if numar_incercari == 3:
                print(f"Ai pierdut! Cuvantul initial era: {cuvant}")
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_ / \ ")
                print(" ")
                break

            print(f"Mai ai {3 - numar_incercari} incercari. " )
            print(f"Literele incercate sunt: {','.join(set_litere_incercate)}")

            if 3-numar_incercari == 1:
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_  ")
                print(" ")

            if 3 - numar_incercari == 2:
                print(" ____")
                print(" |  (xx)")
                print(" |   ")
                print("_|_  ")
                print(" ")

#4 incercari
        if incercari == 4:
            if numar_incercari == 4:
                print(f"Ai pierdut! Cuvantul initial era: {cuvant}")
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_ / \ ")
                print(" ")
                break

            print(f"Mai ai {4 - numar_incercari} incercari. " )
            print(f"Literele incercate sunt: {','.join(set_litere_incercate)}")

            if 4-numar_incercari == 1:
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_  ")
                print(" ")

            if 4 - numar_incercari == 2:
                print(" ____")
                print(" |  (xx)")
                print(" |   ")
                print("_|_  ")
                print(" ")

            if 4 - numar_incercari == 3:
                print(" ____")
                print(" |  (  )")
                print(" |   ")
                print("_|_  ")
                print(" ")

#5 incercari
        if incercari == 5:
            if numar_incercari == 5:
                print(f"Ai pierdut! Cuvantul initial era: {cuvant}")
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_ / \ ")
                print(" ")
                break

            print(f"Mai ai {5 - numar_incercari} incercari. ")
            print(f"Literele incercate sunt: {','.join(set_litere_incercate)}")

            if 5 - numar_incercari == 1:
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_ / ")
                print(" ")

            if 5 - numar_incercari == 2:
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_  ")
                print(" ")

            if 5 - numar_incercari == 3:
                print(" ____")
                print(" |  (xx)")
                print(" |  /|")
                print("_|_  ")
                print(" ")

            if 5 - numar_incercari == 4:
                print(" ____")
                print(" |  (xx)")
                print(" |   | ")
                print("_|_  ")
                print(" ")

#6 incercari
        if incercari == 6:
            if numar_incercari == 6:
                print(f"Ai pierdut! Cuvantul initial era: {cuvant}")
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_ / \ ")
                print(" ")
                break

            print(f"Mai ai {6 - numar_incercari} incercari. ")
            print(f"Literele incercate sunt: {','.join(set_litere_incercate)}")

            if 6 - numar_incercari == 1:
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_ / ")
                print(" ")

            if 6 - numar_incercari == 2:
                print(" ____")
                print(" |  (xx)")
                print(" |  /|\ ")
                print("_|_  ")
                print(" ")

            if 6 - numar_incercari == 3:
                print(" ____")
                print(" |  (xx)")
                print(" |  /|")
                print("_|_  ")
                print(" ")

            if 6 - numar_incercari == 4:
                print(" ____")
                print(" |  (xx)")
                print(" |   |")
                print("_|_  ")
                print(" ")

            if 6 - numar_incercari == 5:
                print(" ____")
                print(" |  (xx)")
                print(" |    ")
                print("_|_  ")
                print(" ")


    if '_' not in cuvant_initial:
        print(" ")
        print(f"Cuvantul este: {cuvant}")
        print("   Ai castigat!")
        inima()
        break

    print(" ".join(cuvant_initial))                             #.join concatenează toate elementele din lista cuvant_initial într-un singur șir de caractere