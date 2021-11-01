#57.Escribe un algoritmo o el respectivo diagrama de flujo que imprima el siguiente patrón.
#1
#12
#123
#1234
#12345
#123456
#1234567
#12345678
#123456789
#12345678910

print("Seguir la secuencia")
print("___________________")

num = int(input("Ingrese un número entero hasta donde quiera que sea la secuencia: "))
cont = 0
secuen = "1"
secuen1= 1

while cont < num:
    print(secuen)
    secuen1 +=1
    secuen= secuen + str(secuen1)
    cont+=1 