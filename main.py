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

## Ejercicio 3: Suma de dígitos múltiplos de un número en arreglo

def suma_digitos_multiplos_secuencial(arr, multiplo):
    resultado = []
    for i in range(len(arr)):
        suma = 0
        num_str = str(abs(arr[i]))
        for j in range(len(num_str)):
            digito = int(num_str[j])
            if digito % multiplo == 0 and digito != 0:
                suma += digito
        resultado.append(suma)
    return resultado

def suma_digitos_multiplos_recursivo(arr, multiplo, indice, suma_actual):
    if indice < 0:
        return []
    else:
        if arr[indice] == 0:
            return suma_digitos_multiplos_recursivo(arr, multiplo, indice - 1, 0) + [suma_actual]
        else:
            if abs(arr[indice]) % 10 % multiplo == 0 and abs(arr[indice]) % 10 != 0:
                if abs(arr[indice]) // 10 == 0:
                    return suma_digitos_multiplos_recursivo(arr, multiplo, indice - 1, 0) + [suma_actual + abs(arr[indice]) % 10]
                else:
                    return suma_digitos_multiplos_recursivo(arr[:indice] + [abs(arr[indice]) // 10] + arr[indice+1:], multiplo, indice, suma_actual + abs(arr[indice]) % 10)
            else:
                if abs(arr[indice]) // 10 == 0:
                    return suma_digitos_multiplos_recursivo(arr, multiplo, indice - 1, 0) + [suma_actual]
                else:
                    return suma_digitos_multiplos_recursivo(arr[:indice] + [abs(arr[indice]) // 10] + arr[indice+1:], multiplo, indice, suma_actual)

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

## Ejercicio 7: Rellenar la matriz en espiral
def llenar_matriz_espiral_secuencial(matriz):
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0

    fila_actual = filas - 1
    col_actual = columnas - 1

    direcciones = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    direccion_actual = 0

    for numero in range(1, filas * columnas + 1):
        matriz[fila_actual][col_actual] = numero
        df, dc = direcciones[direccion_actual]
        proxima_fila = fila_actual + df
        proxima_col = col_actual + dc
        if (proxima_fila < 0 or proxima_fila >= filas or
                proxima_col < 0 or proxima_col >= columnas or
                matriz[proxima_fila][proxima_col] != 0):

            direccion_actual = (direccion_actual + 1) % 4
            df, dc = direcciones[direccion_actual]
            fila_actual += df
            col_actual += dc
        else:
            fila_actual = proxima_fila
            col_actual = proxima_col

def llenar_matriz_espiral_recursivo(matriz, fila, col, direccion, numero):
    if numero > 0:
        matriz[fila][col] = len(matriz)*len(matriz[0]) - numero + 1
        if direccion == 0:
            if col > 0:
                if matriz[fila][col-1] == 0:
                    llenar_matriz_espiral_recursivo(matriz, fila, col-1, 0, numero-1)
                else:
                    llenar_matriz_espiral_recursivo(matriz, fila-1, col, 1, numero-1)
            else:
                llenar_matriz_espiral_recursivo(matriz, fila-1, col, 1, numero-1)
        else:
            if direccion == 1:
                if fila > 0:
                    if matriz[fila-1][col] == 0:
                        llenar_matriz_espiral_recursivo(matriz, fila-1, col, 1, numero-1)
                    else:
                        llenar_matriz_espiral_recursivo(matriz, fila, col+1, 2, numero-1)
                else:
                    llenar_matriz_espiral_recursivo(matriz, fila, col+1, 2, numero-1)
            else:
                if direccion == 2:
                    if col < len(matriz[0])-1:
                        if matriz[fila][col+1] == 0:
                            llenar_matriz_espiral_recursivo(matriz, fila, col+1, 2, numero-1)
                        else:
                            llenar_matriz_espiral_recursivo(matriz, fila+1, col, 3, numero-1)
                    else:
                        llenar_matriz_espiral_recursivo(matriz, fila+1, col, 3, numero-1)
                else:
                    if direccion == 3:
                        if fila < len(matriz)-1:
                            if matriz[fila+1][col] == 0:
                                llenar_matriz_espiral_recursivo(matriz, fila+1, col, 3, numero-1)
                            else:
                                llenar_matriz_espiral_recursivo(matriz, fila, col-1, 0, numero-1)
                        else:
                            llenar_matriz_espiral_recursivo(matriz, fila, col-1, 0, numero-1)

## Ejercicio 8: Recorrido preorden arbol binario
def recorrido_preorden_sec(raiz):
    if not raiz:
        return []
    resultado = []
    pila = [raiz]
    while pila:
        nodo_actual = pila.pop()
        resultado.append(nodo_actual.valor)
        if nodo_actual.derecho:
            pila.append(nodo_actual.derecho)
        if nodo_actual.izquierdo:
            pila.append(nodo_actual.izquierdo)
    return resultado


def recorrido_preorden_rec(raiz):
    if not raiz:
        return []
    return [raiz.valor] + recorrido_preorden_rec(raiz.izquierdo) + recorrido_preorden_rec(raiz.derecho)


## Ejercicio 9: Contar el número de nodos hoja en un árbol
def contar_nodos_hoja_recursivo(raiz):
    if raiz is None or (raiz.izquierdo is None and raiz.derecho is None):
        return 0 if raiz is None else 1
    else:
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


def generar_arbol_aleatorio(profundidad_maxima, probabilidad_rama=1.0):
    if profundidad_maxima == 0 or random.random() > probabilidad_rama:
        return None

    valor = random.randint(1, 100)  # Valores entre 1 y 100
    nodo = Nodo(valor)
    nodo.izquierdo = generar_arbol_aleatorio(profundidad_maxima - 1, probabilidad_rama)
    nodo.derecho = generar_arbol_aleatorio(profundidad_maxima - 1, probabilidad_rama)

    return nodo


def imprimir_arbol(raiz):
    def imprimir_rec(nodo, prefijo="", es_ultimo=True, nivel=0):
        if nodo is not None:
            # Mostrar nodo con nivel en formato compacto [N]
            print(prefijo + ("└── " if es_ultimo else "├── ") + f"{nodo.valor} [{nivel}]")

            # Preparar prefijo para hijos
            extension = "    " if es_ultimo else "│   "
            nuevo_prefijo = prefijo + extension

            # Determinar si hay hijos
            tiene_izq = nodo.izquierdo is not None
            tiene_der = nodo.derecho is not None

            # Imprimir hijos con nivel incrementado
            if tiene_izq and tiene_der:
                imprimir_rec(nodo.izquierdo, nuevo_prefijo, False, nivel + 1)
                imprimir_rec(nodo.derecho, nuevo_prefijo, True, nivel + 1)
            elif tiene_izq:
                imprimir_rec(nodo.izquierdo, nuevo_prefijo, True, nivel + 1)
            elif tiene_der:
                imprimir_rec(nodo.derecho, nuevo_prefijo, True, nivel + 1)

    if raiz:
        print(f"{raiz.valor} [0]")  # Raíz en nivel 0
        if raiz.izquierdo or raiz.derecho:
            if raiz.izquierdo and raiz.derecho:
                imprimir_rec(raiz.izquierdo, "", False, 1)
                imprimir_rec(raiz.derecho, "", True, 1)
            elif raiz.izquierdo:
                imprimir_rec(raiz.izquierdo, "", True, 1)
            elif raiz.derecho:
                imprimir_rec(raiz.derecho, "", True, 1)
    else:
        print("Árbol vacío")

## Menú principal
def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Suma de elementos de un arreglo")
        print("2. Número mayor de un arreglo")
        print("3. Suma de dígitos múltiplos de un número en arreglo")
        print("4. Verificar matriz simétrica")
        print("5. Suma de filas impares de matriz")
        print("6. Relleno matriz serpiente diagonal inversa")
        print("7. Rellenar matriz en espiral")
        print("8. Recorrido preorden de árbol binario")
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
        elif opcion == "3":
            n = int(input("Tamaño del arreglo: "))
            multiplo = int(input("Ingrese el número múltiplo: "))
            arr = generar_arreglo(n)
            print(f"\nArreglo generado: {arr}")
            print(f"Suma dígitos múltiplos (secuencial): {suma_digitos_multiplos_secuencial(arr, multiplo)}")
            print(f"Suma dígitos múltiplos (recursivo): {suma_digitos_multiplos_recursivo(arr, multiplo, len(arr) - 1, 0)}")
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
            filas = int(input("Número de filas de la matriz: "))
            columnas = int(input("Número de columnas de la matriz: "))
            matriz_espiral = generar_matriz(filas, columnas)
            matriz = generar_matriz(filas, columnas)
            llenar_matriz_espiral_secuencial(matriz_espiral)
            llenar_matriz_espiral_recursivo(matriz, filas - 1, columnas - 1, 0, filas * columnas)

            print("\nMatriz generada en espiral:")
            for fila in matriz_espiral:
                print(fila)
            print("\nMatriz generada en espiral recursivo:")
            for fila in matriz:
                print(fila)
        elif opcion == "8":
            arbol = generar_arbol_aleatorio(4)
            print("Árbol generado (visualización):")
            imprimir_arbol(arbol)
            print("Recorrido Secuencial:\t" + str(recorrido_preorden_sec(arbol)))
            print("Recorrido Recursivo:\t" + str(recorrido_preorden_rec(arbol)))

        elif opcion == "9":
            # Generar árbol aleatorio con profundidad máxima 4
            profundidad = random.randint(2, 5)
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