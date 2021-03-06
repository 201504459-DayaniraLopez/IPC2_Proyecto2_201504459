from os import startfile,system

class NodoDato():
    def __init__(self,x,y,letra,valor):
        self.x = x
        self.y = y
        self.Letra = letra
        self.Valor = valor
        self.Siguiente = None
        self.Anterior= None
        self.Abajo = None
        self.Arriba = None



class ListaFila():
    def __init__(self):
        self.Inicio= None
        self.Final =None
    
    def insertar(self, Dato):

        if self.Inicio is None:
            self.Inicio = Dato
            self.Final = Dato

        elif Dato.x < self.Inicio.x:
            self.Inicio.Anterior = Dato
            Dato.Siguiente = self.Inicio
            self.Inicio = self.Inicio.Anterior

        elif Dato.x >= self.Final.x:
            aux = self.Inicio
            while aux.Siguiente != None:
                aux = aux.Siguiente
            aux.Siguiente=Dato
            Dato.Anterior = aux
            self.Final=Dato


class ListaColumna():
    def __init__(self):
        self.Inicio= None
        self.Final =None
    
    def insertar(self, Dato):
        
        if self.Inicio is None:
            self.Inicio=self.Final=Dato

        elif Dato.y < self.Inicio.y:
            self.Inicio.Arriba=Dato
            Dato.Abajo = self.Inicio
            self.Inicio = self.Inicio.Arriba

        elif Dato.y >= self.Final.y:
            aux = self.Inicio
            while aux.Abajo != None:
                aux = aux.Abajo
            aux.Abajo=Dato
            Dato.Arriba = aux
            self.Final=Dato



class NodoCabeceraX():
    def __init__(self, posX):
        self.PosX= posX
        self.ListaH= ListaFila()
        self.Siguiente = None
        self.Anterior = None

class ListaX():
    def __init__(self):
        self.InicioX = None
        self.FinalX= None
    
    def insertarX(self, Dato):
        if self.InicioX is None:
            self.InicioX = self.FinalX = Dato

        elif Dato.PosX < self.InicioX.PosX:
            self.InicioX.Anterior = Dato
            Dato.Siguiente = self.InicioX
            self.InicioX = self.InicioX.Anterior

        elif Dato.PosX >= self.FinalX.PosX:
            aux = self.InicioX
            while aux.Siguiente != None:
                aux = aux.Siguiente
            aux.Siguiente = Dato
            Dato.Anterior = aux
            self.FinalX = Dato


    def Existe(self, x):
            if self.InicioX is None:
                return None
            else:
                aux = self.InicioX
                while aux != None:
                    if aux.PosX == x:
                        return aux

                    aux = aux.Siguiente
            return None

class NodoCabeceraY():
    def __init__(self, posY):
        self.PosY= posY
        self.ListaV= ListaColumna()
        self.Abajo = None
        self.Arriba = None

class ListaY():
       def __init__(self):
        self.InicioY = None
        self.FinalY=None

       def insertarY(self,Dato):
           if self.InicioY is None:
               self.InicioY = self.FinalY = Dato

           elif Dato.PosY < self.InicioY.PosY:
               self.InicioY.Arriba = Dato
               Dato.Abajo = self.InicioY
               self.Inicio = self.InicioY.Arriba

           elif Dato.PosY >= self.FinalY.PosY:
               aux = self.InicioY
               while aux.Abajo != None:
                   aux = aux.Abajo
               aux.Abajo = Dato
               Dato.Arriba = aux
               self.Final = Dato



       def Existe(self, y):
            if self.InicioY is None:
                return None
            else:
                aux = self.InicioY
                while aux != None:
                    if aux.PosY == y:
                        return aux
                    aux = aux.Abajo
            return None

