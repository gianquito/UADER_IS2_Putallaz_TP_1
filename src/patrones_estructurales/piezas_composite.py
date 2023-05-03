import sys

#*------------- Define una clase para los nodos terminales (leaf)
class LeafElement:
	def __init__(self, *args):

#*--- indenta las posiciones a medida que se agregan
		self.position = args[0]

#*--- lista elementos

	def showDetails(self):

		'''Prints the position of the child element.'''
		print("\t", end ="")
		print(self.position)

#*---- Elemento compuesto, representa objetos en cualquier nivel de la jerarquia excepto el último

class CompositeElement:

	def __init__(self, *args):

		self.position = args[0]
		self.children = []

#*----- Crea jerarquia

	def add(self, child):

		self.children.append(child)

#*---- Remueve jerarquia

	def remove(self, child):

		self.children.remove(child)

#*---- muestra detalles (itera a los niveles inferiores)


	def showDetails(self):

		print(self.position)
		for child in self.children:
			print("\t", end ="")
			child.showDetails()


"""main method"""

if __name__ == "__main__":


#*------ Crea el top level de la jerarquia (el producto principal)

	mainProduct = CompositeElement("Producto Principal")

#*----- Crea el primer subconjunto

	subset1 = CompositeElement("Subconjunto de piezas 1")

	subset1Item1 = LeafElement("Pieza 1")
	subset1Item2 = LeafElement("Pieza 2")
	subset1Item3 = LeafElement("Pieza 3")
	subset1Item4 = LeafElement("Pieza 4")


	subset1.add(subset1Item1)
	subset1.add(subset1Item2)
	subset1.add(subset1Item3)
	subset1.add(subset1Item4)


#*----- Crea el segundo subconjunto

	subset2 = CompositeElement("Subconjunto de piezas 2")

	subset2Item1 = LeafElement("Pieza 1")
	subset2Item2 = LeafElement("Pieza 2")
	subset2Item3 = LeafElement("Pieza 3")
	subset2Item4 = LeafElement("Pieza 4")


	subset2.add(subset2Item1)
	subset2.add(subset2Item2)
	subset2.add(subset2Item3)
	subset2.add(subset2Item4)
	
#*----- Crea el tercer subconjunto

	subset3 = CompositeElement("Subconjunto de piezas 3")

	subset3Item1 = LeafElement("Pieza 1")
	subset3Item2 = LeafElement("Pieza 2")
	subset3Item3 = LeafElement("Pieza 3")
	subset3Item4 = LeafElement("Pieza 4")
	
	subset3.add(subset3Item1)
	subset3.add(subset3Item2)
	subset3.add(subset3Item3)
	subset3.add(subset3Item4)

#*----- Crea el cuarto subconjunto

	subset4 = CompositeElement("Subconjunto de piezas 4")

	subset4Item1 = LeafElement("Pieza 1")
	subset4Item2 = LeafElement("Pieza 2")
	subset4Item3 = LeafElement("Pieza 3")
	subset4Item4 = LeafElement("Pieza 4")
	
	subset4.add(subset4Item1)
	subset4.add(subset4Item2)
	subset4.add(subset4Item3)
	subset4.add(subset4Item4)

#*---- Agrega ahora las 3 jerarquias y una cuarta opcional al nivel raiz

	mainProduct.add(subset1)
	mainProduct.add(subset2)
	mainProduct.add(subset3)
	if(len(sys.argv) == 2 and sys.argv[1] == '--opcional'):
		mainProduct.add(subset4)
	
#*---- Muestra el resultado
	mainProduct.showDetails()