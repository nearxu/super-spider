
import heapq

income = [10,20,30]

def double_money(rmb):
    return rmb*2


print(list(map(double_money,income)))

print(income)

grad = []

# 求列表最大值最小值

grad = [314,255,999,1,25,77]
print(heapq.nlargest(3,grad))

stocks = [
    {'ticker':'Google','price':425},
    {'ticker':'Apple','price':300},
    {'ticker':'Facebook','price':600},
]

print(heapq.nlargest(2,stocks,key=lambda stocks:stocks['price']))

