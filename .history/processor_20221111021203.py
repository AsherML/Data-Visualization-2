import numpy as np
import pandas as pd

income=pd.read_csv("levels.csv")
cities=pd.read_csv("uscities.csv")

print(income.shape)
print(cities.columns)

income=income[(income.location!='') & (income.totalyearlycompensation!=0)]

toDf={'county':[], "state":[], "numDevelopers":[]}
countiesToAdd=[]
statesToAdd=[]
count=0
for location in income.location:
    cityName=location[:location.index(",")]
    if cityName in cities.city_ascii.values:
        count+=1
        county=cityRow['county_name']
        state=cityRow['state_name']
        if county in toDf['county']:
            ind=toDf['county'].index(county)
            if ind>=len(toDf['numDevelopers']){
                
            }
        
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


