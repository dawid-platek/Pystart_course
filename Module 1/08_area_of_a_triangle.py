# Pole trójkąta o trzech wierzchołkach.

# Pole trójkąta = 1/2 * (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)

xa = int(input("Podaj x punktu A: "))
ya = int(input("Podaj y punktu A: "))
xb = int(input("Podaj x punktu B: "))
yb = int(input("Podaj y punktu B: "))
xc = int(input("Podaj x punktu C: "))
yc = int(input("Podaj y punktu C: "))

area = 0.5 * (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)
print(f"Pole trójkąta wynosi: {area:.2f}")  # Wyświetlenie pola trójkąta zaokrąglonego do dwóch miejsc po przecinku