# coding:utf -8

a= int(input("Escribe un numero: "))
b= int(input("Escribe un numero mayor que " + str(a) + ": "))

while a >= b:
	b=input(str(b) + "No es mayor que " + str(a) + "Inténtalo de nuevo:")
c=float(input("Escribe un numero entre" + str(a) + " y " + str(b) + ": "))
count=0

while a <= c <= b:
    count += 1
    c=float(input("Escribe un numero entre" + str(a) + " y " + str(b) + ": "))

print("He introducido", count, "numeros entre", a, "y", str(b) + ".")
print("FIN")


