# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:40:07 2021

@author: Alexis.Vivien
"""
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import plotly.graph_objs as go

df = pd.read_csv(r'C:\Users\alexis.vivien\Desktop\TWTR.csv')
dim = df.shape; col = df.columns
data = df.to_numpy()
year21_label = np.array(['Jan 21','Feb 21','Mar 21','Apr 21','May 21','Jun 21','Jul 21','Aug 21','Sep 21','Oct 21','Nov 21','Dec 21'])


plt.plot(data[:,0],data[:,5],label = 'Twitter stock',alpha = 1)
idx = [0,2,4,6,8,10];
plt.xticks(ticks = np.round((252/12)*np.array(idx)),labels = year21_label[idx])

plt.show()