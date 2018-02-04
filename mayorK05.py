# coding:utf -8

num = int(input("Escribe un número: "))
suma = 0

while num > 0:
    suma += num
    num = int(input("Escribe otro número: "))

print()
print("La suma de los numeros positivos es", str(suma) + ".")
print("FIN")
