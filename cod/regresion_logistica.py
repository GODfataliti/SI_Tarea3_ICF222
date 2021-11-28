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
print(df.head())
X = df.iloc[:, 3:13].values
y = df.iloc[:, 13].values

#PARTE 1: TESTEO 25% Y ENTRENAMIENTO 75%
#random state numero random de la semilla entre 1 y 100
seed = random.randint(1,100)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=seed)
print(f'x entrenamiento: {X_train}')
print(f'x test: {X_test}')

print(f'y entrenamiento: {y_train}')
print(f'y test: {y_test}')

#PARTE 2: REGRESION LOGISTICA



