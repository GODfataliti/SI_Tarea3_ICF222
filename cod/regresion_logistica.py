#Aplicando una regresion logistica a una base de datos de datos
# Dependencias
import numpy as np
import matplotlib as plt
import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('Churn_Modelling.csv')
#print(df.head())
X = df.iloc[:, 3:13].values
y = df.iloc[:, 13].values

le_geography = LabelEncoder()
X[:, 1] = le_geography.fit_transform(X[:, 1])
le_gender = LabelEncoder()
X[:, 2] = le_gender.fit_transform(X[:, 2])
X = X[:, 1:]

#PARTE 1: TESTEO 25% Y ENTRENAMIENTO 75%
#random state numero random de la semilla entre 1 y 100
seed = random.randint(1,100)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=seed)
def printtest(X_train, X_test, y_train, y_test):
    print(f'{X_train}')
    print(f'{X_test}')
    print(f'{y_train}')
    print(f'{y_test}')

#PARTE 2: REGRESION LOGISTICA
model = LogisticRegression()
model.fit(X_train, y_train)
def printRegresion(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    print(f'{model.score(X_test, y_test)}')

#printtest(X_train, X_test, y_train, y_test)
printRegresion(model, X_train, X_test, y_train, y_test)


