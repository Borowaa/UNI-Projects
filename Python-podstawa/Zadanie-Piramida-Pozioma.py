def generate_pyramid(height):
    # Generowanie górnej części piramidy
    for y in range(1, height + 1):
        print("#" * y)
    # Generowanie dolnej części piramidy
    for y in range(height - 1, 0, -1):
        print("#" * y)


while True:  # pętla pobierająca wysokość piramidy od użytkownika
    try:
        height = int(input("Podaj wysokość piramidy: "))
    except ValueError:
        print("Wysokość piramidy musi być liczbą całkowitą!")
        continue

    if height <= 0:
        print("Wysokość musi być liczbą dodatnią!")
        continue

    # wywołanie funkcji generującej piramidę i przerwanie pętli
    generate_pyramid(height)
    break