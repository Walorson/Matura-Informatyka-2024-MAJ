import copy

#Zadanie 1.1
plansza1_1a = [
    [None, None, None, None],
    [None, 1, 1, 0],
    [None, 0, 1, 0],
    [None, 0, 1, 1]
]

plansza1_1b = [
    [None, None, None, None],
    [None, 1, 1, 1],
    [None, 0, 0, 1],
    [None, 1, 1, 1],
    [None, 1, 0, 0],
    [None, 1, 1, 1]
]

plansza1_1c = [
    [None, None, None, None, None, None],
    [None, 1, 0, 0, 0, 0],
    [None, 1, 1, 0, 0, 1],
    [None, 0, 1, 0, 0, 1],
    [None, 0, 1, 1, 1, 0],
    [None, 0, 1, 0, 1, 1]
]

#Zadanie 1.2 #rozwiązane metodą prób i błędów
plansza1_2a = [
    [None, None, None, None, None, None],
    [None, 1, 0, 1, 1, 1],
    [None, 0, 1, 1, 1, 1],
    [None, 1, 1, 1, 1, 1],
    [None, 1, 1, 1, 1, 1],
    [None, 1, 1, 1, 1, 1]
]

#Również metodą prób i błędów ~2 minuty mi zajęło xd
plansza1_2b = [
    [None, None, None, None, None],
    [None, 1, 1, 1, 1],
    [None, 0, 0, 0, 1],
    [None, 0, 0, 0, 1],
    [None, 0, 0, 0, 1],
]

A = plansza1_1a
n = len(A) - 1 #rozmiar Y
m = len(A[0]) - 1 #rozmiar X
P = copy.deepcopy(A)

P[1][1] = True

for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i][j] == 0:
            P[i][j] = False
        else:
            if i == 1 and j != 1:
                P[i][j] = P[i][j - 1]
            if i != 1 and j == 1:
                P[i][j] = P[i - 1][j]
            if i != 1 and j != 1:
                P[i][j] = P[i][j - 1] or P[i - 1][j]

print(P[n][m])