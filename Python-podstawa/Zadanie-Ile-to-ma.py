import string
from collections import Counter


def analyze_text():
    text = input("Wpisz tekst: ")

    licznik_spacji=text.count(" ")
    licznik_slow = len(text.split())
    licznik_interpunkcji = len(text) - licznik_spacji
    licznik_liter = Counter(c.lower() for c in text if c.isalpha())
    czestotliwosc_liter = ", ".join(f"{c}: {n}" for c, n in sorted(licznik_liter.items()))

    print(
        f"Liczba spacji: {licznik_spacji}, liczba słów: {licznik_slow}, liczba liter oraz znaków interpunkcyjnych: {licznik_interpunkcji} ")

    print ("częstotliwość liter:", czestotliwosc_liter)

analyze_text()