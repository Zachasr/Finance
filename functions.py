# -*- coding: utf-8 -*-
"""
A module full of usefull functions
@author: Alexis.Vivien

last revised : 01.02.2022
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def plot_tips(inflation, duration, rate, tips_rate):
    nom_tips = 100;
    s_tips = 0;
    bond_tips_coupon = np.array([]); s = np.array([]); s_tips_tab = np.array([])
    for year in range(duration + 1):
        nom_tips = nom_tips*(1+inflation/100)
        bond_tips_coupon = np.append(bond_tips_coupon, nom_tips * (1 + tips_rate/100) - nom_tips)
        s = np.append(s, year*rate)
        s_tips = s_tips + nom_tips * (1 + tips_rate/100) - nom_tips
        s_tips_tab = np.append(s_tips_tab, s_tips)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,
                                   figsize=(8, 4))
    ax1.plot(range(duration+1), bond_tips_coupon, label='TIPS bond coupon')
    ax1.plot(range(duration+1), rate*np.ones([duration+1]), label='Standard bond coupon')
    ax1.set_title('Coupon over time')
    ax1.legend(loc='upper left')
    ax1.set_ylabel('Coupon value [$]'), ax1.set_xlabel('Time [Years]')   
                       
    ax2.plot(range(duration+1), s_tips_tab, label='TIPS bond return')
    ax2.plot(range(duration+1), s, label='Standard bond return')
    ax2.set_title('Total return over time')
    ax2.legend(loc='upper left')
    ax2.set_ylabel('Total return [$]'), ax2.set_xlabel('Time [Years]')  
    fig.tight_layout()                           # REMOVES UNUSED WHITE SPACE IN THE FIGURE  
        
plot_tips.__doc__ = "Compute and compare the coupons and total returns of a standard bond and a TIPS (Treasury Inflation Protected Security) bond"       

def monthly_vec(start, end):
    return pd.date_range(start, end, freq='MS').strftime("%m-%y").tolist()

monthly_vec.__doc__ = "return a list of dates (strings) with every %m-%y on the interval between start and end. Warning it is the american notation \
                        hence  mm.dd.yy"

plot_tips(2,100,2.5,0.5)
plot_tips(2,100,2.5,0.85)
plot_tips(2,100,2.5,1)
plot_tips(2,100,2.5,1.25)