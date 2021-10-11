#11.Escribe un algoritmo o el respectivo diagrama de flujo que determine el tiempo de caída de un objeto que se suelta desde una altura h.
print("Calcular cuanto demora en caer x objeto desde una determinada altura")
print("____________________________________________________________________")
g = 9.8 # Se define la variable g como gravedad.
h = input("Por favor ingrese la altura(h) en la que se solto el objeto en metros(m): ") #Se le pide al usuario que ingrese la altura desde que se solto el objeto.
caracters = "m"
# Este for se utiliza para eliminar caracteres definidos anteriormente (m) de un string Por esta razón no se define el dato ingresado como flotante al inicio si no que se hace depues del ciclo "for". Para que asi el usuario ingrese m o no, no haya problemas.
for x in range(len(caracters)): 
    h = h.replace(caracters[x], "")
h = float(h) # se define "h" como flotante.

if h < 0: #Este condicional imprime la altura es invalida si llega a ingresar un número igual o menor que cero.
    print("Altura invalida ")

else: # Este condicional imprime el tiempo de caida del objeto.
    import math #Se importa el modulo "math" para poder sacar la raiz cuadrada de un número.
    t = math.sqrt(h/(g/2)) # Se usa la ecuación de la caida libre despejando el tiempo y utilizando el modulo "math" para la raiz cuadrada.
    print("El tiempo de caida del objeto es de ", "{0:.2f}".format(t), "segundos.")  # Se utiliza "{0:.2f}".format(t) para que el número impreso solo muestre dos de3cimales.
