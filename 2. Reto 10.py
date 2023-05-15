#2.Reto 10

def producto_punto(arreglo1, arreglo2):
    # Verificar que los arreglos tengan el mismo tamaño
    if len(arreglo1) != len(arreglo2):
        print("Error: Los arreglos deben tener el mismo tamaño")
        return None

    # Inicializar el resultado en cero
    resultado = 0

    # Calcular el producto punto
    for i in range(len(arreglo1)):
        resultado += arreglo1[i] * arreglo2[i]

    return resultado


# Pedir valores
arreglo1 = []
arreglo2 = []

# Ingresar los valores del primer arreglo
valores_arreglo1 = input("Ingrese los valores del primer arreglo separados por espacios: ").split()
for valor in valores_arreglo1:
    arreglo1.append(int(valor))

# Ingresar los valores del segundo arreglo
valores_arreglo2 = input("Ingrese los valores del segundo arreglo separados por espacios: ").split()
for valor in valores_arreglo2:
    arreglo2.append(int(valor))

# Calcular el producto punto y mostrar el resultado
producto = producto_punto(arreglo1, arreglo2)
if producto is not None:
    print("El producto punto es:" + str(producto))

