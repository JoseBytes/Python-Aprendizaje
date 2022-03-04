# Simulacion de Cajero Automatico con un saldo a favor de 1000$ - Ejercicio Basico y Simple
# Simulando Condiciones Multiples

# Menu
print("Menu")
print("Ingrese una de las siguientes opciones para realizar una operacion")
print("1 - Para ingresar dinero")
print("2 - Para retirar dinero")
print("3 - Mostrar saldo")
print("4 - Salir")
print()

# Saldo Inicial
saldo = float(1000)

while True:
    # Entrada
    opcion = int(input("Ingrese una opcion: "))

    if opcion==1:
        sumar = float(input("Ingrese el monto: "))
        saldo+=sumar
        print(f"Saldo: {saldo}")
        print()
    elif opcion==2:
        restar = float(input("Ingrese la cantidad a retirar: "))
        if restar>saldo:
            print("No tiene suficiente dinero")
            print()
        else:
            saldo-=restar
            print(f"Saldo: {saldo}")
            print()
    elif opcion==3:
        print(f"Saldo: {saldo}")
        print()
    elif opcion==4:
        exit()
        break
    else:
        print("Error: Las opcion no es valida.")
        print()
