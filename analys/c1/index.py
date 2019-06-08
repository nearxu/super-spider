import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re as re
import scipy

years = range(1880, 2017)

pieces = []

columns = ['name', 'gender', 'frequency']

for year in years:
    path = './names/yob%d.txt' % year

    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

baby_names = pd.concat(pieces, ignore_index=True)
# print(baby_names)

# print(baby_names.head(10))

# print(baby_names.describe())

# name frequence

print(baby_names.groupby('name').agg({'frequency': sum}))

print(baby_names.groupby('name').agg(
    {'frequency': sum}).sort_values(by=['frequency'], ascending=[0]))

# gender

freq_by_gender_year = baby_names.pivot_table(
    index='year', columns='gender', values='frequency', aggfunc=sum)

# print(freq_by_gender_year)

# print(freq_by_gender_year.tail())

freq_by_gender_year.plot(title='frequency by year and gender')

plt.show()
