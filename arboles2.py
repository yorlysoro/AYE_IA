class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo
    def tieneHijoDerecho(self):
        return self.hijoDerecho
    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self
    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self
    def esRaiz(self):
        return not self.padre
    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)
    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo
    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo
    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
        self.tamano = 0
    def longitud(self):
        return self.tamano
    def __len__(self):
        return self.tamano
    def __iter__(self):
        return self.raiz.__iter__()
    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamano = self.tamano + 1
    def _agregar(self,clave, valor, nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave,valor, nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor, padre=nodoActual)

        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor, nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)
    def __setitem__(self,c,v):
        self.agregar(c,v)
    def obtener(self,clave):
        if self.raiz:
            res = self._obtener(clave,self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None
    def _obtener(self,clave,nodoActual):
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave,nodoActual.hijoDerecho)
    def __getitem__(self,clave):
        return self.obtener(clave)
    def __contains__(self,clave):
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False

    def eliminar(self,clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave,self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano - 1
            else:
                raise KeyError('Error, la clave no esta en el arbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no esta en el arbol')

        if nodoActual.esHoja():
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos():
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil
        else:
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodo.Actual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho)
    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.pader = self.padre

    def __delitem__(self, clave):
        self.eliminar(clave)
    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                for elem in self.hijoIzquierdo:
                    yield elem
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem


miarbol = ArbolBinarioBusqueda()
miarbol[3] = "rojo"
miarbol[4] = "azul"
miarbol[6] = "amarillo"
miarbol[2] = "en"

print(len(miarbol))
print(miarbol[6])
print(miarbol[2])


