#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 18:15:58 2023

@author: dabrahamsson
"""

import numpy as np
import pandas as pd

findex = ['2AM6', '4AMI', '4CHL', 'ACT', 'ALD', 'AZO', 'BOS', 'CAFT1', 'CARB', 'CIN',
          'CL10', 'CLA', 'COR', 'CRL', 'DEE', 'DIU', 'DIP', 'DCP', 'DCHP', 'DBP', 
          'CP4', 'DINO', 'DACN', 'DPPL', 'FUB', 'FUX', 'GLY', 'ILE', 'IMQ', 'ISO', 'LAU', 
          'LOR', 'NNP', 'NND', 'NUA', 'SUL', 'TBF', 'THIA', 'THIX', 'TTC', 'WAR', 
          '43PP', 'FLX', 'FLZ', 'NMD', 'NBPT', 'NEM', 'PYRA', 'SSR', 'TBFD']


li1 =[] 

for i in findex:
    
    file = i
    df = pd.read_csv('Lpercent_' + file + '.csv', index_col=None, header=0)
    li1.append(df)
    
dpl = pd.concat(li1, axis=0, ignore_index=True)
dpl = dpl.drop('Unnamed: 0', axis=1)
dpl.columns = dpl.columns.str.replace('Coul', 'Coul Lper')
dpl.columns = dpl.columns.str.replace('LJ', 'LJ Lper')
dpl.columns = dpl.columns.str.replace('Chemical', 'Chem1')

print(dpl)

li2 =[]

for i in findex:
    
    file = i
    df = pd.read_csv('Hpercent_' + file + '.csv', index_col=None, header=0)
    li2.append(df)
    
dph = pd.concat(li2, axis=0, ignore_index=True)
dph = dph.drop('Unnamed: 0', axis=1)
dph.columns = dph.columns.str.replace('Coul', 'Coul Hper')
dph.columns = dph.columns.str.replace('LJ', 'LJ Hper')
dph.columns = dph.columns.str.replace('Chemical', 'Chem2')

print(dph)


li3 =[]

for i in findex:
    
    file = i
    df = pd.read_csv('average_' + file + '.csv', index_col=None, header=0)
    li3.append(df)
    
da = pd.concat(li3, axis=0, ignore_index=True)
da = da.drop('Unnamed: 0', axis=1)
da.columns = da.columns.str.replace('Coul', 'Coul av')
da.columns = da.columns.str.replace('LJ', 'LJ av')
da.columns = da.columns.str.replace('Chemical', 'Chem3')

print(da)


li4 =[]

for i in findex:
    
    file = i
    df = pd.read_csv('stdev_' + file + '.csv', index_col=None, header=0)
    li4.append(df)
    
ds = pd.concat(li4, axis=0, ignore_index=True)
ds = ds.drop('Unnamed: 0', axis=1)
ds.columns = ds.columns.str.replace('Coul', 'Coul std')
ds.columns = ds.columns.str.replace('LJ', 'LJ std')
ds.columns = ds.columns.str.replace('Chemical', 'Chem3')

print(ds)

df = pd.concat([dpl, dph, da, ds], axis=1)
df = df.sort_values(by='Chem1', ascending=True)
df.shape
df.to_csv('final_0.csv')
