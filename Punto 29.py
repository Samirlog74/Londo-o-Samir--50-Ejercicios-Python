#29.Escribe un algoritmo o el respectivo diagrama de flujo que lea tres números y determine el mayor y el menor de ellos.
print("Determinar el mayor y el menor de 3 números")
print("___________________________________________")

num = float(input("Por favor ingrese un número: "))
count = 0
menor = num
mayor = num
while count < 2: #El usuario ingresara 2 números o variables pero ya se habia ingresado una anteriomente.
    num = float(input("Por favor ingrese un nuevo número: "))
    if num < menor: # se evalua la primera varibale con la 2 ingresada si esta es menor la almacenara en la variable "menor", repitiendo esto con la 3 variable. Tambien se repetira este proceso en el caso contrario almacenando el resultado en la variable "mayor".
        menor = num
    elif num > mayor:
        mayor = num
    count +=1

print("El número menor ingresado fue ", "{0:g}".format(menor)) #"{0:g}".format(menor) se usa para eliminar todo cero despues del punto.
print("El número mayor ingresado fue ", "{0:g}".format(mayor))
