import random
mazo = ["defuse", "defuse", "defuse", "defuse", "defuse", "defuse", "bomba", "bomba", "bomba", "bomba", "comodin", "comodin", "favor", "favor", "favor", "favor", "shuffle", "shuffle", "shuffle", "shuffle", "STF", "STF", "STF", "STF", "STF"]
mano = []
mano2= []
mano3= []
mano4= []

def rotaLista(x):
    x.append(x[0])
    return x[1:]

def checkIn(x,l): #revisa si x esta en l
    if x in l:
        return True
    else:
        return False

def checkBomba(l):
    if checkIn("bomba",l)==True and checkIn("defuse",l)==False:
        return "Perdiste"

def revuelveMazo(l):
    random.shuffle(l)
    return l

def seeTheFuture(l):
    return l[:3]

def tomaCarta(l):
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
    return mano, mano2, mano3, mano4, mazo

def repartidorRec(mazo,x):
    mazo = revuelveMazo(mazo)
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