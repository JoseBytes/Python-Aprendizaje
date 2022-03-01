zapato = float(25)
camisa = float(15)
pantalon = float(5)
descuento = float(0.15)

print("Tienda de Vestuario")
print("\n")
print("Zapatos tienen un valor de 25$")
print("Camisas tienen un valor de 15$")
print("Pantalon tienen un valor de 5$")
print("\n")

compraZ = float(input("Ingrese la cantidad de Zapatos: "))
compraC = float(input("Ingrese la cantidad de Camisas: "))
compraP = float(input("Ingrese la cantidad de Pantalones: "))

compraZ *= zapato
compraC *= camisa
compraP *= pantalon

subtotal = compraZ+compraC+compraP
descuentoC = subtotal*descuento
total = subtotal-descuentoC

print("\n")
print(f'El subtotal es de: {subtotal}$')
print(f'El descuento es de: {descuentoC:.2f}$ (15%)')
print(f'Total a Pagar: {total}$')
