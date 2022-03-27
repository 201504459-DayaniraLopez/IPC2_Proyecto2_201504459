
class NodoCelda:
    def __init__(self,tipocelda,posx,posy, color, valorR):
        self.TipoCelda = tipocelda
        self.PosX = posx
        self.PosY = posy
        self.Color = color
        self.ValorR = valorR
    
class NodoCiudad:
    def __init__(self,nombre,fila, columna, pentrada,precursos,pcivil,pmilitar):
        self.Nombre = nombre
        self.Fila = fila
        self.Columna = columna
        self.Entradas = pentrada
        self.Recursos = precursos
        self.Civil = pcivil
        self.Militar = pmilitar    
        self.Siguiente = None
        
class NodoRobot:
    def __init__(self,tiporobot,valorCombate,mision):
        self.Tipo = tiporobot
        self.ValorC=valorCombate
        self.Mision = mision
        self.Siguiente = None
