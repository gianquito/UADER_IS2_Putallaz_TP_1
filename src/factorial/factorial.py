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

#Controla que se pase un numero como argumento, sino lo solicita
num = 0
if len(sys.argv) < 2:
   print("Debe informar un número!")
   num = int(input('Ingrese un número '))
else:   
    num=int(sys.argv[1])
print("Factorial ",num,"! es ", factorial(num)) 