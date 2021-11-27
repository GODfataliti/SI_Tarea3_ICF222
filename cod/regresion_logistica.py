#Aplicando una regresion logistica a una base de datos de datos
# Dependencias
import numpy as np
import matplotlib as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split


le = LabelEncoder()
le.fit(['France', 'Tokyo', 'Germany', 'Sweden'])
print(le.classes_)
le.transform(['Tokyo', 'Tokyo', 'Germany', 'Sweden'])




