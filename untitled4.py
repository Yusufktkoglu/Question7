# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:31:16 2024

@author: 90539
"""

import pandas as pd

dataset = pd.read_csv("country_vaccination_stats.csv")

countries = dataset['country'].unique()

for country in countries:
    country_row = dataset[dataset['country'] == country].copy()
    dailymin_vaccinations = country_row['daily_vaccinations'].min()
    country_row['daily_vaccinations'].fillna(dailymin_vaccinations, inplace=True)
    dataset.loc[dataset['country'] == country, 'daily_vaccinations'] = country_row['daily_vaccinations']
date_filter = dataset[dataset['date'] == '1/6/2021']
total_vac = date_filter['daily_vaccinations'].sum()
print(total_vac)
