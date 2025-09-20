def draw_column_segment(row,height,space=" "):

    if row <height:
        return space + "| |"
    elif row == height:
        return space + "+-+"
    else:
        return space + "   "

def main():
    while True:
        try:
            a = int(input("podaj wartość pierwszeo słupka (a):  "))
            b = int(input("podaj wartość drugiego słupka (b):  "))
        except ValueError:
            print("błąd: wprowadź poprawną liczbę całkowitą")
            continue
        if not (0<=a<9 and 0 <= b<9):
            print("błąd: wysokości słupka musi być w zakresie 0-8")
            continue
        if a == b:
            print("błąd: wysokości słópków muszą być różne")
            continue

        c=abs(a-b)

        max_height = 9
        space_seperator = "  "

        print(f"\na= {a}, b= {b}, (c={c})")

        print("--+-+--+-+--+-+")

        for row in range(1, max_height):
            line=draw_column_segment(row,a, space_seperator)
            line+=draw_column_segment(row,b, space_seperator)
            line+=draw_column_segment(row,c, space_seperator)
            print(line)

        return
if __name__=='__main__':
    main()