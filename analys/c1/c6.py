import pandas as pd
import matplotlib.pyplot as plt

columns = ['name', 'gender', 'frequency']

years = range(1880, 2017)

baby = []

for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    baby.append(frame)

babys = pd.concat(baby, ignore_index=True)

print(babys)

print(babys.groupby(['year', 'gender']).size())


def add_pct(group):
    group['pct'] = group.frequency/group.frequency.sum()*100
    return group


babys = babys.groupby(['year', 'gender']).apply(add_pct)

# print(babys.head())

babys['ranked'] = babys.groupby(['year', 'gender'])[
    'frequency'].rank(ascending=False)

dfm = babys[babys.gender == 'M']
dff = babys[babys.gender == 'F']


rankm = dfm[dfm.ranked == 1]

# print(rankm)

# plt.plot(rankm.year, rankm.pct, color='blue', linewidth=2)
# plt.fill_between(rankm.year, rankm.pct, color="blue", alpha=0.1)
# plt.show()

name_count = babys.groupby(['year', 'gender']).size()

# to_frame series => dict
# reset_index year and gender change to inde
name_count = name_count.to_frame(name='name_count').reset_index()

print('reset_index', name_count)

name_count_m = name_count[name_count.gender == 'M']

plt.plot(name_count_m.year, name_count_m.name_count, color='blue')
plt.show()
