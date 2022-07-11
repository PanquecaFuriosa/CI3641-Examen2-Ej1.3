from __future__ import annotations

class Church:
    """ Clase que implementa los numerales de Church
    """

    def __init__(self, suc = None, cero = None):
        """Inicialización del Church

        Args:
            suc (int, optional): Es el cero de Church. Defaults toPor defecto None.
            cero (Church, optional): Es un númmeral de Church anterior. Por defecto None.
        """
        self.Suc = suc
        self.Zero = cero
    
    def sucesor(self, actual) -> Church:
        """Función que busca recursivamente el numeral de Church

        Args:
            actual (Church): Es el numeral de Church anterior

        Returns:
            Church: Church del Curch actual
        """
        return Church(suc=actual)

    def __add__(self, other) -> Church:
        """Suma de numerales de Church

        Args:
            other (Church): Otro numeral de Church a sumar

        Returns:
            Church: Es el numeral de church resultante
        """
        if self.Suc == None:
            return other
        if other.Suc == None:
            return self
        return Church(suc=self.Suc.__add__(other))

    def __mul__(self, other) -> Church:
        """multiplicación de numerales de Church

        Args:
            other (Church): Otro numeral de Church a multiplicar

        Returns:
            Church: Es el numeral de church resultante
        """
        if self.Suc == None or other.Suc == None:
            return Church(cero=self.Zero)
        return (self.__mul__(other.Suc)).__add__(self)