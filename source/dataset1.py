#source for reference help
#https://pandas.pydata.org/pandas-docs/stable/reference/
#https://pandas.pydata.org/pandas-docs/stable/user_guide/

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

dfCountry = pd.read_csv('https://raw.githubusercontent.com/miklosd/WDI/master/data/WDICountry.csv', delimiter=',')
countryFilter = dfCountry[dfCountry['Currency Unit'] == 'Euro']['Country Code']


yearIndex = []
for i in range(1960,2018):
    yearIndex.append(str(i))

dfData = df = pd.read_csv('https://raw.githubusercontent.com/miklosd/WDI/master/data/WDIData_subset.csv', delimiter=',')

dfResult = pd.DataFrame(index = yearIndex, columns = ['Year'])
dfResult['Year'] = yearIndex
indicatorFilter = 'AG.AGR.TRAC.NO'

for i in countryFilter:
    countryRes1 = dfData[(df['Indicator Code'] == indicatorFilter) &  (df['Country Code'] == i ) ]
    countryRes2 = countryRes1.filter(items = yearIndex)
    dfResult[i] = countryRes2.values[0]

plt.close('all')
plt.ion()

dfResult.plot()
