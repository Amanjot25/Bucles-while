# coding:utf -8
a= int(input("Escribe un num par:"))
while a % 2!= 0:
    a = int(input(str(a) + " no es un num par. Inténtelo de nuevo: "))
count = 1
pregunta = input("¿Quiere escribir otro número par? (S/N) ")

while pregunta == "S":
	a= int(input("Escribe un num par:"))
	while a % 2!= 0:
           a = int(input(str(a) + " no es un num par. Inténtelo de nuevo: "))
	count += 1
	pregunta = raw_input("¿Quiere escribir otro número par? (S/N) ")

print("He introducido", count, "num pares.")
print("FIN")
