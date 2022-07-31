# 设计一个支持下述操作的食物评分系统：
#
# 修改 系统中列出的某种食物的评分。
# 返回系统中某一类烹饪方式下评分最高的食物。
# 实现 FoodRatings 类：
#
# FoodRatings(String[] foods, String[] cuisines, int[] ratings) 初始化系统。食物由 foods、cuisines 和 ratings 描述，长度均为 n 。
# foods[i] 是第 i 种食物的名字。
# cuisines[i] 是第 i 种食物的烹饪方式。
# ratings[i] 是第 i 种食物的最初评分。
# void changeRating(String food, int newRating) 修改名字为 food 的食物的评分。
# String highestRated(String cuisine) 返回指定烹饪方式 cuisine 下评分最高的食物的名字。如果存在并列，返回 字典序较小 的名字。
# 注意，字符串 x 的字典序比字符串 y 更小的前提是：x 在字典中出现的位置在 y 之前，也就是说，要么 x 是 y 的前缀，或者在满足 x[i] != y[i] 的第一个位置 i 处，x[i] 在字母表中出现的位置在 y[i] 之前。
#
#  
#
# 示例：
#
# 输入
# ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
# [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
# 输出
# [null, "kimchi", "ramen", null, "sushi", null, "ramen"]
#
# 解释
# FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
# foodRatings.highestRated("korean"); // 返回 "kimchi"
#                                     // "kimchi" 是分数最高的韩式料理，评分为 9 。
# foodRatings.highestRated("japanese"); // 返回 "ramen"
#                                       // "ramen" 是分数最高的日式料理，评分为 14 。
# foodRatings.changeRating("sushi", 16); // "sushi" 现在评分变更为 16 。
# foodRatings.highestRated("japanese"); // 返回 "sushi"
#                                       // "sushi" 是分数最高的日式料理，评分为 16 。
# foodRatings.changeRating("ramen", 16); // "ramen" 现在评分变更为 16 。
# foodRatings.highestRated("japanese"); // 返回 "ramen"
#                                       // "sushi" 和 "ramen" 的评分都是 16 。
#                                       // 但是，"ramen" 的字典序比 "sushi" 更小。
#  
#
# 提示：
#
# 1 <= n <= 2 * 104
# n == foods.length == cuisines.length == ratings.length
# 1 <= foods[i].length, cuisines[i].length <= 10
# foods[i]、cuisines[i] 由小写英文字母组成
# 1 <= ratings[i] <= 108
# foods 中的所有字符串 互不相同
# 在对 changeRating 的所有调用中，food 是系统中食物的名字。
# 在对 highestRated 的所有调用中，cuisine 是系统中 至少一种 食物的烹饪方式。
# 最多调用 changeRating 和 highestRated 总计 2 * 104 次

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




