# Blucle While

import math

numero = float(input("Digite un numero: "))

while numero<0:
    print("Ha ocurrido un error!")
    numero = float(input("Digte un numero: "))
calculo = math.sqrt(numero)
print(f"La raiz de cuadrada de {numero} es {calculo:.2f}")

# Ejemplo 2

i = 0 # variable de Iteracion
while i<10: # Mientras que i sea menor a 10 se repite el bucle
    i+=1    # La iteracion se suma +1 las 10 veces
    print(f"{i} Hola Mundo") # Se imprime el valor de la iteracion
    # El bucle se cierra hasta que i es igual a 10

# Ejemplo 3 - Para que imprima 10 veces el bucle
i = 1
while i<=10:
    print(i)
    i+=1
