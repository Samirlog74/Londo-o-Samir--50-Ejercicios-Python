#47.Escribe un algoritmo o el respectivo diagrama de flujo que determine la suma de los números naturales contenidos entre dos números n y m (verificar que m>n)

print("Imprimir números naturales entre un rango dado")
print("______________________________________________")
print("Recuerda que el 2 número ingresado debe ser mayor al primero.")

num = int(input("Por favor ingresa el primer número: "))
num1 = int(input("Por favor ingresa el segundo número: "))


if num < num1:
    cont = num - 1
    numeros = []
    while cont < num1:
        cont += 1
        numeros.append(cont)
    print(" ")
    print("La suma de los números contenidos entre ",num,"y",num1,"es",sum(numeros))

else:
    print("El rango establecido es invalido.")
