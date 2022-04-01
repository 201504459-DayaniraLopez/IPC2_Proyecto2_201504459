import tkinter

from functools import partial
from tkinter import *
from tkinter import Menu, ttk, filedialog
from tkinter import messagebox as MessageBox

class Ventana():

    def __init__(self):
        self.window = Tk()
        self.window.title("ChapinWarrions")
        self.window.geometry('900x500')
        fuente = 'Lucida Sans Typewriter'
        #SE CREARA UNA BARRA DE MENU
        menu = Menu(self.window)
        self.SubMenu1 = Menu(menu, tearoff=0,font=(fuente, 10))
        self.SubMenu1.add_command(label='Cargar Archivo',command = self.Cargar)
        menu.add_cascade(label='Inicio', menu=self.SubMenu1)
        self.window.config(menu=menu)

        #informacion
        Ciudad = Label(self.window, text="CIUDADES ", font=(fuente, 15))
        Ciudad.place(x=250, y=30)
        self.Mapa = StringVar()
        comboC = ttk.Combobox(self.window, textvariable=self.Mapa)
        comboC.place(x=380, y=35)
        opciones1 = ['Mapa1', 'Mapa2', 'Mapa3', 'Mapa4']
        comboC["values"] = opciones1
        btMostrar = Button(self.window, text="Mostrar Mapa", font=(fuente, 10), bg = '#AFC9D3')
        btMostrar.place(x=550, y=30)
        btMision = Button(self.window, text="Iniciar Mision", font=(fuente, 10), bg='#21B9F4', command = partial(Ventana.VentanaRobots,self))
        btMision.place(x=390, y=70)



        self.window.mainloop()

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
        Robots = ['Robot1', 'Ribot2', 'Robot3', 'Robot4']
        RobotsC["values"] = Robots
        btelegir = Button(self.windowR, text="Selecionar Robot", font=(fuente, 10), bg='#AFC9D3',command= partial(Ventana.ElegirRobot,self))
        btelegir.place(x=77, y=105)



        info2 = Label(self.windowR, text="Elija una Mision", font=(fuente, 11), bg='#E5F421')
        info2.place(x=70, y=190)

        self.mision = StringVar()
        combo2 = ttk.Combobox(self.windowR, textvariable=self.mision)
        combo2.place(x=75, y=240)
        opciones2 = ['Rescate', 'Recoletar']
        combo2["values"] = opciones2
       
        btnagregar = Button(self.windowR, text="Realizar Mision",font=(fuente, 11), command= partial(Ventana.cerrarventana, self),bg='#3CFF01' )
        btnagregar.place(x=70, y=275)

    def ElegirRobot(self):
        if self.Robot.get() == "":
            MessageBox.showwarning("Alerta", "No a elegido ningun Robot aun")
            self.windowR.destroy()
            Ventana.VentanaRobots(self)
        else:
            if self.Robot.get() == "Robot1":
                self.RobotTipo.set("ChapinFire")
            else:
                self.RobotTipo.set("ChapinRescate")

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
        ruta = filedialog.askopenfilename(initialdir = "/", title= "Selecione Archivo",filetypes = (("xml files","*.xml"),("todos los archivos","*.*")))
        print(ruta)

def main():
        reproductor = Ventana()
        return 0


if __name__ == '__main__':
    main()


