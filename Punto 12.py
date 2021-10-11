#12.Escribe un algoritmo o el respectivo diagrama de flujo que determine la distancia recorrida por un objeto luego de una cantidad de tiempo, si se sabe que va en línea recta y además se conoce su aceleración y su velocidad.

print("Calcular la idstancia recorrida de un objeto")
print("____________________________________________")

objeto = input("¿A qué objeto nos referiremos? ") #Le pedimos al usuario que ingrese a que objeto nos referimos empezando con una o un + objeto.
objeto = objeto.lower() #convertimos todo el texto en minuscula para que no haya problema.
objeto = objeto.split(" ") #Convertimos el string en lista seprando elementos por espcacio.
if "un" in objeto: #este condicional es para que si el objeto empieza por "un" lo reemplace por "el" y si empieza por "una" lo reemplace por "la".
    objeto[0] = "el "
elif "una" in objeto:
    objeto[0] = "la "
objeto1 = "".join(objeto) #por medio de ".join()" convertimos el texto de nuevo a "str"


time = "Introduzca el tiempo en que se movera "+ objeto1 +" "+"en segundos(seg): " # hacemos una variable donde se introduce la pregunta y el objeto ingresado para la siguiente input.
time1 = float(input(time))

objeto1 = objeto1.split(" ") #Convertimos el string en lista seprando elementos por espcacio.
if "la" in objeto1: #este condicional es para que si el objeto empieza por "la" lo reemplace por "de la" y si empieza por "el" lo reemplace por "del".
    objeto1[0] = "de la "
elif "el" in objeto1:
    objeto1[0] = "del "
# por medio de ".join()" convertimos el texto de nuevo a "str"
objeto2 = "".join(objeto1)

# hacemos una variable donde se introduce la pregunta y el objeto ingresado para la siguiente input.
aceler = "Introduzca la acelaración " + objeto2 +" "+"en metros por segundo cuadrado(m/s**2): "
aceler1 = float(input(aceler))

veloc = "Introduzca la velocidad inicial " + objeto2 +" "+ "en metros por segundo(m/s): " # hacemos una variable donde se introduce la pregunta y el objeto ingresado para la siguiente input.
veloc1 = float(input(veloc))

disti = "Introduzca la distancia inicial " + objeto2 +" " + "en metros(m): " # hacemos una variable donde se introduce la pregunta y el objeto ingresado para la siguiente input.
disti1 = 0
if veloc1 == 0: # Este condicional se refiere a que si la "veloc1" o velocidad inicial es cero su distancia inicial es igual a cero de lo contrario le pedira al usuario que ingrese la distancia inicial.
    disti1 = 0
else:
    disti1 = float(input(disti)) # Por medio de este input se le pide al usuario la distancia inicial

Distf = disti1 + (veloc1*time1) + ((aceler1*(time1**2))/2) # Esta es la formula del Movimiento Uniforme Rectilineo Acelerado.

print("La distancia recorrida por " + objeto2 +" es de ", "{0:g}".format(float(Distf)), "m.") #Imprime los resultados de la formula anterior.
