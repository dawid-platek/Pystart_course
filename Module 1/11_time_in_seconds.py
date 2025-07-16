# Program liczy czas w sekundach i resetuje się po 24 godzinach. Zapisz w klasycznej formie
# czas przedstawiony w formacie: 23400, 34200, 81000

# Wynik powinien być w formacie: 06:30, 09:30, 22:30

value = int(input("Podaj czas wyrażony w sekundach: "))
hour = value // 3600
minutes = (value % 3600) // 60

print(f'{hour:02d}:{minutes:02d}')  # Wyświetlenie czasu w formacie godzin:minut, gdzie minuty są zawsze dwucyfrowe
