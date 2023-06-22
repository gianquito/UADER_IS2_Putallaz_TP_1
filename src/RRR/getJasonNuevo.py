# -*- coding: utf-8 -*-
"""
Extractor de token para acceso API servicios Banco (version 1.0)
"""
#Copyright IS2 © 2022,2023 todos los derechos reservados
import json
import sys
class Singleton():
    """Clase Singleton."""
    def __init__(self):
        pass
    __instancia=None

    @classmethod
    def crear_instancia(cls):
        """Crea la instancia de la clase si no existe."""
        if not cls.__instancia:
            cls.__instancia=Singleton()
        return cls.__instancia

    def compute(self):
        """Muestra la clave asociada al token"""
        if sys.argv[1] == "-h": #Muestra ayuda
            print("El programa getJason debe ser invocado mediante: {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json"+
                    "\nPara obtener ayuda: {path ejecutable}/getJason.pyc -h")
        else:
            cuenta1_handler = CuentaHandler("token1", 1000)
            cuenta2_handler = CuentaHandler("token2", 2000)
            cuenta1_handler.nextHandler = cuenta2_handler
            cuenta2_handler.nextHandler = None

            collection = Collection()
            collection.add_item(PedidoPago(1, 500))
            collection.add_item(PedidoPago(2, 500))
            collection.add_item(PedidoPago(3, 500))
            collection.add_item(PedidoPago(4, 500))
            collection.add_item(PedidoPago(5, 500))
            collection.add_item(PedidoPago(6, 500))
            collection.add_item(PedidoPago(7, 500))
            collection.add_item(PedidoPago(8, 500))
            collection.add_item(PedidoPago(9, 500))


            jsonfile = sys.argv[1]
            with open(jsonfile, 'r') as (myfile): #Abre el archivo y lo lee
                data = myfile.read()
            obj = json.loads(data)

            for pedido in collection:
                token_name = cuenta1_handler.handle(pedido)
                if token_name is not None:
                    print("Se realizo el pedido de pago numero "+ str(pedido.num) +" con la clave "+ str(obj[token_name]) +" y el monto "+ str(pedido.monto))
                else:
                    print("No se encontro una cuenta con saldo suficiente")
                    break

class AbstractPrograma:
    """Branching by abstraction class"""
    def __init__(self, sin):
        self.sin = sin
    def compute(self):
        """Revisa si el modo debug está activado y usa el metodo correspondiente"""
        if __debug__ is True:
            self.sin.compute()
        else:
            compute_viejo()

def compute_viejo():
    """Metodo viejo para mostrar la clave asociada al token"""
    if sys.argv[1] == "-h":
        print("El programa getJason debe ser invocado mediante: {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json"+
                "\nPara obtener ayuda: {path ejecutable}/getJason.pyc -h")
    else:
        jsonfile = sys.argv[1]
        jsonkey = "token1"
        if len(sys.argv) == 3:
            jsonkey = sys.argv[2]
        with open(jsonfile, 'r') as (myfile):
            data = myfile.read()
        obj = json.loads(data)
        print(str(obj[jsonkey]))


class PedidoPago:
    def __init__(self, num, monto):
        self.num = num
        self.monto = monto

class Handler(object):
    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        if self.nextHandler == None:
           print("La lista de cuentas se ha terminado, no se puede resolver el pago")
           return None
        return self.nextHandler.handle(request)

class CuentaHandler(Handler):
    def __init__(self, token, monto_disp):
        self.token = token
        self.monto_disp = monto_disp
    def handle(self, pedido):
        if self.monto_disp >= pedido.monto:
            self.monto_disp -= pedido.monto
            return self.token
        else:
            return super(CuentaHandler, self).handle(pedido)

class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            result = self._collection[self._index]
            self._index += 1
            return result
        except IndexError:
            raise StopIteration

class Collection:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return Iterator(self._items)

    def add_item(self, item):
        self._items.append(item)

branching = AbstractPrograma(Singleton().crear_instancia())

try:
    branching.compute()
except IndexError:
    print("Argumentos invalidos")
except IOError:
    print("No se encontro el archivo especificado")
except KeyError:
    print("No se encontro el token especificado")
except:
    print("Ocurrio un error al ejecutar el programa")
