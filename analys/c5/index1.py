import pandas as pd
import matplotlib.pyplot as plt

col_names = ['sepal_length', 'sepal_width',
             'petal_length', 'petal_width', 'species']

iris = pd.read_csv('iris.txt', names=col_names)

print(iris.head())

print(iris.info())

one = iris[iris.species == 'Iris-setosa']
two = iris[iris.species == 'Iris-versicolor']
three = iris[iris.species == 'Iris-virginica']

ax = one.plot(kind='scatter', x='petal_length', y='petal_width',
              color='Red', label='one', figsize=(10, 6))
two.plot(kind='scatter', x='petal_length', y='petal_width',
         color='Green', ax=ax, label='two')
three.plot(kind='scatter', x='petal_length', y='petal_width',
           color='Orange', ax=ax, label='three')
# iris.plot(kind='scatter', x='petal_length', y='petal_width')
plt.show()
