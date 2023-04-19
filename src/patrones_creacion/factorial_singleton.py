class Factorial:
    __instancia=None
    def __init__(self):
        pass

    def run(self, num):
        return self.calc_factorial(num)

    def calc_factorial(self, num):
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

    @classmethod
    def crearInstancia(cls):
        if not cls.__instancia:
            cls.__instancia=Factorial()
        return cls.__instancia

fact1 = Factorial.crearInstancia()
fact2 = Factorial.crearInstancia()

num = 4
print('El factorial de', num, 'es:', fact1.run(num))
print('El factorial de', num, 'es:', fact2.run(num))
print(id(fact1) == id(fact2))
