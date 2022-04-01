
class ListasCelda:
    def __init__(self):
        self.Inicio=None
        self.Final = None
    
    def Insertar(self,Celda):
        if self.Inicio is None:
            self.Inicio=self.Final= Celda
            return
        Temp = self.Inicio
        while Temp.Siguiente is not None:
            Temp = Temp.Siguiente
        Temp.Siguiente = Celda
        self.Final = Celda

class ListaRobot:
    def __init__(self):
        self.Inicio=None
        self.Final = None
    
    def Insertar(self,Robot):
        if self.Inicio is None:
            self.Inicio=self.Final= Robot
            return
        Temp = self.Inicio
        while Temp.Siguiente is not None:
            Temp = Temp.Siguiente
        Temp.Siguiente = Robot
        self.Final = Robot

class ListaCiudad:
    def __init__(self):
        self.Inicio=None
        self.Final = None
    
    def Insertar(self,Ciudad):
        if self.Inicio is None:
            self.Inicio=self.Final= Ciudad
            return
        Temp = self.Inicio
        while Temp.Siguiente is not None:
            Temp = Temp.Siguiente
        Temp.Siguiente = Ciudad
        self.Final = Ciudad

    def imprimir(self):
        temp = self.Inicio
        ciudades = []
        while temp is not None:
            ciudades.append(temp.Nombre)
            temp = temp.Siguiente
        return ciudades