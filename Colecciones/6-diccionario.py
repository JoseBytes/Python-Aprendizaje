# Estructura de un diccionario
diccionario = {"azul":"blue", "rojo":"red", "verde":"green"}

diccionario["amarillo"] = "yelow" # Agrega un nuevo elemento con valor
diccionario["rojo"] = "RED" # Modifica el valor de un elemento
del(diccionario["azul"]) # Elimina el elemento del diccionario

print(diccionario)

# Otro tipo de estructura
diccionario2 = {"Jose":[22, 1.80], "Liza":{"Edad":22, "Estatura":1.79}}
print(diccionario2)
print(diccionario2["Liza"])

# Ejemplo 3
equipo = {10:"Jose", 8:"Viviana", 3:"Lizangel"}
print(equipo)
print(equipo[10])
print(equipo.get(11, "No existe el jugador")) # Busca el valor de una clave, si no existe da un mensaje
print(equipo.keys()) # Obtiene las claves del diccionario
print(equipo.values()) # Obtiene el valor de las claves
print(equipo.items()) # Obtiene el contenido del diccionario dentro de Tuplas

equipo.clear()  # Vacia el diccionario
print(equipo)







