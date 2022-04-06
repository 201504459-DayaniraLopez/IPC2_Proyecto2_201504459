import tkinter
import xml.etree.ElementTree as ET
from functools import partial
from tkinter import *
from tkinter import Menu, ttk, filedialog
from tkinter import messagebox as MessageBox
import Listas
import Nodos
import ListaOctogonal as LO


LCiudad = Listas.ListaCiudad()
LCelda= Listas.ListasCelda()
LRobot = Listas.ListaRobot()
fuente = 'Lucida Sans Typewriter'

class Ventana():

    def __init__(self):
        self.window = Tk()
        self.window.title("ChapinWarrions")
        self.window.geometry('500x200')

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
        Ciudad.place(x=50, y=30)
        self.Mapa = StringVar()
        comboC = ttk.Combobox(self.window, textvariable=self.Mapa)
        comboC.place(x=180, y=35)
        opciones1 = MapasCiudades
        comboC["values"] = opciones1

        btMostrar = Button(self.window, text="Mostrar Mapa", font=(fuente, 10), bg = '#AFC9D3', command = self.graficar)
        btMostrar.place(x=350, y=30)
        btMision = Button(self.window, text="Iniciar Mision", font=(fuente, 10), bg='#21B9F4', command = partial(Ventana.VentanaRobots,self))
        btMision.place(x=190, y=70)


    def VentanaRobots(self):
        self.color = StringVar()
        self.RobotTipo = StringVar()
        self.Combate = StringVar()
        if self.Mapa.get()!="":
            self.windowR = Toplevel()
            self.windowR.title("Informacion_Robots",)
            self.windowR['bg'] = '#581845'
            self.windowR.geometry('310x575')
            fondo = "#581845"
            letra = "#FFFFFF"
            fuente = 'Lucida Sans Typewriter'
            titulo = Label(self.windowR, text="INFORMACION DE ROBOTS", bg = fondo, font=(fuente, 12), fg="#FFFFFF")
            titulo.place(x=45, y=5)

            TipoR = Label(self.windowR, text="Tipo de Robot", font=(fuente, 11), bg= fondo, fg = letra)
            TipoR.place(x=35, y=150)

            self.RobotTipo.set("No Definido")
            self.Combate.set("No Definido")

            self.txtTipoR = Label(self.windowR, textvariable=self.RobotTipo,font=(fuente, 11),bg='#21C6F4')
            self.txtTipoR.place(x=160, y=150)
            info = Label(self.windowR, text="Robots Disponibles: ", font=(fuente, 11), bg =fondo, fg =letra)
            info.place(x=70, y=40)
            self.Robot = StringVar()
            RobotsC = ttk.Combobox(self.windowR, textvariable=self.Robot)
            RobotsC.place(x=85, y=75)
            Robots = LRobot.imprimir()
            RobotsC["values"] = Robots
            btelegir = Button(self.windowR, text="Selecionar Robot", font=(fuente, 10), bg='#AFC9D3',command= partial(Ventana.ElegirRobot,self))
            btelegir.place(x=87, y=105)
            ValorC = Label(self.windowR, text="Valor de Combate", font=(fuente, 11), bg=fondo, fg=letra)
            ValorC.place(x=35, y=190)
            self.txtCombate = Label(self.windowR, textvariable=self.Combate, font=(fuente, 11), bg='#21C6F4')
            self.txtCombate.place(x=190, y=190)
            info2 = Label(self.windowR, text="Elija una Mision", font=(fuente, 11), bg='#E5F421')
            info2.place(x=82, y=220)
            self.mision = StringVar()
            combo2 = ttk.Combobox(self.windowR, textvariable=self.mision)
            combo2.place(x=85, y=260)
            opciones2 = ['Rescate', 'Extracion De Recursos']
            combo2["values"] = opciones2

            # text fiel para ingresar las posicones en X AND Y INCIAL
            self.titulo1= Label(self.windowR, text="POSICION INICIAL DEL ROBOT",font=(fuente, 11), bg='#005EFB' )
            self.titulo1.place(x=50, y=295)
            self.PosXI = StringVar()
            self.posicionxI = Label(self.windowR, text="POSICION X: ",font=(fuente, 9), bg='#CECFD0' )
            self.posicionxI.place(x=50, y=330)
            # text fiel para ingresar las posicones en x
            self.txtposicionxI = tkinter.Entry(self.windowR,textvariable=self.PosXI)
            self.txtposicionxI.place(x=150, y=330)
            self.PosYI = StringVar()
            self.posicionyI = Label(self.windowR, text="POSICION Y: ", font=(fuente, 9), bg='#CECFD0')
            self.posicionyI.place(x=50, y=360)

            self.txtposicionyI = tkinter.Entry(self.windowR,textvariable=self.PosYI)
            self.txtposicionyI.place(x=150, y=360)
            # text fiel para ingresar las posicones en X AND Y INCIAL
            self.titulo2 = Label(self.windowR, text="POSICION FINAL DEL ROBOT", font=(fuente, 11), bg='#005EFB')
            self.titulo2.place(x=50, y=390)
            self.PosXF = StringVar()
            self.posicionxF = Label(self.windowR, text="POSICION X: ", font=(fuente, 9), bg='#CECFD0')
            self.posicionxF.place(x=50, y=420)
            # text fiel para ingresar las posicones en x
            self.txtposicionxF = tkinter.Entry(self.windowR, textvariable=self.PosXF)
            self.txtposicionxF.place(x=150, y=420)
            self.PosYF = StringVar()
            self.posicionyF = Label(self.windowR, text="POSICION Y: ", font=(fuente, 9), bg='#CECFD0')
            self.posicionyF.place(x=50, y=450)
            # text fiel para ingresar las posicones en y
            self.txtposicionyF = tkinter.Entry(self.windowR, textvariable=self.PosYF)
            self.txtposicionyF.place(x=150, y=450)

            btnagregar = Button(self.windowR, text="Realizar Mision",font=(fuente, 11), command= partial(Ventana.cerrarventana, self),bg='#3CFF01' )
            btnagregar.place(x=75, y=500)
        elif self.Mapa.get() =="":
            MessageBox.showwarning("Alerta", "No a elegido ningun Mapa aun")

    def graficar(self):
        self.ListaOc = LO.ListaOctogonal()
        i=0
        datos = LCiudad.Buscar(self.Mapa.get())
        F = int(datos[0])
        C = int(datos[1])
        Mapap= str(datos[2])
        Nombre = str(datos[3])
        self.ListaOc.insertar(C,F,Mapap)
        Letra = "M"
        DatoM = LCelda.UnidadesM(self.Mapa.get())
        DatoC = LCelda.PatronC(self.Mapa.get())
        print("Caminos")
        print(DatoC)
        while i < len(DatoM):
            if int(DatoM[i][1]) != 0 and int(DatoM[i][1]) !=0:
                FM = int(DatoM[i][1])-1
                CM = int(DatoM[i][0])-1
            elif int(DatoM[i][1]) == 0:
                FM = int(DatoM[i][1])
            elif int(DatoM[i][0]) == 0:
                CM = int(DatoM[i][0])
            VALOR = int(DatoM[i][2])
            self.ListaOc.insertarM(CM, FM, Letra, VALOR)
            i = i+1
        self.ListaOc.graficar(C, F, Mapap, Nombre)
        print(self.ListaOc.recorrer())



    def ElegirRobot(self):
        if self.Robot.get() == "":
            MessageBox.showwarning("Alerta", "No a elegido ningun Robot aun")
            self.windowR.destroy()
            Ventana.VentanaRobots(self)
        else:
            datos = LRobot.buscar(self.Robot.get())
            self.RobotTipo.set(datos[0])
            self.Combate.set(datos[1])

    def cerrarventana(self):
        resultado = self.ListaOc.VerificarCelda(int(self.PosXF.get()),int(self.PosYF.get()),str(self.RobotTipo.get()))
        print(self.RobotTipo.get())
        print(self.mision.get())
        if self.mision.get() == "":
            MessageBox.showwarning("Alerta", "No a elegido ninguna Mision aun")
            self.windowR.destroy()
            Ventana.VentanaRobots(self)
        else:
            if self.RobotTipo.get() == "ChapinFighter" and self.mision.get() =="Rescate" or resultado==False:
                MessageBox.showwarning("Alerta", self.RobotTipo.get()+", no puede realizar Misiones de "+self.mision.get())
                self.windowR.destroy()
                Ventana.VentanaRobots(self)
            elif self.RobotTipo.get() == "ChapinRescue" and self.mision.get()=="Extracion De Recursos" or resultado ==False:
                MessageBox.showwarning("Alerta", self.RobotTipo.get() + ", no puede realizar Misiones de "+self.mision.get())
                self.windowR.destroy()
                Ventana.VentanaRobots(self)
            else:
                MessageBox.showinfo("Informaicon", "La mision ha dado inicio")
                print(self.ListaOc.CaminosDiponibles(int(self.PosXI.get())-1, int(self.PosYI.get())-1, int(self.PosXF.get())-1, int(self.PosYF.get())-1))
                self.windowR.destroy()


    def Cargar(self):
        ruta = filedialog.askopenfilename(initialdir="/", title="Selecione Archivo", filetypes=(("xml files", "*.xml"), ("todos los archivos", "*.*")))
        archivo_xml = ET.parse(ruta)
        raiz = archivo_xml.getroot()
        x = y = 0
        j = n = 0
        CiudadMapa =""
        # iniciar Recorrido
        for padre in raiz:
            if padre.tag == "listaCiudades":
                for hijo in padre:
                    while j <= len(hijo) - 1:
                        if hijo[j].tag == "nombre":
                            filas = hijo[0].get('filas')
                            columnas = hijo[0].get('columnas')
                            nombre = hijo[0].text
                        elif hijo[j].tag == "fila":
                            patron = hijo[j].text.replace('"', "")
                            CiudadMapa = CiudadMapa + str(patron)
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
                            y = y + 1
                        elif hijo[j].tag == "unidadMilitar":
                            tipoc = "Militar"
                            color = "#FF0101"
                            PosxM = hijo[j].get('columna')
                            PosyM = hijo[j].get('fila')
                            ValorM = int(hijo[j].text)
                            LCelda.Insertar(Nodos.NodoCelda(nombre, tipoc, PosxM, PosyM, color, ValorM))
                        j = j + 1
                    LCiudad.Insertar(Nodos.NodoCiudad(nombre, filas, columnas, CiudadMapa))
                    CiudadMapa=""
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
                            capacidad = 0
                        n = n + 1
                        LRobot.Insertar(Nodos.NodoRobot(tipoRobot, NRobot, capacidad, mision))
        self.Iniciar(LCiudad.imprimir())

def main():
        Ventana()
        return 0

if __name__ == '__main__':
    main()


