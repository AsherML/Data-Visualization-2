import numpy as np
import pandas as pd

income=pd.read_csv("levels.csv")
cities=pd.read_csv("uscities.csv")

print(income.shape)
print(cities.columns)

income=income[(income.location!='') & (income.totalyearlycompensation!=0)]


countiesToAdd=[]
statesToAdd=[]
print(income.location[])
# for location in income.location:
#     cityName=location[:location.index(",")+1]
#     if cityName in cities.city:
#         count+=1
#         cityRow=cities[cities.city==cityName]
#         statesToAdd.append(cityRow['state_name'])
#         countiesToAdd.append(cityRow["county_name"])
#     else:
#         statesToAdd.append("")
#         countiesToAdd.append("")
# print(count)
# income['state']=statesToAdd
# income["counties"]=countiesToAdd
# print(income.shape)
# income=income[(income['state']!='')&(income['counties']!='')]
# print(income.shape)
