# 现有一棵由 n 个节点组成的无向树，节点编号从 0 到 n - 1 ，共有 n - 1 条边。
#
# 给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。另给你一个整数数组 restricted 表示 受限 节点。
#
# 在不访问受限节点的前提下，返回你可以从节点 0 到达的 最多 节点数目。
#
# 注意，节点 0 不 会标记为受限节点。
#
# 
#
# 示例 1：
#
#
# 输入：n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
# 输出：4
# 解释：上图所示正是这棵树。
# 在不访问受限节点的前提下，只有节点 [0,1,2,3] 可以从节点 0 到达。
# 示例 2：
#
#
# 输入：n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
# 输出：3
# 解释：上图所示正是这棵树。
# 在不访问受限节点的前提下，只有节点 [0,5,6] 可以从节点 0 到达。
# 
#
# 提示：
#
# 2 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges 表示一棵有效的树
# 1 <= restricted.length < n
# 1 <= restricted[i] < n
# restricted 中的所有值 互不相同

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
    def reachableNodes1(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        d = defaultdict(set)
        restricted = set(restricted)
        for e in edges:
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])
        ans = set()
        queue = [0]
        while len(queue) > 0:
            node = queue.pop(0)
            if node not in ans and node not in restricted:
                for n in d[node]:
                    if n not in ans and node not in restricted:
                        queue.append(n)
                ans.add(node)
        return len(ans)

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # 2024/3/2 DFS写法
        g = defaultdict(list)
        restricted = set(restricted)
        for x, y  in edges:
            g[x].append(y)
            g[y].append(x)
        def dfs(x, fa):
            if x in restricted:
                return 0
            res = 1
            for y in g[x]:
                if y != fa:
                    res += dfs(y, x)
            return res
        return dfs(0, -1)


so = Solution()
print(so.reachableNodes(n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]))
print(so.reachableNodes(n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]))




