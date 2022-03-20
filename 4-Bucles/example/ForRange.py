"""
Llenar una lista con los numeros del 1 al 5.
Luego mostrar la lista con un bucle for.
Los elementos deben mostrarse de la siguiente forma:
1-2-3-4-5-6-...-49-50
"""
#i = 1
#lista = list()
#while i<51:
#    lista.append(i)
#    i+=1

lista = list(range(1,51))

for i in lista:
   print(i,end="-")
