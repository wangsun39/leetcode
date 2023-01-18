# 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，其中每个节点 至多 有一条出边。
#
# 图用一个大小为 n 下标从 0 开始的数组 edges 表示，节点 i 到节点 edges[i] 之间有一条有向边。如果节点 i 没有出边，那么 edges[i] == -1 。
#
# 请你返回图中的 最长 环，如果没有任何环，请返回 -1 。
#
# 一个环指的是起点和终点是 同一个 节点的路径。
#
#  
#
# 示例 1：
#
#
#
# 输入：edges = [3,3,4,2,3]
# 输出去：3
# 解释：图中的最长环是：2 -> 4 -> 3 -> 2 。
# 这个环的长度为 3 ，所以返回 3 。
# 示例 2：
#
#
#
# 输入：edges = [2,-1,3,1]
# 输出：-1
# 解释：图中没有任何环。
#  
#
# 提示：
#
# n == edges.length
# 2 <= n <= 105
# -1 <= edges[i] < n
# edges[i] != i


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

import time
class Solution:
    def longestCycle1(self, edges: List[int]) -> int:
        # @lru_cache(None)
        n = len(edges)
        flag = [0] * n
        ans = -1
        def dfs(node):
            nonlocal ans
            if flag[node]:
                return
            d = {}
            dis = 0
            while 0 == flag[node] and -1 != edges[node]:
                d[node] = dis
                dis += 1
                flag[node] = 1
                node = edges[node]
            if -1 == edges[node]:
                return
            if node in d:
                ans = max(ans, dis - d[node])
        for i in range(n):
            dfs(i)
        return ans
    def longestCycle(self, edges: List[int]) -> int:
        # 拓扑排序实现 2023/1/18
        # 这题还是 DFS 更容易实现
        def buildTopo(conditions, n):  # 迭代删除入度为 1 的点
            tree = defaultdict(set)
            pre_num = [0] * n
            for x, y in enumerate(conditions):
                if y != -1 and y not in tree[x]:
                    tree[x].add(y)
                    pre_num[y] += 1
            queue = deque([i for i in range(n) if pre_num[i] == 0])
            ans = set([i for i in range(n)])
            while len(queue):
                q = queue.popleft()
                ans.remove(q)
                for x in tree[q]:
                    pre_num[x] -= 1
                    if pre_num[x] == 0:
                        queue.append(x)
            return list(ans)
        n = len(edges)
        # start = time.time_ns()
        remain = buildTopo(edges, n)
        # print((time.time_ns() - start) / (1000 * 1000))
        # if len(remain) == 0: return -1
        flag = {k: 0 for k in remain}
        ans = -1
        for x in remain:
            if flag[x] > 0: continue
            length = 0
            while flag[x] == 0:
                flag[x] = 1
                length += 1
                x = edges[x]
            ans = max(ans, length)
        # print((time.time_ns() - start) / (1000 * 1000))
        return ans




so = Solution()
print(so.longestCycle([3,3,4,2,3]))
print(so.longestCycle([2,-1,3,1]))




