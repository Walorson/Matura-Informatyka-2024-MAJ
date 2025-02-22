file = open("liczby.txt")
lines = file.readlines()

ile = 0
wszystkie = len(lines[0])
dzielniki = [int(x) for x in lines[0].split()]
liczby = [int(x) for x in lines[1].split()]

for i in dzielniki:

    for j in liczby:

        if j % i == 0:
            ile += 1
            break

print(ile)
    