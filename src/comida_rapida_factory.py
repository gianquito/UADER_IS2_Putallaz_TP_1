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
    def some_operation(self) -> str:
        # Primero se llama al método factory para crear un nuevo objeto Factura.
        envio = self.factory_method()

        # A continuación uso el objeto creado invocando la operación específica para el mismo (que no figura definida en la clase que estoy usando).
        return envio.operation()


#*-----------------------------------------------------------------------
#* Es necesario hacer implementaciones concretas que reciban el objeto
#* plantilla y le agreguen los métodos y atributos que le sean propios
#*-----------------------------------------------------------------------

class CreatorEntregaMostrador(Creator):
    def factory_method(self) -> Hamburguesa:
        return EntregaMostrador()


class CreatorRetiraCliente(Creator):
    def factory_method(self) -> Hamburguesa:
        return RetiraCliente()

class CreatorEnvioDelivery(Creator):
    def factory_method(self) -> Hamburguesa:
        return EnvioDelivery()

#*------------------------------------------------------------------------------
#* Defino al objeto Hamburguesa
#*-----------------------------------------------------------------------------
class Hamburguesa(ABC):

    #*-------------------------------------------------------------------------
    #* Esta es una interfaz que define todos los métodos que son comunes a 
    #* las facturas independientemente de la condicion impositiva
    #*-------------------------------------------------------------------------

    @abstractmethod
    def operation(self) -> str:
        pass


#*-------------------------------------------------------------------------------
#* Ahora defino facturas concretas con su respectiva definición de condicion impositiva
#*-------------------------------------------------------------------------------

class EntregaMostrador(Hamburguesa):
    def operation(self) -> str:
        return "Se entregará por mostrador"


class RetiraCliente(Hamburguesa):
    def operation(self) -> str:
        return "Lo retirará el cliente"


class EnvioDelivery(Hamburguesa):
    def operation(self) -> str:
        return "Se realiza envio por delivery"



#*-------------------------------------------------------------------------------
#* El código que orquesta empieza con una instancia del Creator (factory) sin
#* definiciones concretas y procede a crearle las subclases de implementación
#* que sean necesarias.
#*-------------------------------------------------------------------------------
def client_code(creator: Creator) -> None:

    print(f"Soy un código que no sé lo que está creando pero invoca a los metodos para hacerlo basado en el creador provisto.\n"
	  f"{creator.some_operation()}",end="")

#*-------------------------------------------------------------------------------
#* Este es el punto de entrada de ejecución (explicito)
#*-------------------------------------------------------------------------------
if __name__ == "__main__":

    print("Crea primero una Hamburguesa con entrega en mostrador")
    client_code(CreatorEntregaMostrador())
    print("\n")

    print("Crea una segunda hamburguesa, que retira el cliente")
    client_code(CreatorRetiraCliente())
    print("\n")

    print("Crea una tercera hamburguesa, que tendrá un envío por delivery")
    client_code(CreatorEnvioDelivery())
