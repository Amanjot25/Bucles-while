# coding: utf-8

a = float(input("Escriba un número: "))
b = float(input("Escriba un número mayor que " + str(a) + ": "))

while b > a:
    b = float(input("Escriba un número mayor que " + str(a) + ": "))

print()
print(b, "no es mayor que", str(a) + ".")
print("FIN")

 
   
