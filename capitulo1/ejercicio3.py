print("Convierta Decimal a Binario")

binario = int(input("Ingrese un valor: "))
bin = format(binario, 'b')
#bin = bin(binario)
#bin = bin.strip('0b')

print(f'El valor es (bin): {bin}')

print("\nConvierta el Binario a Decimal")

decimal = int(input("Ingrese un valor: "), 2)
print(f'El valor es (dec): {decimal}')

longitud = len(bin)
print(f'\nLa longitud del Bin es de {longitud} bit')
