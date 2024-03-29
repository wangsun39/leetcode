# 「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。
#
# 游戏地图用大小为 m x n 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。
#
# 现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：
#
# 玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
# 地板用字符 '.' 表示，意味着可以自由行走。
# 墙用字符 '#' 表示，意味着障碍物，不能通行。
# 箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
# 玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
# 玩家无法越过箱子。
# 返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [["#","#","#","#","#","#"],
#              ["#","T","#","#","#","#"],
#              ["#",".",".","B",".","#"],
#              ["#",".","#","#",".","#"],
#              ["#",".",".",".","S","#"],
#              ["#","#","#","#","#","#"]]
# 输出：3
# 解释：我们只需要返回推箱子的次数。
# 示例 2：
#
# 输入：grid = [["#","#","#","#","#","#"],
#              ["#","T","#","#","#","#"],
#              ["#",".",".","B",".","#"],
#              ["#","#","#","#",".","#"],
#              ["#",".",".",".","S","#"],
#              ["#","#","#","#","#","#"]]
# 输出：-1
# 示例 3：
#
# 输入：grid = [["#","#","#","#","#","#"],
#              ["#","T",".",".","#","#"],
#              ["#",".","#","B",".","#"],
#              ["#",".",".",".",".","#"],
#              ["#",".",".",".","S","#"],
#              ["#","#","#","#","#","#"]]
# 输出：5
# 解释：向下、向左、向左、向上再向上。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# grid 仅包含字符 '.', '#',  'S' , 'T', 以及 'B'。
# grid 中 'S', 'B' 和 'T' 各只能出现一个。
from functools import cache
from typing import List
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'S':
                    s = (i, j)
                elif grid[i][j] == 'T':
                    t = (i, j)
                elif grid[i][j] == 'B':
                    b = (i, j)

        step = 0
        vis = set()
        def bfs(xb, yb, xp, yp):  # [xb, yb] 箱子坐标， [xp, yp] 人坐标，返回人能到达箱子周围哪些点
            res = []
            vi = set()
            q1 = [[xp, yp]]
            while q1:
                q2 = []
                while q1:
                    x, y = q1.pop(0)
                    dx, dy = abs(x - xb), abs(y - yb)
                    if dx <= 1 and dy <= 1 and dx + dy == 1:
                        res.append([x, y])
                    for u, v in dir:
                        x0, y0 = x + u, y + v
                        if 0 <= x0 < r and 0 <= y0 < c:
                            if (x0, y0) in vi: continue
                            vi.add((x0, y0))
                            if grid[x0][y0] in '.ST':
                                q2.append([x0, y0])
                q1 = q2
            return res

        @cache
        def adj(xb, yb, xp, yp):  # [xb, yb] 箱子坐标， [xp, yp] 人坐标，返回能箱子能走到的相邻点（不含重复点）
            v_adj = bfs(xb, yb, xp, yp)
            res = []
            for x, y in v_adj:
                if (xb, yb, x, y) in vis:
                    continue
                vis.add((xb, yb, x, y))
                u, v = xb * 2 - x, yb * 2 - y  # p 关于 b 的对称点
                if 0 <= u < r and 0 <= v < c:
                    if grid[u][v] in '.ST':
                        res.append([u, v, xb, yb])
            return res



        q1 = [(b[0], b[1], s[0], s[1])]
        while q1:
            q2 = []
            while q1:
                x, y, u, v = q1.pop(0)
                if (x, y) == t:
                    return step
                q2 += adj(x, y, u, v)
            q1 = q2
            step += 1

        return -1





obj = Solution()
print(obj.minPushBox( [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#",".","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]))
print(obj.minPushBox( [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#","#","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]))
print(obj.minPushBox( [["#","#","#","#","#","#"],
             ["#","T",".",".","#","#"],
             ["#",".","#","B",".","#"],
             ["#",".",".",".",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]))

