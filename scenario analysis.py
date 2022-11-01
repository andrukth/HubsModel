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

scenario3 = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario3.csv')
scenario3 = reshape_scenarios(scenario3)
scenario3_name = 'Scenario 3'

scenario4 = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario4.csv', sep=',')
scenario4 = reshape_scenarios(scenario4)
scenario4_name = 'Scenario 4'

#scenario5 = pd.read_csv('//ug.kth.se/dfs/home/a/n/andru/appdata/xp.V2/Documents/GitHub/HubsModel/scenario5.csv')
#scenario5 = reshape_scenarios(scenario5)
#scenario5_name = 'Scenario 5'

xlim_left=0
xlim_right=500

fig,ax=plt.subplots()
x = scenario1.index
ax.plot(x,scenario1['Hubs'],label=scenario1_name)
ax.plot(x,scenario2['Hubs'],label=scenario2_name)
ax.plot(x,scenario3['Hubs'],label=scenario3_name)
ax.plot(x,scenario4['Hubs'],label=scenario4_name)
#ax.plot(x,scenario5['Hubs'],label=scenario5_name)
#plt.xticks(range(0,1000,100))
plt.yticks(range(0,15,1))
plt.xlabel('Time')
plt.ylabel('Number of hubs')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=3)
plt.savefig('Number of hubs over time.eps', format='eps')
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = '- - Total utilized capacity\n'+u'\u2500'+'  Number of hubs'
ax.text(1.1, 0.05, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)
ax2=ax.twinx()
ax2.plot(x,scenario1['Total utilized capacity'],'--',label=scenario1_name)
ax2.plot(x,scenario2['Total utilized capacity'],'--',label=scenario2_name)
ax2.plot(x,scenario3['Total utilized capacity'],'--',label=scenario3_name)
ax2.plot(x,scenario4['Total utilized capacity'],'--',label=scenario4_name)
#ax2.plot(x,scenario5['Total utilized capacity'],'--',label=scenario5_name)
ax2.set_ylabel('Utilized hub capacity')
plt.xticks(range(0,500,100))
plt.xlim(xlim_left,xlim_right)
plt.title('Number of hubs and utilized capacity over time')
plt.savefig('Number of hubs and utilized capacity over time.eps', format='eps')
plt.show()

fig,ax=plt.subplots()
x = scenario1.index
plt.plot(x,scenario1['emissions'],label=scenario1_name)
plt.plot(x,scenario2['emissions'],label=scenario2_name)
plt.plot(x,scenario3['emissions'],label=scenario3_name)
plt.plot(x,scenario4['emissions'],label=scenario4_name)
#plt.plot(x,scenario5['emissions'],label=scenario5_name)
plt.xticks(range(0,1000,100))
#plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('CO2 emissions')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=3)
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = '- - Vehicle km\n'+u'\u2500'+'  Emissions'
ax.text(1.125, 0.05, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)
ax2=ax.twinx()
ax2.plot(x,scenario1['vehicle km'],'--',label=scenario1_name)
ax2.plot(x,scenario2['vehicle km'],'--',label=scenario2_name)
ax2.plot(x,scenario3['vehicle km'],'--',label=scenario3_name)
ax2.plot(x,scenario4['vehicle km'],'--',label=scenario4_name)
#ax2.plot(x,scenario5['vehicle km'],'--',label=scenario5_name)
ax2.set_ylabel('Vehicle km')
plt.xticks(range(0,1000,100))
plt.xlim(xlim_left,xlim_right)
plt.title('Emissions and vehicle km over time')
plt.savefig('Emissions and vehicle km over time.eps', format='eps')
plt.show()

fig,ax=plt.subplots()
x = scenario1.index
plt.plot(x,scenario1['Routing efficiency'],label=scenario1_name)
plt.plot(x,scenario2['Routing efficiency'],label=scenario2_name)
plt.plot(x,scenario3['Routing efficiency'],label=scenario3_name)
plt.plot(x,scenario4['Routing efficiency'],label=scenario4_name)
#plt.plot(x,scenario5['Routing efficiency'],label=scenario5_name)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=3)
plt.plot(x,scenario1['Fill rate'],'--',label=scenario1_name)
plt.plot(x,scenario2['Fill rate'],'--',label=scenario2_name)
plt.plot(x,scenario3['Fill rate'],'--',label=scenario3_name)
plt.plot(x,scenario4['Fill rate'],'--',label=scenario4_name)
#plt.plot(x,scenario5['Fill rate'],'--',label=scenario5_name)
plt.xticks(range(0,1000,100))
plt.xlim(xlim_left,xlim_right)
#plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('Efficiency')
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = '- - Fill rate\n'+u'\u2500'+'  Routing efficiency'
ax.text(1.01, 0.05, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)
plt.title('Efficiencies over time')
plt.savefig('Efficiencies over time.eps', format='eps')
plt.show()

fig,ax=plt.subplots()
x = scenario1.index
plt.plot(x,scenario1['share of demand that goes through the hub'],label=scenario1_name)
plt.plot(x,scenario2['share of demand that goes through the hub'],label=scenario2_name)
plt.plot(x,scenario3['share of demand that goes through the hub'],label=scenario3_name)
plt.plot(x,scenario4['share of demand that goes through the hub'],label=scenario4_name)
#plt.plot(x,scenario5['share of demand that goes through the hub'],label=scenario5_name)
plt.xticks(range(0,1000,100))
plt.xlim(xlim_left,xlim_right)
#plt.yticks(range(0,20,1))
plt.xlabel('Time')
plt.ylabel('Share')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=3)
plt.plot(x,scenario1['share of companies that use the hub'],'--', label=scenario1)
plt.plot(x,scenario2['share of companies that use the hub'],'--', label=scenario2)
plt.plot(x,scenario3['share of companies that use the hub'],'--', label=scenario3)
plt.plot(x,scenario4['share of companies that use the hub'],'--', label=scenario4)
#plt.plot(x,scenario5['share of companies that use the hub'],'--', label=scenario5)
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = '- - Companies\n'+u'\u2500'+'  Demand'
ax.text(1.01, 0.05, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)
plt.title('Share of demand that goes through the hub and\nshare of companies that use the hub over time')
plt.show()

fig,ax=plt.subplots()
x = scenario1.index
plt.plot(x,scenario1['monetary value'],label=scenario1_name)
plt.plot(x,scenario2['monetary value'],label=scenario2_name)
plt.plot(x,scenario3['monetary value'],label=scenario3_name)
plt.plot(x,scenario4['monetary value'],label=scenario4_name)
#plt.plot(x,scenario5['monetary value'],label=scenario5_name)
plt.xlabel('Time')
plt.ylabel('$ per company per time period')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=3)
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
textstr = '- - operation cost with hubs\n'+u'\u2500'+'  monetary value'
ax.text(1.125, 0.05, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)
ax2=ax.twinx()
ax2.plot(x,scenario1['operation cost with hubs'],'--')
ax2.plot(x,scenario2['operation cost with hubs'],'--')
ax2.plot(x,scenario3['operation cost with hubs'],'--')
ax2.plot(x,scenario4['operation cost with hubs'],'--')
#ax2.plot(x,scenario5['operation cost with hubs'],'--')
ax2.set_ylabel('$/Box')
plt.xticks(range(0,1000,100))
plt.xlim(xlim_left,xlim_right)
plt.title('Costs and values')
plt.savefig('Costs and values.eps', format='eps')
plt.show()



plt.savefig('Share of demand that goes through the hub over time.eps', format='eps')

