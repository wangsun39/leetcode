# 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
#
#  
#
# 示例 1：
#
#
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,4,7,5,3,6,8,9]
# 示例 2：
#
# 输入：mat = [[1,2],[3,4]]
# 输出：[1,2,3,4]
#  
#
# 提示：
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105





from typing import List
import random
import bisect
class Solution:

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        row, col = len(mat), len(mat[0])
        cr, cc = 0, 0
        dir = 1
        for i in range(row * col):
            ans.append(mat[cr][cc])
            if 1 == dir:
                if cc + 1 >= col:
                    cr += 1
                    dir = -dir
                elif cr - 1 < 0:
                    # if cc + 1 < col:
                    #     cc += 1
                    # else:
                    #     cr += 1
                    cc += 1
                    dir = -dir
                else:
                    cr -= 1
                    cc += 1
            else:
                if cr + 1 >= row:
                    cc += 1
                    dir = -dir
                elif cc - 1 < 0:
                    cr += 1
                    dir = -dir
                else:
                    cr += 1
                    cc -= 1
        return ans


so = Solution()


