# Przygotuj funkcję, która przyjmuje rok urodzenia i zwraca wiek osoby. Sprawdż, czy ta osoba jest
# pełnoletnia, czy nie. Wiek obliczaj na podstawie aktualnego roku oraz czy jest to rok przestępny.

cureent_year = int(input("Podaj aktualny rok kalendarzowy: "))
birth_year = int(input("Podaj rok urodzenia: "))
age = cureent_year - birth_year

print(f'Twój wiek wynosi: {age}')
if age >= 18:
    print("Jesteś pełnoletni/a.")
else:
    print("Będziesz pełnoletni/a za", 18 - age, "lat.")

# Sprawdzenie, czy rok urodzenia jest przestępny
if birth_year % 4 == 0 and birth_year % 100 != 0 or birth_year % 400 == 0:
    print(f"Twój rok urodzenia jest rokiem przestępnym.")