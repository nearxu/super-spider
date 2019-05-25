import numpy as np

value = [1, 2, 3]

arr = np.array(value)
print(arr)

# print(type(arr))

wine_data = np.genfromtxt('winequality-red.csv', delimiter=';', skip_header=1)

print(wine_data)

# data>5

print(wine_data[:, 2])

# axios 求和 0 列 1 行

print(np.sum(wine_data, axis=0))

#  取前10行数据中的8，10，11列,分别对应红酒的PH值、酒精度、质量评分这三类属性
print(wine_data[:10, [8, 10, 11]])
