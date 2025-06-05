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


## Menú principal
def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Suma de elementos de un arreglo")
        print("2. Número mayor de un arreglo")
        print("4. Verificar matriz simétrica")
        print("5. Suma de filas impares de matriz")
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
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()