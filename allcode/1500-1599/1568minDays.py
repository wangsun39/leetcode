# 给你一个大小为 m x n ，由若干 0 和 1 组成的二维网格 grid ，其中 1 表示陆地， 0 表示水。岛屿 由水平方向或竖直方向上相邻的 1 （陆地）连接形成。
#
# 如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。
#
# 一天内，可以将 任何单个 陆地单元（1）更改为水单元（0）。
#
# 返回使陆地分离的最少天数。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：2
# 解释：至少需要 2 天才能得到分离的陆地。
# 将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。
# 示例 2：
#
#
# 输入：grid = [[1,1]]
# 输出：2
# 解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] 为 0 或 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(grid), len(grid[0])
        n = r * c
        fa = list(range(n))

        # fa = {x: x for x in nums}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa[find(y)] = find(x)

        land = set()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0: continue
                land.add((i, j))
                for u, v in dir:
                    x, y = i + u, j + v
                    if 0 <= x < r and 0 <= y < c and grid[x][y]:
                        union(x * c + y, i * c + j)

        for i, j in land:
            find(i * c + j)
        if len(set(find(i * c + j) for i, j in land)) > 1:
            return 0

        if len(land) <= 2:
            return len(land)

        def check(x0, y0):  # 检查[x,y] 是否是割点
            nonlocal fa
            land.remove((x0, y0))
            fa = list(range(n))
            for i, j in land:
                for u, v in dir:
                    x, y = i + u, j + v
                    if (x, y) in land:
                        union(x * c + y, i * c + j)
            group = set()
            for i, j in land:
                group.add(find(i * c + j))
            land.add((x0, y0))
            if len(group) > 1:
                return True
            return False
        if any(check(x, y) for x, y in list(land)):
            return 1
        return 2





so = Solution()
print(so.minDays(grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]]))
print(so.minDays(grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]))




