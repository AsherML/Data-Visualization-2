import numpy as np
import pandas as pd

income=pd.read_csv("levels.csv")
cities=pd.read_csv("uscities.csv")

print(income.shape)
print(cities.columns)

income=income[income.totalyearlycompensation!=0 & income.totalyearlycompensation!='']
print(income.shape)

countiesToAdd=[]
statesToAdd=[]
