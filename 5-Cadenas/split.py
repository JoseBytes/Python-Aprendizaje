import re

lista = "35 + 25"

lt = lista.split(" ")[0]
lb = lista.split(" ")[2]
lsymbol = lista.split(" ")[1]
ltn = int(lt)
lbn = int(lb)

symbolis = f"{lsymbol} "
conca = symbolis + lb
arriba = f"  {lt}"
guion = ""

# Formacion de Guiones
for i in conca:
    guion +="-"

# Suma y Resta
if lsymbol=="+":
    result = ltn + lbn
    print(result)
elif lsymbol=="-":
    result = ltn - lbn
    print(result)

cadena1 = "hola ?mundo'"
for i in cadena1:
    if (re.search("?",cadena1)):
        print("error")
