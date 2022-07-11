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
    
    def zero(self, actual) -> int:
        """Función que busca recursivamente el numeral de Church

        Args:
            actual (Church): Es el numeral de Church anterior

        Returns:
            int: Es el numeral de church buscado
        """
        if actual.Suc != None:
            return self.zero(actual.Suc) + 1
        return actual.Zero + 1

    def __add__(self, other) -> Church:
        """Suma de numerales de Church

        Args:
            other (Church): Otro numeral de Church a sumar

        Returns:
            Church: Es el numeral de church resultante
        """
        return Church(suc=self.zero(self)+self.zero(other)-1)

    def __mul__(self, other) -> Church:
        """multiplicación de numerales de Church

        Args:
            other (Church): Otro numeral de Church a multiplicar

        Returns:
            Church: Es el numeral de church resultante
        """
        return Church(suc=self.zero(self)*self.zero(other)-1)