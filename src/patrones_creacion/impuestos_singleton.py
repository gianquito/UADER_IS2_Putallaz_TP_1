# Elabore una clase para el cálculo del valor de impuestos a ser utilizado por
# todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado
# deberá recibir un valor de importe base imponible y deberá retornar la suma
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre
# esa base imponible.
class Calcular_Impuestos:
    __instancia=None
    def __init__(self):
        pass

    def calc_impuestos(self, base_imp):
        #Se suma 21% de IVA 5% de IIBB y 1.2 % de Contribuciones municipales (27.2% en total) a la base imponible
        return base_imp + (27.2/100*base_imp)

    @classmethod
    def crearInstancia(cls):
        if not cls.__instancia:
            cls.__instancia=Calcular_Impuestos()
        return cls.__instancia

imp = Calcular_Impuestos.crearInstancia()
imp1 = Calcular_Impuestos.crearInstancia()

print(imp.calc_impuestos(100))
print(imp1.calc_impuestos(100))