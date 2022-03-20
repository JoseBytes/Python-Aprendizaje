# Funciones para modificar las listas

lista = [1, 2, 3, 4]
# Usando el metodo .append()
lista.append(5) #La funcion de Append agrega elementos al final de la coleccion
lista.append(6)
lista.append("Hola mundo")
lista.append([1,2,3]) #Agregando una sublista

# Usando el metodo .insert()
lista.insert(6,"Posicionandome en el index 6") #Inserta en una posicion especifica
lista.insert(3, [1,2,3]) # Insertando una sublista en el index 3

# Usando el metodo .extend() Agrega varios elementos a una lista
lista.extend([8, 9, [1,2,3], "cadena"])

# Concatenando dos listas
lista2 = [10, 11, 12, 13]
lista3 = lista + lista2

print(lista)
print(lista3)
