# coding: utf-8

a = int(input("Escriba un número: "))
b = int(input("Escriba un número mayor que " + str(a) + ": "))

while b > a:
    a = b
    b = int(input("Escriba un número mayor que " + str(a) + ": "))

print(b, "no es mayor que", str(a) + ".")
print("FIN")
