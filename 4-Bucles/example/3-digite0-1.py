"""
Ejercicio de Bucles.

Incrementar una lista de numeros aleatorios.
Al introducir el numero 0 el programa se detiene.
Imprimir los elementos de mayor a mentor.
"""

stop = False
col = list()

while not stop:
    number = int(input(">>> "))
    if number == 0:
        stop = True
        col.sort()
    else:
        col.append(number)
print(col)
