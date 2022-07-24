
from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置

# Map = [['U' for _ in range(n)] for _ in range(m)]
import heapq
from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.methods = {}
        self.rate = {}
        self.cuisines = {}
        for i in range(n):
            self.rate[foods[i]] = ratings[i]
            self.cuisines[foods[i]] = cuisines[i]
            if cuisines[i] not in self.methods:
                self.methods[cuisines[i]] = [(-ratings[i], foods[i])]
                continue
            bisect.insort_left(self.methods[cuisines[i]], (-ratings[i], foods[i]))


    def changeRating(self, food: str, newRating: int) -> None:
        rating = self.rate[food]
        cuisine = self.cuisines[food]
        pos = bisect.bisect_left(self.methods[cuisine], (-rating, food))
        del self.methods[cuisine][pos]
        bisect.insort_left(self.methods[cuisine], (-newRating, food))
        self.rate[food] = newRating


    def highestRated(self, cuisine: str) -> str:
        return self.methods[cuisine][0][1]

# ["FoodRatings","changeRating","highestRated","changeRating","changeRating","changeRating","highestRated","highestRated"]
# [,["qnvseohnoe",11],["fajbervsj"],["emgqdbo",3],["jmvfxjohq",9],["emgqdbo",14],["fajbervsj"],["snaxol"]]
so = FoodRatings(["emgqdbo","jmvfxjohq","qnvseohnoe","yhptazyko","ocqmvmwjq"],["snaxol","snaxol","snaxol","fajbervsj","fajbervsj"],[2,6,18,6,5])

print(so.changeRating("qnvseohnoe", 11))
print(so.highestRated("fajbervsj"))
print(so.changeRating("emgqdbo", 3))
print(so.changeRating("jmvfxjohq", 9))
print(so.changeRating("emgqdbo", 14))
print(so.highestRated("fajbervsj"))
print(so.highestRated("snaxol"))



# ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
so = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
print(so.highestRated("korean"))
print(so.highestRated("japanese"))
print(so.changeRating("sushi", 16))
print(so.highestRated("japanese"))
print(so.changeRating("ramen", 16))
print(so.highestRated("japanese"))




