# Odbierz od użytkownika trzy liczby i wyświetl największą z nich oraz najmniejszą.

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))
max_value = c
min_value = c

# Znajdź największą liczbę
if a > b:
    if a > c:
        max_value = a
    else:
        max_value = c
else:
    if b > c:
        max_value = b
    else:
        max_value = c

# Znajdź najmniejszą liczbę
if a < b:
    if a < c:
        min_value = a
    else:
        min_value = c
else:
    if b < c:
        min_value = b
    else:
        min_value = c

print(f"Największa liczba to: {max_value}")
print(f"Najmniejsza liczba to: {min_value}")