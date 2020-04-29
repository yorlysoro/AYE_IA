class Arbol(object):
	def __init__(self):
		self.der = None
		self.izq = None
		self.dato = None

raiz = Arbol()
raiz.dato = 'Raiz'
raiz.izq = Arbol()
raiz.izq.dato = 'Izquierda'
raiz.der = Arbol()
raiz.der.dato = 'Derecha'
print(raiz.izq.dato)
