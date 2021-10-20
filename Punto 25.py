#25.Escribe un algoritmo o el respectivo diagrama de flujo que lea un número y si este es mayor o igual a 10 devuelva el triple de este, de lo contrario la cuarta parte de este.
print("______________________________________________________")

num = float(input("Por favor ingrese un número: "))

if num >= 10: #Si el número es mayor o igual a 10, la variable ingresada se multiplicara por tres de los contrario la variable se divide en 4, terminando imprimiendo el resultado.
    num *= 3
    print("El triple del número ingresado es: ","{0:g}".format(num))
else:
    num /= 4
    print("La cuarta parte del número ingresado es: ","{0:g}".format(num))