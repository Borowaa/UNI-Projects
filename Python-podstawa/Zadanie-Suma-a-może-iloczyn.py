numbers = [8, 2, 6, 5, 4]

num = int(input("Podaj liczbę: "))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == num:
            print("Suma daje wartość dla par:", numbers[i], numbers[j])
        if numbers[i] * numbers[j] == num:
            print("Iloczyn daje wartość dla par:", numbers[i], numbers[j])