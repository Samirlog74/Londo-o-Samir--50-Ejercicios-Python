#48.Escribe un algoritmo o el respectivo diagrama de flujo que lea 10 números y calcule su suma y su promedio.

print("Calcular la suma y promedio de 10 números ingresados")
print("____________________________________________________")

Suma = 0 
Contador = 0
while Contador < 10: 
    numero = float(input("Por favor ingrese un número: ")) #Se le pide al usuario que ingrese un número cualquiera.
    if numero == 0: 
        continue 
    Suma += numero # Se suman los números ingresados.
    Contador += 1  # El contador es igual a los números ingresados. 
    Prom = Suma / Contador # Se saca el promedio diviendo la suma de todos los números
    
print("La suma de los 10 números ingresados es: ", "{0:g}".format (Suma))
print("El promedio de los 10 números ingresados es:", "{0:g}".format (Prom)) # Se usa "{0:g}".format(float(Prom)) para eliminar todos los ceros depues de un punto.
