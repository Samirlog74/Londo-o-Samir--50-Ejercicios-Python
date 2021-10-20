#50.Escribe un algoritmo o el respectivo diagrama de flujo para leer una cantidad variable de números e indicar el promedio de los números pares y el promedio de los números impares.

print("Promediar numeros pares e impares de x cantidad de números")
print("__________________________________________________________")

Suma = 0 
Contador = 0
Contador1 = 0
Contadorprom = 0
pares = []
impares = []
while Contador == 0: 
    numero = float(input("Por favor ingrese un número: "))
    if numero == 0: 
        continue 
    if numero%2==0:
        pares.append(numero)
        Contadorprom += 1
    else:
        impares.append(numero)
        Contador1+=1 
    respuesta = input("Desea ingresar otro número(si o no): ")
    if respuesta.lower() == "si":
        continue
    elif respuesta.lower()== "no":
        break
    else:
        break

print("La suma total entre todos los números ingresados es: ", "{0:g}".format (sum(impares)+sum(pares)))
print("El promedio entre todos los números ingresados es: ", "{0:g}".format ((sum(impares)+sum(pares))/Contador1+Contadorprom))
print("La suma entre los números impares ingresados es: ", "{0:g}".format (sum(impares)))
print("El promedio de los numeros impares ingresados es: ", "{0:g}".format (sum(impares)/Contador1))
print("La suma entre los números pares ingresados es: ", "{0:g}".format (sum(pares)))
print("El promedio de los numeros pares ingresados es: ", "{0:g}".format (sum(pares)/Contadorprom)) 
