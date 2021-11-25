from matplotlib import pyplot
from numpy.core.records import array
import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier


class Exploracion():#recibe un dataframe

    def __init__(self,datos):
        self.datos = datos

    def shape_f(self):
        return self.datos.shape

    def describe_f(self):
        return self.datos.describe()

    def group_f(self,ncolu):
        return self.datos.groupby(ncolu).size()

    def graficas(self,tipo):
        def hist_f(self):
            return self.datos.hist()

        def scatter_f(self):
            return scatter_matrix(self.datos)
           
        if tipo == "h":
            hist_f(self)
        elif tipo == "s":
            scatter_f(self)

        return pyplot.show()

nombres = ["pistilo_len","pistilo_width","petalo_len","petalo_width","Clase"]
datos = pd.read_csv("iris_g.csv",names=nombres) #Carga de DATOS
datos = datos.dropna()
array = datos.values

X = array[:,0:4]
y = array[:,4]

X_train, X_validation, Y_train, Y_validation = train_test_split(X,y,test_size=0.30,random_state=50) #Set de validacion y entrenamiento

nueva_exploracion = Exploracion(datos)
#nueva_exploracion.graficas("s")
#print(nueva_exploracion.describe_f())
model3 = LogisticRegression(solver = "liblinear", multi_class="ovr")
model2 = KNeighborsClassifier()# Mandar llamar al modelo
model = SVC(gamma="auto")
model.fit(X_train, Y_train)# Mandar el set de entrenamiento
predictions = model.predict(X_validation)

#obtener métricas, tienen que mandar el set de validación
print(accuracy_score(Y_validation,predictions))
#print(confusion_matrix(Y_validation,predictions))
print(classification_report(Y_validation,predictions))


