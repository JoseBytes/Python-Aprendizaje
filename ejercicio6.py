# Condiciones con Operaciones Ralacionales y Logicas

edad = int(input("Introduce tu Edad: "))
msg = ""
#if edad>0 and edad<100:
if 0<edad<100:
    status = "Edad correcta"
    if edad>=18:
        msg = "Mayor de edad"
    elif edad<18:
        msg = "Menor de edad"
else:
    status = "Error en la edad"

print(msg)
print(status)

