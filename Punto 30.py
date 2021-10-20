#30.Escribe un algoritmo o el respectivo diagrama de flujo que lea tres números y determine si la suma del primero y el segundo es mayor o menor que el tercero.

num = input("Por favor ingrese 3 números separandolos con comas(,): ")
num = num.split(",") # Se separan las variables por medio de la coma (,).
Suma = float(num[0])+float(num[1]) # Se suma la primera y segunda varibale ingresada.

if Suma > float(num[2]): # si la suma de la primera y segunda variable es mayor se imprimira tal toca, tambien ocurrira lo mismo si son iguales o de lo contrario imprimira que es mnor.
    print("La suma de los dos primeros números ingresados es mayor que", num[2])
elif Suma == float(num[2]):
    print("La suma de los dos primeros números ingresados es igual que", num[2])
else:
    print("La suma de los dos primeros números ingresados es menor que", num[2])