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


#............................................................................................................

'''TOP PLOT: STANDARD DEVIATION OF DELTA1 VS STANDARD DEVIATION OF DELTA2PERFECT'''

years=[2000, 2001, 2002 , 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

std_delta1allyrs=pd.DataFrame()
std_delta2perfallyrs=pd.DataFrame()

for year in years:
    
    #Delta1 for that year
    df_delta1=pd.read_csv("***/delta1_"+ str(year)+ ".csv")
    #delete time column
    del df_delta1["Time"]
    #standard deviation of delta1 by bus
    stdperbus_d1=list(df_delta1.std(axis=0))
    std_delta1allyrs["{}".format(year)]=stdperbus_d1
    std_delta1allyrs["Type"]= r'$ε_{flow}$'#"StandardDev Delta1"
    
    
    #Delta2perf for that year
    df_delta2perf=pd.read_csv("../../delta2perfect/delta2perfect_"+ str(year)+ ".csv")
    #delete time column
    del df_delta2perf["Time"]
    #standard deviation of delta2 by bus
    stdperbus_d2pf=list(df_delta2perf.std(axis=0))
    std_delta2perfallyrs["{}".format(year)]=stdperbus_d2pf
    std_delta2perfallyrs["Type"]= r'$ε_{scheduling}$'#"StandardDev Delta2"    
    

#melt both dataset
std_delta1allyrsx= pd.melt(frame=std_delta1allyrs, id_vars=['Type'])
std_delta2perfallyrsx= pd.melt(frame=std_delta2perfallyrs, id_vars=['Type'])
#concat both datasets
std_d1d2pf=pd.concat([std_delta1allyrsx, std_delta2perfallyrsx])



#............................................................................................................
'''BOTTOM PLOT: MEAN STD DELTA2PERFECT VS ANNUALGEN'''
mean_stdevd2perf=[]
annualgen_hydro=[]
for year in years:
        df_stdlmps = pd.read_csv('***/standard_dev_allyears.csv',header=0)
        df_genhydro = pd.read_csv('***/nodal_hydro_adjusted_{}.csv'.format(year),header=0)
        
        mean_stdevd2perf_yr = df_stdlmps["sd_delta2perf_{}".format(year)].mean()
        mean_stdevd2perf.append(mean_stdevd2perf_yr)
        
        annualgen_hydro_yr=df_genhydro.sum().sum()
        annualgen_hydro.append(annualgen_hydro_yr)
        

#.............................................................................................................
'''JOINT PLOT'''


#define colors
mycolors=["limegreen", "darkorange"]
fig, (axs1, axs2) = plt.subplots(2, sharex=False, figsize=(26,21))
matplotlib.rcParams['font.family'] = "arial"


#plot1 (TOP PLOT)
sns.boxplot(x="variable", y="value", 
                hue="Type", 
                data=std_d1d2pf, palette=mycolors, ax=axs1)
axs1.set_ylabel("Std Dev of LMP Differences,  $/MWh", fontsize=30)
axs1.legend(loc='upper left', ncol=2, fontsize=35)
axs1.set_xlabel("Year", fontsize=30)
axs1.grid(False)  # <-- Disable gridlines


#plot2 (BOTTOM PLOT)
axs2.scatter(annualgen_hydro,mean_stdevd2perf, color="red", s=120)
axs2.set_ylabel("Mean (Std Dev) of ε_scheduling,  $/MWh", fontsize=30) 
axs2.set_xlabel(" Annual Hydro Gen (MWh/year)", fontsize=30)
axs2.grid(False)  # <-- Disable gridlines
for i, txt in enumerate(years):
    axs2.annotate(txt, (annualgen_hydro[i],mean_stdevd2perf[i]), fontsize=20)
plt.tight_layout()
plt.savefig('joint_onlyperfect_manuscript2.png',dpi=400 ,bbox_inches ="tight")





