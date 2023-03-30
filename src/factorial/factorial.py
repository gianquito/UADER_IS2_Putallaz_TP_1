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
min = 0
max = 0
if len(sys.argv) < 2:
   print("Debe informar un número!")
   num = (input('Ingrese un rango (ej: 4-8) ')).split('-')
else:   
    num= sys.argv[1].split('-')
min = int(num[0])
max = int(num[1])
for i in range(min,max + 1):
    print("Factorial ",i,"! es ", factorial(i)) 