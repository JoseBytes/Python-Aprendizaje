import math

print("\nCalcular Area y Longitud de una Circunferencia")

r = float(input("Ingrese el radio: "))

a = round(math.pi * r**2, 2)
l = round(2 * math.pi * r, 2)

# a,l = round(a,2),round(l,2)

print(f'El area es de: {a}')
print(f'La longitud es de: {l}')

