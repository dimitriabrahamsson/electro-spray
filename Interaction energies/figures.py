#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:52:24 2023

@author: dabrahamsson
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.signal import argrelextrema

findex = ['2AM6', '4AMI', '4CHL', 'ACT', 'ALD', 'AZO', 'BOS', 'CAF', 'CAR', 'CIN',
          'CL10', 'CLA', 'COR', 'CP4', 'CRL', 'DACN', 'DBP', 'DCHP', 'DCP', 'DEE', 
          'DINO', 'DIP', 'DIU', 'DPPL', 'FUB', 'FUX', 'GLY', 'ILE', 'IMQ', 'ISO', 
          'LAU', 'LOR', 'NND', 'NUA', 'SUL', 'TBF', 'THIA', 'THIX', 'TTC', 'WAR']

for i in findex:
    
    file = i
    file = file + '1'
    name = (file[:-1])
    
    ie = np.genfromtxt([i for i in open(file + '_interaction_energy_CHE_H.xvg').read().splitlines()
        if not i.startswith(('#','@'))])
    
    df = pd.DataFrame(ie, columns = ['Time (ps)','Coul-SR','LJ-SR'])
    
    '''
    sns.lineplot(data=df, x="Time (ps)", y="Coul-SR")
    plt.xlabel('time (ps)')
    plt.ylabel('interaction energy (kJ/mol)')
    
    sns.lineplot(data=df, x="Time (ps)", y="LJ-SR")
    plt.xlabel('time (ps)')
    plt.ylabel('interaction energy (kJ/mol)')
    '''
    
    x1 = df['Coul-SR'].values
    x2 = df['LJ-SR'].values
    L1 = x1[argrelextrema(x1, np.less)[0]]
    L2 = x2[argrelextrema(x1, np.less)[0]]
    
    
    L1 = np.sort(L1)
    L1 = L1[:5]
    L2 = np.sort(L2)
    L2 = L2[:5]
    
    print ('Local minima')
    print('Coul: ', L1)
    print('LJ: ', L2)
    
    P1 = np.percentile(df['Coul-SR'], 0.5)
    P2 = np.percentile(df['LJ-SR'], 0.5)
    print('Percentiles')
    print('Coul: ', P1)
    print('LJ: ', P2)
    
    A1 = np.average(df['Coul-SR'])
    A2 = np.average(df['LJ-SR'])
    
    print('Averages')
    print('Coul: ', A1)
    print('LJ: ', A2)
    
    S1 = np.std(df['Coul-SR'])
    S2 = np.std(df['LJ-SR'])
    
    print('Standard deviation')
    print('Coul: ', S1)
    print('LJ: ', S2)
    
    d = {'Coul LM1': L1[0:1], 'Coul LM2': L1[1:2],'Coul LM3': L1[2:3],
         'LJ LM1': L2[0:1], 'LJ LM2': L2[1:2], 'LJ LM3': L2[2:3], 
         'Chemical': [file]}
    
    df = pd.DataFrame(data = d)
    df = df.replace('[', '')
    df = df.replace(']', '')
    df.to_csv('locmin_' + name + '.csv')
    
    d = {'Coul': [P1], 'LJ': [P2], 'Chemical': [name]}
    df = pd.DataFrame(data = d)
    df.to_csv('percent_' + name + '.csv')
    
    d = {'Coul': [A1], 'LJ': [A2], 'Chemical': [name]}
    df = pd.DataFrame(data = d)
    df.to_csv('average_' + name + '.csv')
    
    d = {'Coul': [S1], 'LJ': [S2], 'Chemical': [name]}
    df = pd.DataFrame(data = d)
    df.to_csv('stdev_' + name + '.csv')