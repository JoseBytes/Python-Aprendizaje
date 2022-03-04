# Ejercicio determinar si ambos numeros son pares

num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese un valor: "))

if num1%2==0 and num2%2==0:
    print("Ambos numeros son pares.")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es un numero par.")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es un numero par.")
else:
    print("Ambos numeros son impares.")
