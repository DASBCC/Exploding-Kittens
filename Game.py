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

#Mazo y manos de los jugadores

mazo = ["DEFUSE.png", "DEFUSE.png", "DEFUSE.png", "DEFUSE.png", "DEFUSE.png", "DEFUSE.png", "COMODIN1.png", "COMODIN1.png", "COMODIN1.png", "COMODIN1.png", "COMODIN2.png", "COMODIN2.png", "COMODIN2.png", "COMODIN2.png", "COMODIN3.png", "COMODIN3.png", "COMODIN3.png", "COMODIN3.png", "COMODIN4.png", "COMODIN4.png", "COMODIN4.png", "COMODIN4.png", "COMODIN5.png", "COMODIN5.png", "COMODIN5.png", "COMODIN5.png", "FAVOR.png", "FAVOR.png", "FAVOR.png", "FAVOR.png", "SHUFFLE.png", "SHUFFLE.png", "SHUFFLE.png", "SHUFFLE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png"]
mano = []
mano2= []
mano3= []
mano4= []

def revuelveMazo(l):   #revuelve el mazo central
    random.shuffle(l)
    return l

def repartidor(mazo,x):
    mazo = revuelveMazo(mazo)
    while x>0:
        mano.append(mazo[0])
        mano2.append(mazo[1])
        mano3.append(mazo[2])
        mano4.append(mazo[3])
        x = x - 1
        mazo = mazo[4:]
    mazo.extend(["bomba","bomba","bomba","bomba"])
    mazo = revuelveMazo(mazo)
    return mano, mano2, mano3, mano4, mazo

def ij(): #Funcion iniciar juego
    repartidor(mazo,7)
    CARTA1.config(file=mano[0])
    CARTA2.config(file=mano[1])
    CARTA3.config(file=mano[2])
    CARTA4.config(file=mano[3])
    CARTA5.config(file=mano[4])
    CARTA6.config(file=mano[5])
    CARTA7.config(file=mano[6])

def perdiste():
    btnSalir.place(x=1055, y=600)
    MAZO.config(file=mazo[7])
    CARTA1.config(file=mazo[27])

#Función que manda la carta al centro

def carta_al_centro1():
    MAZO.config(file=mano[0])
    CARTA1.config(file="")
def carta_al_centro2():
    MAZO.config(file=mano[1])
    CARTA2.config(file="")
def carta_al_centro3():
    MAZO.config(file=mano[2])
    CARTA3.config(file="")
def carta_al_centro4():
    MAZO.config(file=mano[3])
    CARTA4.config(file="")
def carta_al_centro5():
    MAZO.config(file=mano[4])
    CARTA5.config(file="")
def carta_al_centro6():
    MAZO.config(file=mano[5])
    CARTA6.config(file="")
def carta_al_centro7():
    MAZO.config(file=mano[6])
    CARTA7.config(file="")

#el comando perdiste esta en pruebas

    
lbExplodingKittens = tk.Label(ventana, text="Exploding Kittens",  font=('Ubuntu Monospace', 50))
lbExplodingKittens.place(x=320, y=10)  #titulo

#botones

btnSalir = tk.Button(ventana, text="Salir", command=ventana.quit, font=('Ubuntu Monospace', 20))

btnIniciar = tk.Button(ventana, text="Iniciar juego", command=ij, font=('Ubuntu Monospace', 20))
btnIniciar.place(x=10,y=10) 


#CARTAS DEL JUGADOR Y EN EL CENTRO

CARTA1=tk.PhotoImage(file="")
CARTA1=CARTA1.subsample(1,1)
label=tk.Button(image=CARTA1, command=carta_al_centro1)
label.place(x=10, y=550)

CARTA2=tk.PhotoImage(file="")
CARTA2=CARTA2.subsample(1,1)
label1=tk.Button (image=CARTA2, command=carta_al_centro2)
label1.place(x=150, y=550)

CARTA3=tk.PhotoImage(file="")
CARTA3=CARTA3.subsample(1,1)
label2=tk.Button(image=CARTA3, command=carta_al_centro3)
label2.place(x=290, y=550)

CARTA4=tk.PhotoImage(file="")
CARTA4=CARTA4.subsample(1,1)
label3=tk.Button(image=CARTA4, command=carta_al_centro4)
label3.place(x=440, y=550)

CARTA5=tk.PhotoImage(file="")
CARTA5=CARTA5.subsample(1,1)
label4=tk.Button(image=CARTA5, command=carta_al_centro5)
label4.place(x=590, y=550)

CARTA6=tk.PhotoImage(file="")
CARTA6=CARTA6.subsample(1,1)
label5=tk.Button(image=CARTA6, command=carta_al_centro6)
label5.place(x=740, y=550)

CARTA7=tk.PhotoImage(file="")
CARTA7=CARTA7.subsample(1,1)
label6=tk.Button(image=CARTA7, command=carta_al_centro7)
label6.place(x=890, y=550)

MAZO=tk.PhotoImage(file="")
MAZO=MAZO.subsample(1,1)
label7=tk.Label(image=MAZO)
label7.place(x=500,y=200)
ventana.mainloop()