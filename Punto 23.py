#23.Escribe un algoritmo o el respectivo diagrama de flujo que lea un número e indique si este es par-positivo, par-negativo, impar-positivo o impar-negativo.
print("Determinar si un número es par-positivo o negativo y si es impar-positivo o negativo")
print("_____________________________________")
num = int(input("Por favor ingrese un número entero: "))
num1 = num % 2  # la variable se le saca el mod 2.


if num != 0:  # si el numero ingresado es diferente a cero el programa seguira de lo contrario imprimira que el número ingresado es invalido.
    if num1 == 0:  # Este condicional determina que si el residuo de num1 es 0 el número es par de lo contrario sera impar.
        if num < 0:  # Este condional dice que si el número es menor que 0 sera negativo de lo contrario serapositivo.
            print("El número", "{0:g}".format(num),   "es par-negativo.")  #El "{0:g}".format(num) se utiliza para eliminar todos los ceros depues de un punto.
        else:
            print("El número", "{0:g}".format(num),   "es par-positivo.")
    else:
        if num < 0:  # Este condional dice que si el número es menor que 0 sera negativo de lo contrario serapositivo.
            print("El número", "{0:g}".format(num), "es impar-negativo.")
        else:
            print("El número", "{0:g}".format(num), "es impar-positivo.")
else:
    print("El número ingresado es invalido")
