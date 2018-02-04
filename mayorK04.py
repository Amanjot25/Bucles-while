# coding: utf-8

num1 = int(input("Escribe la cantidad de números positivos: "))
while num1 < 1:
    num1 = int(input("La cantidad tiene que ser mayor que 0. Inténtelo de nuevo: "))


num2 = int(input("Escribe un número: "))
total = 1
if num2 > 0:
    cantidad = 1
else:
    cantidad = 0

while cantidad < num1:
    num2 = int(input("Escribe otro número: "))
    if num2 > 0:
        cantidad += 1
    total += 1


if cantidad == 1:
    print("Ha escrito 1 número positivo.")
else:
    print("Ha escrito", total, "numeros,", num1, "de ellos positivos.")
print("FIN")
