# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 19:37:05 2023

@author: hssemba
"""

import numpy as np
import pandas as pd
import os
from shutil import copy
from pathlib import Path
import math
#%matplotlib inline
from statistics import mean 

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = "arial"
matplotlib.rcParams.update({'font.size': 25})


forecasts=["perfect", "persistent"]


years=[2000, 2001, 2002 , 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]


delta1_allrevenue=[]
delta2perfect_allrevenue=[]

for year in years:
    #GO1 perfect
    dflmps_go1perfect=pd.read_csv("xxx/duals__"+ str(year)+ ".csv")
    #GO1 perfect (sorted)
    dflmps_bus_go1perfect=dflmps_go1perfect.pivot(index="Time", columns="Bus", values="Value")

    #hydro generation GO2perferct
    go2pefect_hydro=pd.read_csv("xxx/Exp{}_100_simple_2000_0/nodal_hydro.csv".format(year))

    

    #GO2 perfect
    dflmps_go2perfect=pd.read_csv("xxx/Exp{}_100_simple_2000_0/duals.csv".format(year))
    #GO2 perfect (sorted)
    dflmps_bus_go2perfect=dflmps_go2perfect.pivot(index="Time", columns="Bus", values="Value")
    #delta2perfect = GO1 perfect -GO2 perfect
    delta2perfect=dflmps_bus_go1perfect-dflmps_bus_go2perfect
    #reset index for delta2perfect to make it match the go2perdect hyfro
    delta2perfect=delta2perfect.reset_index(drop=True)

    #revenue
    delta2perfect_revenues=delta2perfect*go2pefect_hydro
    delta2perfect_totalrevenues=delta2perfect_revenues.sum().sum()
    delta2perfect_allrevenue.append(delta2perfect_totalrevenues)
    
    



#PLOTTING IN FLIPPED FORM SUCH THAT POSITIVE MEANS THAT DP REVENUES INCREASED AND 
#NEGATIVE MEANS DP REVENUES REDUCED
negative_delta2perfect_allrevenue=[-1 * x for x in delta2perfect_allrevenue]
df_negative_delta2perfect_allrevenue=pd.DataFrame()
df_negative_delta2perfect_allrevenue["Values"]=negative_delta2perfect_allrevenue
df_negative_delta2perfect_allrevenue.to_csv("df_negative_delta2perfect_allrevenue.csv", index=None)
mean_negative_delta2perfect_allrevenue=mean(negative_delta2perfect_allrevenue)


matplotlib.rcParams.update({'font.size': 20})
fig, ax = plt.subplots(figsize=(20,10))
ax.grid()
ax.scatter(years, negative_delta2perfect_allrevenue,color="green")
ax.plot(years, negative_delta2perfect_allrevenue,color="green")
ax.axhline(y=mean_negative_delta2perfect_allrevenue, color='orange', linestyle='-')

ax.text(0.75, 0.45, 'Average Cost of Error',
        verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes,
        color='orange', fontsize=25)
plt.title("Differences in Revenue Across Years",fontweight="bold")
# Set x-axis ticks as integers
plt.xticks(range(min(years), max(years)+1),fontsize=15)
#plt.legend()
plt.ylabel("Difference in revenue,$")
plt.xlabel("Years")
plt.savefig("Revenue_Difference_new",dpi=600 ,bbox_inches ="tight")
    
    
