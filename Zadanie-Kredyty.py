from functools import total_ordering


def calculate_loan_installments(loan_amount, years,
                                annual_interest, installment_type):
    total_interest= 0
    total_paid= 0
    monthly_interest= annual_interest/12/100
    total_months = years *12

    #wyświetlanie podstawowego info o kredycie
    print("\nParametry kredytu")
    print(f"kwota kredytu: {loan_amount}")
    print(f"liczba lat: {years}")
    print(f"procent w skali rku:{annual_interest}")
    print(f"typ rat: {installment_type}")

    if installment_type == "stałe":
                            #logika obliczania raty stałej
        q = 1 + monthly_interest #q to składnik równanian
        n = total_months
        monthly_installment = (loan_amount * (q**n) * ((q-1) / ((q**n) -1)))
        for month in range(1, total_months + 1):
            #obliczanie naszej odsetkowej części
            interest_part = ( loan_amount- total_paid)*monthly_interest
            capital_part = monthly_installment - interest_part
            total_interest += interest_part
            total_paid += capital_part
            reameaining_capital = loan_amount - total_paid
            print(
                f"Rata: {month},"
                f"Kapitał: {capital_part:.2f},"
                f"Odsetki: {interest_part:.2f},"
                f"Razem: {monthly_installment:.2f},"
                f"Pozostało: {reameaining_capital:.2f},"
            )
    elif installment_type == "malejące":

        capital_part = loan_amount/ total_months
        for month in range(1, total_months + 1):
            interest_part = ((loan_amount - (capital_part * (month-1))) *monthly_interest)
            total_interest += interest_part
            total_paid += capital_part
            reameaining_capital = loan_amount - total_paid
            monthly_installment = (capital_part + interest_part)
            print(
                f"Rata: {month},"
                f"Kapitał: {capital_part:.2f},"
                f"Odsetki: {interest_part:.2f},"
                f"Razem: {monthly_installment:.2f},"
                f"Pozostało: {reameaining_capital:.2f},"
            )
    print(f"\nCałkowity kapitał: {total_paid:.2f}")
    print(f"\nCałkowity koszt (suma odsetek): {total_interest:.2f}")
    print(f"\nCałkowity Kredyt(suma odsetek i kapitału): {total_paid + total_interest:.2f}")
while True:
    # Pobieranie i walidacja kwoty kredytu
    try:
        loan_amount = float(input("Podaj kwotę kredytu: "))
        if loan_amount <= 0:
            raise ValueError
    except ValueError:
        print("Kwota kredytu musi być liczbą dodatnią!")
        continue
    # Pobieranie i walidacja liczby lat
    try:
        years = int(input("Podaj liczbę lat: "))
        if years <= 0:
            raise ValueError
    except ValueError:
        print("Liczba lat musi być liczbą dodatnią!")
        continue
    # Pobieranie i walidacja procentu w skali roku
    try:
        annual_interest = float(input("Podaj procent w skali roku: "))
        if annual_interest <= 0:
            raise ValueError
    except ValueError:
        print("Procentu w skali roku musi być liczbą dodatnią!")
        continue
    # Pobieranie i walidacja typu rat
    installment_type = input("Podaj typ raty (malejące/stałe): ")
    if installment_type not in ["stałe", "malejące"]:
        print("Typ raty to 'stałe' albo 'malejące'!")
        continue

    # Wywoałenie metody liczącej kredyt
    calculate_loan_installments(loan_amount, years,
                                annual_interest, installment_type)
    break