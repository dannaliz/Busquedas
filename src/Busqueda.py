'''
Metodo de Busqueda binaria, recibe como parametros:
arr: secuencia de números
x: elemento a buscar
low y high: indices que marcan el rango donde buscaremos x
'''
def busqueda_binaria(arr, x, low, high):
    if low > high: #Caso base 1 (No se encuentra elemento)
        return -1
    mid = (low + high) // 2
    if arr[mid] == x: #Caso base 2 (Se encuentra el indice donde esta el elemento)
        return mid
    #Casos recusivos
    elif arr[mid] < x:
        return busqueda_binaria(arr, x, mid + 1, high)
    else:
        return busqueda_binaria(arr, x, low, mid - 1)



'''
Busqueda por interpolación donde tomamos como parametros un arreglo y el elemento a encontrar.
Seguimos la formula de: pos = izq + (z - S[izq]/S[der]-S[izq])(der-izq)
'''
def busqueda_interpolacion(arr, z):
    #Indices del rango que tendremos
    izq = 0
    der = len(arr) - 1
    #Mientras no hayamos recorrido todo el arreglo y z pueda estar en el rango que buscamos
    while izq <= der and arr[izq] <= z <= arr[der]:
        pos = izq + ((z - arr[izq]) * (der - izq)) // (arr[der] - arr[izq]) # Fórmula de interpolación
        if arr[pos] == z:
            return pos
        
        #Si pos no es el indice que buscamos iteramos con nuevos valores
        if arr[pos] < z:
            izq = pos + 1
        else:
            der = pos - 1

    return -1

'''
Busqueda exponencial, donde recorremos el arreglo 2^n veces en cada iteración hasta que
nos pasemos de z, luego hacemos busqueda binaria en el rango donde puede estar z
'''
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


