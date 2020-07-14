import random
mazo = ["defuse", "defuse", "defuse", "defuse", "defuse", "defuse", "comodin", "comodin", "comodin", "comodin", "comodin2", "comodin2", "comodin2", "comodin2", "comodin3", "comodin3", "comodin3", "comodin3", "comodin4", "comodin4", "comodin4", "comodin4", "comodin5", "comodin5", "comodin5", "comodin5", "favor", "favor", "favor", "favor", "shuffle", "shuffle", "shuffle", "shuffle", "STF", "STF", "STF", "STF", "STF"]
mano = []
mano2= []
mano3= []
mano4= []

def rotaLista(x):   #rota la lista 1 posición a la derecha
    x.append(x[0])
    return x[1:]

def checkIn(x,l): #revisa si x esta en l
    if x in l:
        return True
    else:
        return False

def checkBomba(l):   #revisa si la bomba está en el mazo del jugador 
    if checkIn("bomba",l)==True and checkIn("defuse",l)==False:
        return "Perdiste"
    else:
        mazo.append("bomba")
        l.remove("bomba")
        l.remove("defuse")

def revuelveMazo(l):   #revuelve el mazo central
    random.shuffle(l)
    return l

def seeTheFuture(l):   #enseña las siguientes tres cartas en el mazo
    return l[:3]

def tomaCarta(l):   #función para que un jugador coma una carta del mazo central y la ponga en su mazo
    mano.append(mazo[0])
    mazo = mazo[1:]

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

def repartidorRec(mazo,x):  #mazo es la lista con las cartas, x es la cantidad de cartas por jugador
    mazo = revuelveMazo(mazo)  #pasar función a iteración 
    if x>1:
        mano.append(mazo[0])
        mano2.append(mazo[1])
        mano3.append(mazo[2])
        mano4.append(mazo[3])
        mazo = mazo[4:]
        return repartidorRec(mazo,x-1)
    else:
        mano.append(mazo[0])
        mano2.append(mazo[1])
        mano3.append(mazo[2])
        mano4.append(mazo[3])
        x = x - 1
        mazo = mazo[4:]
        return mano, mano2, mano3, mano4, mazo



print (repartidor(mazo,7))