#31.Escribe un algoritmo o el respectivo diagrama de flujo que determine el valor de un pasaje en avión, conociendo la distancia a recorrer, el número de días de estancia, y sabiendo que, si la distancia a recorrer es superior a 1000 Km y el número de días de estancia es superior a 7, la línea aérea le hace un descuento del 15%. (el precio por km. es de $5.000 aunque el mínimo a cobrar siempre es $100.000).
import datetime
print("-Determinar el valor de tu pasaje de avión-")
print("___________________________________________")
print("El precio se dara en pesos colombianos(COP)")

distan = float(input("Por favor ingresa la distancia a reccorrer de tu vuelo: "))
dias = int(input("Por favor ingresa el número de diás de estancia: "))
print(" ")
print("_______________________________________")

if distan > 1000 and dias > 7:
    distan *= 5000
    descuento = distan * 0.15
    distan1 = distan - descuento
    print("Valor original del vuelo: $", distan)
    print("Valor del descuento: $", "{0:g}".format(descuento))
    print("Valor final del vuelo: $", distan1)

else:
    if distan > 20:
        distan *= 5000
        print("Valor del vuelo: $", "{0:g}".format(distan))
    else:
        distan = 100000
        print("Valor del vuelo: $","{0:g}".format(distan))

print("Que tenga un buen viaje.")
print("Fecha: ",datetime.date.today())
print("_______________________________________")
