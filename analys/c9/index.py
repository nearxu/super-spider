import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import calendar
from datetime import datetime
import seaborn as sns

bike = pd.read_csv('bike.csv')


def get_date(x):
    # 2011-01-01 00:00:00 => 2011-01-01
    return (x.split())[0]


def get_hours(x):
    return (x.split(":")[0])


bike['date'] = bike.datetime.apply(get_date)

bike['hours'] = bike.datetime.apply(get_hours)

# week

# dateDT = datetime.strptime(dateString,"%Y-%m-%d")

# type(dateDT)


def get_week(dateString):
    week_day = datetime.strptime(dateString, '%Y-%m-%d').weekday()
    return (calendar.day_name[week_day])


bike['weekday'] = bike.date.apply(get_week)


def get_month(dateString):
    return (datetime.strptime(dateString, '%Y-%m-%d').month)


bike['month'] = bike.date.apply(get_month)

bike['season_label'] = bike.season.map(
    {1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'})

print(bike.head())
# plt.plot(rankm.year, rankm.pct, color='blue', linewidth=2)
sns.FacetGrid(data=bike).map(sns.pointplot, 'hours', 'count',
                             'season_label', palette='deep', ci=None).add_legend()
