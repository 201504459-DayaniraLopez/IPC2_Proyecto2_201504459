
import xml.etree.ElementTree as ET
from tkinter import filedialog
import Nodos
import Listas
import re

LCiudad = Listas.ListaCiudad()
LCelda= Listas.ListasCelda()
LRobot = Listas.ListaRobot()
mapa=[]
class Archivo():
    def __init__(self):
        ruta = filedialog.askopenfilename(initialdir="/", title="Selecione Archivo",filetypes=(("xml files", "*.xml"), ("todos los archivos", "*.*")))
        archivo_xml = ET.parse(ruta)
        raiz = archivo_xml.getroot()
        x=y=0
        j=n=0
        #iniciar Recorrido
        for padre in raiz:
            if padre.tag =="listaCiudades":
                for hijo in padre:
                    while j <= len(hijo) - 1:
                        if hijo[j].tag == "nombre":
                             filas = hijo[j].get('filas')
                             columnas = hijo[j].get('columnas')
                             nombre= hijo[j].text
                        elif hijo[j].tag == "fila":
                                        patron= hijo[j].text.replace('"',"")
                                        mapa.append(patron)
                                        for celda in patron:
                                            if celda == " ":
                                                tipoc = "Camino"
                                                PosxC = int(x)
                                                PosyC = int(y)
                                                colorC = "#FFFFF"

                                            elif celda == "C":
                                                tipoc="Civil"
                                                PosxC= int(x)
                                                PosyC= int(y)
                                                colorC ="#0035FF"
                                            elif celda == "R":
                                                tipoc = "Recursos"
                                                PosxC = int(x)
                                                PosyC = int(y)
                                                colorC = "#797878"
                                            elif celda == "E":
                                                tipoc = "Entrada"
                                                PosxC = int(x)
                                                PosyC = int(y)
                                                colorC = "#09BC06"
                                            if celda != "*":
                                                 LCelda.Insertar(Nodos.NodoCelda(nombre, tipoc, PosxC, PosyC, colorC, None))
                                            x = x + 1
                                        x = 0
                                        y = y + 1
                        elif hijo[j].tag=="unidadMilitar":
                                tipoc= "Militar"
                                color= "#FF0101"
                                PosxM = hijo[j].get('columna')
                                PosyM = hijo[j].get('fila')
                                ValorM= int(hijo[j].text)
                        j=j+1
                    LCiudad.Insertar(Nodos.NodoCiudad(nombre,filas,columnas,mapa))
                    LCelda.Insertar(Nodos.NodoCelda(nombre,tipoc,PosxM,PosyM,color,ValorM))
                    j = 0
                    x = 0
                    y = 0
            elif padre.tag =="robots":
                while n <= len(padre)-1:
                    if padre[n].tag== "robot":
                        tipoRobot = padre[n][0].get("tipo")
                        NRobot = padre[n][0].text
                        if tipoRobot=="ChapinFighter":
                            mision="Extracion De Recursos"
                            capacidad= int(padre[n][0].get("capacidad"))
                        else:
                            mision="Rescate"
                            capacidad = ""
                        n=n+1
                        LRobot.Insertar(Nodos.NodoRobot(tipoRobot,NRobot,capacidad,mision))
        print(LCiudad.imprimir())
        print(LCiudad.Graficar())
def main():
    Archivo()

if __name__ == '__main__':
    main()