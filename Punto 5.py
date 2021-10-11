# 5.Escribe un algoritmo o el respectivo diagrama de flujo que lea un número decimal e imprima su parte entera y su parte decimal por aparte.

#El usuario ingresa un número decimal.
num = float(input("Por favor ingrese un número decimal: ")) 

y = num // 1  # Se divide el número solo parte entera.
num = num%1   #Se saca el residuo del número.
y = int(y)

print("La parte entera del número ingresado es: ", y)
print("La parte decimal del numero ingresado es: ", num)

# Otra opción.
#print("La parte entera del número ingresado es:", int(num))
#print("La parte decimal del número ingresado es:", num- int(num))