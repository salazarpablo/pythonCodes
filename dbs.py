from pymongo import MongoClient
import datetime
import pprint
import json
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")#Crear el objeto de conexión a la base de datos
#client = MongoClient('localhost', 27017)
db = client.test#crear el objeto de base de datos
#dbabrir = "una variable string que recibo"
#db = client[dbabrir]
#db = client['test']

collection = db.equis#crear una colección
#collection = db['equis']

post = {"algo": "muy equis",
        "algomas": "todo bien!",
        "nuevo": ["nuevos", "viejos", "la noticia"],
        "date": datetime.datetime.utcnow()}

posts = db.nuevacole#crear una colección
post_id = posts.insert_one(post).inserted_id#insertar en la colección
#posts.insert_one(post).inserted_id#insertar en la colección

print(post_id)
pprint.pprint(posts.find_one({"_id": post_id}))#encontrar el registro gracias a la llave ID

print(db.list_collection_names())#imprimir las colecciones que se tienen en la db

pprint.pprint(posts.find_one())

new_posts = [{"algo": "equis dos",
               "algomas": "Otra cosa",
               "nuevo": ["masivo", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"algo": "equis tres",
               "algomas": "Otra Cosa Tres",
               "nuevo": "no ",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]

result = posts.insert_many(new_posts)#insertar varias lineas
print(result.inserted_ids)

for post in posts.find():
    pprint.pprint(post)#Imprimir contenido.


#ACTIVIDAD: Tomar uno de los CSVs e introducir 10 FILAS a la base de datos. 

   