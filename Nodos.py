
class NodoCelda:
    def __init__(self,mapa,tipocelda,posx,posy, color, valorR):
        self.Mapa = mapa
        self.TipoCelda = tipocelda
        self.PosX = posx
        self.PosY = posy
        self.Color = color
        self.ValorR = valorR
        self.Siguiente = None
    
class NodoCiudad:
    def __init__(self,nombre,fila, columna, patron):
        self.Nombre = nombre
        self.Fila = fila
        self.Columna = columna
        self.Patron = patron
        self.Siguiente = None
        
class NodoRobot:
    def __init__(self,tiporobot,nombre,valorCombate,mision):
        self.Tipo = tiporobot
        self.ValorC=valorCombate
        self.Mision = mision
        self.Nombre = nombre
        self.Siguiente = None
