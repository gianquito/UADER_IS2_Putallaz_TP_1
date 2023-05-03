#*--- Abstracción de implementación
class TrenLaminador1:
	def produceLamina(self, espesor, ancho):
		print(f"Tren laminador 1 producirá lámina de 5 metros de largo, {espesor}'' de espesor y {ancho} metros de ancho")

#*--- Abstracción de implementación
class TrenLaminador2:
	def produceLamina(self, espesor, ancho):
		print(f"Tren laminador 2 producirá lámina de 10 metros de largo, {espesor}'' de espesor y {ancho} metros de ancho")



#*---Clase Lamina con sus propiedades pero con método de fabricación flexible
 
class Lamina:
	def __init__(self, espesor, ancho, trenLaminador):
		self._espesor = espesor
		self._ancho = ancho

		self._trenLaminador = trenLaminador

#*---- cuando se invoca la producción invoca al objeto cuyo puntero se almacenó al crear

	def produce(self):
		self._trenLaminador.produceLamina(self._espesor, self._ancho)

	def setTrenLaminador(self, trenLaminador):
		self._trenLaminador = trenLaminador


#*-----------------------------------------------------------
#* main
#*-----------------------------------------------------------

#*--- implementa una primera lamina y le asigna TrenLaminador1()
lamina1 = Lamina(0.5, 1.5, TrenLaminador1())
lamina1.produce()

#*--- implementa una segunda lamina y le asigna TrenLaminador2()
lamina2 = Lamina(1, 4, TrenLaminador2())
lamina2.produce()

print("\n Cambia método de producción en run-time TrenLaminador2->TrenLaminador1\n")
lamina2.setTrenLaminador(TrenLaminador1())
lamina2.produce()