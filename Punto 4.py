# 4.Escribe un algoritmo o el respectivo diagrama de flujo para imprimir la suma, resta, multiplicación, división y residuo de dos números dados.
print("Calcular la suma, resta, multiplicación, división y residuo de dos números.")
print("___________________________________________________________________________")
#Se le pide al usuario que ingrese dos números cualesquiera.
num1 = float(input("Por favor ingrese un número: ")) # 
num2 = float(input("Por favor ingrese otro número: "))

#Se usa la función "{0:g}".format(float()) para asi eliminar los ceros depues de un punto.
print("La suma de los dos números es:", "{0:g}".format(float(num1+num2)))#Se suman los dos número dados.
print("La resta de los dos números es:", "{0:g}".format(float(num1-num2)))#Se restan los dos números dados.
print("La multiplicación de los dos números es:", "{0:g}".format(float(num1*num2)))#Se multiplican los dos números dados.
print("La división de los dos números es:", "{0:g}".format(float(num1/num2)))#Se dividen los dos números dados.
print("El residuo de la divisón de los dos números es:", "{0:g}".format(float(num1%num2)))#Se saca el residuo de los dos números dados.



