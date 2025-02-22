a = 0
b = 1
c = 0
n = 333333666666999999
ile = 0

while(n > 0):
    a = n % 10
    n = int(n // 10)
    if a % 2 == 0:
        c = int(c + b * (a // 2))
    else:
        c = int(c + b)
        ile += 1
    b = b * 10

print(f"REZULTAT\nc = {c}\nIle iteracji tego gowna = {ile}")