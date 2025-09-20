niu = [8,2,6,5,4]

def bubble_sort(lista):
    liczba_iteracji = 0
    n = len(lista) #n to długość listy
    for i in range(n):
        liczba_iteracji +=1
        swapped = False
        #- i bo ostatnie i elementów jest już posortowaneych
        # -1 bo nie chemy wyjść poza zakres
        for j in range (0, n-i-1):
            if lista[j]> lista[j+1]:
                swapped = True
                lista[j], lista[j+1]= lista[j+1],lista[j]
        if not swapped:
            break
    print(f"liczba iteracji:{liczba_iteracji}")
    return lista
sorted_asc = bubble_sort(niu.copy())
# sorted_desc = bubble_sort_desc(niu.copy())

print("lista przed sortowaniem:")
print(niu)
print("lista posortowana rosnąco: ")
print(sorted_asc)