import tkinter as tk

TITULO = "Exploding kittens"
ANCHO, ALTO = 500, 500

ventana = tk.Tk()

anchoPantalla = ventana.winfo_screenwidth()
largoPantalla = ventana.winfo_screenheight()

POS_VENTANA_X = int((anchoPantalla/2) - (ANCHO/2))
POS_VENTANA_Y = int((largoPantalla/2) - (ALTO/2))

ventana.title(TITULO)
ventana.geometry("{}x{}+{}+{}".format(ANCHO, ALTO, POS_VENTANA_X, POS_VENTANA_Y))
ventana.resizable(width=False, height=False)
ventana.config(bg="green")

mazo = ["DEFUSE.png", "BOMB.png", "COMODIN.png", "FAVOR.png", "SHUFFLE.png", "SEETHEFUTURE.png"]


lbExplodingKittens = tk.Label(ventana, text="Exploding Kittens")
lbExplodingKittens.place(x=200, y=10)

btnSalir = tk.Button(ventana, text="Salir", command=ventana.quit)

lbPerdiste= tk.Label(ventana, text="PERDISTE!!", bg="green", fg="red", font=('Ubuntu Monospace', 50))

def perdiste():
    lbPerdiste.place(x=60,y=60)
    btnSalir.place(x=450, y=10)

image=tk.PhotoImage(file="ATTACK.png")
image=image.subsample(1,1)
label=tk.Label(image=image)
label.place(x=10, y=300)

image1=tk.PhotoImage(file="BOMB.png")
image1=image1.subsample(1,1)
label1=tk.Button (image=image1,command=perdiste)
label1.place(x=150, y=300)

image2=tk.PhotoImage(file="DEFUSE.png")
image2=image2.subsample(1,1)
label2=tk.Label(image=image2)
label2.place(x=290, y=300)


ventana.mainloop()