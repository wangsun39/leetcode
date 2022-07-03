# 给你一个 m x n 的整数网格图 grid ，你可以从一个格子移动到 4 个方向相邻的任意一个格子。
#
# 请你返回在网格图中从 任意 格子出发，达到 任意 格子，且路径中的数字是 严格递增 的路径数目。由于答案可能会很大，请将结果对 109 + 7 取余 后返回。
#
# 如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。
#
#  
#
# 示例 1：
#
#
#
# 输入：grid = [[1,1],[3,4]]
# 输出：8
# 解释：严格递增路径包括：
# - 长度为 1 的路径：[1]，[1]，[3]，[4] 。
# - 长度为 2 的路径：[1 -> 3]，[1 -> 4]，[3 -> 4] 。
# - 长度为 3 的路径：[1 -> 3 -> 4] 。
# 路径数目为 4 + 3 + 1 = 8 。
# 示例 2：
#
# 输入：grid = [[1],[2]]
# 输出：3
# 解释：严格递增路径包括：
# - 长度为 1 的路径：[1]，[2] 。
# - 长度为 2 的路径：[1 -> 2] 。
# 路径数目为 2 + 1 = 3 。
#  
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# 1 <= grid[i][j] <= 105

from typing import List
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
    def countPaths(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        MAX = int(1e9 + 7)

        @lru_cache(None)
        def dfs(i, j):
            res = 1
            dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for d in dir:
                if 0 <= i + d[0] < m and 0 <= j + d[1] < n and grid[i][j] < grid[i + d[0]][j + d[1]]:
                    res += dfs(i  + d[0], j + d[1])
                    res %= MAX
            return res
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)
                ans %= MAX
        return ans


so = Solution()
print(so.countPaths([[1],[2]]))
print(so.countPaths([[1,1],[3,4]]))




