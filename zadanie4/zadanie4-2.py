file = open("liczby.txt")
lines = file.readlines()

lines[0] = lines[0].split()
lines[0] = [int(x) for x in lines[0]]
lines[0].sort(reverse=True)

print(lines[0][100])