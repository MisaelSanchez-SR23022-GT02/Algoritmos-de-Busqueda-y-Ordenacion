def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i             
    return -1 

mi_lista = [45, 23, 11, 89, 7, 30]
valor_buscado = 89

resultado = busqueda_secuencial(mi_lista, valor_buscado)

if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("El elemento no se encuentra en la lista.")