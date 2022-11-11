import numpy as np
import pandas as pd

income=pd.read_csv("levels.csv")
cities=pd.read_csv("uscities.csv")

print(income.shape)
print(cities.columns)

income=income[(income.location!='') & (income.totalyearlycompensation!=0)]
print(cities.shape)
cities=cities[(cities['county_name']!="")& (cities['state_name']!='')]
print(cities.shape)

toDf={'county':[], "state":[], "numDevelopers":[]}
countiesToAdd=[]
statesToAdd=[]
count=0
for location in income.location:
    cityName=location[:location.index(",")]
    if cityName in cities.city_ascii.values:
        count+=1
        cityRow=cities[cities.city_ascii==cityName]
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
            print(count)
            
# print(count)
# income['state']=statesToAdd
# income["counties"]=countiesToAdd
# print(income.shape)
# income=income[(income['state']!='')&(income['counties']!='')]
# print(income.shape)
numStates=len(toDf['state'])
for s in toDf['state']:
    if s in toDf['county']:
        ind=toDf['county'].index(s)
        toDf['numDevelopers'][ind]+=
df=pd.DataFrame(toDf)
df.to_csv("countyDevCounts.csv")


