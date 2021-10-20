#19.Escribe un algoritmo o el respectivo diagrama de flujo que, dada una cantidad de dinero, determine la menor cantidad de billetes de cada denominación que se puede entregar.

vueltas = input("Por favor ingrese la cantidad de dinero en pesos colombianos(COP): $")
vueltas = vueltas.split(".") # En el caso de ingresar puntos el usuario el comando "split" separara los números.
vueltas = int("".join(vueltas)) #Por medio del comando ".join" volvera a unir los números y convirtiendolos en enteros con el comando "int" para que si el usuario ingrese o no puntos el resultado sea el mismo.

moned_50 = vueltas #Por medio de operaciones se define el número billetes que se puede contener la cantidad de dinero ingresada empezando desde el mayor a menor.
bille_100 = (moned_50-moned_50%100000)//100000
moned_50 = moned_50%100000
bille_50 = (moned_50-moned_50%50000)//50000
moned_50 = moned_50%50000
bille_20 = (moned_50-moned_50%20000)//20000
moned_50 = moned_50%20000
bille_10 = (moned_50-moned_50%10000)//10000
moned_50 = moned_50%10000
bille_5 = (moned_50-moned_50%5000)//5000
moned_50 = moned_50%5000
bille_2 = (moned_50-moned_50%2000)//2000
moned_50 = moned_50%2000
bille_1 = (moned_50-moned_50%1000)//1000
moned_50 = moned_50%1000
moned_500 = (moned_50-moned_50%500)//500
moned_50 = moned_50 % 500
moned_200 = (moned_50-moned_50%200)//200
moned_50 = moned_50%200
moned_100 = (moned_50-moned_50%100)//100
moned_50 = moned_50%100 
moned_50 = (moned_50-moned_50%50)//50
moned_50 = moned_50%50

print("La menor cantidad de billetes a entregar es: ")
print('Billetes de $100.000:',bille_100 )
print('Billetes de $50.000:', bille_50)
print('Billetes de $20.000:', bille_20)
print('Billetes de $10.000:', bille_10 )
print('Billetes de $5.000:',  bille_5)
print('Billetes de $2.000:',  bille_2)
print('Billetes de $1.000:',  bille_1)
print('Monedas de $500:', moned_500)
print('Monedas de $200:', moned_200)
print('Monedas de $100:', moned_100)
print('Monedas de $50: ', moned_50)
