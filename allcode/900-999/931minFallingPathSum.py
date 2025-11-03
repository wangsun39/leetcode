# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
#
# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
#
#
#
# 示例 1：
#
#
#
# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 输出：13
# 解释：如图所示，为和最小的两条下降路径
# 示例 2：
#
#
#
# 输入：matrix = [[-19,57],[-40,-5]]
# 输出：-59
# 解释：如图所示，为和最小的下降路径
#
#
# 提示：
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
from leetcode.allcode.competition.mypackage import *

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        dp1, dp2 = matrix[0][:], [-inf] * c
        for i in range(1, r):
            for j in range(c):
                pre = dp1[j]
                if j:
                    pre = min(pre, dp1[j - 1])
                if j < c - 1:
                    pre  = min(pre, dp1[j + 1])
                dp2[j] = pre + matrix[i][j]
            dp1, dp2 = dp2, [-inf] * c
        return min(dp1)


so = Solution()
