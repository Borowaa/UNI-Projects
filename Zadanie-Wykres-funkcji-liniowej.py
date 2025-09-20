import pylab # zaimportowanie biblioteki zawierającej metody potrzebne do utworzenia wykresu
import numpy as np

def show_chart():
     while True:
         try:
             title = input("Podaj tytuł wykresu:")
             try:
                 a = float(input("Podaj współczynnik a funkcji f()x = a*x + b:"))
                 b = float(input("Podaj współczynnik b funkcji f()x = a*x + b:"))
             except Exception as e:
                print(f"Wystąpił nieoczekiwany błąd {e}")
                continue
             try:
                 x_min= float(input("Podaj minimalną wartośc x:"))
                 x_max= float(input("Podaj maksymalną wartośc x:"))
             except ValueError:
                 print("Musi być liczbą")
                 continue
             if x_min >= x_max:
                print("Błąd")
                continue
             grid_answer = input("Czy wyświetlić siatkę pomocniczą (tak/nie):").lower()
             grid = grid_answer == "tak"
             x= np.linspace(x_min, x_max, 100)
             y= a*x + b
             pylab.plot(x,y)
             pylab.title(title)
             pylab.grid(grid)
             pylab.xlabel("x")
             pylab.ylabel(f"x")
             pylab.show()
         except Exception as e:
            print(f"Wystąpił nieoczekiwany błąd {e}")


def main():
    show_chart()

if __name__ == '__main__':
    main()