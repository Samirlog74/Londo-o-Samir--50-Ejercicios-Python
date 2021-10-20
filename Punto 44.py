#44.Escribe un algoritmo o el respectivo diagrama de flujo que imprima los n primeros números naturales.

print("Imprimir los primeros números naturales indicados")
print("_________________________________________________")

num = int(input("Por favor ingresa un número: "))

cont = 0
numeros = []
while cont < num:
    cont += 1
    numeros.append(cont)
print(" ")
print(numeros)
