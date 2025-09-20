import csv
# 1. Klasa Przedmiot
class Przedmiot:
def __init__(self, nazwa, kod_przedmiotu, prowadzacy, ects):
self.nazwa = nazwa
self.kod_przedmiotu = kod_przedmiotu
self.prowadzacy = prowadzacy
self.ects = ects

def opis(self):
return f"Przedmiot: {self.nazwa}, Kod: {self.kod_przedmiotu}, Prowadzący: {self.prowadzacy}, ECTS: {self.ects}"


# 2. Klasa Student
class Student:
def __init__(self, imie, nazwisko, numer_indeksu):
self.imie = imie
self.nazwisko = nazwisko
self.numer_indeksu = numer_indeksu
self.oceny = []

def dodaj_ocene(self, ocena):
self.oceny.append(ocena)

def srednia_ocen(self):
return sum(self.oceny) / len(self.oceny) if self.oceny else 0


# 3. Klasa Grupa
class Grupa:
def __init__(self):
self.studenci = []

def dodaj_studenta(self, student):
self.studenci.append(student)

def studenci_z_numerem_indeksu(self, numer_indeksu):
return [s for s in self.studenci if s.numer_indeksu == numer_indeksu]

def srednia_ocen_grupy(self):
suma_ocen = sum(s.srednia_ocen() for s in self.studenci if s.oceny)
liczba_studentow = sum(1 for s in self.studenci if s.oceny)
return suma_ocen / liczba_studentow if liczba_studentow else 0

def eksport_csv(self, nazwa_pliku):
with open(nazwa_pliku, mode='w', newline='') as plik:
writer = csv.writer(plik)
writer.writerow(["Imię", "Nazwisko", "Numer Indeksu"])
for student in self.studenci:
writer.writerow([student.imie, student.nazwisko, student.numer_indeksu])

def studenci_z_wysoka_srednia(self, prog):
return [s for s in self.studenci if s.srednia_ocen() > prog]


# 4. Klasa PlanZajec
class PlanZajec:
def __init__(self):
self.przedmioty = []

def dodaj_przedmiot(self, przedmiot):
self.przedmioty.append(przedmiot)

def przedmioty_prowadzacego(self, prowadzacy):
return [p for p in self.przedmioty if p.prowadzacy == prowadzacy]

def sum_ects_studenta(self, lista_kodow_przedmiotow):
return sum(p.ects for p in self.przedmioty if p.kod_przedmiotu in lista_kodow_przedmiotow)


# Przykładowe użycie
przedmiot1 = Przedmiot("Matematyka", "MATH101", "Dr Kowalski", 5)
przedmiot2 = Przedmiot("Fizyka", "PHYS201", "Dr Nowak", 4)

student1 = Student("Jan", "Kowalski", 12345)
student2 = Student("Anna", "Nowak", 67890)

student1.dodaj_ocene(4)
student1.dodaj_ocene(5)
student2.dodaj_ocene(3)
student2.dodaj_ocene(4)

grupa = Grupa()
grupa.dodaj_studenta(student1)
grupa.dodaj_studenta(student2)

plan = PlanZajec()
plan.dodaj_przedmiot(przedmiot1)
plan.dodaj_przedmiot(przedmiot2)

# Testowanie funkcji
print(przedmiot1.opis())
print("Średnia ocen grupy:", grupa.srednia_ocen_grupy())
print("Studenci z wysoką średnią:", [s.imie for s in grupa.studenci_z_wysoka_srednia(3.5)])
print("Przedmioty prowadzone przez Dr Kowalskiego:", [p.nazwa for p in plan.przedmioty_prowadzacego("Dr Kowalski")])
print("Suma ECTS dla studenta:", plan.sum_ects_studenta(["MATH101", "PHYS201"]))