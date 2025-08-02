# Odbierz od użytkownika liczbę całkowitą i sprawdź, czy jest ona palindromem.
# Palindrom to liczba, która czytana od przodu i od tyłu jest taka sama, np. 121, 12321.
# Aby sprawdzić jej długość, użyj funkcji len(liczba).

value = input("Podaj liczbę całkowitą: ")
if value == value[::-1]:
    print(f"Liczba {value} jest palindromem.")
else:
    print(f"Liczba {value} nie jest palindromem.")

# Sprawdzenie długości liczby
if len(value) % 2 == 0 and int(value) % 11 == 0:
    print(f"Liczba {value} jest liczbą palindromiczną.")
