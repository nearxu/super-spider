import pandas as pd


col_names = ['sepal_length', 'sepal_width',
             'petal_length', 'petal_width', 'species']

iris = pd.read_csv('iris.txt', names=col_names)


print(iris.species.value_counts())

print(iris.groupby('species').max())

# agg


def range_iris(arr):
    return arr.max()-arr.min()


print(iris.groupby('species').agg(range_iris))
