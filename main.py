import random


## Ejercicio 1: Suma de elementos de un arreglo
def suma_secuencial(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total


def suma_recursiva(arr, index):
    if index == 0:
        return arr[0]
    else:
        return arr[index] + suma_recursiva(arr, index - 1)


## Ejercicio 2: Número mayor de un arreglo
def mayor_secuencial(arr):
    mayor = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > mayor:
            mayor = arr[i]
    return mayor


def mayor_recursivo(arr, index, mayor_actual):
    if index < 0:
        return mayor_actual
    else:
        if arr[index] > mayor_actual:
            return mayor_recursivo(arr, index - 1, arr[index])
        else:
            return mayor_recursivo(arr, index - 1, mayor_actual)


## Ejercicio 4: Verificar matriz simétrica
def simetrica_secuencial(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


def simetrica_recursiva(matriz, i, j):
    if i < 0:
        return True
    else:
        if j < i:
            return simetrica_recursiva(matriz, i - 1, len(matriz) - 1)
        else:
            if matriz[i][j] != matriz[j][i]:
                return False
            else:
                return simetrica_recursiva(matriz, i, j - 1)


## Ejercicio 5: Suma filas impares (secuencial y recursivo)
def suma_filas_impares_sec(matriz):
    total = 0
    for i in range(len(matriz)):
        if i % 2 != 0:
            for j in range(len(matriz[i])):
                total += matriz[i][j]
    return total


def suma_filas_impares_rec(matriz, fila, col=0, total=0):
    if fila < 0:
        return total
    else:
        if col >= len(matriz[fila]):
            return suma_filas_impares_rec(matriz, fila - 1, 0, total)
        else:
            if fila % 2 != 0:
                return suma_filas_impares_rec(matriz, fila, col + 1, total + matriz[fila][col])
            else:
                return suma_filas_impares_rec(matriz, fila, col + 1, total)


## Ejercicio 6: Relleno matriz serpiente diagonal inversa
def llenar_serpiente_diagonal_sec(matriz):
    n = len(matriz)
    contador = 1

    for diagonal in range(2 * n - 2, -1, -1):
        if diagonal >= n - 1:
            i = diagonal - (n - 1)
            for j in range(i, n):
                if diagonal % 2 == 0:
                    matriz[n - 1 - j + i][j] = contador
                    contador += 1
                else:
                    matriz[j][n - 1 - j + i] = contador
                    contador += 1
        else:
            i = diagonal
            for j in range(i, -1, -1):
                if diagonal % 2 != 0:
                    matriz[i - j][j] = contador
                    contador += 1
                else:
                    matriz[j][i - j] = contador
                    contador += 1


def llenar_serpiente_diagonal_rec(matriz, diagonal, contador, i, j):
    if diagonal < 0:
        return matriz
    else:
        if diagonal >= len(matriz) - 1:
            if i + (diagonal - (len(matriz) - 1)) < len(matriz):
                if diagonal % 2 == 0:
                    matriz[len(matriz) - 1 - (diagonal - (len(matriz) - 1) + i) + (diagonal - (len(matriz) - 1))][diagonal - (len(matriz) - 1) + i] = contador
                    return llenar_serpiente_diagonal_rec(matriz, diagonal, contador + 1, i + 1, j)
                else:
                    matriz[diagonal - (len(matriz) - 1) + i][len(matriz) - 1 - (diagonal - (len(matriz) - 1) + i) + (diagonal - (len(matriz) - 1))] = contador
                    return llenar_serpiente_diagonal_rec(matriz, diagonal, contador + 1, i + 1, j)
            else:
                return llenar_serpiente_diagonal_rec(matriz, diagonal - 1, contador, 0, 0)
        else:
            if j <= diagonal:
                if diagonal % 2 == 0:
                    matriz[diagonal - j][j] = contador
                    return llenar_serpiente_diagonal_rec(matriz, diagonal, contador + 1, i, j + 1)
                else:
                    matriz[j][diagonal - j] = contador
                    return llenar_serpiente_diagonal_rec(matriz, diagonal, contador + 1, i, j + 1)
            else:
                return llenar_serpiente_diagonal_rec(matriz, diagonal - 1, contador, 0, 0)

#Ejercicio 7: Rellenar la matriz en espiral
def generar_matriz_espiral(matriz):
    m = len(matriz)     # Filas de la matriz
    n = len(matriz[0])  # Columnas de la matriz
    num = 1
    top, bottom = 0, m - 1
    left, right = 0, n - 1

    while num <= m * n:
        for col in range(right, left - 1, -1):
            matriz[bottom][col] = num
            num += 1
        bottom -= 1
        if num > m * n:
            break

        for row in range(bottom, top - 1, -1):
            matriz[row][left] = num
            num += 1
        left += 1
        if num > m * n:
            break

        for col in range(left, right + 1):
            matriz[top][col] = num
            num += 1
        top += 1
        if num > m * n:
            break

        for row in range(top, bottom + 1):
            matriz[row][right] = num
            num += 1
        right -= 1

    return matriz

#Ejercicio 9: Contar el número de nodos hoja en un árbol
def contar_nodos_hoja_recursivo(raiz):
    if raiz is None or (raiz.izquierdo is None and raiz.derecho is None):
        return 0 if raiz is None else 1
    return contar_nodos_hoja_recursivo(raiz.izquierdo) + contar_nodos_hoja_recursivo(raiz.derecho)


## Clases para el programa
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

## Generación de estructuras de datos
def generar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]


def generar_matriz_cuadrada(n, simetrica=False):
    if not simetrica:
        return [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
    else:
        # Generamos matriz triangular inferior
        matriz = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                matriz[i][j] = random.randint(1, 100)
        # Hacemos simétrica copiando la triangular inferior a la superior
        for i in range(n):
            for j in range(i+1, n):
                matriz[i][j] = matriz[j][i]
        return matriz

def generar_matriz(m, n):
    return [[0] * n for _ in range(m)]


def generar_arbol_aleatorio(profundidad_maxima, probabilidad_rama=0.7):
    if profundidad_maxima == 0 or random.random() > probabilidad_rama:
        return None

    valor = random.randint(1, 100)  # Valores entre 1 y 100
    nodo = Nodo(valor)
    nodo.izquierdo = generar_arbol_aleatorio(profundidad_maxima - 1, probabilidad_rama)
    nodo.derecho = generar_arbol_aleatorio(profundidad_maxima - 1, probabilidad_rama)

    return nodo

def imprimir_arbol(raiz, espacio=0, nivel=0):
    if raiz is None:
        return

    espacio += 5

    # Primero el hijo derecho
    imprimir_arbol(raiz.derecho, espacio, nivel + 1)

    # Imprimir el nodo actual
    print()
    for _ in range(5, espacio):
        print(" ", end="")
    print(f"{raiz.valor}({nivel})")

    # Luego el hijo izquierdo
    imprimir_arbol(raiz.izquierdo, espacio, nivel + 1)

## Menú principal
def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Suma de elementos de un arreglo")
        print("2. Número mayor de un arreglo")
        print("4. Verificar matriz simétrica")
        print("5. Suma de filas impares de matriz")
        print("6. Relleno matriz serpiente diagonal inversa")
        print("7. Rellenar matriz en espiral")
        print("9. Calcular el número de nodos hoja en un árbol binario")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            n = int(input("Tamaño del arreglo: "))
            arr = generar_arreglo(n)
            print(f"\nArreglo generado: {arr}")
            print(f"Suma secuencial: {suma_secuencial(arr)}")
            print(f"Suma recursiva: {suma_recursiva(arr, len(arr) - 1)}")
        elif opcion == "2":
            n = int(input("Tamaño del arreglo: "))
            arr = generar_arreglo(n)
            print(f"\nArreglo generado: {arr}")
            print(f"Mayor secuencial: {mayor_secuencial(arr)}")
            print(f"Mayor recursivo: {mayor_recursivo(arr, len(arr) - 1, arr[-1])}")
        elif opcion == "4":
            n = int(input("Tamaño de la matriz cuadrada: "))
            simetrica = input("¿Generar matriz simétrica? (s/n): ").lower() == 's'
            matriz = generar_matriz_cuadrada(n, simetrica)

            print("\nMatriz generada:")
            for fila in matriz:
                print(fila)
            print(f"\nEs simétrica (secuencial): {simetrica_secuencial(matriz)}")
            print(f"Es simétrica (recursivo): {simetrica_recursiva(matriz, len(matriz) - 1, len(matriz) - 1)}")
        elif opcion == "5":
            n = int(input("Tamaño de la matriz cuadrada: "))
            matriz = generar_matriz_cuadrada(n)
            print("\nMatriz generada:")
            for fila in matriz:
                print(fila)
            print(f"\nSuma filas impares (secuencial): {suma_filas_impares_sec(matriz)}")
            print(f"Suma filas impares (recursivo): {suma_filas_impares_rec(matriz, len(matriz) - 1, 0, 0)}")
        elif opcion == "6":
            n = int(input("Tamaño de la matriz cuadrada: "))
            matriz = generar_matriz_cuadrada(n)
            print("\nMatriz generada secuencialmente:")
            llenar_serpiente_diagonal_sec(matriz)
            for fila in matriz:
                print(fila)
            print("\nMatriz generada recursivamente:")
            llenar_serpiente_diagonal_rec(matriz, (2 * n - 2), 1, 0, 0)
            for fila in matriz:
                print(fila)
        elif opcion == "7":
            m = int(input("Número de filas de la matriz: "))
            n = int(input("Número de columnas de la matriz: "))
            matriz = generar_matriz(m, n)
            matriz_espiral = generar_matriz_espiral(matriz)
            print("\nMatriz generada en espiral:")
            for fila in matriz_espiral:
                print(fila)
        elif opcion == "9":
            # Generar árbol aleatorio con profundidad máxima 4
            profundidad = 4
            arbol = generar_arbol_aleatorio(profundidad)

            print("Árbol generado (visualización):")
            imprimir_arbol(arbol)

            hojas = contar_nodos_hoja_recursivo(arbol)
            print(f"\nEl árbol tiene {hojas} nodos hoja")

            # Mostrar algunos detalles adicionales
            print(f"\nDetalles del árbol generado:")
            print(f"- Profundidad máxima configurada: {profundidad}")
            print(f"- Nodos hoja encontrados: {hojas}")
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()