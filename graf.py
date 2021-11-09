from clas1_b import * 
#####################################################################
import numpy as np
import matplotlib.pyplot as plt
from pandasql import sqldf
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd     

def open_csv():
    x = OpenFormats()
    df = x.csvOpen("csvs/TSLA1.csv")
    return df

def graf_one():
    #fig, ax = plt.subplots()
    x = np.random.randint(1,10, size=10)
    y = 2*x 
    plt.plot(x,y) # same as ax.plot(x,y)
    plt.show()

def graf_multi(df):
    # Multiple lines
    #fig, ax = plt.subplots()
    x = np.random.randint(1,10, size=10)
    y = 2*x 
    y = df['Low'].head(50)
    x = df['High'].head(50)
    plt.plot(x,y)
    plt.plot(x,x+3)
    plt.show()

def graf_fresa(df):
    #fig, ax = plt.subplots()
    x = np.linspace(0,10,1000)
    y = 2*x
    #x = df['Volume']
    #y = df['High']
    # set of default color and style
    plt.plot(x, np.cos(x))
    # RGB tuple, values 0 to 1, solid style
    plt.plot(x, np.sin(x), color=(1.0,0.2,0.3),linestyle='-')
    # specify color by name, dashed style
    plt.plot(x, y, color='blue', linestyle='--', label="cos de x")
    #plt.legend() #Agregar el elemento
    # short color code (rgbcmyk), dotted style   
    plt.plot(x, x+3, color='g',linestyle=':')
    # Grayscale between 0 and 1, dashdot style    
    plt.plot(x, np.log(x), color='0.75',linestyle='-.')
    # Hex code (RRGGBB from 00 to FF), dashed style  
    plt.plot(x, x, color='#FFDD44',linestyle='--')
    #plt.xlim(0, 11)
    #plt.ylim(-1.5, 10)

    plt.show()

def graf_puntos(df):
    plt.subplots(figsize = (12,6))
    x = df['Open'].head(50)
    y = df['High'].head(50)
    
    pysqldf = lambda q: sqldf(q, globals())
    print (pysqldf("SELECT * FROM df WHERE Open>2;"))

    plt.scatter(x,y)
    #plt.xticks(np.arange(1,10,step =0.35))
    plt.xticks(np.arange(1,step =0.35))
    plt.yticks(np.arange(1,10,step =0.35))
    plt.title('Open vs High')
    plt.xlabel('Open')
    plt.ylabel('High')
    plt.show()


def new_csv():
    df = pd.read_csv('prueba.csv')

    df = df.loc[(df['y'] >= 1.5) & (df.loc[df['x']] >= 10)]
    df = df.append(pd.DataFrame())
    df.to_csv("prueba_2.csv")

def graf_dim(df):
    df = df.head(50)
    #from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['Open'],df['High'],df['Low'], s=25)
    ax.set( xlabel='Open', ylabel='High',zlabel='Low')


    ax2 = fig.add_subplot(111, projection='3d')
    ax2.scatter(df['Open'],df['High'],df['Low'], s=25)
    ax2.set( xlabel='Open', ylabel='High',zlabel='Low')
    #plt.xticks(np.arange(1,9,step =1))
    plt.xticks()
    plt.show()

def graf_his(df):
    fig = plt.figure(figsize=(8,6))
    plt.hist(df['High'], bins=3, density=True)
    plt.grid(alpha=0.2)
    plt.show()

def graf_box():
    # Create dataset
    user_1 = [10, 3, 15, 21, 17, 14]
    user_2 = [5, 13, 10, 7, 9, 12,3,4]
    data = [user_1, user_2]
    fig = plt.figure(figsize =(8, 6)) 
    
    # Create axes instance 
    ax = fig.add_axes([0, 0, 1, 1]) 
    
    # Create plot 
    bp = ax.boxplot(data) 
    
    # Show plot 
    plt.xticks([1,2],['user_1','user_2'])
    plt.show()



#graf_puntos(open_csv())


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
def multi_inone():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02) 
    plt.figure(1)
    plt.subplot(331)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') 
    plt.subplot(332)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--') 
    plt.subplot(333)
    #plt.show()#
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') 
    plt.subplot(334)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--') 
    #plt.show()#
    plt.subplot(335)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') 
    plt.subplot(336)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--') 
    plt.show()#
#Date   Open   High    Low  Close  Adj Close    Volume

#plt.plot()                      #Creación de una gráfica de línea
#plt.show()                      #Mostrar la figura
#plt.savefig(nombre.formato)     # (Opcional) Guardar la figura
#plt.close('all')                #Cerrar