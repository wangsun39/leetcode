# 给定 M×N 矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。
#
# 示例：
#
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从右下角开始查找
        r, c = len(matrix), len(matrix[0])
        i, j = r - 1, 0
        while j < c and i >= 0:
            if matrix[i][j] == target: return True
            if matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False


so = Solution()




