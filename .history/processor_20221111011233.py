import numpy as np
import pandas as pd

income=pd.read_csv("levels.csv")
cities=pd.read_csv("uscities.csv")

print(income.shape)
print(cities.columns)

income=income[(income.location!='') & (income.totalyearlycompensation!=0)]
print(income.shape)

countiesToAdd=[]
statesToAdd=[]
print(cities[cities.city.lower=="San Francisco"])
for location in income.location:
    cityName=location[:location.index(",")]
    if cityName in cities.city:
        state=cities[cities.city==cityName]
        statesToAdd.append()
        countiesToAdd.append("")
    else:
        statesToAdd.append("")
        countiesToAdd.append("")
income["city"]
