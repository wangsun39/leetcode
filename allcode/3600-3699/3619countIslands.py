# 给你一个 m x n 的矩阵 grid 和一个正整数 k。一个 岛屿 是由 正 整数（表示陆地）组成的，并且陆地间 四周 连通（水平或垂直）。
#
# 一个岛屿的总价值是该岛屿中所有单元格的值之和。
#
# 返回总价值可以被 k 整除 的岛屿数量。
#
#
#
# 示例 1:
#
#
# 输入: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
#
# 输出: 2
#
# 解释:
#
# 网格中包含四个岛屿。蓝色高亮显示的岛屿的总价值可以被 5 整除，而红色高亮显示的岛屿则不能。
#
# 示例 2:
#
#
# 输入: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
#
# 输出: 6
#
# 解释:
#
# 网格中包含六个岛屿，每个岛屿的总价值都可以被 3 整除。
#
#
#
# 提示:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# 0 <= grid[i][j] <= 106
# 1 <= k < = 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(grid), len(grid[0])
        vis = [[0] * c for _ in range(r)]

        def bfs(x0, y0):
            dq = deque([[x0, y0]])
            s = grid[x0][y0]
            vis[x0][y0] = 1
            while dq:
                x, y = dq.popleft()
                for dx, dy in dir:
                    u, v = x + dx, y + dy
                    if 0 <= u < r and 0 <= v < c and grid[u][v] and vis[u][v] == 0:
                        s += grid[u][v]
                        vis[u][v] = 1
                        dq.append([u, v])
            return s % k == 0

        ans = 0
        for i in range(r):
            for j in range(c):
                if vis[i][j] or grid[i][j] == 0: continue
                if bfs(i, j):
                    ans += 1
        return ans




so = Solution()
print(so.countIslands(grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5))  # 2
print(so.countIslands(grid = [[0,0,0],[0,0,1],[11,0,6],[0,10,2],[0,0,0],[8,0,0]], k = 19))  # 1




