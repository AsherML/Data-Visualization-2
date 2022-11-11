import numpy as np
import pandas as pd

income=pd.read_csv("levels.csv")
cities=pd.read_csv("uscities.csv")

print(income.shape)
print(cities.columns)

income=income[(income.location!='') & (income.totalyearlycompensation!=0)]


countiesToAdd=[]
statesToAdd=[]
count=0
for location in income.location:
    cityName=location[:location.index(",")]
    if cityName in cities.city:
        print('hi')
        cityRow=cities[cities.city==cityName]
        statesToAdd.append(cityRow['state_name'])
        countiesToAdd.append(cityRow["county_name"])
    else:
        statesToAdd.append("")
        countiesToAdd.append("")
income['state']=statesToAdd
income["counties"]=countiesToAdd
print(income.shape)
income=income[(income['state']!='')&(income['counties']!='')]
print(income.shape)
