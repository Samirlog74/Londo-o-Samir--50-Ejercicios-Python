#2.	Escribe un algoritmo o el respectivo diagrama de flujo para imprimir el cuadrado de un número dado.

print("Calcular el cuadrado de un número")
print("_________________________________")
#Se le pide al usuario que ingrese un número cualquiera.
num = float(input("Por favor ingrese un número: ")) 
#Se eleva el número ingresado al cuadrado.
num = num**2 
#Se usa la función "{0:g}".format(float()) para asi eliminar los ceros depues de un punto.
print("El cuadrado del número ingresado es", "{0:g}".format(float(num)))
