# 6.Escribe un algoritmo o el respectivo diagrama de flujo que determine el IVA (19%) de una venta realizada, indicando el valor original, el valor del IVA y el valor de la venta con IVA incluido.
print("Factura de venta")
print("________________")
#Le decimos al usuario que ingrese el valor orginal de la venta.
venta = float((input("Por favor ingrese el valor de la venta realizada en COP: $")))

iva = venta*0.19 #Le sacamos el 19% del valor de la venta.
valorTotal= iva + venta # Se suma el valor de la venta con su 19%.

# Usamos el "{0:.3f}".format()) para que al mostrar por pantalla los números conserven 3 decimales despues del punto incluyendo los ceros. 
print("_____________________________________")
print("Valor de la venta original: ","$", "{0:.3f}".format(venta))
print("Valor del IVA  de la venta: ","$","{0:.3f}".format(iva))
print("Valor  de  la  venta total: ","$", "{0:.3f}".format(valorTotal))
import datetime #Usamos la libreria datetime para mostrar por pantalla la fecha actual en que se hizo la factura.
print("Fecha: ",datetime.date.today())
print("Gracias por su compra, vuelva pronto.")
print("_____________________________________")
