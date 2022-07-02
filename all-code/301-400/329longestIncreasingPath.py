# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
#
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
#
#  
#
# 示例 1：
#
#
# 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
# 输出：4
# 解释：最长递增路径为 [1, 2, 6, 9]。
# 示例 2：
#
#
# 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
# 输出：4
# 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 示例 3：
#
# 输入：matrix = [[1]]
# 输出：1
#  
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1


from typing import List
from functools import lru_cache
class Solution:
    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        res = 1
        def update(i, j):  # 自底向上的遍历
            nonlocal res
            if i > 0 and matrix[i][j] < matrix[i - 1][j] and dp[i][j] + 1 > dp[i - 1][j]:
                dp[i - 1][j] = dp[i][j] + 1
                res = max(res, dp[i - 1][j])
                update(i - 1, j)
            if j > 0 and matrix[i][j] < matrix[i][j - 1] and dp[i][j] + 1 > dp[i][j - 1]:
                dp[i][j - 1] = dp[i][j] + 1
                res = max(res, dp[i][j - 1])
                update(i, j - 1)
            if i < row - 1 and matrix[i][j] < matrix[i + 1][j] and dp[i][j] + 1 > dp[i + 1][j]:
                dp[i + 1][j] = dp[i][j] + 1
                res = max(res, dp[i + 1][j])
                update(i + 1, j)
            if j < col - 1 and matrix[i][j] < matrix[i][j + 1] and dp[i][j] + 1 > dp[i][j + 1]:
                dp[i][j + 1] = dp[i][j] + 1
                res = max(res, dp[i][j + 1])
                update(i, j + 1)
        for i in range(row):
            for j in range(col):
                if dp[i][j] == 0:
                    dp[i][j] = 1
                    update(i, j)
        print(dp)
        return max(map(max, dp))

    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:  # 这个性能优于上一种解法，避免的每个dp[i][j]多次更新，相当与自顶向下的遍历
        Dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row = len(matrix)
        col = len(matrix[0])
        res = 1
        @lru_cache(None)
        def get(i, j):
            nonlocal res
            length = 0
            for [x, y] in Dirs:
                ni, nj = i + x, j + y
                if 0 <= ni < row and 0 <= nj < col and matrix[i][j] > matrix[ni][nj]:
                    length = max(length, get(ni, nj) + 1)
            length = max(1, length)
            res = max(res, length)
            return length
        for i in range(row):
            for j in range(col):
                get(i, j)
        return res

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:  # 与上个解法类似，自己保存dp数组,不用Dirs可以减少比较的次数
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        def get(i, j):
            if dp[i][j] > 0:
                return dp[i][j]
            a1 = get(i - 1, j) if i and matrix[i][j] < matrix[i - 1][j] else 0
            a2 = get(i, j + 1) if j + 1 < col and matrix[i][j] < matrix[i][j + 1] else 0
            a3 = get(i + 1, j) if i + 1 < row and matrix[i][j] < matrix[i + 1][j] else 0
            a4 = get(i, j - 1) if j and matrix[i][j] < matrix[i][j - 1] else 0
            dp[i][j] = max(a1, a2, a3, a4) + 1
            return dp[i][j]
        res = 1
        for i in range(row):
            for j in range(col):
                res = max(res, get(i, j))
        return res


so = Solution()
print('res =', so.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print('res =', so.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))



