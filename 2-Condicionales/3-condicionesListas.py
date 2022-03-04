# Determinar cual letra es una vocal

l = input("Escriba un caracter: ")

vocal = ('a','e','i','o','u')
consonantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
numeros = ('0','1','2','3','4','5','6','7','8','8')

#if l=='a' or l=='e' or l=='i' or l=='o' or l=='u':

if l.lower() in vocal:
    print(f"{l} es una vocal")
elif l in consonantes:
    print(f"{l} es una consonante")
elif l in numeros:
    print(f"{l} es un numero")
else:
    print(f"{l} no es un numero, vocal y consonante.")
    exit()