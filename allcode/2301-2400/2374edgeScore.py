# 给你一个有向图，图中有 n 个节点，节点编号从 0 到 n - 1 ，其中每个节点都 恰有一条 出边。
#
# 图由一个下标从 0 开始、长度为 n 的整数数组 edges 表示，其中 edges[i] 表示存在一条从节点 i 到节点 edges[i] 的 有向 边。
#
# 节点 i 的 边积分 定义为：所有存在一条指向节点 i 的边的节点的 编号 总和。
#
# 返回 边积分 最高的节点。如果多个节点的 边积分 相同，返回编号 最小 的那个。
#
#  
#
# 示例 1：
#
#
# 输入：edges = [1,0,0,0,0,7,7,5]
# 输出：7
# 解释：
# - 节点 1、2、3 和 4 都有指向节点 0 的边，节点 0 的边积分等于 1 + 2 + 3 + 4 = 10 。
# - 节点 0 有一条指向节点 1 的边，节点 1 的边积分等于 0 。
# - 节点 7 有一条指向节点 5 的边，节点 5 的边积分等于 7 。
# - 节点 5 和 6 都有指向节点 7 的边，节点 7 的边积分等于 5 + 6 = 11 。
# 节点 7 的边积分最高，所以返回 7 。
# 示例 2：
#
#
# 输入：edges = [2,0,0,2]
# 输出：0
# 解释：
# - 节点 1 和 2 都有指向节点 0 的边，节点 0 的边积分等于 1 + 2 = 3 。
# - 节点 0 和 3 都有指向节点 2 的边，节点 2 的边积分等于 0 + 3 = 3 。
# 节点 0 和 2 的边积分都是 3 。由于节点 0 的编号更小，返回 0 。
#  
#
# 提示：
#
# n == edges.length
# 2 <= n <= 105
# 0 <= edges[i] < n
# edges[i] != i


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

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        integral = [0] * n
        for idx, val in enumerate(edges):
            integral[val] += idx
        id, mx = 0, 0
        for idx, val in enumerate(integral):
            if val > mx:
                id = idx
                mx = val
        return id



so = Solution()
print(so.edgeScore([1,0,0,0,0,7,7,5]))
print(so.edgeScore([2,0,0,2]))




