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
print(income.location[0])
print("Redwood City" in cities.city_ascii.values)
for location in income.location:
    cityName=location[:location.index(",")]
    print(cityName)
    if cityName in cities.city_ascii.values:
        count+=1
        
        cityRow=cities[cities.city==cityName]
        statesToAdd.append(cityRow['state_name'])
        countiesToAdd.append(cityRow["county_name"])
    else:
        statesToAdd.append("")
        countiesToAdd.append("")
print(count)
income['state']=statesToAdd
income["counties"]=countiesToAdd
print(income.shape)
income=income[(income['state']!='')&(income['counties']!='')]
print(income.shape)
df=pd.Dataframe()
income.to_csv("finalIncome", columns=["totalyearlycompensation", "state", "county" ])
