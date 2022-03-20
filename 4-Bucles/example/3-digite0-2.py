"""
Ejercicio de Bucles.

Incrementar una lista de numeros aleatorios.
Al introducir el numero 0 el programa se detiene.
Imprimir los elementos de mayor a mentor.
"""

lista = list()

while 0 not in lista:
    number=int(input(">>> "))
    lista.append(number)
    lista.sort()
else:
    lista.pop(0)

print(lista)
