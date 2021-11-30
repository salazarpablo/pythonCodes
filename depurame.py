import random
from enum import Enum
import pandas as pd


OPCIONES = ["piedra", "papel", "tijera", "lizard", "spock"]

class Resultados(Enum):
    GANADOR = 1
    PERDEDOR = 2
    EMPATE = 0

def ganador(competidor_1, competidor_2):
    """Regresa el resultado desde la perspectiva del competidor 1"""
    if (competidor_1 == "piedra" and competidor_2 == "tijera") or \
       (competidor_1 == "piedra" and competidor_2 == "lizard") or \
       (competidor_1 == "papel"  and competidor_2 == "piedra") or \
       (competidor_1 == "papel" and competidor_2 == "spock") or \
       (competidor_1 == "tijera" and competidor_2 == "lizard") or \
       (competidor_1 == "tijera" and competidor_2 == "papel") or \
       (competidor_1 == "spock" and competidor_2 == "tijeras") or \
       (competidor_1 == "spock" and competidor_2 == "piedra") or \
       (competidor_1 == "lizard" and competidor_2== "tijeras") or \
       (competidor_1 == "lizard" and competidor_2== "papel"):
       return Resultados.GANADOR.value
    elif competidor_1 == competidor_2:
        return Resultados.EMPATE.value
    else:
        return Resultados.PERDEDOR.value

def crear_jugadores(numJug):#recibe numero de jugadores
    lista_jugador = []
    for i in range(0,numJug):
        #print("Creado Jugador", i+1)
        #print("Estrategia asignada",estrategias(i))
        lista_jugador.append((i+1,estrategias(i)))
    print(lista_jugador)
    return lista_jugador

def estrategias(numEstrategia):#recibe numero de estrategia
    dic_estrategias = {1:"Azar",
                2:"Piedra",
                3:"Tijera",
                4:"Papel",
                5:"Contrario",
                6:"Mismo si gana",
                7:"Mismo si pierde",
                8:"Derrota Anterior",
                9:"Sería Derrotado",
                10:"Sigue un ciclo",
                11:"Mas frecuencia"}
    return dic_estrategias[numEstrategia+1]

