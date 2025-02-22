file = open("liczby.txt")
lines = file.readlines()

lines[0] = lines[0].split()
lines[0] = [int(x) for x in lines[0]]
liczby = lines[0]

najwieksza_srednia = 0
od_jakiej_liczby = None
ile_liczb = None

for n in range(50, len(liczby)):
    for i in range(0, len(liczby) - (n - 1)):
        srednia = sum(liczby[i:n + i]) / len(liczby[i:n + i])
        if srednia > najwieksza_srednia:
            najwieksza_srednia = srednia
            od_jakiej_liczby = liczby[i]
            ile_liczb = n

print("Największa średnia: " + str(najwieksza_srednia))
print("Dla " + str(ile_liczb) + " liczb")
print("zaczynających się od tej liczby: " + str(od_jakiej_liczby))

#Wymagana forma odpowiedzi
print("\nODPOWIEDŹ: " + str(najwieksza_srednia) + " " + str(ile_liczb) + " " + str(od_jakiej_liczby))