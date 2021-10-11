#7.	Escribe un algoritmo o el respectivo diagrama de flujo que imprima el área y el perímetro de un círculo.

#Se le pide al usuario que ingrese el radio(r) del circulo poniendo o no centimentros (cm) despues de este.
r = input("Por favor ingrese el radio(r) del circulo en cm: ")
caracters = "cm"
# Este for se utiliza para eliminar los caracteres definidos anteriormente (cm) de un "string".
#Por esta razón no se define el dato ingresado como flotante al inicio si no que se hace depues del ciclo "for".
for x in range(len(caracters)): 
    r = r.replace(caracters[x],"")
r = float(r)

p = 2* 3.1416 * r #Por medio del dato ingresado se desarrolla la ecuación del perimetro de un circulo.
a = 3.1416 * r**2 #Por medio del dato ingresado se desarrolla la ecuación del area de un circulo.

print("El area del  circulo es:", a ,"cm**2"+".")
print("El perimetro del circulo es:", p ,"cm"+".")