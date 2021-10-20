#49.Escribe un algoritmo o el respectivo diagrama de flujo que lea n números y calcule su suma y su promedio.

print("Calcular la suma y promedio de 10 números ingresados")
print("____________________________________________________")

Suma = 0 
Contador = 0
Contadorprom = 0
while Contador == 0: # Se define un ciclo while que se repetira 10 veces ya que el contador vale 0 y solo seguira mientras sea menor de 3.
    numero = float(input("Por favor ingrese un número: ")) #Se le pide al usuario que ingrese un número cualquiera.
    if numero == 0: # Este condicional tiene un continue pues si el usuario ingresa un cero el ciclo continuara hasta que ingrese los 3 números que se piden.
        continue 
    Suma += numero # Se suman los números ingresados. 
    Contadorprom += 1
    Prom = Suma / Contadorprom # Se saca el promedio diviendo la suma de todos los números por 3.
    respuesta = input("Desea ingresar otro número(si o no): ")
    if respuesta.lower() == "si":
        continue
    elif respuesta.lower()== "no":
        break
    else:
        break
    
print("La suma de los números ingresados es: ", "{0:g}".format (Suma))
print("El promedio de los  números ingresados es:", "{0:g}".format (Prom)) # Se usa "{0:g}".format(float(Prom)) para eliminar todos los ceros depues de un punto.
