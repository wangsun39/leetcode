# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1：
#
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
# 示例 2：
#
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row, col = len(grid), len(grid[0])
        fa = {i: i for i in range(row * col) if grid[i // col][i % col] == '1'}
        # print(fa)
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                for d in dir:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < row and 0 <= y < col:
                        if grid[x][y] == '1':
                            union(i * col + j, x * col + y)
        ans = 0
        for k in fa:
            if k == find(k):
                ans += 1
        return ans


so = Solution()
print(so.numIslands(grid = [["1","1","1"],["0","1","0"],["1","1","1"]]))  # 1

print(so.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))  # 1

print(so.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])) # 3

