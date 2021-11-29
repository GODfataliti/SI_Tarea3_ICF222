# Dependencias
import numpy as np
import matplotlib as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split


def main():
    datos = pd.read_csv('Churn_Modelling.csv')
    #print(datos.head())
    X = datos.iloc[:, 3:13].values
    y = datos.iloc[:, 13].values
    #print(X)
    #print(y)
    #print(X.shape)


    le_geography = LabelEncoder()
    X[:, 1] = le_geography.fit_transform(X[:, 1])
    le_gender = LabelEncoder()
    X[:, 2] = le_gender.fit_transform(X[:, 2])
    X = X[:, 1:]
    print(X)
    print(X.shape)
    print(y.shape)




    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)




if __name__ == '__main__':
    main()

# Seleccionar un 75% de los datos para entrenamiento y 25% para prueba
# Separar los datos en conjunto de entrenamiento y conjunto de prueba
# Usar una regresión logística para predecir el valor de la variable de salida
# Calcular la precisión del modelo