# Dependencias
import numpy as np
import matplotlib as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def sktest():
    le_geography = LabelEncoder()
    X[:, 1] = le_geography.fit_transform(X[:, 1])
    le_gender = LabelEncoder()
    X[:, 2] = le_gender.fit_transform(X[:, 2])
    ohe = OneHotEncoder(categorical_features=[1])
    X = ohe.fit_transform(X).toarray()
    # evitar trampa de variable irrrelevante ;)
    X = X[:, 1:]
    print(X)
    print(X.shape)
    y.shape

def main():
    
    datos = pd.read_csv('Churn_Modelling.csv')
    #print(datos.head())
    X = datos.iloc[:, 3:13].values
    y = datos.iloc[:, 13].values
    print(X)
    print(y)
    print(X.shape)
    sktest()


if __name__ == '__main__':
    main()

# Seleccionar un 75% de los datos para entrenamiento y 25% para prueba
# Separar los datos en conjunto de entrenamiento y conjunto de prueba
# Usar una regresión logística para predecir el valor de la variable de salida
# Calcular la precisión del modelo