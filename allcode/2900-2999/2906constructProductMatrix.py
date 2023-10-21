# 给你一个下标从 0 开始、大小为 n * m 的二维整数矩阵 grid ，定义一个下标从 0 开始、大小为 n * m 的的二维矩阵 p。如果满足以下条件，则称 p 为 grid 的 乘积矩阵 ：
#
# 对于每个元素 p[i][j] ，它的值等于除了 grid[i][j] 外所有元素的乘积。乘积对 12345 取余数。
# 返回 grid 的乘积矩阵。
#
#
#
# 示例 1：
#
# 输入：grid = [[1,2],[3,4]]
# 输出：[[24,12],[8,6]]
# 解释：p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
# p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
# p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
# p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
# 所以答案是 [[24,12],[8,6]] 。
# 示例 2：
#
# 输入：grid = [[12345],[2],[1]]
# 输出：[[2],[0],[0]]
# 解释：p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2
# p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0 ，所以 p[0][1] = 0
# p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0 ，所以 p[0][2] = 0
# 所以答案是 [[2],[0],[0]] 。
#
#
# 提示：
#
# 1 <= n == grid.length <= 105
# 1 <= m == grid[i].length <= 105
# 2 <= n * m <= 105
# 1 <= grid[i][j] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        r, c = len(grid), len(grid[0])
        pre = [[0] * c for _ in range(r)]
        sup = [[0] * c for _ in range(r)]
        ans = [[0] * c for _ in range(r)]
        cur = 1
        for i in range(r):
            for j in range(c):
                pre[i][j] = cur
                cur *= grid[i][j]
                cur %= MOD
        cur = 1
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                sup[i][j] = cur
                cur *= grid[i][j]
                cur %= MOD
        for i in range(r):
            for j in range(c):
                ans[i][j] = (pre[i][j] * sup[i][j]) % MOD
        return ans


so = Solution()
print(so.constructProductMatrix(grid = [[12345],[2],[1]]))
print(so.constructProductMatrix(grid = [[3,2,5],[6,4,3],[6,3,1]]))
print(so.constructProductMatrix(grid = [[1,2],[3,4]]))




