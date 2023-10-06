
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
# https://leetcode.cn/problems/number-of-good-paths


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        fa = list(range(n))  # 存放每个点所在连通块的代表元（未必每个点的fa值都是最新的，调用find获取，不要直接fa[i]获取）
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        size = [1] * n  # 存放每个点所属连通块内，具有最大值的节点个数（一般只有每个连通块的代表元的size值是准确的）
        ans = n
        for vx, x in sorted(zip(vals, range(n))):
            fx = find(x)   # 路径压缩 + 找到代表元
            for y in adj[x]:
                y = find(y)  # x, y 之间不比较，而是用他们的代表元进行比较
                if y == fx or vals[y] > vx:  # y == fx 说明y节点已在x节点之前就处理过了，不能重复统计
                    continue
                # 把 x 和 y 所在的连通块合并
                if vals[y] == vx:  # 具有好路径
                    ans += size[y] * size[fa[x]]
                    size[fx] += size[y]
                fa[y] = fx
        return ans

class Solution:
    def func(self):
        n = 10
        fa = list(range(n))
        # fa = {x: x for x in nums}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)
        def setNum():
            ans = 0
            for k in fa:
                if k == find(k):
                    ans += 1
            return ans




