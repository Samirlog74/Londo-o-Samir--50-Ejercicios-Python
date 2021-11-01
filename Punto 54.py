#54.Construye un algoritmo y el respectivo diagrama de flujo que permita leer sólo números positivos hasta reunir 10 números pares o veinte veces el número 5. Indicar luego la totalidad de números leídos, la cantidad de pares, de impares y la cantidad de números 5.

print("_______________________________________")

Contador = 0
numeros = 0
pares = 0
impares = 0
números5 = 0

while Contador == 0:
    numero = int(input("Por favor ingrese un número entero: "))
    if numero == 0 or numero < 0:
        continue
    numeros +=1
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        if numero == 5:
            números5+=1

    if pares == 10 or números5 == 20:
        break

print(" ")
print("De los números enteros ingresados fueron:")
print("Cantidad números ingresados: ",numeros)
print("Números pares: ", pares)
print("Números impares: ", impares)
print("Cantidad de números 5: ", números5)

