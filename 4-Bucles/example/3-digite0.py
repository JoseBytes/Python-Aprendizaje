"""
Ejercicio de Bucles.

Incrementar una lista de numeros aleatorios.
Al introducir el numero 0 el programa se detiene.
Imprimir los elementos de mayor a mentor.
"""

l = list()
n = int(1)
while n>0:
    n = int(input(">>> "))
    l.append(n)
    if n==0:
        l.remove(0)
        l.sort()
print(l)
