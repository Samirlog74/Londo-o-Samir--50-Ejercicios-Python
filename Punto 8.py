#8.Escribe un algoritmo o el respectivo diagrama de flujo que calcule el área de un hexágono.
#Ha de decir que este programa solo calculara el area de un hexágono regular.
print("Calcular el área de un hexágono.")
print("________________________________")
#Se le pide al usuario que ingrese la medida del lado  del hexágono poniendo o no centimentros (cm) despues de este.
lado = input("Por favor ingrese la medida del lado del hexágono en cm: ")
caracters = "cm"
# Este for se utiliza para eliminar los caracteres definidos anteriormente (cm) de un "string".
#Por esta razón no se define el dato ingresado como flotante al inicio si no que se hace depues del ciclo "for".
for x in range(len(caracters)): 
    lado = lado.replace(caracters[x],"")
lado = float(lado)

if lado <= 0: #Este condicional se aplica para que si ingresan un número negativo muestre por pantalla que el número es invalido, de lo contrario mostrara el área del hexágono.
    print("La medida ingresada es invalida.")
else:
    import math  # Aca se importa una libreria para poder aplicar la raiz cuadrada de un número
# se multiplica el lado por 6 para sacar el perimetro del hexagono.
    perim = lado*6
# se aplica el teorema de pitagoras despejando uno de sus catetos por lo que debemos sacar la raiz cuadrada de la hipotenusa usando el modulo "math" con ".sqrt".
    apotem = math.sqrt((lado**2)-((lado/2)**2))
# Se calcula el área del hexágono usando la formula de perimetro*apotema/2
    area = (perim*apotem)/2
    print("El área del hexagono es: " "{0:.2f}".format(area), "cm**2.") # se usa la función "{0:.2f}".format(area) para mostrar solo dos decimales en el número. 
