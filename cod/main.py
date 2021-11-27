# Dependencias
import numpy as np
import matplotlib as plt
import pandas as pd


def main():
    
    datos = pd.read_csv('Churn_Modelling.csv')
    print(datos)


if __name__ == '__main__':
    main()
