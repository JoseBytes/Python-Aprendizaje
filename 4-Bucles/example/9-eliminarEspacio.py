"""
Ejercicio 9:
Ingresar frases y remover espacios.
Contar numero de caracteres
"""

frase = input("Ingrese una frase: ")
print(f"Frase anterior: {frase}")

n = frase.replace(" ", "")
cantidad = 0
for i in n:
    cantidad+=1

print(n)
print(f"Cantidad de Caracteres: {cantidad}")
