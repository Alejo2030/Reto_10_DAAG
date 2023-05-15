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