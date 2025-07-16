# Zapytaj użytkownika o liczbę i sprawdź, czy jest dodatnia, ujemna czy równa zero.

value = float(input("Podaj liczbę: "))

if value > 0:
    print(f"Liczba {value} jest dodatnia.")
elif value < 0:
    print(f"Liczba {value} jest ujemna.")
else:
    print("Liczba jest równa zero.")