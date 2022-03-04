# Ejerciciones de Operaciones Logicas, Aritmeticas y Relacionales

a = float(input("A) Ingresa una variable: "))
b = float(input("B) Ingresa una variable: "))
c = float(input("C) Ingresa una variable: "))
d = float(input("D) Ingresa una variable: "))
cal3 = float(0)

calb = ((a<2)*2 or (c==d)) and ((d>10)-2 or (d==c))
cal = (a+a) / (c+d)
cal2 =  (a+b) % (c+d)
cal3 = cal + cal2

print(cal)
print(cal2)
print(cal3)
print(calb)