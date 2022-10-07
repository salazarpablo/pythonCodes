import pandas as pd
import pymongo
from pymongo import MongoClient
import pprint
#Jalando los datos de variables de entorno (Secrets)

df = pd.read_csv("prueba.csv")#tesisData 6 csv
otro = df.head(10).to_dict(orient="records")

#extraigas host y port de un config file
#puerto = config['puerto'] #27017
#host = config['host'] # 127.0.0.1

#mc = MongoClient()
#mc = MongoClient('localhost,27017') 
#def cargarconfig():
#     ddc = read("config.json")
#     nombrecole = value("nombre de coleccion")

nombrecole = "computer_science" #Llenado de datos desde un archivo de configuracion
nombrebd = "student_database"
mc = MongoClient('127.0.0.1',27017) 
db = mc[nombrebd] 
cole = db[nombrecole] 

#doc = {"maestria":"de datos"}
w = cole.insert_many(otro).inserted_ids
print(w)

f = cole.find({"x":{"$gt":7.5}})
#f = cole.find()
fl = list(f)
pprint.pprint(fl)

ndf = pd.DataFrame(fl)
print(ndf.describe())

ndf.to_csv("nuezTres.csv")

#im = cole.insert_many(otro)#por los keys.
#matplot lib o seaborn
#Graficacion
#Discovery de los datos, describe, aggregation.
#La parte de modelos de ML o etc
#


