# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
#
#
#
# 示例 1：
#
# 输入：matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# 输出：15
# 解释：
# 边长为 1 的正方形有 10 个。
# 边长为 2 的正方形有 4 个。
# 边长为 3 的正方形有 1 个。
# 正方形的总数 = 10 + 4 + 1 = 15.
# 示例 2：
#
# 输入：matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# 输出：7
# 解释：
# 边长为 1 的正方形有 6 个。
# 边长为 2 的正方形有 1 个。
# 正方形的总数 = 6 + 1 = 7.
#
#
# 提示：
#
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        left = [[0] * c for _ in range(r)]  # [i][j] 左侧有多少个连续1
        upper = [[0] * c for _ in range(r)]  # [i][j] 上方有多少个连续1
        cube = [[0] * c for _ in range(r)]  # 以 [i][j] 为右下角的方形最大边长
        ans = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0: continue
                left[i][j] = upper[i][j] = 1
                if i:
                    upper[i][j] = max(upper[i - 1][j] + 1, upper[i][j])
                if j:
                    left[i][j] = max(left[i][j - 1] + 1, left[i][j])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0: continue
                if i == 0 or j == 0:
                    cube[i][j] = matrix[i][j]
                else:
                    cube[i][j] = min(cube[i - 1][j - 1] + 1, upper[i][j], left[i][j])
                ans += cube[i][j]
        return ans




so = Solution()
print(so.countSquares(matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))
print(so.countSquares(matrix =
[
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]))




