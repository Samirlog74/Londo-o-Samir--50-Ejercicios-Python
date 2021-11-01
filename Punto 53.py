#53.Construye un algoritmo y el respectivo diagrama de flujo que permita leer una cantidad variable de números indicando finalmente lo siguiente:
#• cuántos números fueron positivos
#• cuántos fueron negativos
#• cuantos fueron pares
#• cuantos fueron impares
#• cuántos fueron múltiplos de ocho

Contador = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
multiocho = 0
while Contador == 0: 
    numero = int(input("Por favor ingrese un número entero: "))
    if numero == 0: 
        continue 

    if numero > 0:
        positivos += 1
    else:
        negativos+=1
    
    if numero % 2 == 0:
        pares += 1
        if numero % 8 == 0:
            multiocho += 1
    else:
        impares+=1

    respuesta = input("Desea ingresar otro número (si o no): ")
    if respuesta.lower() == "si":
        continue
    elif respuesta.lower()== "no":
        break
    else:
        break
print(" ")
print("De los números enteros ingresados fueron:")
print("Positivos: ",positivos)
print("Negativos: ", negativos)
print("Pares: ",pares)
print("Impares: ",impares)
print("Multiplos de ocho: ", multiocho)
