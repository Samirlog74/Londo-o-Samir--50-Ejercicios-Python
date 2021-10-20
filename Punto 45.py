#45.Escribe un algoritmo o el respectivo diagrama de flujo que dado un número n, imprima los números entre 1 y n siguiendo la siguiente secuencia: 1   -2   3  -4   5  -6 ….

print("Seguir la secuencia")
print("___________________")

num = int(input("Por favor ingresa un número: "))

cont = 0
numeros = []
while cont < num:
    cont += 1
    if cont % 2 == 0:
        cont1 = cont * -1
        numeros.append(cont1)
    else:
        numeros.append(cont)

print(" ")
print(numeros)
