"""
Hacer una suma se numeros pares dentro de un rango:
Ejemplo: 
Suma de numeros pares del 2 al 30
Suma total: 240
"""

a = int(input(">>> "))
b = int(input(">>> "))
b +=1
suma = 0

for i in range(a,b):
    if i%2==0:
        suma += i
print(suma)
