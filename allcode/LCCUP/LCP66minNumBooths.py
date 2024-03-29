# 力扣嘉年华将举办一系列展览活动，后勤部将负责为每场展览提供所需要的展台。 已知后勤部得到了一份需求清单，记录了近期展览所需要的展台类型， demand[i][j] 表示第 i 天展览时第 j 个展台的类型。 在满足每一天展台需求的基础上，请返回后勤部需要准备的 最小 展台数量。
#
# 注意：
#
# 同一展台在不同天中可以重复使用。
# 示例 1：
#
# 输入：demand = ["acd","bed","accd"]
#
# 输出：6
#
# 解释： 第 0 天需要展台 a、c、d； 第 1 天需要展台 b、e、d； 第 2 天需要展台 a、c、c、d； 因此，后勤部准备 abccde 的展台，可以满足每天的展览需求;
#
# 示例 2：
#
# 输入：demand = ["abc","ab","ac","b"]
#
# 输出：3
#
# 提示：
#
# 1 <= demand.length,demand[i].length <= 100
# demand[i][j] 仅为小写字母

from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import math
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
import heapq
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache, cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

import string
# string.digits  表示 0123456789
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        counter = Counter()
        for de in demand:
            ct = Counter(de)
            for x, y in ct.items():
                counter[x] = max(counter[x], y)
        return sum(counter.values())


so = Solution()
print(so.minNumBooths(["acd","bed","accd"]))
print(so.minNumBooths(["abc","ab","ac","b"]))




