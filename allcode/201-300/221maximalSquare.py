# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#  
#
# 示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
# 示例 2：
#
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
# 示例 3：
#
# 输入：matrix = [["0"]]
# 输出：0
#  
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'



from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp1 = [1 if matrix[0][i] == '1' else 0 for i in range(col)]
        res = max(dp1)
        dp2 = [0] * col
        for i in range(1, row):
            dp2[0] = 1 if matrix[i][0] == '1' else 0
            for j in range(1, col):
                dp2[j] = min(dp1[j-1], dp1[j], dp2[j-1]) + 1 if matrix[i][j] == '1' else 0
            res = max(res, max(dp2))
            dp1, dp2 = dp2, dp1
            print(dp2)
        return res * res



so = Solution()
print(so.maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]))  # 4
print(so.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))  # 4
print(so.maximalSquare([["0","1"],["1","0"]]))  # 1
print(so.maximalSquare([["0"]]))  # 0

