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


forecasts=["perfect", "persistent"]

#years=[2000]
years=[2000, 2001, 2002 , 2003, 2004, 2005, 2006, 2007, 2008, 2009,
      2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

lmp_prices=[]
nodes=[]
for year in years:
    #GO1 perfect
    dflmps_go1perfect=pd.read_csv("***/duals__"+ str(year)+ ".csv")
    #GO1 persistence
    dflmps_go1persistence=pd.read_csv("***/duals.csv".format(year))
    


    ### e_flow (delta1)
    #GO1 perfect (sorted) by time and bus
    dflmps_bus_go1perfect=dflmps_go1perfect.pivot(index="Time", columns="Bus", values="Value")
    #GO1 persistence (sorted)
    dflmps_bus_go1persistence=dflmps_go1persistence.pivot(index="Time", columns="Bus", values="Value")
    #e_flow (delta1) = GO1perfect -GO1persistence
    delta1=dflmps_bus_go1perfect-dflmps_bus_go1persistence
    #export to csv
    delta1.to_csv("delta1/delta1_"+str(year)+".csv")
    
 
    ### e_scheduling (delta2)
    ##GO1perfect- GO2perfect
    dflmps_go2perfect=pd.read_csv("***/duals.csv".format(year))
    #GO2 perfect (sorted) by time and bus
    dflmps_bus_go2perfect=dflmps_go2perfect.pivot(index="Time", columns="Bus", values="Value")
    #delta2perfect = GO1 perfect -GO2 perfect
    delta2perfect=dflmps_bus_go1perfect-dflmps_bus_go2perfect
    delta2perfect.to_csv("delta2perfect/delta2perfect_"+str(year)+".csv")
    

      
    
    ##GO1persistence - GO2persistence
    #GO2 persistence
    dflmps_go2persistence=pd.read_csv("***/duals"+ str(year)+ ".csv")
    #GO2 persistence (sorted)
    dflmps_bus_go2persistence=dflmps_go2persistence.pivot(index="Time", columns="Bus", values="Value")
    #delta2persistence = GO1 persistence -GO2 persistence
    delta2persistence=dflmps_bus_go1persistence-dflmps_bus_go2persistence
    delta2persistence.to_csv("delta2persistence/delta2persist_"+str(year)+".csv")

        
    
