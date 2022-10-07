from pymongo import MongoClient
import datetime
import pprint
import json
import pandas as pd

def open_csv(file):
    df = pd.read_csv(file)
    return df

df = open_csv('Covid_19_Mexico_Clean_Complete.csv')

post = df.head(10).to_dict(orient='records')

client = MongoClient("mongodb://localhost:27017/")  # Crear el objeto de conexión a la base de datos
# client = MongoClient('localhost', 27017)
db = client.test  # crear el objeto de base de datos
# db = client['test']

collection = db.equis  # crear una colección
# collection = db['equis']


posts = db.equis  # crear una colección
#post_id = posts.insert_one(post).inserted_id  # insertar en la colección
# posts.insert_one(post).inserted_id#insertar en la colección

#print(post_id)
#pprint.pprint(posts.find_one({"_id": post_id}))  # encontrar el registro gracias a la llave ID

print(db.list_collection_names())  # imprimir las colecciones que se tienen en la db
pprint.pprint(posts.find_one())

new_posts = df.tail(10).to_dict(orient='records')
result = posts.insert_many(new_posts)  # insertar varias lineas
print(result.inserted_ids)

for post in posts.find():
    pprint.pprint(post)  # Imprimir contenido.

# Tomar uno de los CSVs e introducir 10 FILAS a la base de datos.

f = pd.read_csv("Basketball.csv", encoding='utf-8')
for row in f.head(10).iterrows():
    posts.insert_one(row[1].to_dict())

