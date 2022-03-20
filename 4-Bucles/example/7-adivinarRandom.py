"""
Realizar un juego para adivinar un numero:
Realiza un rango de numeros aleatorias de 0-100
Luego ir pidiendo numeros indicando "es mayor" o "es menor" segun sea
mayor o menor con respecto al N. El proceso termina cuando el usario acierta y 
mostrar el numeros de intentos
"""

import random as rd

objetivo = rd.randint(0,100)
i = 0
while True:
    i+=1
    numero = int(input(">>> "))
    if numero>objetivo:
        print("El numero es mayor")
    elif numero<objetivo:
        print("El numero es menor")
    else:
        print(f"El numero es {objetivo}")
        break
print(f"Total de intentos {i}")
