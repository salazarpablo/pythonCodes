import pandas as pd
import json

class OpenFormats:
#Todas las funciones reciben un String con el Path ó nombre del Archivo
    def csvOpen(self,f):
        #Regresa como DFrame
        data=""
        try:
            #data = pd.read_csv("csvs/TSLA1.csv")
            data = pd.read_csv(f)
            print(data.head())
            print(data.describe())
        except:
            print("Algo Fallo en csvOpen")
        return data

    def jsonOpen(self,f,op=2):
        data= ""
        #opcion 1: regresa como DFrame
        if op == 1:
            try:
                data = pd.read_json(f)
                #data = json.load(f)
                print(data)
            except:
                print("Algo Fallo en jsonOpen")
        #opcion 2: regresa como Dict        
        elif op == 2:
            try:
                #data = ""
                with open(f) as jsonFile:
                    data = json.load(jsonFile)
                    #datan = pd.json_normalize(data["clients"])
                    #data = pd to_dict()
                #print(f)
                print(data)
            except:
                print("Algo Fallo en jsonOpen")
        else:
            print("opcion no válida")
        return data 

    
    def txtOpen(self,f):
        #Regresa Lista de Líneas separadas por el salto de línea
        data=""
        try:
            with open(f) as file:
                data = file.readlines()
            print(data)
        except:
            print("Algo Fallo en txtOpen ")
        return data    