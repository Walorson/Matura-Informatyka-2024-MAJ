def shortcut(n):
    wynik = 0
    mnoznik = 1
    krok = 1

    while(n // krok != 0):
        num = (n // krok) % 10
        if num % 2 == 1:
            wynik += num * mnoznik
            mnoznik *= 10

        krok *= 10

    return wynik

#print(shortcut(294762))

ile = 0
najwieksza = 0
file = open("skrot.txt")
lines = file.readlines()
    
for i in lines:
    if len(i) > 0:
        i = int(i)

    if shortcut(i) == 0:
        ile += 1

        if i > najwieksza:
            najwieksza = i


print("Tyle jest liczb: " + str(ile))
print("A no i ta jest najwieksza: " + str(najwieksza))

import math

file2 = open("skrot2_przyklad.txt")
lines2 = file2.readlines()

for i in lines2:
    if(len(i) > 0):
        i = int(i)
    
    if(shortcut(i) != 0):
        if math.gcd(i, shortcut(i)) == 7:
            print(i)