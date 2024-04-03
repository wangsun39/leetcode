# 给你一个下标从 0 开始、大小为 m x n 的整数矩阵 matrix ，新建一个下标从 0 开始、名为 answer 的矩阵。使 answer 与 matrix 相等，接着将其中每个值为 -1 的元素替换为所在列的 最大 元素。
#
# 返回矩阵 answer 。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
# 输出：[[1,2,9],[4,8,6],[7,8,9]]
# 解释：上图显示了发生替换的元素（蓝色区域）。
# - 将单元格 [1][1] 中的值替换为列 1 中的最大值 8 。
# - 将单元格 [0][2] 中的值替换为列 2 中的最大值 9 。
# 示例 2：
#
#
# 输入：matrix = [[3,-1],[5,2]]
# 输出：[[3,2],[5,2]]
# 解释：上图显示了发生替换的元素（蓝色区域）。
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 2 <= m, n <= 50
# -1 <= matrix[i][j] <= 100
# 测试用例中生成的输入满足每列至少包含一个非负整数。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        ans = [[0] * c for _ in range(r)]
        mx = [-2] * c
        for i in range(c):
            for j in range(r):
                mx[i] = max(mx[i], matrix[j][i])
        for i in range(c):
            for j in range(r):
                if matrix[j][i] == -1:
                    ans[j][i] = mx[i]
                else:
                    ans[j][i] = matrix[j][i]
        return ans


so = Solution()
print(so.modifiedMatrix(matrix = [[1,2,-1],[4,-1,6],[7,8,9]]))
print(so.modifiedMatrix(matrix = [[3,-1],[5,2]]))




