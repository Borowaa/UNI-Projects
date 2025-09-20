import random

#możliwe wybory
choices = ["K", "P", "N"]

#Aktualny wynik
user_score = 0
computer_score = 0

while True:
    #Pobieranie wyboru usera
    user_choice = input("Wybierz 'K' dla kamienia, 'P' dla papieru, 'N' dla nożyczek: ")
    if user_choice not in choices:
        print("Nieprawidłowy wybór, spróbuj jeszcze raz")

    #Losowy wybór komputera
    computer_choice = random.choice(choices)
    print(f"Wybór komputera: {computer_choice}")

    #Logika gry
    if user_choice == computer_choice:
        print("Remis!")
    elif (user_choice == "K" and computer_choice == "N") or \
        (user_choice == "P" and computer_choice == "K") or \
        (user_choice == "N" and computer_choice == "P"):
        user_score += 1
        print("Wygrałeś rundę!")
    else:
        computer_score += 1
        print("Komputer wygrał rundę")

    #Wyświetlanie wyniku
    print(f"Aktualny wynik: Ty {user_score} - Komputer {computer_score}")

    continue_game = input(f"Chcesz grać dalej? (tak/nie): ").lower()
    if continue_game != "tak":
        print("Dzięki za grę!")
        break