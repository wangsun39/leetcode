# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。
#
# 请返回 封闭岛屿 的数目。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
# 示例 2：
#
#
#
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
# 示例 3：
#
# 输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#
#
# 提示：
#
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1


from typing import List
from collections import Counter, defaultdict


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        fa = {}
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    fa[(i, j)] = (i, j)

        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa[find(y)] = find(x)

        for i in range(r):
            for j in range(c):
                if grid[i][j]: continue
                if i + 1 < r and grid[i + 1][j] == 0:
                    union((i, j), (i + 1, j))
                if j + 1 < c and grid[i][j + 1] == 0:
                    union((i, j), (i, j + 1))
        s1 = set()  # 记录 所有土地 的 fa
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    s1.add(find((i, j)))
        for i in range(r):
            if grid[i][0] == 0:
                s1 -= {find((i, 0))}
            if grid[i][c - 1] == 0:
                s1 -= {find((i, c - 1))}
        for i in range(c):
            if grid[0][i] == 0:
                s1 -= {find((0, i))}
            if grid[r - 1][i] == 0:
                s1 -= {find((r - 1, i))}
        return len(s1)



obj = Solution()
print(obj.closedIsland( grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
print(obj.closedIsland( grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
print(obj.closedIsland( grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]))

