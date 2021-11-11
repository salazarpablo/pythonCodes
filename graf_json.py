from os import read
import random
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def open_csv(file):
    df = pd.read_csv(file)
    return df

def p(*args):
    def lab():
        return plt.title
    return lab()

def graf_puntos_grid(df):
    grupos = df.groupby(df.Nombre)
    cont=1
    plt.figure(figsize=(12,6))
    x = df['x']
    y = df['y']
    colores = ["red", "green", "grey", "purple", "yellow", "blue",]
    temp = len(df.Nombre.unique())
    temp = math.ceil(math.sqrt(temp))
    
    for column in df.Nombre.unique():
        plt.subplot(temp,temp,cont)
        nombre = grupos.get_group(column)
        plt.scatter(nombre['x'],nombre['y'], color = random.choice(colores), label = column)
        cont=cont+1
        plt.savefig(column+".png")
    #nombre_df = grupos.get_group('Nombre')
    #plt.scatter(x, y)
    plt.xticks(np.arange(.3, 100, step=10))
    plt.yticks(np.arange(0, 3.5, step=.1))
    #plt.legend(loc="upper right")
    p('Retardo')
    plt.xlabel('Amplitud')
    plt.ylabel('Frecuencia')
    plt.show()
    #plt.xlim(0, 11)
    #plt.ylim(-1.5, 10)

graf_puntos_grid(open_csv("prueba.csv"))



