# 在二维网格 grid 上，有 4 种类型的方格：
#
# 1 表示起始方格。且只有一个起始方格。
# 2 表示结束方格，且只有一个结束方格。
# 0 表示我们可以走过的空方格。
# -1 表示我们无法跨越的障碍。
# 返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。
#
# 每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。
#
#
#
# 示例 1：
#
# 输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# 输出：2
# 解释：我们有以下两条路径：
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# 示例 2：
#
# 输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# 输出：4
# 解释：我们有以下四条路径：
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# 示例 3：
#
# 输入：[[0,1],[2,0]]
# 输出：0
# 解释：
# 没有一条路能完全穿过每一个空的方格一次。
# 请注意，起始和结束方格可以位于网格中的任意位置。
#
#
# 提示：
#
# 1 <= grid.length * grid[0].length <= 20
from functools import cache
from math import log
from typing import List, Optional

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(grid), len(grid[0])
        vis = 0  # 表示走过的点
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    start = [i, j]
                    vis |= (1 << (i * c + j))
                elif grid[i][j] == 2:
                    end = [i, j]
                elif grid[i][j] == -1:
                    vis |= (1 << (i * c + j))
        @cache
        def dfs(i, j, vis):
            if end == [i, j]:
                return vis == 2 ** (r * c) - 1
            res = 0
            for u, v in dir:
                x, y = i + u, v + j
                if 0 <= x < r and 0 <= y < c:
                    bit = x * c + y
                    if vis & (1 << bit) == 0:
                        res += dfs(x, y, vis | (1 << bit))
            return res
        return dfs(start[0], start[1], vis)


so = Solution()
print(so.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(so.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(so.uniquePathsIII([[0,1],[2,0]]))

