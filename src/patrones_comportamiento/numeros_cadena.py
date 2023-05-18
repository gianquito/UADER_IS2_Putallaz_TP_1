import sys
#*--------------------------------------------------------------------
#* Implementación de chain of responsibility gestiona numeros
#*--------------------------------------------------------------------
class Handler(object):

    def __init__(self):
        self.nextHandler = None

    def handle(self, number):
        if self.nextHandler == None:
           print(f"El numero {number} no fue consumido \n")
           return
        self.nextHandler.handle(number)

#*-------------------------------- Numeros Primos Handler

class PrimosHandler(Handler):

    def handle(self, number):
        
        if(self.es_primo(number)):
            print(f"El numero {number} es primo, lo consume PrimosHandler \n")
        else:
            print("Handler primo: pasa al siguiente actuador")
            super(PrimosHandler, self).handle(number)

    def es_primo(self, number):
        if number <= 1:
            return False
        elif number == 2:
            return True
        elif number % 2 == 0:
            return False

        i = 3
        while i * i <= number:
            if number % i == 0:
                return False
            i += 2

        return True

#*-------------------------------- Numeros pares Handler

class ParesHandler(Handler):
    def handle(self, number):
        if(number % 2 == 0):
            print(f"El numero {number} es par, lo consume ParesHandler \n")
        else:
            print("Handler par: pasa al siguiente actuador")
            super(ParesHandler, self).handle(number)

class ErrorHandler(Handler):

    def handle(self, request):
        print ("Invalid request")



if __name__ == '__main__':

#*---------------------------------------------------------------
#* Inicializa los actuadores de numeros
#*---------------------------------------------------------------
    primos_handler = PrimosHandler()
    pares_handler = ParesHandler()

#*---- Establece ahora la cadena de llamada

    primos_handler.nextHandler = pares_handler


#*---- Envia los numeros del 1 al 100 a la cadena para que se procesen

    for i in range(1,101):
        primos_handler.handle(i)
