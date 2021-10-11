#9.	Escribe un algoritmo o el respectivo diagrama de flujo que dados tres números calcule el promedio de dichos números.
print("Calcular promedio de tres números.")
print("_________________________________")

Suma = 0 
Contador = 0
while Contador < 3: # Se define un ciclo while que se repetira 3 veces ya que el contador vale 0 y solo seguira mientras sea menor de 3.
    numero = float(input("Por favor ingrese un número: ")) #Se le pide al usuario que ingrese un número cualquiera.
    if numero == 0: # Este condicional tiene un continue pues si el usuario ingresa un cero el ciclo continuara hasta que ingrese los 3 números que se piden.
        continue 
    Suma += numero # Se suman los números ingresados.
    Contador += 1  # El contador es igual a los números ingresados. 
    Prom = Suma / Contador # Se saca el promedio diviendo la suma de todos los números por 3.

print("El promedio de los 3 números ingresados es:", "{0:g}".format(float(Prom))) # Se usa "{0:g}".format(float(Prom)) para eliminar todos los ceros depues de un punto.
