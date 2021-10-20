#33.Escribe un algoritmo o el respectivo diagrama de flujo que permita resolver una ecuación cuadrática de tipo ax2 + bx + c (tenga en cuenta todas las raíces, tanto las reales como las complejas).
print("Resolución de ecuaciones de 2do grado")
print("_____________________________________")
print("""La ecuación cuadrática tiene la forma ax**2 + bx + c. 
Donde a, b y c son variables y la x es la incognita.""")
print("_____________________________________")

from math import sqrt

ecua = input("Por favor ingrese la ecuación cuadrática como la descrita anteriormente (ax**2 + bx + c): ")
caracter = "*2"
for x in range(len(caracter)):
    ecua = ecua.replace(caracter[x], "")
ecua = ecua.split("x")

if ((float(ecua[1])**2)-4*float(ecua[0])*float(ecua[2])) < 0:
    print("La solución de la ecuación es con números complejos.")
else:
    x1 = (-float(ecua[1])+sqrt(float(ecua[1])**2-(4*float(ecua[0])*float(ecua[2]))))/(2*float(ecua[0]))
    x2 = (-float(ecua[1])-sqrt(float(ecua[1])**2-(4*float(ecua[0])*float(ecua[2]))))/(2*float(ecua[0]))
    print("Las soluciones de la ecuación son: ", "{0:g}".format(x1), "y","{0:g}".format(x2))


#Ota solución.
#A = int(input("Ingrese la variable a: "))
#B = int(input("Ingrese la variable b: "))
#C = int(input("Ingrese la variable c: "))

#if ((B**2)-4*A*C) < 0:
    #print("La solución de la ecuación es con números complejos")
#else:
    #x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
    #x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
    #print("Las soluciones de la ecuación son: ", x1, "y", x2)
