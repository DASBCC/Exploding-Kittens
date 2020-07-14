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

<<<<<<< HEAD
mazo = ["DEFUSE.png", "BOMB.png", "COMODIN.png", "FAVOR.png", "SHUFFLE.png", "SEETHEFUTURE.png"]


lbExplodingKittens = tk.Label(ventana, text="Exploding Kittens")
lbExplodingKittens.place(x=200, y=10)

btnSalir = tk.Button(ventana, text="Salir", command=ventana.quit)


lbPerdiste= tk.Label(ventana, text="PERDISTE!!", bg="green", fg="red", font=('Ubuntu Monospace', 50))
=======
mazo = ["DESUFE.png", "DESUFE.png", "DESUFE.png", "DESUFE.png", "DESUFE.png", "DESUFE.png", "COMODIN1.png", "COMODIN1.png", "COMODIN1.png", "COMODIN1.png", "COMODIN2.png", "COMODIN2.png", "COMODIN2.png", "COMODIN2.png", "COMODIN3.png", "COMODIN3.png", "COMODIN3.png", "COMODIN3.png", "COMODIN4.png", "COMODIN4.png", "COMODIN4.png", "COMODIN4.png", "COMODIN5.png", "COMODIN5.png", "COMODIN5.png", "COMODIN5.png", "FAVOR.png", "FAVOR.png", "FAVOR.png", "FAVOR.png", "SHUFFLE.png", "SHUFFLE.png", "SHUFFLE.png", "SHUFFLE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png", "SEETHEFUTURE.png"]
mano = []
mano2= []
mano3= []
mano4= []
>>>>>>> 526e55b1ed174f646e270c7befbf93613ccbeedf

def perdiste():
    btnSalir.place(x=1055, y=600)
    MAZO.config(file=mazo[7])
    CARTA1.config(file=mazo[27])

#el comando perdiste esta en pruebas

    
lbExplodingKittens = tk.Label(ventana, text="Exploding Kittens",  font=('Ubuntu Monospace', 50))
lbExplodingKittens.place(x=320, y=10)  #titulo

btnSalir = tk.Button(ventana, text="Salir", command=ventana.quit, font=('Ubuntu Monospace', 20))
btnIniciar = tk.Button(ventana, text="Iniciar juego", font=('Ubuntu Monospace', 20))
btnIniciar.place(x=10,y=10)  #botones


#CARTAS DEL JUGADOR Y EN EL CENTRO

CARTA1=tk.PhotoImage(file="ATTACK.png")
CARTA1=CARTA1.subsample(1,1)
label=tk.Label(image=CARTA1)
label.place(x=10, y=550)

CARTA2=tk.PhotoImage(file="BOMB.png")
CARTA2=CARTA2.subsample(1,1)
label1=tk.Button (image=CARTA2,command=perdiste)
label1.place(x=150, y=550)

CARTA3=tk.PhotoImage(file="DEFUSE.png")
CARTA3=CARTA3.subsample(1,1)
label2=tk.Label(image=CARTA3)
label2.place(x=290, y=550)

CARTA4=tk.PhotoImage(file="DEFUSE.png")
CARTA4=CARTA4.subsample(1,1)
label3=tk.Label(image=CARTA4)
label3.place(x=440, y=550)

CARTA5=tk.PhotoImage(file="DEFUSE.png")
CARTA5=CARTA5.subsample(1,1)
label4=tk.Label(image=CARTA5)
label4.place(x=590, y=550)

CARTA6=tk.PhotoImage(file="DEFUSE.png")
CARTA6=CARTA6.subsample(1,1)
label5=tk.Label(image=CARTA6)
label5.place(x=740, y=550)

CARTA7=tk.PhotoImage(file="DEFUSE.png")
CARTA7=CARTA7.subsample(1,1)
label6=tk.Label(image=CARTA7)
label6.place(x=890, y=550)

MAZO=tk.PhotoImage(file="DEFUSE.png")
MAZO=MAZO.subsample(1,1)
label7=tk.Label(image=MAZO)
label7.place(x=500,y=200)
ventana.mainloop()