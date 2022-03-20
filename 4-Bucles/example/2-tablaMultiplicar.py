#!/usr/bin/python

# Hacer una lista del 1 al 10 y luego multiplicar todos los elementos por un numero que digite el usuario.

lista = list(range(1,11))
x = int(input(">>> "))

#index = 0
#for i in lista:
#    lista[index] *= x
#    index +=1

for index,i in enumerate(lista):
    lista[index] *= x

for i in lista:
    print(i,end=" ")
