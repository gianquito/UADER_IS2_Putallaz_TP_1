# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json, sys
try:
    if sys.argv[1] == "-h":
        print "El programa getJason debe ser invocado mediante: {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json \nPara obtener ayuda: {path ejecutable}/getJason.pyc -h"
    else:
        jsonfile = sys.argv[1]
        jsonkey = "token1"
        if len(sys.argv) == 3:
            jsonkey = sys.argv[2]
        with open(jsonfile, 'r') as (myfile):
            data = myfile.read()
        obj = json.loads(data)
        print str(obj[jsonkey])
except IndexError:
    print "Argumentos invalidos"
except IOError:
    print "No se encontro el archivo especificado"
except KeyError:
    print "No se encontro el token especificado"