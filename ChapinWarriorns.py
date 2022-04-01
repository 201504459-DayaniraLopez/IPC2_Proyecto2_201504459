import tkinter
import xml.etree.ElementTree as ET
from functools import partial
from tkinter import *
from tkinter import Menu, ttk, filedialog
from tkinter import messagebox as MessageBox
import Listas
import Nodos


LCiudad = Listas.ListaCiudad()
LCelda= Listas.ListasCelda()
LRobot = Listas.ListaRobot()
fuente = 'Lucida Sans Typewriter'

class Ventana():

    def __init__(self):
        self.window = Tk()
        self.window.title("ChapinWarrions")
        self.window.geometry('900x500')

        #SE CREARA UNA BARRA DE MENU
        menu = Menu(self.window)
        self.SubMenu1 = Menu(menu, tearoff=0,font=(fuente, 10))
        self.SubMenu1.add_command(label='Cargar Archivo',command = self.Cargar)
        menu.add_cascade(label='Inicio', menu=self.SubMenu1)
        self.window.config(menu=menu)
        self.window.mainloop()

    def Iniciar(self, MapasCiudades):

        #informacion
        Ciudad = Label(self.window, text="CIUDADES ", font=(fuente, 15))
        Ciudad.place(x=250, y=30)
        self.Mapa = StringVar()
        comboC = ttk.Combobox(self.window, textvariable=self.Mapa)
        comboC.place(x=380, y=35)
        opciones1 = MapasCiudades
        comboC["values"] = opciones1

        btMostrar = Button(self.window, text="Mostrar Mapa", font=(fuente, 10), bg = '#AFC9D3')
        btMostrar.place(x=550, y=30)
        btMision = Button(self.window, text="Iniciar Mision", font=(fuente, 10), bg='#21B9F4', command = partial(Ventana.VentanaRobots,self))
        btMision.place(x=390, y=70)


    def VentanaRobots(self):
        self.windowR = Toplevel()
        self.windowR.title("Informacion_Robots",)
        self.windowR['bg'] = '#581845'
        self.windowR.geometry('300x375')
        fondo = "#581845"
        letra = "#FFFFFF"
        fuente = 'Lucida Sans Typewriter'
        titulo = Label(self.windowR, text="INFORMACION DE ROBOTS", bg = fondo, font=(fuente, 12), fg="#FFFFFF")
        titulo.place(x=35, y=5)

        TipoR = Label(self.windowR, text="Tipo de Robot", font=(fuente, 11), bg= fondo, fg = letra)
        TipoR.place(x=25, y=150)

        self.infoR=self.color=self.RobotTipo= StringVar()
        self.RobotTipo.set("No Definido")
        self.infoR.set("No Definido")

        self.txtTipoR = Label(self.windowR, textvariable=self.infoR,font=(fuente, 11),bg='#21C6F4')
        self.txtTipoR.place(x=150, y=150)
        info = Label(self.windowR, text="Robots Disponibles: ", font=(fuente, 11), bg =fondo, fg =letra)
        info.place(x=60, y=40)


        self.Robot = StringVar()
        RobotsC = ttk.Combobox(self.windowR, textvariable=self.Robot)
        RobotsC.place(x=75, y=75)
        Robots = LRobot.imprimir()
        RobotsC["values"] = Robots
        btelegir = Button(self.windowR, text="Selecionar Robot", font=(fuente, 10), bg='#AFC9D3',command= partial(Ventana.ElegirRobot,self))
        btelegir.place(x=77, y=105)

        info2 = Label(self.windowR, text="Elija una Mision", font=(fuente, 11), bg='#E5F421')
        info2.place(x=70, y=190)

        self.mision = StringVar()
        combo2 = ttk.Combobox(self.windowR, textvariable=self.mision)
        combo2.place(x=75, y=240)
        opciones2 = ['Rescate', 'Extracion De Recursos']
        combo2["values"] = opciones2
       
        btnagregar = Button(self.windowR, text="Realizar Mision",font=(fuente, 11), command= partial(Ventana.cerrarventana, self),bg='#3CFF01' )
        btnagregar.place(x=70, y=275)

    def ElegirRobot(self):
        if self.Robot.get() == "":
            MessageBox.showwarning("Alerta", "No a elegido ningun Robot aun")
            self.windowR.destroy()
            Ventana.VentanaRobots(self)
        else:
            TipoRobot = LRobot.buscar(self.Robot.get())
            self.RobotTipo.set(TipoRobot)
        self.infoR.set(self.RobotTipo.get())

    def cerrarventana(self):
        if self.mision.get() == "":
            MessageBox.showwarning("Alerta", "No a elegido ninguna Mision aun")
            self.windowR.destroy()
            Ventana.VentanaRobots(self)
        else:
            if self.RobotTipo.get() == "ChapinFire" and self.mision.get()=="Rescate":
                MessageBox.showwarning("Alerta", self.RobotTipo.get()+", no puede realizar Misiones de "+self.mision.get())
                self.windowR.destroy()
                Ventana.VentanaRobots(self)
            elif self.RobotTipo.get() == "ChapinRescate" and self.mision.get()=="Recoletar":
                MessageBox.showwarning("Alerta", self.RobotTipo.get() + ", no puede realizar Misiones de "+self.mision.get())
                self.windowR.destroy()
                Ventana.VentanaRobots(self)
            else:
                MessageBox.showinfo("Informaicon", "La mision ha dado inicio")
                self.windowR.destroy()

    def Cargar(self):
        ruta = filedialog.askopenfilename(initialdir="/", title="Selecione Archivo", filetypes=(("xml files", "*.xml"), ("todos los archivos", "*.*")))
        archivo_xml = ET.parse(ruta)
        raiz = archivo_xml.getroot()
        x = y = 0
        j = n = 0
        mapa = []
        # iniciar Recorrido
        for padre in raiz:
            if padre.tag == "listaCiudades":
                for hijo in padre:
                    while j <= len(hijo) - 1:
                        if hijo[j].tag == "nombre":
                            filas = hijo[j].get('filas')
                            columnas = hijo[j].get('columnas')
                            nombre = hijo[j].text
                        elif hijo[j].tag == "fila":
                            patron = hijo[j].text.replace('"', "")
                            for celda in patron:
                                if celda == " ":
                                    tipoc = "Camino"
                                    PosxC = int(x)
                                    PosyC = int(y)
                                    colorC = "#FFFFF"
                                elif celda == "C":
                                    tipoc = "Civil"
                                    PosxC = int(x)
                                    PosyC = int(y)
                                    colorC = "#0035FF"
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
                            mapa.append(patron)
                            y = y + 1
                        elif hijo[j].tag == "unidadMilitar":
                            tipoc = "Militar"
                            color = "#FF0101"
                            PosxM = hijo[j].get('columna')
                            PosyM = hijo[j].get('fila')
                            ValorM = int(hijo[j].text)
                        j = j + 1
                    LCiudad.Insertar(Nodos.NodoCiudad(nombre, filas, columnas, mapa))
                    LCelda.Insertar(Nodos.NodoCelda(nombre, tipoc, PosxM, PosyM, color, ValorM))
                    mapa.clear()
                    j = 0
                    x = 0
                    y = 0
            elif padre.tag == "robots":
                while n <= len(padre) - 1:
                    if padre[n].tag == "robot":
                        tipoRobot = padre[n][0].get("tipo")
                        NRobot = padre[n][0].text
                        if tipoRobot == "ChapinFighter":
                            mision = "Extracion De Recursos"
                            capacidad = int(padre[n][0].get("capacidad"))
                        else:
                            mision = "Rescate"
                            capacidad = ""
                        n = n + 1
                        LRobot.Insertar(Nodos.NodoRobot(tipoRobot, NRobot, capacidad, mision))
        self.Iniciar(LCiudad.imprimir())

def main():
        reproductor = Ventana()
        return 0

if __name__ == '__main__':
    main()


