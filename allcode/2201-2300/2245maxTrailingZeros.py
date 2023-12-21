# 给你一个二维整数数组 grid ，大小为 m x n，其中每个单元格都含一个正整数。
#
# 转角路径 定义为：包含至多一个弯的一组相邻单元。具体而言，路径应该完全 向水平方向 或者 向竖直方向 移动过弯（如果存在弯），而不能访问之前访问过的单元格。在过弯之后，路径应当完全朝 另一个 方向行进：如果之前是向水平方向，那么就应该变为向竖直方向；反之亦然。当然，同样不能访问之前已经访问过的单元格。
#
# 一条路径的 乘积 定义为：路径上所有值的乘积。
#
# 请你从 grid 中找出一条乘积中尾随零数目最多的转角路径，并返回该路径中尾随零的数目。
#
# 注意：
#
# 水平 移动是指向左或右移动。
# 竖直 移动是指向上或下移动。
#
#
# 示例 1：
#
#
#
# 输入：grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
# 输出：3
# 解释：左侧的图展示了一条有效的转角路径。
# 其乘积为 15 * 20 * 6 * 1 * 10 = 18000 ，共计 3 个尾随零。
# 可以证明在这条转角路径的乘积中尾随零数目最多。
#
# 中间的图不是一条有效的转角路径，因为它有不止一个弯。
# 右侧的图也不是一条有效的转角路径，因为它需要重复访问已经访问过的单元格。
# 示例 2：
#
#
#
# 输入：grid = [[4,3,2],[7,6,1],[8,8,8]]
# 输出：0
# 解释：网格如上图所示。
# 不存在乘积含尾随零的转角路径。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 1 <= grid[i][j] <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dir = {0: [-1, 0], 1: [1, 0], 2: [0, -1], 3: [0, 1]}

        @cache
        def count(x):
            n0 = n2 = n5 = 0
            while x % 10 == 0:
                n0 += 1
                x //= 10
            y = x
            while y % 2 == 0:
                n2 += 1
                y //= 2
            y = x
            while y % 5 == 0:
                n5 += 1
                y //= 5
            return n0, n2, n5


        def dfs(x, y, d, turned):
            x0, y0 = dir[d]
            res = 0
            for i in range(max(r, c)):
                u, v = x + x0, y + y0
                if 0 <= u < r and 0 <= v < c:
                    u0, u5, u2 = dfs(u, v, d, turned)
                    x0, x5, x2 = count(grid[x][y])
                    c0, c5, c2 = u0 + x0, u5 + x5, u2 + x2
                    res = max(res, c0 + min(c5, c2))





so = Solution()
print(so.maxTrailingZeros())




