#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

#funcion factorial, calcula el factorial del numero que se le pase
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

min = 1
max = 60
#Controla que se pase un numero como argumento, sino lo solicita
if len(sys.argv) < 2:
   print("Debe informar un número!")
   num = (input('Ingrese un rango (ej: 4-8) ')).split('-')
else:   
    num= sys.argv[1].split('-')


if num[0]: #si tiene rango inferior lo asigna como minimo
    min = int(num[0])
if num[1]: #si tiene rango superior lo asigna como maximo
    max = int(num[1])

#calcula el factorial de los numeros en el rango dado
for i in range(min,max + 1):
    print("Factorial ",i,"! es ", factorial(i)) 