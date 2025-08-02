# Zapytaj użytkownika o długość boku trójkąta równobocznego. Jakie jest pole i obwód tego trójkąta?

from math import sqrt
a = int(input('Podaj długość boku trójkąta równobocznego: '))

# Pole trójkąta równobocznego = (a^2 * sqrt(3)) / 4
field = (a ** 2 * sqrt(3)) / 4
print(f'Pole trójkąta równobocznego o boku {a} wynosi: {field:.2f}')

# Obwód trójkąta równobocznego = 3 * a
print(f'Obwód trójkąta równobocznego o boku {a} wynosi: {3 * a:.2f}')


