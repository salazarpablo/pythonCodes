import pymongo #mongoengine

cliente = pymongo.MongoClient("mongodb://localhost:27017/")#con Atlas es el mismo procedimiento, cambia la URL

unadb = cliente["laclase"]#el nombre de la base de datos
#print(unadb.name)
listadbs = cliente.list_database_names() #mostrar la lista de base de datos

if "laclase" in listadbs:
    print("Si existe")

unacole = unadb["lacoleccion"]
print(unadb.list_collection_names())

undic = {"nombre":"cualquiera","apellido":"otra cosa","numero":"3325438191"}

res = unacole.insert_one(undic)# o insert many
print(res.inserted_id)

#Leer un CSV, sacar entre 5 y 10 de filas, e insertarlas en MONGODB

vardic = [{"nombre":"cualquiera1","apellido":"otra cosa1","numero":"3325438191"},
        {"nombre":"cualquiera2","numero":"3325438191"},
        {"nombre":"cualquiera3","apellido":"otra cosa3"},
        {"nombre":"cualquiera4","apellidos":"otra cosa4","numeros":"3325438191"}]

resmany = unacole.insert_many(vardic)
print(resmany.inserted_ids)