# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:24:11 2021

@author: jkern
"""

# import libaries
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


'''1. ANALYSIS'''

#years=[2000]
years=[2000, 2001, 2002 , 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]


percent_revenue_gain_loss_yr=pd.DataFrame()
for year in years:
    #Import GO1 perfect LMPs
    dflmps_go1perfect=pd.read_csv("xxx/duals__"+ str(year)+ ".csv")

    #GO1 perfect LMPs by bus (sorted)
    dflmps_bus_go1perfect=dflmps_go1perfect.pivot(index="Time", columns="Bus", values="Value").reset_index(drop=True)


    #GO2perferct hydro generation 
    go2pefect_hydro_bus=pd.read_csv("xxx/Exp{}_100_simple_2000_0/nodal_hydro.csv".format(year))
    go2pefect_hydro_bus=go2pefect_hydro_bus.reset_index(drop=True)

    
    #GO2 perfect LMPs
    dflmps_go2perfect=pd.read_csv("xxx/Exp{}_100_simple_2000_0/duals.csv".format(year))
    #GO2 perfect LMPs (sorted)
    dflmps_bus_go2perfect=dflmps_go2perfect.pivot(index="Time", columns="Bus", values="Value").reset_index(drop=True)

    #expected revenue (GO1PerfectPx x GO2Perfect Hydro)
    expectedrev_go1pfpx_go2pfhydro=dflmps_bus_go1perfect*go2pefect_hydro_bus
    #sum expected revenue for the year
    sum_expectedrev_go1pfpx_go2pfhydro=expectedrev_go1pfpx_go2pfhydro.sum(axis=0)
    
    #actual revenue (GO2PerfectPx x GO2Perfect Hydro)
    actualrev_go2pfpx_go2pfhydro=dflmps_bus_go2perfect*go2pefect_hydro_bus
    #sum actual revenue for the year
    sum_actualrev_go2pfpx_go2pfhydro=actualrev_go2pfpx_go2pfhydro.sum(axis=0)
    
    # percentage_revenue_gain or loss 
    percent_revenue_gainorloss=(sum_actualrev_go2pfpx_go2pfhydro-sum_expectedrev_go1pfpx_go2pfhydro)/sum_expectedrev_go1pfpx_go2pfhydro*100
    percent_revenue_gainorloss=percent_revenue_gainorloss.to_frame().reset_index(drop=True)
    #fillna with 0
    #the NAs are the nodes where there is no hydro
    percent_revenue_gainorloss=percent_revenue_gainorloss.fillna(0)
    

    percent_revenue_gain_loss_yr[year]=percent_revenue_gainorloss[0]
# #buses
buses=list(expectedrev_go1pfpx_go2pfhydro.columns)
# #Add bus column
percent_revenue_gain_loss_yr["buses"]=buses








'''2. MAP PLOT'''
    


#find global vmin and vmax

#all years global perc_revgainloss min
allyearsmin_perc_revgainloss=[]
#all years global perc_revgainloss max 
allyearsmax_perc_revgainloss=[]

for year in years:
    df_d2pf_perc_revgainloss=percent_revenue_gain_loss_yr
    #local minimum perc_revgainloss
    yrmin_perc_revgainloss=df_d2pf_perc_revgainloss[year].min()
    allyearsmin_perc_revgainloss.append(yrmin_perc_revgainloss)
    #local maximum perc_revgainloss
    yrmax_perc_revgainloss=df_d2pf_perc_revgainloss[year].max()
    allyearsmax_perc_revgainloss.append(yrmax_perc_revgainloss)

#min all years global perc_revgainlossmin
vminglob=min(allyearsmin_perc_revgainloss)


'''ON PURPOSE'''
#make the maximum value the absolute value of the minimum for symmetry 
vmaxglob=abs(min(allyearsmin_perc_revgainloss))

for year in years:
        df_perc_revgainloss = pd.read_csv('d2pf_revenue_gain_loss_yr.csv',header=0)
        df_full = pd.read_csv('WECC_nodes_10k.csv',header=0)
        df_selected = pd.read_csv('WECC_nodes_100.csv',header=0)
        subset = list(df_selected['SelectedNodes'])
        df_selected = df_full.loc[df_full['Number'].isin(subset),:]
        df_selected = df_selected.reset_index(drop=True)
        
        df_branches = pd.read_csv('WECC_lines_100.csv',header=0)
        df_branches = df_branches[['fbus','tbus','rateA']]
        
        buses = list(df_selected['Number'])
        
        for b in buses:
            if buses.index(b) < 1:
                df_selected_GPS = df_full.loc[df_full['Number']==b,:]
            else:
                a = df_full.loc[df_full['Number']==b,:]
                df_selected_GPS = pd.concat([df_selected_GPS,a])
                
        df_selected_GPS = df_selected_GPS.reset_index(drop=True)
        

        
        globals()[f'df_perc_revgainloss_{year}'] = df_perc_revgainloss[["buses","{}".format(year)]]
        

        
     
def makeplot(year):
    graph = nx.from_pandas_edgelist(df_branches, 'fbus','tbus')
    A_list = list(graph.nodes())
    
    matplotlib.rcParams.update({'font.size': 20})
    m = Basemap(
        ax=axs,
        projection='merc',
        llcrnrlon=-130,
        llcrnrlat=30,
        urcrnrlon=-100,
        urcrnrlat=50,
        lat_ts=0,
        resolution='l',
        suppress_ticks=True)
    

    

    value_perc_revgainloss_yr=globals()[f'df_perc_revgainloss_{year}']
    perc_revgainloss = []
    for a in A_list:
        b = 'bus_' + str(a)
        perc_revgainloss.append(value_perc_revgainloss_yr.loc[value_perc_revgainloss_yr['buses']==b,'{}'.format(str(year))].values[0])
    

    
    mx, my = m(df_selected_GPS['lon'].values, df_selected_GPS['lat'].values)
    pos = {}
    for count, elem in enumerate (df_selected_GPS['Number']):
        pos[elem] = (mx[count], my[count])
    
    nx.draw_networkx_nodes(G = graph, pos = pos, nodelist = graph.nodes(), node_color = perc_revgainloss, cmap='bwr_r', vmin=vminglob, vmax=vmaxglob, alpha = 1, node_size = 250, ax=axs)
    nx.draw_networkx_edges(G = graph, pos = pos, edge_color='k', alpha=0.6, width = 1,arrows = False, ax=axs)
    
    m.drawcountries(linewidth = 1, ax=axs)
    m.drawstates(linewidth = 1, ax=axs)
    m.drawcoastlines(linewidth=1, ax=axs)
    

    
    sm = plt.cm.ScalarMappable(cmap='bwr_r', norm=plt.Normalize(vmin = vminglob, vmax=vmaxglob))
    sm._A = []
    axs.set_title("{}".format(year),fontsize=30)
    plt.tight_layout()
          
            
fig, axs = plt.subplots(1,1,figsize=(15,10))               
for year in years:
    if year==2000:
        makeplot(year)


sm = plt.cm.ScalarMappable(cmap='bwr_r', norm=plt.Normalize(vmin = vminglob, vmax=vmaxglob))
sm._A = []


matplotlib.rcParams.update({'font.size': 25})
fig.colorbar(sm, ax=axs, shrink=0.5)
 

fig.tight_layout()
plt.savefig("2000percent_revenue_gain_loss.png", bbox_inches="tight", dpi = 400)        

