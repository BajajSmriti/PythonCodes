# -*- coding: utf-8 -*-


print("hello")

import pandas as pd
data=pd.read_csv('Data.csv',sep=',',na_values=".")
print(data)
print(data.shape)
#nominal
print(data["sex"])
#ordinal
group=data.groupby('sex')
#print(group)
#interval
for sex,value in group['age']:
    print(sex,value.mean())