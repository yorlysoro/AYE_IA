from collections import deque

cola = deque()

cola.append(5)
cola.append(6)
cola.appendleft(1)

print(cola)

class Nodo():

    def __init__(self, elemento=None, siguiente=None, anterior=None):
        self.elemento = elemento
        self.siguiente = siguiente
        self.anterior = anterior

class Cola():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def encolar(self, elemento):
        if self.vacia():
            self.primero = Nodo(elemento)
            self.ultimo = self.primero
        else:
            self.ultimo.siguiente = Nodo(elemento)
            aux = self.ultimo
            self.ultimo = self.ultimo.siguiente
            self.ultimo.anterior = aux
        self.tamano += 1

    def desencolar(self):
        if self.primero == None:
            return None
        else:
            elmento = self.primero.elemento
            self.primero = self.primero.siguiente
            self.tamano -= 1
            return elmento
    def vacia(self):
        return self.tamano == 0

    def primero(self):
        if self.primero == None:
            return None
        else:
            return self.primero.elemento

    def __str__(self):
        cola = []
        siguiente = self.primero
        for i in range(self.tamano):
            if i == 0:
                cola.append(siguiente.elemento)
            else:
                siguiente = siguiente.siguiente
                cola.append(siguiente.elemento)
        return str(cola)
    def reverse(self):
        cola = []
        anterior = self.ultimo
        for i in range(self.tamano):
            if i == 0:
                cola.append(anterior.elemento)
            else:
                anterior = anterior.anterior
                cola.append(anterior.elemento)
        return cola

    def insertarPrincipio(self, elemento):
        if self.vacia():
            self.encolar(elemento)
        else:
            aux_primero = self.primero
            self.primero = Nodo(elemento)
            aux_primero.anterior = self.primero
            self.primero.siguiente = aux_primero
            self.tamano += 1
            del aux_primero

    def insertarFinal(self, elemento):
        if self.vacia():
            self.encolar(elemento)
        else:
            aux_ultimo = self.ultimo
            self.ultimo = Nodo(elemento)
            self.ultimo.anterior = aux_ultimo
            aux_ultimo.siguiente = self.ultimo
            self.tamano += 1
            del aux_ultimo

    def eliminarPrincipio(self):
        if self.tamano == 1:
            return self.desencolar()
        else:
            aux_primero = self.primero
            self.primero = aux_primero.siguiente
            self.primero.anterior = None
            del aux_primero
            self.tamano -= 1
    def eliminarFinal(self):
        if self.tamano == 1:
            return self.desencolar()
        else:
            aux_ultimo = self.ultimo
            self.ultimo = aux_ultimo.anterior
            self.ultimo.siguiente = None
            del aux_ultimo
            self.tamano -= 1

cola = Cola()

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

cola.insertarPrincipio(4)
cola.insertarFinal(5)

print(cola)
print(cola.reverse())
cola.eliminarPrincipio()
print(cola)
print(cola.reverse())
cola.eliminarFinal()
print(cola)
print(cola.reverse())

