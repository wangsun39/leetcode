# 给你一棵 n个节点的树（连通无向无环的图），节点编号从0到n - 1且恰好有n - 1条边。
#
# 给你一个长度为 n下标从 0开始的整数数组vals，分别表示每个节点的值。同时给你一个二维整数数组edges，其中edges[i] = [ai, bi]表示节点ai 和bi之间有一条无向边。
#
# 一条 好路径需要满足以下条件：
#
# 开始节点和结束节点的值 相同。
# 开始节点和结束节点中间的所有节点值都 小于等于开始节点的值（也就是说开始节点的值应该是路径上所有节点的最大值）。
# 请你返回不同好路径的数目。
#
# 注意，一条路径和它反向的路径算作 同一路径。比方说，0 -> 1与1 -> 0视为同一条路径。单个节点也视为一条合法路径。
#
#
#
# 示例1：
#
#
#
# 输入：vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
# 输出：6
# 解释：总共有 5 条单个节点的好路径。
# 还有 1 条好路径：1 -> 0 -> 2 -> 4 。
# （反方向的路径 4 -> 2 -> 0 -> 1 视为跟 1 -> 0 -> 2 -> 4 一样的路径）
# 注意 0 -> 2 -> 3 不是一条好路径，因为 vals[2] > vals[0] 。
# 示例 2：
#
#
#
# 输入：vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
# 输出：7
# 解释：总共有 5 条单个节点的好路径。
# 还有 2 条好路径：0 -> 1 和 2 -> 3 。
# 示例 3：
#
#
#
# 输入：vals = [1], edges = []
# 输出：1
# 解释：这棵树只有一个节点，所以只有一条好路径。
#
#
# 提示：
#
# n == vals.length
# 1 <= n <= 3 * 104
# 0 <= vals[i] <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges表示一棵合法的树。
#
# https://leetcode.cn/problems/number-of-good-paths


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





so = Solution()
print(so.numberOfGoodPaths([2,5,5,1,5,2,3,5,1,5], [[0,1],[2,1],[3,2],[3,4],[3,5],[5,6],[1,7],[8,4],[9,7]]))
print(so.numberOfGoodPaths(vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]))
print(so.numberOfGoodPaths(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))
print(so.numberOfGoodPaths(vals = [1], edges = []))




