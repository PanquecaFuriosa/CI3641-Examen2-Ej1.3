import math

class Arbol:
    """Clase que implementa un arbol binario
    """
    #Campos
    arbolPre = []
    arbolPost = []
    esMaxHeap = True

    def __init__(self, valor, a = None, b = None):
        """Inicialización del árbol

        Args:
            valor (any): Valor de la hoja o la rama
            a (Arbol, optional): Hijo izquierdo del arbol. Por defecto None.
            b (Arbol, optional): Hijo derecho del arbol. Por defecto None.
        """
        self.valor = valor
        self.hojaI = a
        self.hojaD = b
    
    def preorder(self, actual, max):
        """Recorre el arbol en preorder, también verifica que es un max heap

        Args:
            actual (Arbol): Arbol actual a ser recorrido.
            max (int): Es el valor del árbol padre.
        """
        if (actual != None):
            if (max < actual.valor):
                self.esMaxHeap = False
            max = actual.valor
            self.arbolPre.append(actual.valor)
            self.preorder(self.hojaI, max)
            self.preorder(self.hojaD, max)
    
    def postorder(self, actual):
        """Recorre el arbol en postorder, también verifica que es un max heap

        Args:
            actual (Arbol): Arbol actual a ser recorrido.
            max (int): Es el valor del árbol padre.
        """
        if (actual != None):
            if (max < actual.valor):
                self.esMaxHeap = False
            max = actual.valor
            self.postorder(self.hojaI, max)
            self.postorder(self.hojaD, max)
            self.arbolPost.append(actual.valor)
    
    def esMaxHeapSimetrico(self) -> bool: 
        """Función que determina si el árbol es un max heap simétrico o no.

        Returns:
            bool: True si es un max heap simétrico, false si no.
        """
        self.preorder(self, math.inf)
        self.postorder(self, math.inf)
        return (self.arbolPre == self.arbolPost and self.esMaxHeap)