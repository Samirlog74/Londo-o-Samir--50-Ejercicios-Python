#32.Escribe un algoritmo o el respectivo diagrama de flujo que permita determinar si un año dado es o no bisiesto.

print("Comprobar si un año es bisiesto")
print("_______________________________")
año = int(input("Por favor ingrese el año: "))

if año % 4 == 0 and año % 100 != 0: #Si la variable ingresada es divisible entre 4 pero no entre 100 se imprime que el año es bisiesto, tambien si es divisible entre 400 es bisiesto de lo contrario se imprimira que el año ingresado no es bisiesto.
    print("El año", año, "es bisiesto.")

elif año % 400 == 0:
    print("El año", año, "es bisiesto.")

else:
    print("El año", año, "no es bisiesto.")


