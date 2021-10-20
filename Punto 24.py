#24.Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%) de una venta, si esta es mayor o igual 150.000 aplicar un descuento del 5%

import datetime 
print("Factura de venta")
print("________________")
venta = float((input("Por favor ingrese el valor de la venta realizada en COP: $")))

# Usamos el "{0:.3f}".format()) para que al mostrar por pantalla los números conserven 3 decimales despues del punto incluyendo los ceros. 
print("_____________________________________")
print("Valor de la venta original: ","$", "{0:.3f}".format(venta))
if venta >= 150.000: #si la venta es mayor o igual de 150.000 se le aplicara un descuento del 5% y luego el iva del 19% se le sumara ala venta total terminando imprimiendola, de lo contrario solo se le aplicara el iva del 19% de la venta.
    Descuento = venta*0.05 #Le sacamos el 5% de la venta.
    valorTotal = venta - Descuento
    iva = valorTotal*0.19  # Le sacamos el 19% del valor de la venta.
    valorTotal += iva
    print("Valor del descuento(5%) de la venta: ""$", "{0:.3f}".format(Descuento))
    print("Valor del IVA(19%) de la venta: ", "$", "{0:.3f}".format(iva))
    print("Valor  de  la  venta total: ","$", "{0:.3f}".format(valorTotal))
else:
    iva = venta*0.19  # Le sacamos el 19% del valor de la venta.
    valorTotal = venta + iva
    print("Valor del IVA(19%) de la venta: ", "$", "{0:.3f}".format(iva))
    print("Valor  de  la  venta total: ", "$", "{0:.3f}".format(valorTotal))
print("Fecha: ", datetime.date.today()) #Usamos la libreria datetime.date para mostrar por pantalla la fecha actual en que se hizo la factura.
print("Gracias por su compra, vuelva ponto.")
print("_____________________________________")
