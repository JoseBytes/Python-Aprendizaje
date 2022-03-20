# El Bucle for funciona con determinadas interaciones
# El Bucle for trabaja con Colecciones en Python

# El Bucle for recorrera en una Coleccion elementos por elementos
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista:
    print("Hola Mundo")

# Ejemplo 2: la variable de iteracion mostrara los elementos en el recorrido
lista2 = ["Jose", "Viviana", "Lizangel", True, 1, 2, 3]

for i in lista2:
    print(f"Los valores Lista2: {i}")

# Ejemplo 3: Diccionarios

diccionario = {"Jose":{28, 1.80}, "Viviana":{2, 1}, "Lizangel":{25, 1.78}}

for i in diccionario:
    print(diccionario[i]) #Mostrara los valores de cada clave en el recorrido
    print(f"Clave: {i} Valor: {diccionario[i]}") # Muestra Clave y Valor

for clave,valor in diccionario.items():
    print(f"{clave} -> {valor}")

# Ejemplo 4: Recorriendo cadenas Caracter en Caracter
cadena = "Lizangel".range(10)

for i in cadena:
    #print(i)
    print(i,end=" ") # Lo imprime con espacios usan ,end=" " podria agregar cualquier simbolo



