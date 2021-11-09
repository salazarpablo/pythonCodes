import pandas as pd
import numpy as np

def open_csv(file):
    df = pd.read_csv(file)
    x = df.x.to_numpy()
    y = df.y.to_numpy()
    return df,x,y

df,x,y=open_csv("prueba.csv")

print(df)
print(x)
print(y)

suma = x + y
resta = x - y
print(suma)
print(resta)