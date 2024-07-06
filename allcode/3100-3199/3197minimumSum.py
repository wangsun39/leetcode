# 给你一个二维 二进制 数组 grid。你需要找到 3 个 不重叠、面积 非零 、边在水平方向和竖直方向上的矩形，并且满足 grid 中所有的 1 都在这些矩形的内部。
#
# 返回这些矩形面积之和的 最小 可能值。
#
# 注意，这些矩形可以相接。
#
#
#
# 示例 1：
#
# 输入： grid = [[1,0,1],[1,1,1]]
#
# 输出： 5
#
# 解释：
#
#
#
# 位于 (0, 0) 和 (1, 0) 的 1 被一个面积为 2 的矩形覆盖。
# 位于 (0, 2) 和 (1, 2) 的 1 被一个面积为 2 的矩形覆盖。
# 位于 (1, 1) 的 1 被一个面积为 1 的矩形覆盖。
# 示例 2：
#
# 输入： grid = [[1,0,1,0],[0,1,0,1]]
#
# 输出： 5
#
# 解释：
#
#
#
# 位于 (0, 0) 和 (0, 2) 的 1 被一个面积为 3 的矩形覆盖。
# 位于 (1, 1) 的 1 被一个面积为 1 的矩形覆盖。
# 位于 (1, 3) 的 1 被一个面积为 1 的矩形覆盖。
#
#
# 提示：
#
# 1 <= grid.length, grid[i].length <= 30
# grid[i][j] 是 0 或 1。
# 输入保证 grid 中至少有三个 1 。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        def minimumArea(r1, r2, c1, c2) -> int:
            # 求一个矩形区域内，包含所有1的最小矩形，没有1时，返回1
            left, right, up, down = inf, -inf, -inf, inf
            for i in range(r1, r2):
                for j in range(c1, c2):
                    if grid[i][j]:
                        left = min(left, j)
                        right = max((right, j))
                        up = max(up, i)
                        down = min(down, i)
            if left == inf:
                return 1
            return (right - left + 1) * (up - down + 1)

        ans = inf

        def f():
            nonlocal ans
            # 上中下三个矩形
            for i in range(1, r):
                for j in range(i + 1, r):
                    ans = min(ans, minimumArea(0, i, 0, c) + minimumArea(i, j, 0, c) + minimumArea(j, r, 0, c))
            # 上/左下/右下 三个矩形
            for i in range(1, r):
                for j in range(1, c):
                    ans = min(ans, minimumArea(0, i, 0, c) + minimumArea(i, r, 0, j) + minimumArea(i, r, j, c))
            # 左上/右上/下 三个矩形
            for i in range(1, r):
                for j in range(1, c):
                    ans = min(ans, minimumArea(0, i, 0, j) + minimumArea(0, i, j, c) + minimumArea(i, r, 0, c))

        f()
        grid = list(zip(*grid[::-1]))
        r, c = len(grid), len(grid[0])
        f()
        return ans



so = Solution()
print(so.minimumSum([[1,0,1],[1,1,1]]))
print(so.minimumSum([[1,0,1,0],[0,1,0,1]]))




