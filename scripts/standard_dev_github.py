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

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = "arial"
matplotlib.rcParams.update({'font.size': 25})
gos=["GO1"]
#gos=["GO1", "GO2"]

forecasts=["perfect"]#, "persistent"]

#years=[2000]
years=[2000, 2001, 2002 , 2003, 2004, 2005, 2006, 2007, 2008, 2009,
      2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

#lmp_prices=[]
#nodes=[]
sd_delta1_allyears=[]
#standard deviation saved
sd_delta2perfect_allyears=[]

sd_yr=pd.DataFrame()
for year in years:
    
    delta1=pd.read_csv("../delta1/delta1_"+ str(year)+ ".csv")
    del delta1["Time"]
    delta2perfect=pd.read_csv("../delta2perfect/delta2perfect_"+ str(year)+ ".csv")
    del delta2perfect["Time"]
    
    #standard deviation of each node
    #std Delta1
    sd_delta1=delta1.std()
    #save std_delta1 to list 
    sd_delta1_allyears.append(list(sd_delta1))
    
    #std Delta2Perfect
    sd_delta2perfect=delta2perfect.std()
    #save std_delta1 to list 
    sd_delta2perfect_allyears.append(list(sd_delta2perfect))
    
    #std Delta1/ Std Delta2Perfect
    sdd1_div_sdd2perf=sd_delta1/sd_delta2perfect
    #std Delta2Perfect/ Std Delta1 per node
    sdd2perf_div_sdd1=sd_delta2perfect/sd_delta1
    
    
    # #plotting stdev d2 perf divide by sdd1
    # x_nodes=list(sdd2perf_div_sdd1.index)
    # y=sdd2perf_div_sdd1.tolist()
    # fig = plt.figure(figsize=(20,10))
    # plt.scatter(x_nodes, y)
    # plt.title("Year {} Std Delta2Perfect ÷  Std Delta1 for each node".format(year),fontweight="bold")
    # plt.ylabel("Standard deviation of LMPs")
    # plt.xlabel("Node")
    # ax = plt.gca()
    # #plt.xticks(rotation = 90)
    # ax.axes.xaxis.set_ticklabels([])
    # #plt.savefig("sdd1_div_sdd2perf_"+str(year),dpi=200 ,bbox_inches ="tight")
    # #plt.legend()

    
    #saving to csv
    sd_yr["sd_delta1_{}".format(str(year))]=list(sd_delta1)
    sd_yr["sd_delta2perf_{}".format(str(year))]=list(sd_delta2perfect)
    sd_yr["sdd1_div_sdd2perf_{}".format(str(year))]=list(sdd1_div_sdd2perf)
    sd_yr["sdd2perf_div_sdd1_{}".format(str(year))]=list(sdd2perf_div_sdd1)
    
sd_yr.insert(0,"buses",list(sdd2perf_div_sdd1.index))
sd_yr.to_csv("standard_dev_allyears.csv", index=None)


#create a txt file to save stats (max and min of std_delta1 and std_delta2perfect)
with open("stats_for_deltas.txt", "w") as file:
    file.write("min std_delta1 for all years: {}.\n".format(min(min(inner_list) for inner_list in sd_delta1_allyears)))
    file.write("max std_delta1 for all years: {}.\n".format(max(max(inner_list) for inner_list in sd_delta1_allyears)))
    
    file.write("min std_delta2perfect for all years: {}.\n".format(min(min(inner_list) for inner_list in sd_delta2perfect_allyears)))
    file.write("max std_delta2perfect for all years: {}.\n".format(max(max(inner_list) for inner_list in sd_delta2perfect_allyears)))
    


    