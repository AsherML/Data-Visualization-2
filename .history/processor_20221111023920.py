import numpy as np
import pandas as pd

income=pd.read_csv("levels.csv")
cities=pd.read_csv("uscities.csv")

print(income.shape)
print(cities.columns)

income=income[(income.location!='') & (income.totalyearlycompensation!=0)]
cities=cities[cities['county_name']!]

toDf={'county':[], "state":[], "numDevelopers":[], "averageSalary":[]}
countiesToAdd=[]
statesToAdd=[]
count=0
for location in income.location:
    cityName=location[:location.index(",")]
    if cityName in cities.city_ascii.values:
        count+=1
        cityRow=cities[cities.city==cityName]
        try:
            county=cityRow['county_name'].values[0]
            state=cityRow['state_name'].values[0]
            if(count%100==0):
                print(count)
            if county in toDf['county']:
                ind=toDf['county'].index(county)
                toDf['numDevelopers'][ind]+=1
            else:
                toDf['county'].append(county)
                toDf['state'].append(state)
                toDf['numDevelopers'].append(1)
        except:
            print(cityRow)
            
# print(count)
# income['state']=statesToAdd
# income["counties"]=countiesToAdd
# print(income.shape)
# income=income[(income['state']!='')&(income['counties']!='')]
# print(income.shape)
df=pd.DataFrame(toDf)
df.to_csv("countyDevCounts")


