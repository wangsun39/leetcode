# 给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。
#
# 返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。
#
# 注意：本题相对书上原题稍作改动
#
# 示例：
#
# 输入：
# [
#    [-1,0],
#    [0,-1]
# ]
# 输出：[0,1,0,1]
# 解释：输入中标粗的元素即为输出所表示的矩阵
#
#
# 说明：
#
# 1 <= matrix.length, matrix[0].length <= 200


from leetcode.allcode.competition.mypackage import *


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])

        s = [[0] * (c + 1) for _ in range(r + 1)]  # 二维前缀和
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

        def sumRegion(row1: int, col1: int, row2: int, col2: int) -> int:
            return s[row2 + 1][col2 + 1] - s[row1][col2 + 1] - s[row2 + 1][col1] + s[row1][col1]

        mx = matrix[0][0]
        ans = [0, 0, 0, 0]
        for i in range(r):
            for k in range(i + 1):
                dp = [0] * c  # 考虑从k行到i行，以j列结尾的所有子矩阵的最大和
                dp[0] = sumRegion(k, 0, i, 0)
                if mx < dp[0]:
                    ans = [k, 0, i, 0]
                    mx = dp[0]
                for j in range(1, c):
                    dp[j] = max(dp[j], dp[j - 1] + sumRegion(k, j, i, j))
                    if mx < dp[j]:
                        ans = [k, j, i, j]
                        mx = dp[j]
        return ans




so = Solution()
print(so.getMaxMatrix([
   [-1,0],
   [0,-1]
]))





