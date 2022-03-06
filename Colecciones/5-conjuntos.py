a = {1, 2, 3}
b = {3, 4, 5}

c = {1, 2, 3, 4, 5}

print(a.union(b))                   # a | b Union: Une solo los elementos que hay en ambos conjuntos
print(a.intersection(b))            # a & b Interseccion: Agrega los elementos que se repite en A y B
print(a.difference(b))              # a - b Diferencia: Agrega los elementos que estan en A y no en B
print(a.symmetric_difference(b))    # a ^ b Diferencia Simetrica: Agrega los elementos que no estan en A y B

print(a.issubset(c)) # Determina si A es un subconjunto de C
print(c.issuperset(a)) # Determina si C es un superconjunto de A
print(a.isdisjoint(c)) # Determina si A no compartes elementos en comun con B

inmutable = frozenset(a) # Convierte un conjunto en inmutable
print(inmutable)
