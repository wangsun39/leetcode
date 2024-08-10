# 给你一个 m x n 的二进制矩阵 grid 。
#
# 如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。
#
# 你可以将 grid 中任意格子的值 翻转 ，也就是将格子里的值从 0 变成 1 ，或者从 1 变成 0 。
#
# 请你返回 最少 翻转次数，使得矩阵中 所有 行和列都是 回文的 ，且矩阵中 1 的数目可以被 4 整除 。
#
#
#
# 示例 1：
#
# 输入：grid = [[1,0,0],[0,1,0],[0,0,1]]
#
# 输出：3
#
# 解释：
#
#
#
# 示例 2：
#
# 输入：grid = [[0,1],[0,1],[0,0]]
#
# 输出：2
#
# 解释：
#
#
#
# 示例 3：
#
# 输入：grid = [[1],[1]]
#
# 输出：2
#
# 解释：
#
#
#
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m * n <= 2 * 105
# 0 <= grid[i][j] <= 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        ans = 0
        for i in range(r // 2):
            for j in range(c // 2):
                v1 = grid[i][j]
                v2 = grid[r - i - 1][j]
                v3 = grid[i][c - j - 1]
                v4 = grid[r - i - 1][c - j - 1]
                counter = Counter([v1, v2, v3, v4])
                add = min(4 - counter[1], counter[1])
                ans += add
        mid_one = 0  # 中间的行列有多少已经成对的1
        pairs = 0  # 中间行列有多少对不成对的(0，1)
        if r & 1:
            for j in range(c // 2):
                if grid[r // 2][j] == grid[r // 2][c - j - 1] == 1:
                    mid_one += 2
                elif grid[r // 2][j] != grid[r // 2][c - j - 1]:
                    pairs += 1
        if c & 1:
            for i in range(r // 2):
                if grid[i][c // 2] == grid[r - i - 1][c // 2] == 1:
                    mid_one += 2
                elif grid[i][c // 2] != grid[r - i - 1][c // 2]:
                    pairs += 1
        if r & 1 and c & 1 and grid[r // 2][c // 2]:
            mid_one += 1
        r = mid_one % 4
        if r == 0:
            return ans + pairs
        if r == 2:
            if pairs > 0:
                return ans + pairs
            return ans + pairs + 2
        if r == 1:
            return ans + pairs + 1
        if r == 3:
            if pairs > 0:
                return ans + pairs + 1
            else:
                return ans + pairs + 3



so = Solution()
print(so.minFlips(grid = [[0]]))
print(so.minFlips(grid = [[1,0,0],[0,1,0],[0,0,1]]))
print(so.minFlips(grid = [[0,1],[0,1],[0,0]]))
print(so.minFlips(grid = [[1],[1]]))




