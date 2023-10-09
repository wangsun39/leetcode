# 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，每个节点 至多 有一条出边。
#
# 有向图用大小为 n 下标从 0 开始的数组 edges 表示，表示节点 i 有一条有向边指向 edges[i] 。如果节点 i 没有出边，那么 edges[i] == -1 。
#
# 同时给你两个节点 node1 和 node2 。
#
# 请你返回一个从 node1 和 node2 都能到达节点的编号，使节点 node1 和节点 node2 到这个节点的距离 较大值最小化。如果有多个答案，请返回 最小 的节点编号。如果答案不存在，返回 -1 。
#
# 注意 edges 可能包含环。
#
#  
#
# 示例 1：
#
#
#
# 输入：edges = [2,2,3,-1], node1 = 0, node2 = 1
# 输出：2
# 解释：从节点 0 到节点 2 的距离为 1 ，从节点 1 到节点 2 的距离为 1 。
# 两个距离的较大值为 1 。我们无法得到一个比 1 更小的较大值，所以我们返回节点 2 。
# 示例 2：
#
#
#
# 输入：edges = [1,2,-1], node1 = 0, node2 = 2
# 输出：2
# 解释：节点 0 到节点 2 的距离为 2 ，节点 2 到它自己的距离为 0 。
# 两个距离的较大值为 2 。我们无法得到一个比 2 更小的较大值，所以我们返回节点 2 。
#  
#
# 提示：
#
# n == edges.length
# 2 <= n <= 105
# -1 <= edges[i] < n
# edges[i] != i
# 0 <= node1, node2 < n


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
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # if node1 == node2:
        #     return node1
        def find(node):
            d = {}
            distance = 0
            while node not in d and node != -1:
                d[node] = distance
                node = edges[node]
                distance += 1
            return d
        n = len(edges)
        d1, d2 = find(node1), find(node2)
        inter = set(d1.keys()) & set(d2.keys())
        if len(inter) == 0:
            return -1
        ans = [n, n]
        for node in inter:
            dis = max(d1[node], d2[node])
            if dis < ans[0]:
                ans = [dis, node]
            elif dis == ans[0]:
                ans[1] = min(ans[1], node)
        return ans[1]




so = Solution()
print(so.closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 0))
print(so.closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2))
print(so.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))




