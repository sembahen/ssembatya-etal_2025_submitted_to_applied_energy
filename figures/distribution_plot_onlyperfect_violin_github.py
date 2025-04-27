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


years=[2000, 2001, 2002 , 2003, 2004, 2005, 2006, 2007, 2008, 2009,
      2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

delta1all=[]
delta2perfectall=[]
delta2persistenceall=[]

for year in years:
    
    #Delta1 for that year
    df_delta1=pd.read_csv("***/delta1_"+ str(year)+ ".csv")
    #delete time column
    del df_delta1["Time"]
    #moving all values to a list
    delta1_list = df_delta1[df_delta1.columns].values.T.ravel().tolist()
    delta1all.append(delta1_list)

    
    #Delta2perf for that year
    df_delta2perf=pd.read_csv("***/delta2perfect_"+ str(year)+ ".csv")
    #delete time column
    del df_delta2perf["Time"]
    #moving all values to a list
    delta2perf_list = df_delta2perf[df_delta2perf.columns].values.T.ravel().tolist()
    delta2perfectall.append(delta2perf_list) 
    

    #Delta2persistence for that year
    df_delta2persistence=pd.read_csv("***/delta2persist_"+ str(year)+ ".csv")
    #delete time column
    del df_delta2persistence["Time"]
    #moving all values to a list
    delta2persistence_list = df_delta2persistence[df_delta2persistence.columns].values.T.ravel().tolist()
    delta2persistenceall.append(delta2persistence_list)     
    

delta1all_list = list(np.concatenate(delta1all))
delta2perfectall_list=list(np.concatenate(delta2perfectall))
delta2persistenceall_list=list(np.concatenate(delta2persistenceall))




#epsilon greek
eps="ε"
#dataframe for all D1 values
df_delta1all=pd.DataFrame()
df_delta1all["Values"]=delta1all_list
df_delta1all["Type"]=r'$ε_{flow}$' #"Delta 1" 


#dataframe for all D2Perfect values
df_delta2perfectall=pd.DataFrame()
df_delta2perfectall["Values"]=delta2perfectall_list
df_delta2perfectall["Type"]=r'$ε_{scheduling}$' #"Delta 2"


#concatenate delta1, delta2perfect (no delta2persistence)
df_distribution=pd.concat([df_delta1all, df_delta2perfectall])#, df_delta2persistenceall])



#BOX PLOT
plt.figure(figsize=(30,20))
sns.set(style="whitegrid", font_scale=2)


matplotlib.rcParams.update({'font.size': 35})
sns.set_context("talk", font_scale=2.5)
sns.violinplot(x="Type", y="Values", 
                data=df_distribution )
plt.xticks(fontsize=50)
matplotlib.rcParams.update({'font.size': 35})
plt.ylabel("Differences in LMPs , $/MWh", fontweight="bold")

plt.savefig("d1_d2pf_distribution_onlyperfect_violin_mscript.png",dpi=500 ,bbox_inches ="tight")


# quantiles=pd.DataFrame()
# quantiles["Quantiles"]=["P00", "P25", "P50", "P75", "P100"]
# quantiles["Delta 1"]=np.quantile(delta1all, [0,0.25,0.5,0.75,1])
# quantiles["Delta 2Perfect"]=np.quantile(delta2perfectall, [0,0.25,0.5,0.75,1])
# quantiles["Delta 2Persist"]=np.quantile(delta2persistenceall, [0,0.25,0.5,0.75,1])
# quantiles.to_excel("quantiles.xlsx", index=None)
  



