# Programa 1: Búsqueda en Arreglo Multidimensional
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return None

# Valor que deseas buscar
valor_buscado = 5

# Realizar la búsqueda
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición: fila {posicion[0] + 1}, columna {posicion[1] + 1}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
