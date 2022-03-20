# Determinar si una palabra es Palindromo

cadena = input("Ingrese una palabra: ")
palindromo = cadena[::-1] #slicing invierte el orden de la cadena

if cadena == palindromo:
    print("\nLa palabra es un Palindromo")
else:
    print("La palabra no es un Palindromo")

print(f"Palabra inicial: {cadena}")
print(f"Palabara invertida: {palindromo}")
