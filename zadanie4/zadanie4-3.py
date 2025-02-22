file = open("liczby.txt")
lines = file.readlines()

lines[0] = lines[0].split()
lines[0] = [int(x) for x in lines[0]]

lines[1] = lines[1].split()
lines[1] = [int(x) for x in lines[1]]

da_sie_przedstawic = []

for i in lines[1]:
    num = i
    for j in lines[0]:
        if num % j == 0:
            num /= j

    if num == 1:
        da_sie_przedstawic.append(i)

print(da_sie_przedstawic)