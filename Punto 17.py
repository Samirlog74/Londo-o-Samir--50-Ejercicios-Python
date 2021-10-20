#17.Escribe un algoritmo o el respectivo diagrama de flujo que dada una cantidad de segundos indique cuántos minutos representan

print("Conversion de segundos a minutos")
print("______________________________")

# Le pedimos al usuario que ingrese la cantidad de segundos que quiera
seg = float(input("Por favor ingrese la cantidad de segundos(seg): "))
minutos = seg/60

print("{0:g}".format(seg), "segundos son ", "{0:.2f}".format(minutos), "minutos.")
