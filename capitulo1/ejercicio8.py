# Determinar cual letra es una vocal

l = str(input("Escriba un caracter: ")).lower()

if l=='a' or l=='e' or l=='i' or l=='o' or l=='u':
    print(f"{l} es una vocal")
else:
    print(f"{l} No es una vocal")
