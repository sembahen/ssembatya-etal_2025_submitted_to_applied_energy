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
import seaborn as sns
#%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = "arial"
matplotlib.rcParams.update({'font.size': 25})


colorname=dict({"summer":"red", 
                "fall": "darkred",
                "winter": "blue",
                "spring": "cyan"})


years=[2000, 2001, 2002 , 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]



delta1_seas_results=pd.DataFrame()
delta2perfect_seas_results=pd.DataFrame()



for year in years:
    
    #season of occurence
    season_all=pd.read_csv("season_CISO_2000_2019.csv")
    
    
    #IMPORT GO1 Perfect, GO1 Persistence, GO2 Perfect
    #GO1 perfect LMPs
    dflmps_go1perfect=pd.read_csv("***/duals__"+ str(year)+ ".csv")
    #GO1 persistence LMPs
    dflmps_go1persist=pd.read_csv("***/duals.csv".format(year))
    #GO2 perfect LMPs
    dflmps_go2perfect=pd.read_csv("***/duals.csv".format(str(year)))
    
    #GROUP THE DATAFRAMES BY BUS NAME    
    #GO1 perfect (sorted)
    dflmps_bus_go1perfect=dflmps_go1perfect.pivot(index="Time", columns="Bus", values="Value")
    #GO1 persistence (sorted)
    dflmps_bus_go1persist=dflmps_go1persist.pivot(index="Time", columns="Bus", values="Value")
    #GO2 perfect (sorted)
    dflmps_bus_go2perfect=dflmps_go2perfect.pivot(index="Time", columns="Bus", values="Value")    
    
    
    
    #delta1 = GO1perfect - GO1persistence
    delta1=(dflmps_bus_go1perfect-dflmps_bus_go1persist).reset_index(drop=True)
    #delta2perfect = GO1perfect -GO2 perfect
    delta2perfect=(dflmps_bus_go1perfect-dflmps_bus_go2perfect).reset_index(drop=True)
    
#...................................................................................................    
    #DELTA1 BREAKING DOWN BY SEASON (BASED ON INDICES FROM YEAR 2000)
    #create empty dataframes of delta1 and enter seasonal slices of the yearly data
    delta1_winter_yr = pd.DataFrame()
    delta1_spring_yr = pd.DataFrame()    
    delta1_summer_yr = pd.DataFrame()
    delta1_fall_yr = pd.DataFrame()    

    delta1_winter_yr=pd.concat([delta1.iloc[0:1440],delta1.iloc[8040:]])
    delta1_spring_yr=delta1.iloc[1440:3648]
    delta1_summer_yr=delta1.iloc[3648:5856]
    delta1_fall_yr=delta1.iloc[5856:8040]
    
    #find the standard deviation of prices at every bus
    stdev_delta1_winter_yr=delta1_winter_yr.std(axis=0).to_frame().reset_index() 
    stdev_delta1_spring_yr=delta1_spring_yr.std(axis=0).to_frame().reset_index() 
    stdev_delta1_summer_yr=delta1_summer_yr.std(axis=0).to_frame().reset_index() 
    stdev_delta1_fall_yr=delta1_fall_yr.std(axis=0).to_frame().reset_index() 
    
    #find the average of the 100 standard deviation values 
    delta1_winter_yr_std_avg=stdev_delta1_winter_yr[0].mean()
    delta1_spring_yr_std_avg=stdev_delta1_spring_yr[0].mean()
    delta1_summer_yr_std_avg=stdev_delta1_summer_yr[0].mean()
    delta1_fall_yr_std_avg=stdev_delta1_fall_yr[0].mean()
    
    delta1_seas_yr_avg=pd.DataFrame({
                                "Year": [year]*4,
                                "Season":["winter","spring","summer","fall"],
                                "Value": [delta1_winter_yr_std_avg, delta1_spring_yr_std_avg, delta1_summer_yr_std_avg, delta1_fall_yr_std_avg]
                               })

    delta1_seas_results=pd.concat([delta1_seas_results, delta1_seas_yr_avg])
    
    
