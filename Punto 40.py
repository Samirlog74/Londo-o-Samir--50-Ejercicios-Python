#40.Escribe un algoritmo o el respectivo diagrama de flujo que lea 3 números e indique si al menos 2 de ellos son iguales.

print("Deterinar si almenos dos de los 3 números ingresados con iguales")
print("________________________________________________________________")

num = input("Por favor ingrese 3 números separandolos con comas(,): ")

num = num.split(",")

if float(num[0]) == float(num[1]) == float(num[2]):
    print("Todos los números ingresados son iguales.")

elif float(num[0]) == float(num[1]):
    print("Los dos primeros números ingresados son iguales","("+num[0]+" y "+num[1]+").")

else:
    if float(num[1]) == float(num[2]):
        print("Los dos ultimos números ingresados son iguales","("+num[1]+" y "+num[2]+").")
    elif float(num[0]) == float(num[2]):
        print("El primer y ultimo número ingresado son iguales","("+num[0]+" y "+num[2]+").")
    else:
        print("Todos los números ingresados son diferentes.")
