#18.Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántos horas minutos y segundos representan. Por ejemplo si el valor es 86399, imprimirá el siguiente resultado -->  23:59:59
import datetime #Importamos el modulo "datatime" para ejecutar la función "datatime.timedelta" y asi hacer conversiones del tiempo de minutos o segundos a horas.
print("Conversion de segundos a horas, minutos y segundos")
print("______________________________")

seg = float(input("Por favor ingrese la cantidad de segundos(seg): ")) # Le pedimos al usuario que ingrese la cantidad de segundos que quiera 

print("{0:g}".format(seg),"segundos en horas,minutos y segundos son ",datetime.timedelta(seconds = seg),".")