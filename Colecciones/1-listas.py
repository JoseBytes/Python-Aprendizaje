lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 40, 5.6, [1,2,3], True, "Martes"]

print(lista) # Muestra los elementos de la lista

#Listado por rango
print(lista[1]) # Muestra el elemento del index 1
print(lista[-1]) # Muestra el elemento de la posicion -1
print(lista[0:3]) # Muestra los elementos en un rango de posicion 0 al 3
print(lista[2:]) # Muestra los elementos a partir desde una posicion al final

#Contar elementos
print(len(lista)) # Muestra la cantidad de elemenos de una lista
print(len(lista[7])) # Muestra la cantidad de sub-elemenos de una posicion

#Busqueda por Elementos
print(lista.index("Viernes")) # Muestra la posicion de un elemento
print(40 in lista) # Muestra si 40 esta dentro de la lista

print(lista.count("Martes"))    # Muestra cuantas veces se repite un elementos

