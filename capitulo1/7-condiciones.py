# Cual es el numero mayor

a = int(input("Ingrese un valor A: "))
b = int(input("Ingrese un valor B: "))
c = int(input("Ingrese un valor C: "))

if a>=b and a>=c:
    print(f"El numero mayor es: {a}")
elif b>=a and b>=c:
    print(f"El numero mayor es {b}")
elif c>=a and c>=b:
    print (f"El numero mayor es {c}")