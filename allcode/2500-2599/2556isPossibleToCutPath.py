# 给你一个下标从 0 开始的 m x n 二进制 矩阵 grid 。你可以从一个格子 (row, col) 移动到格子 (row + 1, col) 或者 (row, col + 1) ，前提是前往的格子值为 1 。如果从 (0, 0) 到 (m - 1, n - 1) 没有任何路径，我们称该矩阵是 不连通 的。
#
# 你可以翻转 最多一个 格子的值（也可以不翻转）。你 不能翻转 格子 (0, 0) 和 (m - 1, n - 1) 。
#
# 如果可以使矩阵不连通，请你返回 true ，否则返回 false 。
#
# 注意 ，翻转一个格子的值，可以使它的值从 0 变 1 ，或从 1 变 0 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[1,1,1],[1,0,0],[1,1,1]]
# 输出：true
# 解释：按照上图所示我们翻转蓝色格子里的值，翻转后从 (0, 0) 到 (2, 2) 没有路径。
# 示例 2：
#
#
#
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：false
# 解释：无法翻转至多一个格子，使 (0, 0) 到 (2, 2) 没有路径。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# grid[0][0] == grid[m - 1][n - 1] == 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        r, c = len(grid), len(grid[0])
        if r == c == 1: return False
        path1 = []
        def dfs1(i, j):  # 尽量沿着上面走的一条路径
            path1.append((i, j))
            if i == r - 1 and j == c - 1:
                return True
            if j < c - 1 and grid[i][j + 1]:
                if dfs1(i, j + 1):
                    return True
            if i < r - 1 and grid[i + 1][j]:
                if dfs1(i + 1, j):
                    return True
            path1.pop()
            return False
        dfs1(0, 0)
        if len(path1) == 0:
            return True
        path2 = []
        def dfs2(i, j):  # 尽量沿着下面走的一条路径
            path2.append((i, j))
            if i == r - 1 and j == c - 1:
                return True
            if i < r - 1 and grid[i + 1][j]:
                if dfs2(i + 1, j):
                    return True
            if j < c - 1 and grid[i][j + 1]:
                if dfs2(i, j + 1):
                    return True
            path2.pop()
            return False

        dfs2(0, 0)
        path1.pop(0)
        path1.pop(-1)
        path2.pop(0)
        path2.pop(-1)
        if len(set(path1) & set(path2)):  # 看两条路径是否有交点
            return True
        return False

so = Solution()
print(so.isPossibleToCutPath(grid = [[1]]))
print(so.isPossibleToCutPath(grid = [[1,1,1],[0,0,0],[1,1,1]]))
print(so.isPossibleToCutPath(grid = [[1,1]]))
print(so.isPossibleToCutPath(grid = [[1,1,1],[1,0,0],[1,1,1]]))
print(so.isPossibleToCutPath(grid = [[1,1,1],[1,0,1],[1,1,1]]))




