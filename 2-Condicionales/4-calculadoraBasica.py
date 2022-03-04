# Calculadora Aritmetica Basica
# Simulando condiciones multiples

print("Presione (+) para sumar")
print("Presione (-) para restar")
print("Presione (*) para multiplicar")
print("Presione (/) para dividir")
print("\n")

operacion = str(input("Ingresa el simbolo de operacion: "))
valor1 = float(input("Ingresa un valor: "))
valor2 = float(input("Ingresa un valor: "))

if operacion == '+':
    resultado = valor1+valor2
elif operacion == '-':
    resultado = valor1-valor2
elif operacion == '*':
    resultado = valor1*valor2
elif operacion == '/':
    resultado = valor1/valor2
else:
    print("Error: La operacion es incorrecta.")
    exit()

print(f"El resultado es: {resultado}")