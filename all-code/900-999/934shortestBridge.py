# 给你一个大小为 n x n 的二元矩阵 grid ，其中 1 表示陆地，0 表示水域。
#
# 岛 是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。grid 中 恰好存在两座岛 。
#
# 你可以将任意数量的 0 变为 1 ，以使两座岛连接起来，变成 一座岛 。
#
# 返回必须翻转的 0 的最小数目。
#
#
#
# 示例 1：
#
# 输入：grid = [[0,1],[1,0]]
# 输出：1
# 示例 2：
#
# 输入：grid = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
# 示例 3：
#
# 输入：grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1
#
#
# 提示：
#
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] 为 0 或 1
# grid 中恰有两个岛
# https://leetcode.cn/problems/shortest-bridge/


import copy
from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        island1, island2 = set(), set()
        count = 0
        def dfs(i, j, island):
            island.add((i, j))
            for x, y in dir:
                u, v = i + x, j + y
                if 0 <= u < row and 0 <= v < col and grid[u][v] and (u, v) not in island:
                    dfs(u, v, island)

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    if count == 0:
                        dfs(i, j, island1)
                        count += 1
                    elif (i, j) not in island1:
                        dfs(i, j, island2)
                        break
        print(island1, island2)
        if len(island2) < len(island1): island1, island2 = island2, island1
        ans = 1000
        def bfs(i, j):
            nonlocal ans
            lv = 0
            q = [(i, j), '|']
            flag = [[0] * col for _ in range(row)]
            while len(q) > 1:
                e = q.pop(0)
                if e == '|':
                    lv += 1
                    q.append('|')
                    continue
                for x, y in dir:
                    u, v = e[0] + x, e[1] + y
                    if 0 <= u < row and 0 <= v < col:
                        if 0 == grid[u][v] and 0 == flag[u][v]:
                            flag[u][v] = 1
                            q.append((u, v))
                        elif (u, v) in island2:
                            ans = min(ans, lv)
                            return

        for i, j in island1:
            bfs(i, j)
        return ans


so = Solution()
print(so.shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))  # 1
print(so.shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))  # 2
print(so.shortestBridge(grid = [[0,1],[1,0]]))  # 1

