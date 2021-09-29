# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:18:49 2021

@author: andru
"""

import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns



def reshape_scenarios(scenario_name):
    scenario_name = scenario_name.fillna('Unknown')
    for i in range(scenario_name.shape[0]):
        if scenario_name.iloc[i,2] == 'Unknown':
            for j in range(2,scenario_name.shape[1]):
                scenario_name.iloc[i,j]=scenario_name.iloc[i,1]
    scenario_name = scenario_name.set_index('Time')
    scenario_name = scenario_name.transpose() 
    scenario_name = scenario_name.apply(pd.to_numeric)
    for col in scenario_name.columns:
        if col.isupper()==True:
            del scenario_name[col]

    return scenario_name

base_scenario = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/base scenario.csv')
base_scenario = reshape_scenarios(base_scenario)
base_scenario_name = 'Base Scenario'

scenario_1 = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario 1.csv')
scenario_1 = reshape_scenarios(scenario_1)
scenario_1_name = 'Scenario 1'

scenario_2 = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario 2.csv')
scenario_2 = reshape_scenarios(scenario_2)
scenario_2_name = 'Scenario 2'


fig,ax=plt.subplots()
x = base_scenario.index
ax.plot(x,base_scenario['Hubs'],label=base_scenario_name)
ax.plot(x,scenario_1['Hubs'],label=scenario_1_name)
ax.plot(x,scenario_2['Hubs'],label=scenario_2_name)
#plt.xticks(range(0,1000,100))
plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('Number of hubs')
plt.legend(bbox_to_anchor=(1.1, 1.05))
#plt.savefig('Number of hubs over time.eps', format='eps')
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = '- - Total utilized capacity\n'+u'\u2500'+'  Number of hubs'
ax.text(1.1, 0.05, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)
ax2=ax.twinx()
ax2.plot(x,base_scenario['Total utilized capacity'],'--',label=base_scenario_name)
ax2.plot(x,scenario_1['Total utilized capacity'],'--',label=scenario_1_name)
ax2.plot(x,scenario_2['Total utilized capacity'],'--',label=scenario_2_name)
ax2.set_ylabel('Utilized hub capacity')
plt.xticks(range(0,1000,100))
plt.title('Number of hubs and total utilized capacity over time')

plt.show()


x = base_scenario.index
plt.plot(x,base_scenario['emissions'],label=base_scenario_name)
plt.plot(x,scenario_1['emissions'],label=scenario_1_name)
plt.plot(x,scenario_2['emissions'],label=scenario_2_name)
plt.xticks(range(0,1000,100))
#plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('CO2 emissions')
plt.legend()
plt.title('Emissions over time')
#plt.savefig('Emissions over time.eps', format='eps')
plt.show()


x = base_scenario.index
plt.plot(x,base_scenario['Routing and consolidation efficiency'],label=base_scenario_name)
plt.plot(x,scenario_1['Routing and consolidation efficiency'],label=scenario_1_name)
plt.plot(x,scenario_2['Routing and consolidation efficiency'],label=scenario_2_name)
plt.xticks(range(0,1000,100))
#plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('Efficiency')
plt.legend()
plt.title('Routing and consolidation efficiency over time')
#plt.savefig('Routing and consolidation efficiency over time.eps', format='eps')
plt.show()


x = base_scenario.index
plt.plot(x,base_scenario['share of demand that goes through the hub'],label=base_scenario_name)
plt.plot(x,scenario_1['share of demand that goes through the hub'],label=scenario_1_name)
plt.plot(x,scenario_2['share of demand that goes through the hub'],label=scenario_2_name)
plt.xticks(range(0,1000,100))
#plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('Share of demand')
plt.legend()
plt.title('Share of demand that goes through the hub over time')
#plt.savefig('Share of demand that goes through the hub over time.eps', format='eps')
plt.show()
