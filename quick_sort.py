def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    
    return quick_sort(izquierda) + medio + quick_sort(derecha)

mi_lista = [34, 7, 23, 32, 5, 62, 10, 23]
lista_ordenada = quick_sort(mi_lista)

print(f"Lista original: {mi_lista}")
print(f"Lista ordenada: {lista_ordenada}")