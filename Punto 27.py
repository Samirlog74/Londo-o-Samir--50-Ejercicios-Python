#27.Escribe un algoritmo o el respectivo diagrama de flujo que lea dos números y determine el mayor de ellos.

print("Determinar entre dos números cual es mayor")
print("__________________________________________")

num = float(input("Por favor ingrese un número: "))
num1 = float(input("Por favor ingrese otro número: "))

if num > num1: # si la primera variable ingresada es mayor que la segunda se imprimira que este es mayor, tambien si son iguales se imrpimira tal cosa, de lo contrario a todo esto se imprimira que la 2 varible es mayor que la primera.
    print("El número", "{0:g}".format(num), "es mayor que", "{0:g}".format(num1)) #"{0:g}".format(num1) se usa para eliminar los ceros despues de un punto.
elif num == num1:
    print("Los dos números son iguales")
else:
    print("El número","{0:g}".format(num1), "es mayor que", "{0:g}".format(num))
