#15.Escribe un algoritmo o el respectivo diagrama de flujo que dadas coordenadas x1,y1 y x2,y2 en el plano cartesiano calcule la distancia entre ellos (considere todos los valores positivos).
import math #Importamos la libreria "math" para poder agregar la raiz cuadrada a varias operaciones.
print("Calcular distancia entre dos puntos")
print("___________________________________")


P1 = input("Por favor ingrese el punto 1 (X1,Y1) separando los dos valores con una coma(,): ") #Se le pide al usuario que ingrese el punto 1 del plano cartesiano
P2 = input("Por favor ingrese el punto 2 (X2,Y2) separando los dos valores con una coma(,): ") #Se le pide al usuario que ingrese el punto 2 del plano cartesiano

P1 = P1.split(",") #Por medio del comando ".split()" convertimos la variable en una lista seprando los valores por medio de un caracter en este caso una coma(,)
P2 = P2.split(",")
# Formula de la distancia entre dos puntos.
Distancia = math.sqrt((float(P2[0])-float(P1[0]))**2 + (float(P2[1])-float(P1[1]))**2)

print("La distancia entre el punto 1 y punto 2 es: ", "{0:.2f}".format(Distancia)) # Se imprime la distancia entre los dos puntos pero se utiliza la función "{0:.2f}".format(Distancia) para que ese solo imprima 3 decimales.
