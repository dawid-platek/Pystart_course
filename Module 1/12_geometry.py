# Odbierz od użytkownika dwa dowolne punkty na płaszczyźnie (x1, y1, x2, y2),
# które tworzą odcinek. Znajdź jego środek. Wypisz pole ora promień okręgu, którego ten odcinek jest średnicą.
# Zastanów się jakie pole i obwód ma prostokąt, którego ten odcinek jest przekątną.

from math import sqrt, pi

x1 = int(input("Podaj punkt x1: "))
y1 = int(input("Podaj punkt y1: "))
x2 = int(input("Podaj punkt x2: "))
y2 = int(input("Podaj punkt y2: "))

# 1. Długość odcinka - średnica
# sqrt((x2 - x1)**2 + (y2 - y1)**2)
length = sqrt((x2 - x1)**2 + (y2 - y1)**2)
radius = length / 2
print(f"Długość odcinka (średnica) wynosi: {length:.2f}")

# 2. Środek odcinka
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2
print(f"Środek odcinka to: ({mid_x:.2f}, {mid_y:.2f})")

# 3. Pole okręgu, który posiada promień z punktu 1
circle_area = pi * radius ** 2
print(f"Pole okręgu o promieniu {radius:.2f} wynosi: {circle_area:.2f}")

# 4. Pole i obwód prostokąta, którego przekątną jest odcinek z punktu 1
rectangle_area = (length ** 2) / 2
rectangle_perimeter = 2 * (length / sqrt(2)) * (length / sqrt(2))
print(f"Pole prostokąta o przekątnej {length:.2f} wynosi: {rectangle_area:.2f}")
print(f"Obwód prostokąta o przekątnej {length:.2f} wynosi: {rectangle_perimeter:.2f}")



