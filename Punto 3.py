#3.	Escribe un algoritmo o el respectivo diagrama de flujo para imprimir la suma de dos números dados.
print("Sumar dos números cualesquiera")
print("______________________________")
#Se le pide al usuario que ingrese dos número mediante "input".
num1 = float(input("Por favor ingrese un número a sumar: "))
num2 = float(input("Por favor ingrese otro número: "))
#Se suman los dos números ingresados.
Suma = num2 + num1
#Se usa la función "{0:g}".format(float()) para asi eliminar los ceros depues de un punto.
print("La suma de los dos números ingresados es: ", "{0:g}".format(float(Suma)))
