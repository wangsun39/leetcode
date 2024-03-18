# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
# 示例 2：
#
#
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
# 提示：
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
#
#
# 进阶：
#
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？

from leetcode.allcode.competition.mypackage import *

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r, c = len(matrix), len(matrix[0])
        first_row_zero = 0
        first_col_zero = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j]: continue
                # 第一列中有0，first_col_zero = 1， 第一行中有0，first_row_zero = 1
                # 一行中有0，则把第一列的格子置0  （除了第一行）
                # 一列中有0，则把第一行的格子置0  （除了第一列）
                matrix[i][0] = 0
                if i == 0:
                    first_row_zero = 1
                if j == 0:
                    first_col_zero = 1
                if matrix[i][j] == 0 and i != 0 != j:
                    matrix[0][j] = 0
        for i in range(1, r):
            if matrix[i][0] == 0:
                for j in range(1, c):
                    matrix[i][j] = 0
        for j in range(1, c):
            if matrix[0][j] == 0:
                for i in range(1, r):
                    matrix[i][j] = 0
        if first_row_zero:
            for j in range(c):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(r):
                matrix[i][0] = 0
        return matrix


so = Solution()
print(so.setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]]))
print(so.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))




