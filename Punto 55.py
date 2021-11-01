#55.Escribe un algoritmo o el respectivo diagrama de flujo que dado un número determine la cantidad de números entre los cuales se puede dividir es decir sus factores.

print("Factores de un número")
print("_____________________")

num = int(input("Ingrese un número entero para hayar sus factores: "))
count = 0
mod = 1
fact = []
if num == 0:
    print(1)
else:
    while count < num:
        if num%mod==0:
            fact.append(mod)
            mod+=1
        elif num == 0:
            print(1)
        else:
            mod+=1
        count +=1
print("Los factores del número ingresado son:",fact)


#Otra opción de internet.
#print("Los factores de ", num,"son: ",)
#def factors(x):
    #if x == 1:
        #print(1 ,end =" ")
    #elif num % x == 0:
        #factors(x-1)
        #print(x, end =" ")
    #else:
        #factors(x-1)

#x = num = int(input('Enter an integer: '))

#print('The factors of', x, 'are: ',end =" ")
#factors(x)