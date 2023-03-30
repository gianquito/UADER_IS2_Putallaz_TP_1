class Factorial:
    def __init__(self, min=1, max=60):
        self.__min = min
        self.__max = max

    def run(self):
        for i in range(self.__min, self.__max + 1):
            print("Factorial ",i,"! es ", self.calc_factorial(i))

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
    
    def getMin(self):
        return self.__min
    
    def getMax(self):
        return self.__max
    
    def setMin(self, min):
        self.__min = min
    
    def setMax(self, max):
        self.__max = max

fact = Factorial(min=50)
fact.run()