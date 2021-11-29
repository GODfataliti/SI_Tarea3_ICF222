# Dependencias
import numpy as np
import matplotlib as plt
import pandas as pd
import random
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def main():
    df = pd.read_csv('Churn_Modelling.csv')
    #print(df.head())
    X = df.iloc[:, 3:13].values
    y = df.iloc[:, 13].values

    #Eliminacion de datos no numericos
    le_geography = LabelEncoder()
    X[:, 1] = le_geography.fit_transform(X[:, 1])
    le_gender = LabelEncoder()
    X[:, 2] = le_gender.fit_transform(X[:, 2])
    X = X[:, 1:]

    #random state numero random de la semilla entre 1 y 100
    seed = random.randint(1,100)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=seed)

    print(X_train.shape)
    print(X_test.shape)

    sc = StandardScaler()
    X_test = sc.fit_transform(X_test)
    #print(X_test,end="\n\n")
    #print(X_train)




    #Creacion del modelo
    model = LogisticRegression(random_state=0)
    model.fit(X_train, y_train)
    model.score(X_test, y_test)







    #Capa oculta
    classifier = Sequential()
    #capa oculta
    classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu', input_dim=9))

    #capa oculta
    #classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu'))

    #capa oculta
    #classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu'))

    classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))

    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    classifier.fit(X_train, y_train, epochs=100, batch_size=10)
    
    # y_pred = classifier.predict(X_test)
    # y_pred = (y_pred > 0.5)
    # print(y_pred)

    # #Evaluacion del modelo
    # from sklearn.metrics import confusion_matrix
    # cm = confusion_matrix(y_test, y_pred)
    # print(cm)


if __name__ == '__main__':
    main()

# Seleccionar un 75% de los datos para entrenamiento y 25% para prueba
# Separar los datos en conjunto de entrenamiento y conjunto de prueba
# Usar una regresión logística para predecir el valor de la variable de salida
# Calcular la precisión del modelo