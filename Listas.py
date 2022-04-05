

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

    def UnidadesM(self,mapa):
        temp = self.Inicio
        celda=[]
        while temp is not None:
            if temp.TipoCelda == "Militar" and temp.Mapa == mapa:
                posx= temp.PosX
                posy= temp.PosY
                Valor = temp.ValorR
                celda.append([posx,posy,Valor])
                temp = temp.Siguiente
            elif temp.TipoCelda != "Militar" or  temp.Mapa != mapa:
                temp = temp.Siguiente

        return celda

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

    def imprimir(self):
        temp = self.Inicio
        Robots = []
        while temp is not None:
            Robots.append(temp.Nombre)
            temp = temp.Siguiente
        return Robots
    def buscar(self, nombre):
        temp = self.Inicio
        while temp is not None:
            if nombre == temp.Nombre:
                tipo = temp.Tipo
                combate = temp.ValorC
                return tipo,combate
                break
            temp = temp.Siguiente
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


    def Buscar(self, Mapa):
        temp = self.Inicio
        while temp is not None:
            if Mapa == temp.Nombre:
                nombre = temp.Nombre
                Lpatron = temp.Patron
                FilaM = temp.Fila
                ColumnaM=temp.Columna
                return FilaM,ColumnaM, Lpatron , nombre
                break
            temp = temp.Siguiente

    def imprimir(self):
        temp = self.Inicio
        ciudades = []
        while temp is not None:
            ciudades.append(temp.Nombre)
            temp = temp.Siguiente
        return ciudades