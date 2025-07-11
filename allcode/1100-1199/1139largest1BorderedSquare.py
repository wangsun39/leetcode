# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。
#
#
#
# 示例 1：
#
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
# 示例 2：
#
# 输入：grid = [[1,1,0,0]]
# 输出：1
#
#
# 提示：
#
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] 为 0 或 1

from leetcode.allcode.competition.mypackage import *


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        r, l = len(grid), len(grid[0])
        x1 = [[[0] * 2 for _ in range(l)] for _ in range(r)]  # (i, j) 上侧 和 左侧 连续 1 的个数
        x2 = [[[0] * 2 for _ in range(l)] for _ in range(r)]  # (i, j) 下侧 和 右侧 连续 1 的个数
        x1[0][0], x2[-1][-1] = [grid[0][0], grid[0][0]], [grid[-1][-1], grid[-1][-1]]
        for i in range(r):
            for j in range(l):
                if grid[i][j] == 0:
                    continue
                x1[i][j] = [1, 1]
                if i > 0:
                    x1[i][j][0] = x1[i - 1][j][0] + 1
                if j > 0:
                    x1[i][j][1] = x1[i][j - 1][1] + 1
        for i in range(r - 1, -1, -1):
            for j in range(l - 1, -1, -1):
                if grid[i][j] == 0:
                    continue
                x2[i][j] = [1, 1]
                if i < r - 1:
                    x2[i][j][0] = x2[i + 1][j][0] + 1
                if j < l - 1:
                    x2[i][j][1] = x2[i][j + 1][1] + 1
        print(x1)
        print(x2)
        max_l = 0
        for i in range(r):
            for j in range(l):
                k = max_l
                while i + k < r and j + k < l:
                    mn = min(min(x2[i][j]), min(x1[i + k][j + k]))
                    if mn >= k + 1:
                        max_l = max(max_l, k + 1)
                    k += 1
        return max_l * max_l




obj = Solution()
print(obj.largest1BorderedSquare([[1,0],[0,1]]))
print(obj.largest1BorderedSquare([[0,0,0,1]]))
print(obj.largest1BorderedSquare([[1,1,0,0]]))
print(obj.largest1BorderedSquare(grid = [[0]]))
print(obj.largest1BorderedSquare(grid = [[1,1,1],[1,0,1],[1,1,1]]))

