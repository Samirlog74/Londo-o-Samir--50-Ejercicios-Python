#22.Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y determine si es positivo o negativo.
print("Determinar si un número es negativo o positivo")
print("______________________________________________")

num = float(input("Por favor ingrese un número: "))

if num!=0:#si el numero ingresado es diferente a cero el programa seguira de lo contrario imprimira que el número ingresado es invalido.
    if num < 0: #Este condional dice que si el número es menor que 0 sera negativo de lo contrario serapositivo.
        print("El número", "{0:g}".format(num), "es negativo.") #El "{0:g}".format(num) se utiliza para eliminar todos los ceros depues de un punto.
    else:
        print("El número","{0:g}".format(num), "es positivo.")
else:
    print("El número ingresado es invalido")





#Otra opción.
#num = str(num)
#if num.startswith("-"):
    #print("El número", "{0:g}".format(float(num)),"es negativo.")
#else:
    #print("El número", "{0:g}".format(float(num)), "es positivo.")
