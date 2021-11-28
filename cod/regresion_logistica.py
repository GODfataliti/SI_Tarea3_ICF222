#Aplicando una regresion logistica a una base de datos de datos
# Dependencias
import numpy as np
import matplotlib as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv('Churn_Modelling.csv')
print(df.head())
X = df.iloc[:, 3:13].values
y = df.iloc[:, 13].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
print(f'x entrenamiento: {X_train}')
print(f'x test: {X_test}')

print(f'y entrenamiento: {y_train}')
print(f'y test: {y_test}')



