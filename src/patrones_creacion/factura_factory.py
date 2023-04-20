from __future__ import annotations
from abc import ABC, abstractmethod

#*--------------------------------------------------
#* La clase Creador es una superclase creadora de 
#* objetos donde las clases no están especificadas
#*--------------------------------------------------
class Creator(ABC):
    """
    La clase Creator declara la "factory" que retorna un puntero a un objeto
    pero que no tiene implementaciones concretas de sus métodos, es como 
    una plantilla de creación futura
    """

    @abstractmethod

    def factory_method(self):
        pass

#*----------------------------------------------------------------
#* Podría no crearlo pero también es posible implementar alguna
#* operación que sea común a todas las posibles implementaciones
#* esta lógica puede ser luego revertida al crear los objetos
#* operativos propiamente dichos
#*----------------------------------------------------------------
    def some_operation(self, importe) -> str:
        # Primero se llama al método factory para crear un nuevo objeto Factura.
        factura = self.factory_method()

        # A continuación uso el objeto creado invocando la operación específica para el mismo (que no figura definida en la clase que estoy usando).
        return factura.operation(importe)


#*-----------------------------------------------------------------------
#* Es necesario hacer implementaciones concretas que reciban el objeto
#* plantilla y le agreguen los métodos y atributos que le sean propios
#*-----------------------------------------------------------------------

class CreatorIVAResponsable(Creator):
    def factory_method(self) -> Factura:
        return IVAResponsable()


class CreatorIVANoInscripto(Creator):
    def factory_method(self) -> Factura:
        return IVANoInscripto()

class CreatorIVAExcento(Creator):
    def factory_method(self) -> Factura:
        return IVAExcento()

#*------------------------------------------------------------------------------
#* Defino al objeto Factura
#*-----------------------------------------------------------------------------
class Factura(ABC):

    #*-------------------------------------------------------------------------
    #* Esta es una interfaz que define todos los métodos que son comunes a 
    #* las facturas independientemente de la condicion impositiva
    #*-------------------------------------------------------------------------

    @abstractmethod
    def operation(self, importe) -> str:
        pass


#*-------------------------------------------------------------------------------
#* Ahora defino facturas concretas con su respectiva definición de condicion impositiva
#*-------------------------------------------------------------------------------

class IVAResponsable(Factura):
    def operation(self, importe) -> str:
        return f"Factura con importe {importe} generada con condicion IVA Responsable"


class IVANoInscripto(Factura):
    def operation(self, importe) -> str:
        return f"Factura con importe {importe} generada con condicion IVA No inscripto"


class IVAExcento(Factura):
    def operation(self, importe) -> str:
        return f"Factura con importe {importe} generada con condicion IVA excento"



#*-------------------------------------------------------------------------------
#* El código que orquesta empieza con una instancia del Creator (factory) sin
#* definiciones concretas y procede a crearle las subclases de implementación
#* que sean necesarias.
#*-------------------------------------------------------------------------------
def client_code(creator: Creator, importe) -> None:

    print(f"Soy un código que no sé lo que está creando pero invoca a los metodos para hacerlo basado en el creador provisto.\n"
	  f"{creator.some_operation(importe)}",end="")

#*-------------------------------------------------------------------------------
#* Este es el punto de entrada de ejecución (explicito)
#*-------------------------------------------------------------------------------
if __name__ == "__main__":

    print("Crea primero una Factura como responsable inscripto")
    client_code(CreatorIVAResponsable(), 2000)
    print("\n")

    print("Crea una segunda factura, vuelve a invocar client_code con el creator especifico de Iva No inscripto")
    client_code(CreatorIVANoInscripto(), 473)
    print("\n")

    print("Crea una tercera factura, invoca ahora client_code pero con el creator especifico de Iva excento")
    client_code(CreatorIVAExcento(), 1230)
