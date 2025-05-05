# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 19:37:05 2023

@author: hssemba
"""

import pandas as pd
import numpy as np
import networkx as nx
import mpl_toolkits
mpl_toolkits.__path__.append('/usr/lib/python3.7/dist-packages/mpl_toolkits/')
from mpl_toolkits.basemap import Basemap
import matplotlib.lines as mlines

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = "arial"
import glob
import math
import os
from shutil import copy
from pathlib import Path
import seaborn as sns
import itertools
from matplotlib.pyplot import *
import glob
matplotlib.rcParams['font.family'] = "arial"
matplotlib.rcParams.update({'font.size': 25})



#delta1 by bus
delta1_allyrs_bybus=pd.DataFrame()

#delta2perfect by bus
delta2perfect_allyrs_bybus=pd.DataFrame()




years=[2000, 2001, 2002 , 2003, 2004, 2005, 2006, 2007, 2008, 2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]



#wecc topology and lines
df_full = pd.read_csv('xxx/WECC_nodes_10k.csv',header=0)
df_selected = pd.read_csv('xxx/WECC_nodes_100.csv',header=0)
subset = list(df_selected['SelectedNodes'])
df_selected = df_full.loc[df_full['Number'].isin(subset),:]
df_selected = df_selected.reset_index(drop=True)

df_branches = pd.read_csv('xxx/WECC_lines_100.csv',header=0)
df_branches = df_branches[['fbus','tbus','rateA']]

buses = list(df_selected['Number'])

for b in buses:
    if buses.index(b) < 1:
        df_selected_GPS = df_full.loc[df_full['Number']==b,:]
    else:
        a = df_full.loc[df_full['Number']==b,:]
        df_selected_GPS = pd.concat([df_selected_GPS,a])
        
df_selected_GPS = df_selected_GPS.reset_index(drop=True)


        
delta1_std_all=pd.DataFrame()
delta2perfect_std_all= pd.DataFrame()
for year in years:
    
    #Delta1 for that year
    df_delta1=pd.read_csv("xxx/delta1_"+ str(year)+ ".csv")
    #delete time column
    del df_delta1["Time"]
    #find the standard deviation of deltas at every bus
    stdev_delta1_yr=df_delta1.std(axis=0).to_frame().reset_index() 
    #turn it into a dataframe
    stdev_delta1_yr_df= pd.DataFrame([dict(zip(stdev_delta1_yr["index"], stdev_delta1_yr[0]))])
    #add to main dataframe for all years
    delta1_std_all=pd.concat([delta1_std_all, stdev_delta1_yr_df])





    #delta2perfect for that year
    df_delta2perfect=pd.read_csv("xxx/delta2perfect_"+ str(year)+ ".csv")
    #delete time column
    del df_delta2perfect["Time"]
    #find the standard deviation of deltas at every bus
    stdev_delta2perfect_yr=df_delta2perfect.std(axis=0).to_frame().reset_index() 
    #turn it into a dataframe
    stdev_delta2perfect_yr_df= pd.DataFrame([dict(zip(stdev_delta2perfect_yr["index"], stdev_delta2perfect_yr[0]))])
    #add to main dataframe for all years
    delta2perfect_std_all=pd.concat([delta2perfect_std_all, stdev_delta2perfect_yr_df])


#find the average of standard deviations for delta1 and delta2perfect
delta1_std_all_avg=delta1_std_all.mean(axis=0).to_frame().reset_index()
#rename columns
delta1_std_all_avg = delta1_std_all_avg.rename(columns={'index': 'buses', 0 : "std_avg_delta1"})


delta2perfect_std_all_avg=delta2perfect_std_all.mean(axis=0).to_frame().reset_index()
#rename columns
delta2perfect_std_all_avg = delta2perfect_std_all_avg.rename(columns={'index': 'buses', 0 : "std_avg_delta2perfect"})





'''PLOT'''
def makeplot(dataset, numy):
    graph = nx.from_pandas_edgelist(df_branches, 'fbus','tbus')
    A_list = list(graph.nodes())
    
    matplotlib.rcParams.update({'font.size': 20})
    m = Basemap(
        ax=axs[numy],
        projection='merc',
        llcrnrlon=-130,
        llcrnrlat=30,
        urcrnrlon=-100,
        urcrnrlat=50,
        lat_ts=0,
        resolution='l',
        suppress_ticks=True)
    

    
    if dataset== "delta1":   
        sd_Delta = []
        for a in A_list:
            b = 'bus_' + str(a)
            sd_Delta.append(delta1_std_all_avg.loc[delta1_std_all_avg['buses']==b,'std_avg_delta1'].values[0])
        vminglob=delta1_std_all_avg['std_avg_delta1'].min()
        vmaxglob=delta1_std_all_avg['std_avg_delta1'].max()
        cmaps='PiYG'
        
    elif dataset=="delta2perf":
        sd_Delta = []
        for a in A_list:
            b = 'bus_' + str(a)
            sd_Delta.append(delta2perfect_std_all_avg.loc[delta2perfect_std_all_avg['buses']==b,'std_avg_delta2perfect'].values[0])    
        vminglob=delta2perfect_std_all_avg['std_avg_delta2perfect'].min()
        vmaxglob=delta2perfect_std_all_avg['std_avg_delta2perfect'].max()
        cmaps='coolwarm_r'
  
    
    mx, my = m(df_selected_GPS['lon'].values, df_selected_GPS['lat'].values)
    pos = {}
    for count, elem in enumerate (df_selected_GPS['Number']):
        pos[elem] = (mx[count], my[count])
    
    nx.draw_networkx_nodes(G = graph, pos = pos, nodelist = graph.nodes(), node_color = sd_Delta, cmap=cmaps, vmin=vminglob, vmax=vmaxglob, alpha = 1, node_size = 250, ax=axs[ numy])
    nx.draw_networkx_edges(G = graph, pos = pos, edge_color='k', alpha=0.6, width = 1,arrows = False, ax=axs[numy])
    
    m.drawcountries(linewidth = 1, ax=axs[numy])
    m.drawstates(linewidth = 1, ax=axs[numy])
    m.drawcoastlines(linewidth=1, ax=axs[numy])
    

    sm = plt.cm.ScalarMappable(cmap=cmaps, norm=plt.Normalize(vmin = vminglob, vmax=vmaxglob))
    sm._A = []
    if dataset== "delta1": 
        plt.colorbar(sm, ax=axs[numy], shrink=0.5)
        #plt.title("Year {} Std Delta1".format(year),fontsize=30)
        axs[numy].set_title("$ε_{flow}$ (Standard_Dev)",fontsize=25)
    elif dataset=="delta2perf" :
        #axs[numy].plt.colorbar(sm, ax=plt.gca())
        plt.colorbar(sm, ax=axs[numy], shrink=0.5)
        #plt.title("Year {} Std Delta1".format(year),fontsize=30)
        axs[numy].set_title("$ε_{scheduling}$ (Standard_Dev)",fontsize=25)   
          
            
fig, axs = plt.subplots(1,2,figsize=(20,15))               
#make the 2 plots
makeplot("delta1", 0)
makeplot("delta2perf", 1)
#savefig

plt.savefig("stdavg_Delta_combined_cbar_mspt_rev.png", dpi = 400, bbox_inches ="tight")
       
 