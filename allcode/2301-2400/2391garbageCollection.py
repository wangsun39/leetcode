# 给你一个下标从 0 开始的字符串数组 garbage ，其中 garbage[i] 表示第 i 个房子的垃圾集合。garbage[i] 只包含字符 'M' ，'P' 和 'G' ，但可能包含多个相同字符，每个字符分别表示一单位的金属、纸和玻璃。垃圾车收拾 一 单位的任何一种垃圾都需要花费 1 分钟。
#
# 同时给你一个下标从 0 开始的整数数组 travel ，其中 travel[i] 是垃圾车从房子 i 行驶到房子 i + 1 需要的分钟数。
#
# 城市里总共有三辆垃圾车，分别收拾三种垃圾。每辆垃圾车都从房子 0 出发，按顺序 到达每一栋房子。但它们 不是必须 到达所有的房子。
#
# 任何时刻只有 一辆 垃圾车处在使用状态。当一辆垃圾车在行驶或者收拾垃圾的时候，另外两辆车 不能 做任何事情。
#
# 请你返回收拾完所有垃圾需要花费的 最少 总分钟数。
#
#  
#
# 示例 1：
#
# 输入：garbage = ["G","P","GP","GG"], travel = [2,4,3]
# 输出：21
# 解释：
# 收拾纸的垃圾车：
# 1. 从房子 0 行驶到房子 1
# 2. 收拾房子 1 的纸垃圾
# 3. 从房子 1 行驶到房子 2
# 4. 收拾房子 2 的纸垃圾
# 收拾纸的垃圾车总共花费 8 分钟收拾完所有的纸垃圾。
# 收拾玻璃的垃圾车：
# 1. 收拾房子 0 的玻璃垃圾
# 2. 从房子 0 行驶到房子 1
# 3. 从房子 1 行驶到房子 2
# 4. 收拾房子 2 的玻璃垃圾
# 5. 从房子 2 行驶到房子 3
# 6. 收拾房子 3 的玻璃垃圾
# 收拾玻璃的垃圾车总共花费 13 分钟收拾完所有的玻璃垃圾。
# 由于没有金属垃圾，收拾金属的垃圾车不需要花费任何时间。
# 所以总共花费 8 + 13 = 21 分钟收拾完所有垃圾。
# 示例 2：
#
# 输入：garbage = ["MMM","PGM","GP"], travel = [3,10]
# 输出：37
# 解释：
# 收拾金属的垃圾车花费 7 分钟收拾完所有的金属垃圾。
# 收拾纸的垃圾车花费 15 分钟收拾完所有的纸垃圾。
# 收拾玻璃的垃圾车花费 15 分钟收拾完所有的玻璃垃圾。
# 总共花费 7 + 15 + 15 = 37 分钟收拾完所有的垃圾。
#  
#
# 提示：
#
# 2 <= garbage.length <= 105
# garbage[i] 只包含字母 'M' ，'P' 和 'G' 。
# 1 <= garbage[i].length <= 10
# travel.length == garbage.length - 1
# 1 <= travel[i] <= 100


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
# heap.heapify(nums)
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

import string
# string.digits  表示 0123456789

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def helper(chr):
            tr = 0
            ans = garbage[0].count(chr)
            for i, gar in enumerate(garbage[1:]):
                tr += travel[i]
                if chr in gar:
                    ans += gar.count(chr)
                    ans += tr
                    tr = 0
            return ans
        ans = helper('P') + helper('M') + helper('G')
        return ans



so = Solution()
print(so.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3]))
print(so.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))




