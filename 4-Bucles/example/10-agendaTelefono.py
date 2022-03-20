# Simular una agenda telefonica, debe estar en un diccionario cuya clave sea nombre y valor telefono.
# Tiene que contener un menu para agregar, modificar, eliminar, ver contactos y salir.

# Menu
print("Contactos")
print("(1) Agregar")
print("(2) Modificar")
print("(3) Eliminar")
print("(4) Ver contactos")
print("(5) Salir")

# Declaracion de variables
contacts = {}

# Condicionales
while True:
    options = int(input("\nIngrese una opcion para continuar: "))
    if options==1:
        name = input("Nombre del contacto: ")
        if name in contacts:
            print("El contacto ya existe")
            print()
        else:
            number = int(input("Ingrese un numero telefonico: "))
            contacts[name]=number
            print("Contacto agregado!")
    elif options == 2:
        print("\nModificar Contacto")
        name = input("Nombre del contacto: ")
        if name in contacts:
            number = int(input("Ingrese el nuevo numero telefonico: "))
            contacts[name] = number
            print("Contacto modificado!")
        else:
            print("El contacto no existe")
    elif options == 3:
        while True:
            print("\nEliminar Contacto")
            name = input("Nombre del contacto: ")
            if name in contacts:
                confirm = input("Estas seguro de eliminar? S/n: ")
                if confirm=="S" or confirm=="s":
                    del(contacts[name])
                    print("Contacto eliminado!")
                    break
                elif confirm=="N" or confirm=="n":
                    print()
                    break
                else:
                    print("Opcion invalida")
            else:
                print("El contacto no existe")
    elif options == 4:
        print("Contactos:")
        for k,v in contacts.items():
            print(f"{k} -> {v}")
    elif options == 5:
        break
    else:
        print("Opcion invalida")
