# Napisz program, który sprawdzi, czy liczba podzielna przez 5 i 11.

value = int(input("Podaj liczbę: "))

if value % 5 == 0 and value % 11 == 0:
    print(f"Liczba {value} jest podzielna przez 5 i 11.")
elif value % 5 == 0:
    print(f"Liczba {value} jest podzielna przez 5, ale nie przez 11.")
elif value % 11 == 0:
    print(f"Liczba {value} jest podzielna przez 11, ale nie przez 5.")
else:
    print(f"Liczba {value} nie jest podzielna ani przez 5, ani przez 11.")
