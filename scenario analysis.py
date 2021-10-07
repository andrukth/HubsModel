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
    #uncomment lines below to remove exogenous constants
    #for col in scenario_name.columns:
     #   if col.isupper()==True:
      #      del scenario_name[col]

    return scenario_name

scenario1 = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario1.csv')
scenario1 = reshape_scenarios(scenario1)
scenario1_name = 'Scenario 1'

scenario2 = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario2.csv')
scenario2 = reshape_scenarios(scenario2)
scenario2_name = 'Scenario 2'

scenario2b = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario2b.csv')
scenario2b = reshape_scenarios(scenario2b)
scenario2b_name = 'Scenario 2b'

scenario3 = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario3.csv')
scenario3 = reshape_scenarios(scenario3)
scenario3_name = 'Scenario 3'

scenario4 = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario4.csv', sep=',')
scenario4 = reshape_scenarios(scenario4)
scenario4_name = 'Scenario 4'


fig,ax=plt.subplots()
x = scenario1.index
ax.plot(x,scenario1['Hubs'],label=scenario1_name)
ax.plot(x,scenario2['Hubs'],label=scenario2_name)
ax.plot(x,scenario2b['Hubs'],label=scenario2b_name)
ax.plot(x,scenario3['Hubs'],label=scenario3_name)
ax.plot(x,scenario4['Hubs'],label=scenario4_name)
#plt.xticks(range(0,1000,100))
plt.yticks(range(0,15,1))
plt.xlabel('Time')
plt.ylabel('Number of hubs')
plt.legend(bbox_to_anchor=(1.1, 1.05))
#plt.savefig('Number of hubs over time.eps', format='eps')
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = '- - Total utilized capacity\n'+u'\u2500'+'  Number of hubs'
ax.text(1.1, 0.05, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)
ax2=ax.twinx()
ax2.plot(x,scenario1['Total utilized capacity'],'--',label=scenario1_name)
ax2.plot(x,scenario2['Total utilized capacity'],'--',label=scenario2_name)
ax2.plot(x,scenario2b['Total utilized capacity'],'--',label=scenario2b_name)
ax2.plot(x,scenario3['Total utilized capacity'],'--',label=scenario3_name)
ax2.plot(x,scenario4['Total utilized capacity'],'--',label=scenario4_name)
ax2.set_ylabel('Utilized hub capacity')
plt.xticks(range(0,1000,100))
plt.title('Number of hubs and utilized capacity over time')
plt.show()

fig,ax=plt.subplots()
x = scenario1.index
plt.plot(x,scenario1['emissions'],label=scenario1_name)
plt.plot(x,scenario2['emissions'],label=scenario2_name)
plt.plot(x,scenario2b['emissions'],label=scenario2b_name)
plt.plot(x,scenario3['emissions'],label=scenario3_name)
plt.plot(x,scenario4['emissions'],label=scenario4_name)
plt.xticks(range(0,1000,100))
#plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('CO2 emissions')
plt.legend(bbox_to_anchor=(1.4, 1.05))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = '- - Vehicle km\n'+u'\u2500'+'  Emissions'
ax.text(1.125, 0.05, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)
ax2=ax.twinx()
ax2.plot(x,scenario1['vehicle km'],'--',label=scenario1_name)
ax2.plot(x,scenario2['vehicle km'],'--',label=scenario2_name)
ax2.plot(x,scenario2b['vehicle km'],'--',label=scenario2b_name)
ax2.plot(x,scenario3['vehicle km'],'--',label=scenario3_name)
ax2.plot(x,scenario4['vehicle km'],'--',label=scenario4_name)
ax2.set_ylabel('Vehicle km')
plt.xticks(range(0,1000,100))
plt.title('Emissions and vehicle km over time')
#plt.savefig('Emissions over time.eps', format='eps')
plt.show()


x = scenario1.index
plt.plot(x,scenario1['Routing efficiency'],label=scenario1_name)
plt.plot(x,scenario2['Routing efficiency'],label=scenario2_name)
plt.plot(x,scenario2b['Routing efficiency'],label=scenario2b_name)
plt.plot(x,scenario3['Routing efficiency'],label=scenario3_name)
plt.plot(x,scenario4['Routing efficiency'],label=scenario4_name)
plt.xticks(range(0,1000,100))
#plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('Efficiency')
plt.legend()
plt.title('Routing efficiency over time')
#plt.savefig('Routing and consolidation efficiency over time.eps', format='eps')
plt.show()


x = scenario1.index
plt.plot(x,scenario1['share of demand that goes through the hub'],label=scenario1_name)
plt.plot(x,scenario2['share of demand that goes through the hub'],label=scenario2_name)
plt.plot(x,scenario2b['share of demand that goes through the hub'],label=scenario2b_name)
plt.plot(x,scenario3['share of demand that goes through the hub'],label=scenario3_name)
plt.plot(x,scenario4['share of demand that goes through the hub'],label=scenario4_name)
plt.xticks(range(0,1000,100))
#plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('Share of demand')
plt.legend()
plt.title('Share of demand that goes through the hub over time')
#plt.savefig('Share of demand that goes through the hub over time.eps', format='eps')
plt.show()
