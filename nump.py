import numpy as np
from numpy import save
from numpy import load
from numpy.core.defchararray import asarray
import base64


df = np.genfromtxt("TSLA2.csv", delimiter=',',dtype=int)
print(type(df))
print(df.sum())

p= np.loadtxt('TSLA2.csv',skiprows=1)
p.sum()
arreglo = np.array([[1,2,3],[1,2,3],[1,2,3]])

ar = np.array([1,2,3,4,5,6,7,8,9])
print(ar.sum())
ar = np.array([1,2,3,4,5,6,7,8,9])
print(ar[0:1])
arn=[ar>5]
print(arn)
print(ar[ar>5])
st = "hola"



print(ar.min())
print(ar.max())
print(ar.mean())
print(np.sort(ar))
print("ORDENADO")


arreglo = np.array([[10,2,30],[2,44,5]],dtype=float)
arreglo = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arreglo[1:2,1])


print(np.sort(arreglo,axis=0))
print(arreglo)
print(arreglo.max(axis=0))
print(arreglo.max(axis=1))
print(arreglo.cumsum(axis=1))
print(np.median(arreglo))
print(np.corrcoef(arreglo))
print(np.std(arreglo))

ar2 = arreglo.copy()
print(ar2)

ar3= np.copy(arreglo)
print(ar3)

arreglo = np.array([[10,2,3],[2,3,3],[5,6,3]], dtype=np.int64)
arreglo2 = np.array([[1,2,3],[5,6,3],[5,6,3]], dtype=np.int64)
arreglo_vacio = np.empty((3,2))
arreglo_ceros = np.zeros((3,3,4))
print(arreglo_ceros)

pasos = np.arange(10,30,5)

valores_aleatorios = np.random.random((3,3))
print(valores_aleatorios)

valores_aleatorios = np.random.randint(5,10,size=(3,3))
print(valores_aleatorios)

datos = asarray([[1,2,3],[8,9,10],[1,2,3]])
print(type(datos))
#resultado = np.add(datos,datos)
#print(resultado)
datos = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(type(datos))
#datos_de_txt = np.loadtxt("algo.txt")
print("AQUIIIIIIIIIII")
datos_de_csv = np.genfromtxt("TSLA2.csv",delimiter=",")
df = np.genfromtxt("TSLA2.csv", delimiter=',')
print(type(datos_de_csv))
df.sum()
print(type(df))
print(df)
save("nuev.npy",datos)
resultado = np.subtract(arreglo,arreglo2)#resta arreglo - arreglo2
#resultado = np.add(arreglo,arreglo2)
matr = np.matrix([[1,2],[3,4]])
matr2 = np.matrix([[1,2],[3,4]])
#print(matr)
#print(np.transpose(matr))
#print(matr+matr2)
resultado = np.multiply(arreglo,arreglo2)
#print(type(resultado))
#print(np.dot(arreglo,arreglo2))
#print(resultado)
datosrecuperados = load("nuev.npy")
print(type(datosrecuperados)) 

#datos_encoded = base64.b64encode(datosrecuperados)
#print(datos_encoded)

#from html.parser import HTMLParser

#class HTMLFilter(HTMLParser):
#    text = ""
#    def handle_data(self, data):
#        self.text += data
#data= "Cloud &amp; no se que mas"
#f = HTMLFilter()
#f.feed(data)
#print(f.text)