def evaluar(jp,jc,nj,resDic,ban,frec):#    
    j = ["Primera Tirada O","Segunda Tirada O"]

    print("Evaluación ",str(jp)," vs ",str(jc))
    print("Que tiré yo en el Anterior ",resDic["Tirada Uno"])
    print("Que tiró el otro en Anterior ",resDic["Tirada Dos"])
    print("Gané 1, Perdi 2, Empate 0 -->  ",resDic["Resultado"])
    if jp[0] == 1 or jc[0] == 1:#Azar
        j1 = random.choice(OPCIONES)
        if jp[0] == 1:
            j[0]= j1
        if jc[0] == 1:
            j[1]= j1
        if jp[0] == jc[0]:
            j[0]= j1
            j[1]= j1
        
    if jp[0] == 2 or jc[0] == 2:#Siempre Piedra 
        j1 = "piedra"
        if jp[0] == 2:
            j[0]= j1
        if jc[0] == 2:
            j[1]= j1
        if jp[0] == jc[0]:
            j1 = "piedra"
            j[0]= j1
            j[1]= j1
        
    if jp[0] == 3 or jc[0] == 3: #Siempre Tijera
        j1 = "tijera"
        if jp[0] == 3:
            j[0]= j1
        if jc[0] == 3:
            j[1]= j1
        if jp[0] == jc[0]:
            j1 = "tijera"
            j[0]= j1
            j[1]= j1

    if jp[0] == 4 or jc[0] == 4:#Siempre Papel 
        j1 = "papel"
        if jp[0] == 4:
            j[0]= j1
        if jc[0] == 4:
            j[1]= j1
        if jp[0] == jc[0]:
            j1 = "papel"
            j[0]= j1
            j[1]= j1

    if jp[0] == 5 or jc[0] == 5: # tiro contrario
        j1 = resDic["Tirada Dos"]
        if jp[0] == 5:
            j[0]= j1
        if jc[0] == 5:
            j[1]= j1
        if jp[0] == jc[0]:
            j[0]= j1
            j[1]= j1


    if jp[0] == 6 or jc[0] == 6:#mismo si gané, contrario si perdí 
        if resDic["Resultado"] == -1:
            j1 = resDic["Tirada Dos"]#algo default para el inicio
        elif resDic["Resultado"] == 2:
            j1 = resDic["Tirada Dos"]
        else:
            j1 = resDic["Tirada Uno"]
        if jp[0] == 6:
            j[0]= j1
        if jc[0] == 6:
            j[1]= j1
        if jp[0] == jc[0]:
            j[0]= j1
            j[1]= j1


    if jp[0] == 7 or jc[0] == 7:#mismo si perdio, contrario si ganó 
        if resDic["Resultado"] == -1:
            j1 = resDic["Tirada Dos"]#algo default para el inicio
        elif resDic["Resultado"] == 2:
            j1 = resDic["Tirada Uno"]
        else:
            j1 = resDic["Tirada Dos"]
        if jp[0] == 7:
            j[0]= j1
        if jc[0] == 7:
            j[1]= j1
        if jp[0] == jc[0]:
            j[0]= j1
            j[1]= j1


    if jp[0] == 8 or jc[0] == 8: #derrotar elección anterior adversario
        j1 = "DEF"
        if resDic["Resultado"] == -1:
            j1 = resDic["Tirada Dos"]#algo default para el inicio
        else:
            ta = resDic["Tirada Dos"]#tirada del adversario
            for o in OPCIONES:
                if ganador(o,ta) == 1:#ganar
                    j1=o
                    break            
        if jp[0] == 8:
            j[0]= j1
        if jc[0] == 8:
            j[1]= j1
        if jp[0] == jc[0]:
            j[0]= j1
            j[1]= j1


    if jp[0] == 9 or jc[0] == 9: #sería derrotado por elección anterior adversario
        j1 = "DEF"
        if resDic["Resultado"] == -1:
            j1 = resDic["Tirada Dos"]#algo default para el inicio
        else:
            ta = resDic["Tirada Dos"]#tirada del adversario
            for o in OPCIONES:
                if ganador(o,ta) == 2:#perder
                    j1=o
                    break            
        if jp[0] == 9:
            j[0]= j1
        if jc[0] == 9:
            j[1]= j1
        if jp[0] == jc[0]:
            j[0]= j1
            j[1]= j1


    if jp[0] == 10 or jc[0] == 10: #Sigue un ciclo piedra,tijera,papel necesitas papel, piedra, tijera
        j1 = "DEF"
        if ban == 0:
            j1 = "papel"
        elif ban == 1:
            j1 = "piedra"
        elif ban == 2:
            j1 = "tijera"      
        if jp[0] == 10:
            j[0]= j1
        if jc[0] == 10:
            j[1]= j1
        if jp[0] == jc[0]:
            j[0]= j1
            j[1]= j1

    if jp[0] == 11 or jc[0] == 11: #derrotar elección anterior adversario de acuerdo a la frecuencia de las des
        j1 = "DEFu"
        if resDic["Resultado"] == -1:
            j1 = resDic["Tirada Dos"]#algo default para el inicio
        else:
            ta = frec#tirada del adversario frecuente
            for o in OPCIONES:
                if ganador(o,ta) == 1:#ganar
                    j1=o
                    break            
        if jp[0] == 11:
            j[0]= j1
        if jc[0] == 11:
            j[1]= j1
        if jp[0] == jc[0]:
            j[0]= j1
            j[1]= j1

    #Armado Return
    todo = {
                "Jugador Uno":jp[0],
                "Tirada Uno":j[0],
                "Jugador Dos":jc[0],
                "Tirada Dos":j[1],
                "Resultado":ganador(j[0],j[1]),
                "Número Juego":nj+1}
    return todo    

    
def jugar(lj):#recibe lista de jugadores
    res = []
    cero = {
                "Jugador Uno":"",
                "Tirada Uno":random.choice(OPCIONES),
                "Jugador Dos":"",
                "Tirada Dos":random.choice(OPCIONES),
                "Resultado":"-1",
                "Número Juego":""}
    for juga in lj:
        for contra in lj:
            res_ant = []
            ban=0
            frec = "default"
            for juego in range(0,10):
                if juego == 0:
                    ev = evaluar(juga, contra, juego,cero,ban,"tijera")
                    res.append(ev)
                    res_ant.append(ev)
                    ban = ban +1
                else:
                    f = pd.DataFrame(res_ant)
                    f = f.groupby(["Tirada Dos"]).size().reset_index(name='frec')
                    f = f.iloc[0]
                    frec = f.values
                    if juga[0] == 10 or contra[0] == 10:
                        eve = evaluar(juga, contra, juego,res_ant[juego-1],ban,frec[0])
                        ban = ban +1
                        if ban>2:
                            ban=0
                    else:
                        eve = evaluar(juga, contra, juego,res_ant[juego-1],ban,frec[0])
                    res.append(eve)
                    res_ant.append(eve)

    reporte(res)
    
def reporte(listi):
    rdata = pd.DataFrame(listi)
    print(rdata)
    rdata.to_csv("reporte.csv")

jugar(crear_jugadores(11))