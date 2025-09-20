#Funkcja odpowiedziealna za generowanie funkcji
from os import execle


def genrate_pyramid(height):
    #iteracja od góry do dołu piramidy
    for y in range(height - 1, -1, -1):
        #iteracja po kazdej lini od prawej
        for x in range(1, height * 2):
        #jeśli wartosć w zakresie to wpisz #
            if x > y and x < (height * 2 - y):
                print("#", end="")
        # jeśli ni to wpisz spacja (" ")
            else:
                print(" ", end="")
    #zakończ linie przed przejściem do kolejnej
        print()
while True: #będzie działać dopóki nie zbrakeujemy lub sama się przerwie pętla
    #Pobranie i walidacja wysokości piramidy od usera
    try:
        height =int(input("Podaj wysokoścć piramidy: "))
    except ValueError:
        print("Wysokość piramidy musi być liczą całkowitą!")
        continue
    #sprawdzenie czy wysokąość jest większa od 0
    if height <= 0:
        print("wysokość musi być liczbą dodatnią")
        continue
    #wywołanie funkcji generującej i piramidę i przerwanie pętli
    genrate_pyramid(height)
    break