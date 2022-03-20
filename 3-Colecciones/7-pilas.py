# Pila o Stack es una estructura de datos donde el ultimo en entrar es el primero en salir
# Last Input / First Output
# Se hacen mediante listas

pila = ["Jose", "Viviana", "Liza", "Maria"]

print(f"La pila actual es: {pila}")

pila.append("Brenda")

print(f"El ultimo en entrar es: {pila[-1]}")
print(pila)

primero = pila.pop()
print(f"El primero en salir es: {primero}")
print(pila)
