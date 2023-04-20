import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getAvion(self):
      avion = Avion()
      
      # Primero el chasis
      body = self.__builder.getBody()
      avion.setBody(body)
      
      # Luego las 2 turbinas
      turbina = self.__builder.getTurbina()
      avion.attachTurbina(turbina)
      avion.attachTurbina(turbina)
      
      # Luego las 2 alas
      ala = self.__builder.getAla()
      avion.attachAla(ala)
      avion.attachAla(ala)

      #Y por ultimo el tren de aterrizaje
      trenAterrizaje = self.__builder.getTrenAterrizaje()
      avion.setTrenAterrizaje(trenAterrizaje)

      # Retorna el vehiculo completo
      return avion

#*----------------------------------------------------------------
#* Esta es la definición de un objeto Avion inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Avion:
   def __init__(self):
      self.__turbina = list()
      self.__ala = list()
      self.__trenAterr = None
      self.__body = None

   def setBody(self, body):
      self.__body = body

   def attachAla(self, ala):
      self.__ala.append(ala)

   def attachTurbina(self, turbina):
      self.__turbina.append(turbina)

   def setTrenAterrizaje(self, ta):
      self.__trenAterr = ta

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("turbinas: %d" % (self.__turbina[0].horsepower))
      print ("alas: %d\'" % (self.__ala[0].size))
      print ("tren de aterrizaje: %s" % (self.__trenAterr.pesoMaximo))

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
      def getAla(self): pass
      def getTurbina(self): pass
      def getTrenAterrizaje(self): pass
      def getBody(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Boeing747
#* Establece instancias para tomar alas, turbinas, chasis y tren de aterrizaje
#* estableciendo las partes específicas que (en un 747) 
#* deben tener esas partes
#*-------------------------------------------------------
class Boeing747Builder(Builder):
   
   def getAla(self):
      ala = Ala()
      ala.size = 120
      return ala
   
   def getTurbina(self):
      turbina = Turbina()
      turbina.horsepower = 820
      return turbina
   
   def getTrenAterrizaje(self):
      ta = TrenAterrizaje()
      ta.pesoMaximo = 4000
      return ta
   
   def getBody(self):
      body = Body()
      body.shape = "747"
      return body

#*----------------------------------------------------------------
#* Define partes genéricas para un avion (sin inicializar)
#*----------------------------------------------------------------
class Ala:
   size = None

class Turbina:
   horsepower = None

class TrenAterrizaje:
   pesoMaximo = None

class Body:
   shape = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   avionBuilder = Boeing747Builder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Boeing 747
#*----------------------------------------------------------------   
   director.setBuilder(avionBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un 747 según
#* la hoja de ruta
#*----------------------------------------------------------------
   b747 = director.getAvion()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   b747.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un vehículo\n")

   main()
