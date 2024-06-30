# 给你一个二维 二进制 数组 grid。请你找出一个边在水平方向和竖直方向上、面积 最小 的矩形，并且满足 grid 中所有的 1 都在矩形的内部。
#
# 返回这个矩形可能的 最小 面积。
#
#
#
# 示例 1：
#
# 输入： grid = [[0,1,0],[1,0,1]]
#
# 输出： 6
#
# 解释：
#
#
#
# 这个最小矩形的高度为 2，宽度为 3，因此面积为 2 * 3 = 6。
#
# 示例 2：
#
# 输入： grid = [[0,0],[1,0]]
#
# 输出： 1
#
# 解释：
#
#
#
# 这个最小矩形的高度和宽度都是 1，因此面积为 1 * 1 = 1。
#
#
#
# 提示：
#
# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] 是 0 或 1。
# 输入保证 grid 中至少有一个 1 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        left, right, up, down = inf, -inf, -inf, inf
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    left = min(left, j)
                    right = max((right, j))
                    up = max(up, i)
                    down = min(down, i)
        return (right - left + 1) * (up - down + 1)


so = Solution()
print(so.minimumArea([[0,1,0],[1,0,1]]))




