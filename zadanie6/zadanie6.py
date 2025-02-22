def dziesietna_na_trojkowy(liczba):
    wynik = ""

    while liczba > 0:
        wynik += str(liczba % 3)
        liczba //= 3

    return wynik[::-1]

print("WYNIK DODAWANIA: " + dziesietna_na_trojkowy(int("101112", 3) + int("121", 9)))
print("WYNIK ODEJMOWANIA: " + dziesietna_na_trojkowy(int("101112", 3) - int("121", 9)))