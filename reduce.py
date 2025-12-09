from functools import reduce #to use reduce, we must first import it from functool module

def add(x,y):
    return x + y

def mul(x,y):
    return x * y

arr = [1,2,3,4,5]

reduceList = reduce(add, arr)
"""
reduce will work like below:
1+2 → 3
3+3 → 6
6+4 → 10
10+5 → 15
"""
print(reduceList)

reduceListMul = reduce(mul, arr)
print(reduceListMul)