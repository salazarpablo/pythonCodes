from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import statsmodels.api as sm


datos = load_boston()
#print(datos)
#print(datos["DESCR"])
#print(datos["data"][0])

modelo = LinearRegression()

X = datos["data"]
Y = datos["target"]

modelo.fit(X,Y)

X =sm.add_constant(X)
modelo2 = sm.OLS(Y,X).fit()
print(modelo2.summary())

#print(modelo.predict([X[10]]))
#print(Y[10])

#print(modelo.coef_[0])
#print(modelo.coef_)
#print(modelo.intercept_)

#predecir = modelo.predict(X)
#mederror = mean_squared_error(Y,predecir)
#rmederror = np.sqrt(mederror)
#print(mederror)
#print(rmederror)