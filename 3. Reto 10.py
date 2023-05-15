# 3.Reto 10
Lista = [] # Se crea una lista vacia 
n = int(input("Ingrese los numero que dese ingresar a la lista  ")) # se define n como la variable entera 
while (n != 1000): # Mientras el numero no sea 1000 se sigue con el ingreso de los elementos 
    Lista.append(n) # Se agrega el elemento a la lista vacia 
    n= int(input("Ingrese los elementos de su arreglo, para terminar de adicionar elememntos digite 1000"))
print(Lista) #Imprimir la lista 

numero_de_ceros = Lista.count(0) # se define numero_de_ceros como el contador de ceros en la lista creada 
print("El numero de ceros en la lista es " + str(numero_de_ceros)) # Se imprime el numero de ceros en la lista 