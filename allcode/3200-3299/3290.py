

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [[-inf] * 4 for _ in range(n)]  # dp[i][j] 前i个数，长度为j的最大值
        dp[0][0] = a[0] * b[0]
        for i in range(1, n):
            for j in range(4):
                if j == 0:
                    dp[i][j] = max(dp[i - 1][j], a[j] * b[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[j] * b[i])
        return dp[-1][-1]



so = Solution()
print(so.maxScore(a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]))
print(so.maxScore(a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]))




