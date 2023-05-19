

import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string


	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:
    
	def __init__(self):
		self.objs = []

	def save(self, writer):
		obj = writer.save()
		self.objs.insert(0, obj)
		if len(self.objs) > 4:
			self.objs.pop()

	def undo(self, writer, i):
		writer.undo(self.objs[i])


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	writer.write("Tercer write\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	writer.write("Cuarto write\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	writer.write("Quinto write\n")
	print(writer.content + "\n\n")

	est = int(input("Ingrese el estado que quiere recuperar (0..3) "))
	caretaker.undo(writer, est)
	print(f"Luego de undo: {writer.content}")
