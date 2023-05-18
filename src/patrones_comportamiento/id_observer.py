import os

class Subject:

#*------- Representa lo que se está observando

	def __init__(self):

		self._observers = []

	def notify(self, modifier = None):


		for observer in self._observers:
			if modifier != observer:
				observer.update(self)

	def attach(self, observer):

#*------- Agregar observador si ya no está en la lista

		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):

#*------- Remover observador si está en la lista


		try:
			self._observers.remove(observer)
		except ValueError:
			pass


#*----------- Define a los observadores

class Data(Subject):

	def __init__(self):
		Subject.__init__(self)
		self._data = ""

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value
		print(f"El dato bajo observación ha sido actualizado al valor {value}")
		self.notify()


class Clase1Viewer:
	def __init__(self):
		self._id = "xGh6"

	def update(self, subject):
		if(self._id == subject.data):
			print(f"El ID emitido ({subject.data}) coincide con la id de la Clase 1")

class Clase2Viewer:
	def __init__(self):
		self._id = "l@U5"

	def update(self, subject):
		if(self._id == subject.data):
			print(f"El ID emitido ({subject.data}) coincide con la id de la Clase 2")

class Clase3Viewer:
	def __init__(self):
		self._id = "0jc4"

	def update(self, subject):
		if(self._id == subject.data):
			print(f"El ID emitido ({subject.data}) coincide con la id de la Clase 3")

class Clase4Viewer:
	def __init__(self):
		self._id = "p.1f"

	def update(self, subject):
		if(self._id == subject.data):
			print(f"El ID emitido ({subject.data}) coincide con la id de la Clase 4")

"""main function"""

if __name__ == "__main__":


	os.system("clear")

	print("Crea los observadores de las 4 clases\n")
	view1 = Clase1Viewer()
	view2 = Clase2Viewer()
	view3 = Clase3Viewer()
	view4 = Clase4Viewer()


	print("\nCrea un objeto de datos, subscribe a las clases observadoras\n")
	obj1 = Data()
	obj1.attach(view1)
	obj1.attach(view2)
	obj1.attach(view3)
	obj1.attach(view4)

	idList = ["iuj4", "0jc4", "g_3Q", "96l+","xGh6", "l@U5", "o0ty", "p.1f"]
	for id in idList:
		print("\n")
		print(f"Modifica el dato a la id {id}")
		obj1.data = id

