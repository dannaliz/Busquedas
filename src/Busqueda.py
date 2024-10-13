def busqueda_binaria(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2

    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return busqueda_binaria(arr, x, mid + 1, high)
    else:
        return busqueda_binaria(arr, x, low, mid - 1)

#x = izq + (z - S[izq]/S[der]-S[izq])(der-izq)

# Búsqueda por Interpolación
def busqueda_interpolacion(arr, z):
    izq = 0
    der = len(arr) - 1
    
    while izq <= der and arr[izq] <= z <= arr[der]:
        # Fórmula de interpolación
        pos = izq + ((z - arr[izq]) * (der - izq)) // (arr[der] - arr[izq])
        if arr[pos] == z:
            return pos

        if arr[pos] < z:
            izq = pos + 1
        else:
            der = pos - 1

    return -1

# Búsqueda Exponencial
def busqueda_exponencial(arr, z):
    if arr[0] == z:
        return 0
    # Encuentra el rango para la búsqueda binaria
    i = 1
    while i < len(arr) and arr[i] <= z:
        i *= 2
    # Llama a búsqueda binaria en el rango encontrado
    return busqueda_binaria(arr, z, i // 2, min(i, len(arr)-1))


# Ejecutar el programa
if __name__ == "__main__":
    archivo = input("Ingresa el nombre del archivo: ")
    #Hacer cosa de archivo XD donde vea el número a buscar k y la secuencia de núms
    with open(archivo, 'r') as file:
        lines = file.readlines()
        secuencia = [int(num) for num in lines[0].split()]
        z = int(lines[1])
    opcion = int(input("Elige el número de la búsqueda que quieres hacer: \n 1. Búsqueda Exponencial \n 2. Búsqueda por Interpolación \n"))
    
    if opcion == 1:
        resul = busqueda_exponencial(secuencia,z)
    elif opcion == 2:
        resul = busqueda_interpolacion(secuencia,z)
    else:
        print("Opción inválida")
    
    if resul != -1:
        print(f"Elemento encontrado en el índice {resul}")
    else:
        print("Elemento no encontrado en la secuencia.")


