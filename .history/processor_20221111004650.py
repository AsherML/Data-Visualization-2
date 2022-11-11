import numpy as np
import pandas as pd

income=pd.read_csv("levels.csv")
cities=pd.read_csv("uscities.csv")

print(income.columns)
print(cities.columns)

income=income[location!='' ]

countiesToAdd=[]
statesToAdd=[]
