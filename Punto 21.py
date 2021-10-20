#21.Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y determine si es par o impar.
print("Determinar si un número es par o impar")
print("_____________________________________")
num = int(input("Por favor ingrese un número entero: "))
num1 = num%2 #la variable se le saca el mod 2.


if num != 0:#si el numero ingresado es diferente a cero el programa seguira de lo contrario imprimira que el número ingresado es invalido.
    if num1 == 0: # Este condicional determina que si el residuo de num1 es 0 el número es par de lo contrario sera impar.
        print("El número", num, "es par." )
    else:
        print("El número", num, "es impar.")
else:
    print("El número ingresado es invalido")