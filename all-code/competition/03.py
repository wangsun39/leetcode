
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

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def query(k, trim):
            res = []
            for num in nums:
                res.append(num[-trim:])
            # print(res)
            newArray = [[i, e] for i, e in enumerate(res)]
            n = len(res)
            for i in range(n):
                for j in range(i, n):
                    if newArray[i][1] > newArray[j][1]:
                        newArray[i], newArray[j] = newArray[j], newArray[i]
                    elif newArray[i][1] == newArray[j][1] and newArray[i][0] > newArray[j][0]:
                        newArray[i], newArray[j] = newArray[j], newArray[i]


            # print(newArray, k)
            # print(newArray[k - 1], res.index(newArray[k - 1]))
            return newArray[k - 1][0]
        ans = []
        for qry in queries:
            idx = query(qry[0], qry[1])
            ans.append(idx)
        return ans




so = Solution()
# [1, 2, 11, 10, 7, 0, 0, 1, 13, 13, 2, 12]
print(so.smallestTrimmedNumbers(["64333639502","65953866768","17845691654","87148775908","58954177897","70439926174","48059986638","47548857440","18418180516","06364956881","01866627626","36824890579","14672385151","71207752868"], [[9,4],[6,1],[3,8],[12,9],[11,4],[4,9],[2,7],[10,3],[13,1],[13,1],[6,1],[5,10]]))
print(so.smallestTrimmedNumbers(nums = ["24","37","96","04"], queries = [[2,1],[2,2]]))
print(so.smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]))




