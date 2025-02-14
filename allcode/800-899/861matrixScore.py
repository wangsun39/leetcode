# 给你一个大小为 m x n 的二元矩阵 grid ，矩阵中每个元素的值为 0 或 1 。
#
# 一次 移动 是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
#
# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的 得分 就是这些数字的总和。
#
# 在执行任意次 移动 后（含 0 次），返回可能的最高分数。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
# 示例 2：
#
# 输入：grid = [[0]]
# 输出：1
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# grid[i][j] 为 0 或 1

from leetcode.allcode.competition.mypackage import *


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        for i in range(r):
            if grid[i][0] == 0:
                grid[i] = [1 ^ x for x in grid[i]]
        for j in range(1, c):
            cnt = sum(grid[i][j] for i in range(r))
            if cnt * 2 < r:
                for i in range(r):
                    grid[i][j] ^= 1
        ans = 0
        for i in range(r):
            for j in range(c):
                ans += grid[i][j] << (c - j - 1)
        return ans


so = Solution()
print(so.matrixScore(grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]))

