# 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
#
# 请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
#
#
# 示例 1：
#
#
#
# 输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# 输出：2
# 解释：总和小于或等于 4 的正方形的最大边长为 2，如图所示。
# 示例 2：
#
# 输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# 输出：0
#
#
# 提示：
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 104
# 0 <= threshold <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # 1. 计算 mat 的二维前缀和
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

        ans = 0
        for i in range(m):
            for j in range(n):
                for k in range(1, min(i, j) + 2):
                    # k 为边长，[i, j] 是正方形右下角
                    # [i - k, j - k], [i, j - k], [i - k, j]
                    v1 = s[i - k + 1][j - k + 1]
                    v2 = s[i - k + 1][j + 1]
                    v3 = s[i + 1][j - k + 1]
                    v4 = s[i + 1][j + 1]
                    area = v1 + v4 - v2 - v3
                    if threshold >= area:
                        ans = max(ans, k)
        return ans

so = Solution()
print(so.maxSideLength(mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4))
print(so.maxSideLength(mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1))




