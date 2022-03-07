#programa que verfica si un numero es primo 
#Autor: Marco Lanza
num = int(input("Ingrese un numero: "))
if(num > 1):
    for i in range(2,num):
        if(num % i == 0):
            print("El numero no es primo")
            break
    else:
        print("El numero es primo")
else:
    print("El numero no es primo")
