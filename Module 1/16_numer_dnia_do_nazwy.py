# Napisz program, który zamieni numer dnia tygodnia na jego nazwę.
# 1 wyświetla poniedziałek, 2 wtorek itd.

day_number = int(input("Podaj numer dnia tygodnia (od 1 do 7): "))

if day_number == 1:
    print("Poniedziałek")
elif day_number == 2:
    print("Wtorek")
elif day_number == 3:
    print("Środa")
elif day_number == 4:
    print("Czwartek")
elif day_number == 5:
    print("Piątek")
elif day_number == 6:
    print("Sobota")
elif day_number == 7:
    print("Niedziela")
else:
    print("Nieprawidłowy numer dnia tygodnia. Proszę podać liczbę od 1 do 7.")

# Można również użyć match-case (Python 3.10+):

match day_number:
    case 1:
        print("Poniedziałek")
    case 2:
        print("Wtorek")
    case 3:
        print("Środa")
    case 4:
        print("Czwartek")
    case 5:
        print("Piątek")
    case 6:
        print("Sobota")
    case 7:
        print("Niedziela")
    case _:
        print("Nieprawidłowy numer dnia tygodnia. Proszę podać liczbę od 1 do 7.")