#...................................................................................................      
    #create empty dataframes of delta2perfect and enter seasonal slices of the yearly data
    delta2perfect_winter_yr = pd.DataFrame()
    delta2perfect_spring_yr = pd.DataFrame()    
    delta2perfect_summer_yr = pd.DataFrame()
    delta2perfect_fall_yr = pd.DataFrame() 
    
    delta2perfect_winter_yr=pd.concat([delta2perfect.iloc[0:1440],delta2perfect.iloc[8040:]])
    delta2perfect_spring_yr=delta2perfect.iloc[1440:3648]
    delta2perfect_summer_yr=delta2perfect.iloc[3648:5856]
    delta2perfect_fall_yr=delta2perfect.iloc[5856:8040]    

    #find the standard deviation of prices at every bus
    stdev_delta2perfect_winter_yr=delta2perfect_winter_yr.std(axis=0).to_frame().reset_index() 
    stdev_delta2perfect_spring_yr=delta2perfect_spring_yr.std(axis=0).to_frame().reset_index() 
    stdev_delta2perfect_summer_yr=delta2perfect_summer_yr.std(axis=0).to_frame().reset_index() 
    stdev_delta2perfect_fall_yr=delta2perfect_fall_yr.std(axis=0).to_frame().reset_index() 

    #find the average of the 100 standard deviation values 
    delta2perfect_winter_yr_std_avg=stdev_delta2perfect_winter_yr[0].mean()
    delta2perfect_spring_yr_std_avg=stdev_delta2perfect_spring_yr[0].mean()
    delta2perfect_summer_yr_std_avg=stdev_delta2perfect_summer_yr[0].mean()
    delta2perfect_fall_yr_std_avg=stdev_delta2perfect_fall_yr[0].mean()
    
    delta2perfect_seas_yr_avg=pd.DataFrame({
                                "Year": [year]*4,
                                "Season":["winter","spring","summer","fall"],
                                "Value": [delta2perfect_winter_yr_std_avg, delta2perfect_spring_yr_std_avg, delta2perfect_summer_yr_std_avg, delta2perfect_fall_yr_std_avg]
                               }) 
    
    delta2perfect_seas_results=pd.concat([delta2perfect_seas_results, delta2perfect_seas_yr_avg])
    
    
    
#PLOTTING DELTA1 AND DELTA2 PERFECT
plt.figure(figsize=(30,13))
#delta1
#sns.set(style="whitegrid", font_scale=2.5)
matplotlib.rcParams.update({'font.size': 30})

sns.scatterplot(data = delta1_seas_results, x = "Year", y = "Value", hue = "Season", s=200, palette=colorname) 
sns.lineplot(data = delta1_seas_results, x = "Year", y = "Value", hue = "Season", palette=colorname, linestyle='--',legend=False) 

#delta2perfect
#sns.set(style="whitegrid", font_scale=2.5)
sns.scatterplot(data = delta2perfect_seas_results, x = "Year", y = "Value", hue = "Season", s=200, palette=colorname, legend=False) 
sns.lineplot(data = delta2perfect_seas_results, x = "Year", y = "Value", hue = "Season", palette=colorname, legend=False) 


#Custom legend
skill1, = plt.plot( np.NaN, np.NaN, color='black', linestyle = '--', label= r'$ε_{flow}$', markersize=25, )
skill2, = plt.plot( np.NaN, np.NaN, color='black', linestyle = 'solid', label=r'$ε_{scheduling}$' , markersize=25)
legend_seas_1, = plt.plot( np.NaN, np.NaN, marker="o", color='cyan', linestyle = 'None', label='spring', markersize=13)
legend_seas_2, = plt.plot( np.NaN, np.NaN, marker="o", color='red', linestyle = 'None', label='summer', markersize=13 )
legend_seas_3, = plt.plot( np.NaN, np.NaN, marker="o", color='darkred', linestyle = 'None', label='fall', markersize=13 )
legend_seas_4, = plt.plot( np.NaN, np.NaN, marker="o", color='blue', linestyle = 'None', label='winter', markersize=13 )

# You can adjust the parameters below according to your needs <3
plt.legend(handles=[skill1, skill2, legend_seas_1, legend_seas_2, legend_seas_3, legend_seas_4],
           loc='upper left',columnspacing=.89, handlelength=1, handletextpad=.2, ncol=5, frameon=True, bbox_to_anchor=(0.2, 1), fontsize=35)


plt.xticks(years)


plt.ylabel("Standard Dev of LMP Forecast Errors, $/MWh", fontsize=30) 
plt.tight_layout() 
plt.savefig("seasonaldelta_std_avg_manuscript.jpg",dpi=400 ,bbox_inches ="tight")











