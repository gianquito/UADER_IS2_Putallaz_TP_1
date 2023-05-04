#*--- La clase que representa el numero
class Numero:

	def __init__(self, valor):
		self._valor = valor

	def render(self):
		return self._valor

#*--- Esta es la clase que suma 2
class SumaWrapper(Numero):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return self._wrapped.render() + 2

#*--- Esta es la clase que multiplica 2
class ProductoWrapper(Numero):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return self._wrapped.render() * 2

#*--- Esta es la clase que divide por 3
class DivisionWrapper(Numero):

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return self._wrapped.render() / 3

#*------------------------------------------------------------------------
#* main
#*------------------------------------------------------------------------
if __name__ == '__main__':

    numero = Numero(8)
    print(f"Número original: {numero.render()}")
    numero_operaciones = DivisionWrapper(ProductoWrapper(SumaWrapper(numero)))
    print(f"Número después de las operaciones: {numero_operaciones.render()}")
