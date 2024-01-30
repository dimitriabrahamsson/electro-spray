#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 21:41:33 2023

@author: anton
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm

df = pd.read_csv('ChemNamesAndProps.csv')
df1 = pd.read_csv('final_0.csv')
df1.columns

df1 = df1[['Chem1','LJ Lper', 'LJ av', 'LJ std', 'LJ Hper', 
           'Coul Lper', 'Coul av', 'Coul std', 'Coul Hper']]

df1.columns = df1.columns.str.replace('Chem1', 'Chem') 
df = pd.merge(df1, df, on='Chem')

df['log VP'] = np.log10(df['VP'])

# remove chemicals with high RSD (>15%) in log RRF
df = df[~df['Chem'].str.contains('SSR')]
df = df[~df['Chem'].str.contains('ISO')]
#df = df[~df['Chem'].str.contains('CRL')]
#df = df[~df['Chem'].str.contains('FUX')]

# run if you want to remove chemicals with large errors
df = df.sort_values(by='Total', ascending=True)
df['pen flag 1'] = np.where((df['Total'] > 300), 1, 0)
df['pen flag 2'] = np.where((df['Total over 50'] > 10), 1, 0)
df['pen flag 3'] = np.where((df['pen flag 1'] == 1) & (df['pen flag 2'] == 1), 1, 0)

df.to_csv('final_combined.csv')

df = df[df['pen flag 1'] == 0]



x = df[['LJ Lper', 'LJ av', 'LJ std', 'LJ Hper', 
        'Coul Lper', 'Coul av', 'Coul std', 'Coul Hper',
        'VP']]


#x = df[['E QSPR', 'S QSPR', 'A QSPR', 'B QSPR', 'V', 'L QSPR']]

y = df['log RRF']
#y = (10**y)/100
#y = np.log(y)

 
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(x, y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

dr = {'Parameter': ['LJ Lper', 'LJ av', 'LJ std ', 'LJ Hper ', 'Coul Lper', 'Coul av', 'Coul std', 'Coul Hper', 'VP'], 
                    'Intercept': regr.intercept_, 'Coefficients': regr.coef_}
r = pd.DataFrame(dr)

r.loc[-1] = ['const', regr.intercept_, regr.intercept_]
r = r.drop('Intercept', axis=1)
r.index = r.index + 1  # shifting index
r = r.sort_index()  # sorting by index
print(r)
r.to_csv('coefficients.csv')

# with statsmodels
x = sm.add_constant(x) # adding a constant
 
model = sm.OLS(y, x).fit()
predictions = model.predict(x) 
 
print_model = model.summary()
print(print_model)


#notes

