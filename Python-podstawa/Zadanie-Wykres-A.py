def draw_column(height, max_height):
    padding  =max_height - height
    print(" "*padding + "+" + "-"*height+"+")
    print(" " * padding + "|" + " "*height + "|")
    print(" " * padding + "+" + "-"*height + "+")
def deaw_seperatr(max_height):
    print(max_height * " "+ "|")
def draw_column_with_seperator(height, max_height):
    draw_column(height, max_height)
    deaw_seperatr(max_height)

def main():
    while True:
        try:
            a= int(input("Podaj wysokość pierwszeo słupka(a)"))
            c= int(input("Podaj wysokość trzeciego słupka (c)"))
        except ValueError:
            print("Błąd: wprowadzona wartość nie jest liczbą całkowitą")
            continue
#function to check if started as script
        if a<=0 or a>=20 or c<=0 or c>=20:
            print("wartośćsłupka musi być w przedziale od 1 do 19")
            continue
        if a == c:
            print("wartości muszą być różne")
            continue
        b= round((a+c)/2)
        max_height = max (a,b,c)
        print(f"\na={a}, (b={b}), (c={c})")
        draw_column_with_seperator(a, max_height)
        draw_column_with_seperator(b, max_height)
        draw_column_with_seperator(c, max_height)
        break

if __name__ == '__main__':
    main()