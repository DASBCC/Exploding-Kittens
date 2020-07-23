import tkinter as tk
import random 
TITULO = "Exploding kittens"
ANCHO, ALTO = 1150, 750

ventana = tk.Tk()

anchoPantalla = ventana.winfo_screenwidth()
largoPantalla = ventana.winfo_screenheight()

POS_VENTANA_X = int((anchoPantalla/2) - (ANCHO/2))
POS_VENTANA_Y = int((largoPantalla/2) - (ALTO/2))

ventana.title(TITULO)
ventana.geometry("{}x{}+{}+{}".format(ANCHO, ALTO, POS_VENTANA_X, POS_VENTANA_Y))
ventana.resizable(width=False, height=False)
ventana.config(bg="green")

#Lo anterior son características de la ventana

#Mazo y manos de los jugadores

mazo = ["DEFUSE.png", "DEFUSE.png", "DEFUSE.png", "DEFUSE.png", "DEFUSE.png", "DEFUSE.png", "COMODIN1.png", "COMODIN1.png", "COMODIN1.png", "COMODIN1.png", "COMODIN2.png", "COMODIN2.png", "COMODIN2.png", "COMODIN2.png", "COMODIN3.png", "COMODIN3.png", "COMODIN3.png", "COMODIN3.png", "COMODIN4.png", "COMODIN4.png", "COMODIN4.png", "COMODIN4.png", "COMODIN5.png", "COMODIN5.png", "COMODIN5.png", "COMODIN5.png", "FAVOR.png", "FAVOR.png", "FAVOR.png", "FAVOR.png", "SHUFFLE.png", "SHUFFLE.png", "SHUFFLE.png", "SHUFFLE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png"]
mano = []
mano2= []
mano3= []
mano4= []
bombas = ["BOMB.png","BOMB.png","BOMB.png","BOMB.png"]

def revuelveMazo(l):   #revuelve el mazo central(l)
    random.shuffle(l)
    return l

def repartidor(mazo,x): #reparte el mazo
    mazo = revuelveMazo(mazo)
    while x>0:
        mano.append(mazo[0])
        mano2.append(mazo[1])
        mano3.append(mazo[2])
        mano4.append(mazo[3])
        x = x - 1
        mazo = mazo[4:]
    mazo.extend(bombas)
    revuelveMazo(mazo)
    return mano, mano2, mano3, mano4, mazo



def ij(): #Funcion iniciar juego
    repartidor(mazo,7)
    CARTA.config(file=mano[0])

def comer(): #Funcion comer cartas del mazo, come una carta y la agrega a la mano
    global mano, mazo
    mano.append(mazo[0])
    mazo = mazo[1:]

def jugar():  #Funcion que juega la carta seleccionada
    if mano[0] == "SEETHEFUTURE.png":
        print (seeTheFuture(mazo))
        return seeTheFuture(mazo) and carta_usada()
    if mano[0] == "SHUFFLE.png":
        return revuelveMazo(mazo) and carta_usada()
    if mano[0] == "COMODIN1.png" or mano[0] == "COMODIN2.png" or mano[0] == "COMODIN3.png" or mano[0] == "COMODIN4.png" or mano[0] == "COMODIN5.png":
        if buscaComodin() == True:
            return True
        else:
            return False

def carta_usada(): #La carta que se usa se borra
    if mano[0]=="SEETHEFUTURE.png":
        C_USADAS.config(file=mano[0])
        mano.remove("SEETHEFUTURE.png")
    if mano[0]=="BOMB.png":
        C_USADAS.config(file=mano[0])

def buscaComodin():
    if mano.count("COMODIN1.png") >=2 or mano.count("COMODIN2.png") >=2 or mano.count("COMODIN3.png") >=2 or mano.count("COMODIN4.png") >=2 or mano.count("COMODIN5.png") >=2:
        print ("True")
        return True
    else:
        #print (mano.count("COMODIN1.png"))
        #print (mano.count("COMODIN2.png"))
        #print (mano.count("COMODIN3.png"))
        #print (mano.count("COMODIN4.png"))
        #print (mano.count("COMODIN5.png"))
        #print ("False")
        return False
    
def perdiste():
    btnSalir.place(x=1055, y=600) #funcion jugador perdio

def seeTheFuture(l):   #enseña las siguientes tres cartas en el mazo
    return l[:3]

def checkIn(x,l): #revisa si x esta en l
    if x in l:
        return True
    else:
        return False

def checkBomba(l):   #revisa si la bomba está en el mazo(l) del jugador 
    if checkIn("BOMBA.png",l)==True and checkIn("DEFUSE.png",l)==False:
        return perdiste
    else:
        mazo.append("BOMBA.png")
        l.remove("BOMBA.png")
        l.remove("DEFUSE.png")

def siguiente(): #siguiente carta
    global mano
    mano.append(mano[0])
    mano = mano[1:]
    #print(mano)
    CARTA.config(file=mano[0])

   
lbExplodingKittens = tk.Label(ventana, text="Exploding Kittens",  font=('Ubuntu Monospace', 50))
lbExplodingKittens.place(x=320, y=10)  #titulo

#botones

btnSalir = tk.Button(ventana, text="Salir", command=ventana.quit, font=('Ubuntu Monospace', 20))

btnIniciar = tk.Button(ventana, text="Iniciar Juego", command=ij, font=('Ubuntu Monospace', 20))
btnIniciar.place(x=10,y=10) 

btnComer = tk.Button(ventana, text="Comer", command=comer, font=('Ubuntu Monospace', 20))
btnComer.place(x=100,y=100)

btnJugar = tk.Button(ventana, text="Jugar", command=jugar, font=('Ubuntu Monospace', 20))
btnJugar.place(x=220,y=100)

btnSiguiente = tk.Button(ventana, text="Siguiente", command=siguiente, font=('Ubuntu Monospace', 20))
btnSiguiente.place(x=340,y=100)


#CARTAS DEL JUGADOR Y EN EL CENTRO

CARTA=tk.PhotoImage(file="")
CARTA=CARTA.subsample(1,1)
label=tk.Label(image=CARTA)
label.place(x=550, y=250)


C_USADAS=tk.PhotoImage(file="")
C_USADAS=C_USADAS.subsample(1,1)
lbC_USADAS=tk.Button(image=C_USADAS)
lbC_USADAS.place(x=250, y=250)

ventana.mainloop()