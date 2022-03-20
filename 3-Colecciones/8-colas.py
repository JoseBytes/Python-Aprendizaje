# Las colas First Input / First Output

cola = ["Viviana", "Jose", "Lizangel"]

print(f"La cola actual es: {cola}")

cola.append("Brenda") # Ultimo en llegar

print(f"El ultimo en llegar es: {cola[-1]}")

print(cola)

atendido = cola.pop(0)

print(f"{atendido} esta siendo atendida")

print(cola)
