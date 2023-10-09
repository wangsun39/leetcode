# 为了缓解「力扣嘉年华」期间的人流压力，组委会在活动期间开设了一些交通专线。path[i] = [a, b] 表示有一条从地点 a通往地点 b 的 单向 交通专线。
# 若存在一个地点，满足以下要求，我们则称之为 交通枢纽：
#
# 所有地点（除自身外）均有一条 单向 专线 直接 通往该地点；
# 该地点不存在任何 通往其他地点 的单向专线。
# 请返回交通专线的 交通枢纽。若不存在，则返回 -1。
#
# 注意：
#
# 对于任意一个地点，至少被一条专线连通。
# 示例 1：
#
# 输入：path = [[0,1],[0,3],[1,3],[2,0],[2,3]]
#
# 输出：3
#
# 解释：如下图所示：
# 地点 0,1,2 各有一条通往地点 3 的交通专线，
# 且地点 3 不存在任何通往其他地点的交通专线。
#
#
# 示例 2：
#
# 输入：path = [[0,3],[1,0],[1,3],[2,0],[3,0],[3,2]]
#
# 输出：-1
#
# 解释：如下图所示：不存在满足 交通枢纽 的地点。
#
#
# 提示：
#
# 1 <= path.length <= 1000
# 0 <= path[i][0], path[i][1] <= 1000
# path[i][0] 与 path[i][1] 不相等
#
# https://leetcode.cn/problems/D9PW8w


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

from functools import lru_cache
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

class Solution:
    def transportationHub(self, path: List[List[int]]) -> int:
        inner, outer = defaultdict(int), defaultdict(int)
        for x, y in path:
            inner[y] += 1
            outer[x] += 1
        n = len(set(inner.keys()) | set(outer.keys()))
        for k in inner:
            if outer[k] == 0 and inner[k] == n - 1:
                return k
        return -1



so = Solution()
print(so.transportationHub([[0,1],[0,3],[1,3],[2,0],[2,3]]))
print(so.transportationHub([[0,3],[1,0],[1,3],[2,0],[3,0],[3,2]]))




