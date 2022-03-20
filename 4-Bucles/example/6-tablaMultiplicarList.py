"""
Tabla de multiplicar:
Guardar en una lista las tablas de multiplicar hasta el 10.
Por ejemplo: si digita el 5 las lista tendra: 5,10,15,20,25,30,35...50
"""

numero = int(input("Ingrese un numero a multiplicar: "))
tabla = list()

while numero<0:
    print("Error, el numero debe ser positivo: ")
    numero = int(input("Ingrese un numero a multiplicar"))

for x in range(1,11):
    multiplicacion = x*numero
    tabla.append(multiplicacion)

print(tabla)
