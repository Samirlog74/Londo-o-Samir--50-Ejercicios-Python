#42.Escribe un algoritmo o el respectivo diagrama de flujo que imprima los primeros 10 números naturales impares.

print("Imprimir los primeros 10 números impares")
print("________________________________________")

cont = 0
numeros = []
while cont <= 19:
    cont +=1
    if cont%2 != 0:
        numeros.append(cont)

print(" ")
print(numeros)
