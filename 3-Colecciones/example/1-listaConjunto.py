# Un programa donde tenga una lista y acontinuacion elimine los elementos
# repetidos y por ultimo mostrar la lista

lista = ["Jose", "Viviana", "Luna", "Estrellas", "Marte", "Jose", 1, 2, 2, 3, 1]

#conjunto = set(lista)
#lista = list(conjunto)

lista = list(set(lista))
print(lista)
