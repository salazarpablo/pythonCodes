import numpy as np

ar = np.array([1,2,3,4,5,6,7,8,9])
ar = np.array([[1,2,3,4],[1,2,3,4]])
ar = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
ar = np.array([1,2,3,4,5,6,7,8,9])
st = "hola"
print(st[0:1])

print(ar[0:1])
arn=[ar>5]
print(arn)
print(ar[ar>5])
print(type(ar))
print(ar)

arreglo = np.array([[1,23,3],[44,5,6],[75,8,9]])
print(arreglo[1:2,1])
print(arreglo)

print(np.sort(arreglo,axis=0))

print(arreglo.max(axis=0))
print(arreglo.max(axis=1))
print(arreglo.cumsum(axis=1))

from numpy import save
from numpy import load

datos_de_csv = np.genfromtxt("prueba.csv",delimiter=",")
save("1millon.npy",datos_de_csv)
datosrecuperados = load("nv.npy")
print(type(datosrecuperados)) 