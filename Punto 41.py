#41.Escribe un algoritmo o el respectivo diagrama de flujo que imprima los 10 primeros números naturales.

print("Imprimir los 10 primeros números naturales")
print("__________________________________________")

cont = 0
numeros = []
while cont < 10:
    cont += 1
    numeros.append(cont)
print(" ")
print(numeros)

#Otra opción 
#for x in range(1,11):
#print(x)
