# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:18:49 2021

@author: andru
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_scenario = pd.read_csv('C:/Users/andru/Downloads/base scenario.csv')

base_scenario = base_scenario.fillna('Unknown')


for i in range(base_scenario.shape[0]):
    if base_scenario.iloc[i,2] == 'Unknown':
        for j in range(2,base_scenario.shape[1]):
            base_scenario.iloc[i,j]=base_scenario.iloc[i,1]

base_scenario = base_scenario.set_index('Time')
base_scenario = base_scenario.transpose()

base_scenario = base_scenario.apply(pd.to_numeric)

for i in range(base_scenario.shape[1]):
    

plt.figure()
sns.lineplot(data=base_scenario)
plt.show()