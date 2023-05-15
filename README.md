# Reto_10_DAAG
## :blue_heart: Vamos, llegando al final de la Champions para ver al Manchester City  alzar la orejona :blue_heart:

# Iniciemos con el reto 10


## :seedling: 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.  :evergreen_tree:

## :anger: Código :anger:

```ruby 

#1.Reto 10 
lista_elementos = []# Crear una lista vacia 
R = float(input(" Ingrese los numeros que estaran es su arreglo")) #Definir la variabble R 
while (R != 1000): # Mientras el numero no sea 1000 se sigue con el ingreso de los elementos  
    lista_elementos.append(R) # Agregar el elemento a la lista
    R= float(input("Ingrese los elementos de su arreglo, para terminar de adicionar elememntos digite 1000")) #Ingresar los balores a lista pero que no sea 1000 porque se para el programa
print(lista_elementos) # Imprimir la lista de los elementos ingresados 

sumar_lista = sum(lista_elementos) # Se suman los elementos de la lista 
promedio_lista= sum(lista_elementos)/ len(lista_elementos) # Se define promedio como la divison de la suma de los elementos y el numero de elementos 
print( "El promedio de este arreglo es: " + str(promedio_lista)) # Dar el promedio de la lista 

```

## :seedling: 2.Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño. :evergreen_tree:

## :anger: Código :anger:

```ruby 
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
    print("El producto punto es:" +  str(producto))

```
## :seedling: 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo. :evergreen_tree:

## :anger: Código :anger:

```ruby
# 3.Reto 10
Lista = [] # Se crea una lista vacia 
n = int(input("Ingrese los numero que dese ingresar a la lista  ")) # se define n como la variable entera 
while (n != 1000): # Mientras el numero no sea 1000 se sigue con el ingreso de los elementos 
    Lista.append(n) # Se agrega el elemento a la lista vacia 
    n= int(input("Ingrese los elementos de su arreglo, para terminar de adicionar elememntos digite 1000"))
print(Lista) #Imprimir la lista 

numero_de_ceros = Lista.count(0) # se define numero_de_ceros como el contador de ceros en la lista creada 
print("El numero de ceros en la lista es " + str(numero_de_ceros)) # Se imprime el numero de ceros en la lista 
```

## :seedling: 4. Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación):evergreen_tree:

### :anger:El algoritmo de ordenamiento de burbuja, también conocido como Bubble Sort en inglés, es un método simple para ordenar una lista o arreglo de elementos. Su nombre se debe a que los elementos más grandes "burbujean" hacia arriba a medida que se comparan y se intercambian a lo largo del arreglo hasta que todos los elementos estén en su posición correcta.

El algoritmo funciona de la siguiente manera:

Comenzando desde el primer elemento, se comparan los pares adyacentes de elementos en el arreglo.
Si el par de elementos está en el orden incorrecto (el elemento de la derecha es menor que el de la izquierda), se intercambian.
Se repite el paso anterior para cada par de elementos adyacentes a lo largo del arreglo, desde el principio hasta el final.
Una vez completado un recorrido completo del arreglo, el elemento más grande se coloca en la posición final.
Se repiten los pasos 1 al 4 para el resto del arreglo, excluyendo el último elemento en cada iteración, ya que ya está en su posición correcta.
El algoritmo continúa iterando sobre el arreglo hasta que todos los elementos estén ordenados en forma ascendente.
Ventajas del Bubble Sort:

Es fácil de entender e implementar.
No requiere espacio adicional de memoria.
Es adaptable a diferentes tipos de datos.
Es un algoritmo de ordenamiento estable, lo que significa que los elementos con el mismo valor mantienen su orden relativo en la salida ordenada.
Desventajas del Bubble Sort:

Referencia: Bubble Sort - GeeksforGeeks 







##  :collision::collision: Gracias por su atencion espero les sirva de ayuda, vamos Manchester City!!!!! :blue_heart::blue_heart::blue_heart:  :collision::collision:
