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
            jsonfile = sys.argv[1]
            jsonkey = "token1"
            if len(sys.argv) == 3:
                jsonkey = sys.argv[2]
            with open(jsonfile, 'r') as (myfile): #Abre el archivo y lo lee
                data = myfile.read()
            obj = json.loads(data)
            print(str(obj[jsonkey]))#Muestra la clave

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
