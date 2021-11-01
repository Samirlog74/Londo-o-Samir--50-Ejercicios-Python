#52.Construye un algoritmo y el respectivo diagrama de flujo que permita leer una cantidad variable de números y nos indique cuantos fueron mayores a 100 y cuántos menores a 100.

print("Determinar cuantos números son mayores y menores 100")
print("____________________________________________________")


Contador = 0
Contador1 = 0
Contador2 = 0
while Contador == 0: 
    numero = float(input("Por favor ingrese un número: "))
    if numero == 0: 
        continue 
    if numero < 100:
        Contador1 += 1
    else:
        Contador2+=1 
        
    respuesta = input("Desea ingresar otro número(si o no): ")
    if respuesta.lower() == "si":
        continue
    elif respuesta.lower()== "no":
        break
    else:
        break

print("Los números ingresados mayores a 100 fueron: ",Contador2)
print("Los números ingresados menores a 100 fueron: ",Contador1)
