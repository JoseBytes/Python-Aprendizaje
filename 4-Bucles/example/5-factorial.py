import math

numero = int(input(">>> "))

while numero<0:
    print("Error: el valor debe ser positivo")
    numero = int(input(">>> "))

factorial = 1

for i in range(1,numero+1):
    factorial*=i

print(factorial)
