# Programa dos listas y que a continuacion cree las siguientes listas en las que no debe de haber repeticiones:
# Lista de palabras que aparecen en las dos listas
# Lista de palabras que aparecen en la primera lista pero no en la segunda
# Lista de palabras que aparecen en la segunda lista pero no en la primera
# Lista de palabras que aparecen en ambas listas

lista1 = [1, 2, 3, 4, 5, 6, "J", "M", "K", "P", 8]
lista2 = [7, 9, 3, 2, "J", "A", "E", "Z", "R", 8]

a = set(lista1)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = (a & b)

print(union)
print(soloA)
print(soloB)
print(interseccion)
