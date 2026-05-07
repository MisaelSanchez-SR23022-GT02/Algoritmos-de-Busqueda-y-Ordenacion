def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio  
        elif valor_medio < objetivo:
            izquierda = medio + 1  
        else:
            derecha = medio - 1 

    return -1 

datos = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91] 
objetivo = 23

resultado = busqueda_binaria(datos, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("El elemento no se encuentra en la lista.")