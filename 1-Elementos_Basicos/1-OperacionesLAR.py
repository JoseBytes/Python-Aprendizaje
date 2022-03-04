# Ejerciciones de Operaciones Logicas, Aritmeticas y Relacionales

a = 10
b = 11
c = 12
d = 10

calculo = ((a>b) or (a<c)) and ((a==c) or (a>=b)) # El resultado es False

negacion = not(calculo) # Niega a False y genera True

print(f'El resultado es {negacion}') # El resultado es True
print(f'Esto es una impresion de texto')