class ListaOctogonal():

    def __init__(self):
        self.Horizontal = ListaX()
        self.Vertical = ListaY()

    def Verificar(self,x,y):
        nodoy = self.Vertical.InicioY
        while nodoy != None:
            aux = nodoy.ListaV.Inicio

            while aux is not None:
                if aux.x == x and aux.y == y:
                    return aux
                
                aux = aux.Siguiente

            nodoy = nodoy.Abajo

        return None
    
    def insertar(self, x, y,Dato):
        i = 0
        j = 0
        n = 0
        while i < x:
            if self.Verificar(i,j) == None:
                if self.Horizontal.Existe(i) == None:
                    self.Horizontal.insertarX(NodoCabeceraX(i))
            while j < y:
                Letra = Dato[n]
                if self.Vertical.Existe(j)== None:
                        self.Vertical.insertarY(NodoCabeceraY(j))
                TempX = self.Horizontal.Existe(i)
                TempY = self.Vertical.Existe(j)
                Nuevo = NodoDato(i,j,Letra,None)
                TempY.ListaV.insertar(Nuevo)
                TempX.ListaH.insertar(Nuevo)
                n = n + x
                j = j+1
            i=i+1
            n=i
            j=0

    def insertarM(self, x, y,letra,valor):
        temp = self.Vertical.InicioY
        while temp != None:
            temp2 = temp.ListaV.Inicio
            while temp2 != None:
                if temp2.x == int(x) and temp2.y== int(y):
                   temp2.Letra=letra
                   temp2.Valor=int(valor)
                temp2 = temp2.Abajo
            temp = temp.Abajo
    def CaminosDiponibles(self,xI,yI,xF,yF,):
        Caminos=[]
        x=0
        y=0
        temp1= self.Vertical.InicioY
        PosyI = yI
        PosxI = xI
        while temp1 != None:
            if yI < yF and xI < xF:
                temp2 = temp1.ListaV.Inicio
                while temp2 != None:
                        #Si mi pisicion final esta a la derecha
                        if yI <= yF:
                            #incia el recorrido en x
                            if temp2.y == PosyI:
                                #buscamos en la fila inicio las celdas blancas
                                if temp2.Letra == ' ':
                                    posx = temp2.x+1
                                    posy = temp2.y+1
                                    Letra = temp2.Letra
                                    Caminos.append([posx, posy, Letra])
                                    temp2 = temp2.Abajo
                                if temp2.Abajo.Letra == "M" or temp2.Abajo.Letra == '*':
                                    PosyI = temp2.y
                                    PosxI = temp2.x

                            if temp2.y == PosyI and temp2.x == PosxI:
                                posx = temp2.x + 1
                                posy = temp2.y + 1
                                Letra = temp2.Letra
                                Caminos.append([posx, posy, Letra])
                                temp2 = temp2.Abajo

                            elif temp2.y != PosyI or temp2.x != PosxI:
                                temp2 = temp2.Abajo
            temp1 = temp1.Abajo
        return Caminos


    def VerificarCelda(self, x, y,robot):
        temp = self.Vertical.InicioY
        while temp != None:
            temp2 = temp.ListaV.Inicio
            while temp2 != None:
                if temp2.x == int(x)-1 and temp2.y == int(y)-1:
                   letra = temp2.Letra
                   if letra=="C" and robot ==  "ChapinRescue" or letra=="R" and robot == "ChapinFighter" :
                        return True
                   else:
                        return False
                elif temp2.x != int(x)-1 or temp2.y != int(y)-1 :
                   temp2 = temp2.Abajo
            temp = temp.Abajo
    def recorrer(self):
        juntar = ''
        temp = self.Vertical.InicioY
        while temp != None:
            temp2 = temp.ListaV.Inicio
            juntar = str(juntar) + '|'
            while temp2 != None:
                juntar = str(juntar) + str(temp2.Letra) + ' '
                temp2 = temp2.Abajo
            juntar = str(juntar) + '|\n'
            temp = temp.Abajo
        return str(juntar)
   

    def graficar(self,c,f,co, nombreM):
        i=1
        j=1
        enlacesn=''
        juntar = ''
        alinear = ''
        alinear2=''
        alinearco=''
        temp = self.Vertical.InicioY
        while temp != None:
            temp2 = temp.ListaV.Inicio
            while temp2 != None:
                if (temp2.Letra =='*'):
                    color="black"
                    juntar = str(juntar)+'nodo'+str(i)+'_'+str(j)+'[label="''",fillcolor="'+str(color)+'", grupo='+str(j+1)+' ];\n'
                    if j == 1:
                        alinear = alinear + '\nFila' + str(i) + '->'+'nodo'+str(i)+'_'+str(j)+'\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                        alinearco = alinearco + 'Columna'+str(j)+ '->'+'nodo'+str(i)+'_'+str(j)+';'
                        enlacesn = enlacesn + '\nnodo' + str(i) + '_' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j + 1) + ';'
                    elif j<c:
                        enlacesn = enlacesn +'\nnodo'+str(i)+'_'+str(j)+'->'+'nodo'+str(i)+'_'+str(j+1)+';'
                        alinear2 = alinear2+'\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                    elif j == c:
                        alinear2 = alinear2 + '\n{rank = same; Fila' + str(i) + ';' + 'nodo' + str(i) + '_' + str(j) + '}\n'
                    if i == 1:
                        enlacesn = enlacesn + '\nColumna' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j) + ';'
                    elif i>1:
                        enlacesn = enlacesn + '\n nodo' + str(i-1) + '_' + str(j) +'->' + 'nodo' + str(i) + '_' + str(j) + ';'

                elif(temp2.Letra ==' '):
                    color = "white"
                    juntar = str(juntar) +'\nnodo'+str(i)+'_'+str(j)+'[label="''",fillcolor="' + str(color) + '", grupo='+str(j+1)+'];\n'
                    if j == 1:
                        alinear = alinear + '\nFila' + str(i) + '->'+'nodo'+str(i)+'_'+str(j)+';' + '\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                        enlacesn = enlacesn + '\nnodo' + str(i) + '_' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j + 1) + ';'
                    elif j < c:
                        enlacesn = enlacesn +'\nnodo'+str(i)+'_'+str(j)+'->'+'nodo'+str(i)+'_'+str(j+1)+';'
                        alinear2 = alinear2+'\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                    elif j == c:
                        alinear2 = alinear2 + '\n{rank = same; Fila' + str(i) + ';' + 'nodo' + str(i) + '_' + str(j) + '}\n'
                    if i == 1:
                        enlacesn = enlacesn + '\nColumna' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j) + ';'
                    elif i > 1:
                        enlacesn = enlacesn + '\n nodo' + str(i-1) + '_' + str(j) +'->' + 'nodo' + str(i) + '_' + str(j) + ';'

                elif (temp2.Letra =='E'):
                    color="green"
                    juntar = str(juntar)+'nodo'+str(i)+'_'+str(j)+'[label="''", fillcolor="'+str(color)+'", grupo='+str(j+1)+'];\n'
                    if j == 1:
                        alinear = alinear + '\nFila' + str(i) + '->'+'nodo'+str(i)+'_'+str(j)+'\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                        alinearco = alinearco + 'Columna'+str(j)+ '->'+'nodo'+str(i)+'_'+str(j)+';'
                        enlacesn = enlacesn + '\nnodo' + str(i) + '_' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j + 1) + ';'
                    elif j<c:
                        enlacesn = enlacesn +'\nnodo'+str(i)+'_'+str(j)+'->'+'nodo'+str(i)+'_'+str(j+1)+';'
                        alinear2 = alinear2+'\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                    elif j == c:
                        alinear2 = alinear2 + '\n{rank = same; Fila' + str(i) + ';' + 'nodo' + str(i) + '_' + str(j) + '}\n'
                    if i == 1:
                        enlacesn = enlacesn + '\nColumna' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j) + ';'
                    elif i>1:
                        enlacesn = enlacesn + '\n nodo' + str(i-1) + '_' + str(j) +'->' + 'nodo' + str(i) + '_' + str(j) + ';'

                elif (temp2.Letra =='C'):
                    color="blue"
                    juntar = str(juntar)+'nodo'+str(i)+'_'+str(j)+'[label="''", fillcolor="'+str(color)+'", grupo='+str(j+1)+'];\n'
                    if j == 1:
                        alinear = alinear + '\nFila' + str(i) + '->'+'nodo'+str(i)+'_'+str(j)+'\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                        alinearco = alinearco + 'Columna'+str(j)+ '->'+'nodo'+str(i)+'_'+str(j)+';'
                        enlacesn = enlacesn + '\nnodo' + str(i) + '_' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j + 1) + ';'
                    elif j<c:
                        enlacesn = enlacesn +'\nnodo'+str(i)+'_'+str(j)+'->'+'nodo'+str(i)+'_'+str(j+1)+';'
                        alinear2 = alinear2+'\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                    elif j == c:
                        alinear2 = alinear2 + '\n{rank = same; Fila' + str(i) + ';' + 'nodo' + str(i) + '_' + str(j) + '}\n'
                    if i == 1:
                        enlacesn = enlacesn + '\nColumna' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j) + ';'
                    elif i>1:
                        enlacesn = enlacesn + '\n nodo' + str(i-1) + '_' + str(j) +'->' + 'nodo' + str(i) + '_' + str(j) + ';'
                elif (temp2.Letra =='R'):
                    color="gray"
                    juntar = str(juntar)+'nodo'+str(i)+'_'+str(j)+'[label="''", fillcolor="'+str(color)+'", grupo='+str(j+1)+'];\n'
                    if j == 1:
                        alinear = alinear + '\nFila' + str(i) + '->'+'nodo'+str(i)+'_'+str(j)+'\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                        alinearco = alinearco + 'Columna'+str(j)+ '->'+'nodo'+str(i)+'_'+str(j)+';'
                        enlacesn = enlacesn + '\nnodo' + str(i) + '_' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j + 1) + ';'
                    elif j<c:
                        enlacesn = enlacesn +'\nnodo'+str(i)+'_'+str(j)+'->'+'nodo'+str(i)+'_'+str(j+1)+';'
                        alinear2 = alinear2+'\n{rank = same; Fila' + str(i) + ';' +'nodo'+str(i)+'_'+str(j)+'}\n'
                    elif j == c:
                        alinear2 = alinear2 + '\n{rank = same; Fila' + str(i) + ';' + 'nodo' + str(i) + '_' + str(j) + '}\n'
                    if i == 1:
                        enlacesn = enlacesn + '\nColumna' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j) + ';'
                    elif i>1:
                        enlacesn = enlacesn + '\n nodo' + str(i-1) + '_' + str(j) +'->' + 'nodo' + str(i) + '_' + str(j) + ';'

                elif (temp2.Letra == 'M'):
                    color = "red"
                    juntar = str(juntar) + 'nodo' + str(i) + '_' + str(j) + '[label="''", fillcolor="' + str(color) + '", grupo=' + str(j + 1) + '];\n'
                    if j == 1:
                        alinear = alinear + '\nFila' + str(i) + '->' + 'nodo' + str(i) + '_' + str(
                            j) + '\n{rank = same; Fila' + str(i) + ';' + 'nodo' + str(i) + '_' + str(j) + '}\n'
                        alinearco = alinearco + 'Columna' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j) + ';'
                        enlacesn = enlacesn + '\nnodo' + str(i) + '_' + str(j) + '->' + 'nodo' + str(i) + '_' + str(
                            j + 1) + ';'
                    elif j < c:
                        enlacesn = enlacesn + '\nnodo' + str(i) + '_' + str(j) + '->' + 'nodo' + str(i) + '_' + str(
                            j + 1) + ';'
                        alinear2 = alinear2 + '\n{rank = same; Fila' + str(i) + ';' + 'nodo' + str(i) + '_' + str(
                            j) + '}\n'
                    elif j == c:
                        alinear2 = alinear2 + '\n{rank = same; Fila' + str(i) + ';' + 'nodo' + str(i) + '_' + str(
                            j) + '}\n'
                    if i == 1:
                        enlacesn = enlacesn + '\nColumna' + str(j) + '->' + 'nodo' + str(i) + '_' + str(j) + ';'
                    elif i > 1:
                        enlacesn = enlacesn + '\n nodo' + str(i - 1) + '_' + str(j) + '->' + 'nodo' + str(
                            i) + '_' + str(j) + ';'
                j = j + 1
                temp2 = temp2.Abajo
            j = 1
            i = i + 1
            juntar = str(juntar)
            temp = temp.Abajo

        #return juntar
        i = 1
        j = 1
        columnas=""
        cadenac = ""
        enlacesc = ""
        cadenaf = ""
        enlacesf = ""
        graphviz='digraph G {\nnode[shape = box fillcolor = "#FFEDDB" style = filled ]\n   label = "Mapa: '+nombreM+'"\n   bgcolor = ""#008B8B"\n   subgraph clustre_p{\n   raiz[label ='"C01"' fillcolor="#008B8B"]\n   edge [dir= "both"]\n'
        while (i <= f):
           if i < f:
               cadenaf = cadenaf+'\nFila'+str(i)+'[label="'+str(i)+'", group=1];'
               enlacesf ="\n" +enlacesf+'Fila'+str(i)+'->'+'Fila'+str(i+1)+';'
           elif i == f:
               cadenaf = cadenaf + '\nFila' + str(i) + '[label="' + str(i) + '", group=1];'
           i = i + 1
        while (j<=c):
            if j < c:
                cadenac = cadenac + '\nColumna' + str(j) + '[label="'+str(j) + '", group='+str(j+1) +' fillcolor = "#E6E6FA"];'
                enlacesc = enlacesc + 'Columna'+str(j) +'->'+'Columna'+str(j+1)+";\n"
                columnas = columnas + 'Columna' + str(j) + ';'
            elif j == c:
                cadenac = cadenac + '\nColumna' + str(j) + '[label="' + str(j) + '", group='+str(j+1) +' fillcolor = "#E6E6FA"];'
                columnas = columnas + 'Columna' + str(j)
            j = j + 1
        graphviz = graphviz+cadenaf+enlacesf+"\n"+cadenac+"\n"+enlacesc+"\n"+'raiz->Fila1\nraiz->Columna1\n{rank = same; raiz;'+columnas+'}'+juntar+alinear+alinear2+enlacesn+'\n}\n}'
        miArchivo = open('Graficas/graphviz.dot', 'w')
        miArchivo.write(graphviz)
        miArchivo.close()
        # Motor de grafic lo compile
        system('dot -Tpng Graficas/graphviz.dot -o Graficas/graphviz.jpg')  # nombre del archivo que se escribio/ archivo de salida
        startfile('Graficas\graphviz.jpg')
        return juntar+alinear+enlacesn+alinear2
      