#14.Escribe un algoritmo o el respectivo diagrama de flujo que determine la energía (en Julios) de un objeto si se conoce la masa de un objeto (en kg) y la velocidad de la luz (en m/s).

print("Calcular la energía cinética de un objeto en Julios")
print("___________________________________________________")

objeto = input("Por favor introduzca a que objeto nos referimos: ") # Se le pide al usuario que ingrese el nombre del objeto refiriendose a el por "un" o "una" + objeto.

if objeto.startswith("una"): #Con este condicional hacemos que si la palabra comienza por "una" este cambia esa palabra por "de la"
    objeto=objeto.replace("una","de la", 1)
elif objeto.startswith("un"): #Con este condicional hacemos que si la palabra comienza por "un" este cambia esa palabra por "del"
    objeto=objeto.replace("un", "del", 1)


masa = "Por favor introduzca la masa "+ objeto +" en kilogramos(kg): " # Definimos una pregunta junto al objeto ingresado anteriormente para pedirle un dato al usuario en e proximo "input".
masa1 = float(input(masa))

veloc = "Por favor introduzca la velocidad "+ objeto + " en metros por segundo(m/s): " # Definimos una pregunta junto al objeto ingresado anteriormente para pedirle un dato al usuario en el proximo "input"
veloc1 = float(input(veloc))

energi = (masa1*(veloc1**2))/2 # Esta es la formula de la cinética de un objeto en movimiento.

print("La energia cinetica " + objeto +" es de ", "{0:g}".format(float(energi)), "J.") # Muestra la energía de dicho objeto en Julios, si el número es muy grande lo podra mostrar en notación cientifica.