import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

nombres = ["pistilo_len","pistilo_width","petalo_len","petalo_width","Clase"]
datos = pd.read_csv("iris_g.csv",names=nombres)

datos = datos.dropna()
array = datos.values

X = array[:,0:4]
y = array[:,4]

X_train, X_validation, Y_train, Y_validation = train_test_split(X,y,test_size=0.20,random_state=1000)

#clasificador = SVC(gamma="auto")
clasificador = KNeighborsClassifier() #la que corre el modelo
clasificador.fit(X_train, Y_train)# 80% Algo ADECUADO -- 85%, 90% ES VANIDAD

scores = cross_val_score(clasificador, X, y, cv=10)

print(scores.mean())