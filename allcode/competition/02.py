# 给你一个下标从 0 开始的整数矩阵 grid 和一个整数 k。
#
# 返回包含 grid 左上角元素、元素和小于或等于 k 的 子矩阵 的
# 数目
# 。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[7,6,3],[6,6,1]], k = 18
# 输出：4
# 解释：如上图所示，只有 4 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 18 。
# 示例 2：
#
#
# 输入：grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
# 输出：6
# 解释：如上图所示，只有 6 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 20 。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= n, m <= 1000
# 0 <= grid[i][j] <= 1000
# 1 <= k <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        s = [[0] * c for _ in range(r)]
        s[0][0] = grid[0][0]
        if s[0][0] > k:
            return 0
        ans = 1
        for i in range(1, c):
            s[0][i] = s[0][i - 1] + grid[0][i]
            if s[0][i] <= k:
                ans += 1
            else:
                break
        for i in range(1, r):
            row = 0
            for j in range(c):
                row += grid[i][j]
                s[i][j] = s[i - 1][j] + row
                if s[i][j] <= k:
                    ans += 1
                else:
                    break
        return ans



so = Solution()
print(so.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18))
print(so.countSubmatrices(grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20))
print(so.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18))




