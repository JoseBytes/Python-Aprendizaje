"""
Hacer un simulador de cajero automatico:
Ingresar saldo
Retirar saldo
Mostrar saldo
Salir del sistema
"""

print("MENU")
print("1 - Ingresar dinero en la cuenta")
print("2 - Retirar dinero")
print("3 - Mostrar saldo")
print("4 - Salir")

saldo = float(1000)

while True:
    opcion = int(input("\nIngrese una opcion: "))
    if opcion==1:
        cantidad = float(input("Ingrese una cantidad: "))
        saldo+=cantidad
        print(f"Saldo: {saldo}")
        print()
    elif opcion==2:
        cantidad = float(input("Ingrese una cantidad: "))
        if cantidad>saldo:
            print("No tiene suficiente dinero.")
        else:
            saldo-=cantidad
            print(f"Saldo: {saldo}")
            print()
    elif opcion==3:
        print(f"Saldo: {saldo}")
        print()
    elif opcion==4:
        break
    else:
        print("La opcion es invalida.")
