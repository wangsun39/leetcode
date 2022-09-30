# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
#
#  
#
# 示例 1：
#
# 输入：
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出：
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2：
#
# 输入：
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出：
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#
# https://leetcode.cn/problems/zero-matrix-lcci





from typing import List

from collections import Counter

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0, col0 = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row0.add(i)
                    col0.add(j)
        for i in row0:
            matrix[i] = [0] * n
        for i in col0:
            for j in range(m):
                matrix[j][i] = 0
        print(matrix)
        return

so = Solution()
print(so.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))
print(so.setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
]))




