#20.Escribe un algoritmo o el respectivo diagrama de flujo que, dada un numero de 4 cifras, reordene sus dígitos de manera inversa. Por ejemplo 3245 ---> 5423
print("Devolver un número alrevez")
print("__________________________")
num = int(input("Dame un número entero de 4 cifras: "))
inver = 0
r = 0
while num != 0: #Este ciclo "While" sacara el residuo del número guardandolo en"r", luego se divide en 10 sacando el entero, luego se multiplica y se suma 10 +r. repitiendose el ciclo hasta que "num" sea cero.
    r = num%10 # Se le saca el residuo a ese número con 10
    num = num//10 # se divide por 10.
    inver = inver*10+r # se le suma el residuo multiplicado por 10.

print("El número de 4 cifras invertido sera: ",inver)