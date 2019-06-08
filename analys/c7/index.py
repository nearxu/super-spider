# 导入Matplotlib做图工具
import matplotlib.pyplot as plt
# 导入numpy和pandas包
import numpy as np
import pandas as pd

# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()


df = pd.read_excel('sample-salesv3.xlsx')

print(df.head())

# top_10 = df.groupby('name')['ext price'].agg(
#     ['sum', 'count']).reset_index().sort_values(by='sum', ascending=False)[:10]

# print(top_10)

# top_10.rename(columns={'name': 'Name', 'sum': 'Sales',
#                        'count': 'Purchase'}, inplace=True)

plt.style.use('ggplot')

# plt.barh(top_10.Name, top_10.Sales, height=0.5)

# plt.pie(top_10.Sales,labels=top_10.Name,autopct='%1.1f%%')

# kulas = df[df.name == 'Kulas Inc']

# ax = kulas.plot(kind='unit price', x='date', y='unit price',
#                 color='Red', label='kulas')

# plt.show()
