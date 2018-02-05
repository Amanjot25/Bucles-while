# coding:utf -8

max= float(input("Escribe el valor límite: "))
while max <= 0:
    max= float(input("El lim debe ser mayor que 0. Inténtelo de nuevo: "))

num = float(input("Escribe un número: "))
suma = 0
suma += num

while suma < max:
    num = float(input("Escribe otro número: "))
    suma += num

print("Ha superado el lim. La suma de los num positivos es", str(suma) + ".")
print("FIN")
