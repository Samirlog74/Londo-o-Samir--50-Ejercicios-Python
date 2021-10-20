#16.Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántas horas representan.

print("Conversion de segundos a horas")
print("______________________________")

seg = float(input("Por favor ingrese la cantidad de segundos(seg): ")) # Le pedimos al usuario que ingrese la cantidad de segundos que quiera 

horas = seg/3600 

print("{0:g}".format(seg),"segundos son ", "{0:.2f}".format(horas),"horas.")
