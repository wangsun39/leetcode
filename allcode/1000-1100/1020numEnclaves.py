# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
#
# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
#
# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
# 示例 2：
#
#
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 的值为 0 或 1

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue, set2 = [], set()  # 开始set2 存放为1的坐标所有元素，将与边界相邻的坐标依次放入queue中
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    if i == 0 or j == 0 or i == row - 1 or j == col - 1:
                        queue.append((i, j))
                    else:
                        set2.add((i, j))
        while len(queue) > 0:
            (e1, e2) = queue.pop(0)
            if (e1 - 1, e2) in set2:
                queue.append((e1 - 1, e2))
                set2.remove((e1 - 1, e2))
            if (e1 + 1, e2) in set2:
                queue.append((e1 + 1, e2))
                set2.remove((e1 + 1, e2))
            if (e1, e2 - 1) in set2:
                queue.append((e1, e2 - 1))
                set2.remove((e1, e2 - 1))
            if (e1, e2 + 1) in set2:
                queue.append((e1, e2 + 1))
                set2.remove((e1, e2 + 1))
        return len(set2)

obj = Solution()
print(obj.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))
print(obj.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))

