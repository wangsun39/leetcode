# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
#
# 给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。
#
# 答案可能很大，你需要对 109 + 7 取模 。
#
#
#
# 示例 1：
#
# 输入：n = 1, k = 6, target = 3
# 输出：1
# 解释：你扔一个有 6 个面的骰子。
# 得到 3 的和只有一种方法。
# 示例 2：
#
# 输入：n = 2, k = 6, target = 7
# 输出：6
# 解释：你扔两个骰子，每个骰子有 6 个面。
# 得到 7 的和有 6 种方法：1+6 2+5 3+4 4+3 5+2 6+1。
# 示例 3：
#
# 输入：n = 30, k = 30, target = 500
# 输出：222616187
# 解释：返回的结果必须是对 109 + 7 取模。
#
#
# 提示：
#
# 1 <= n, k <= 30
# 1 <= target <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (target + 1) for _ in range(n)]  # dp[i][j]  前i个骰子，得分为j的总数
        # dp[i][j] = dp[i-1][j-1]+dp[i-1][j-2]+dp[i-1][j-3]+...+dp[i-1][j-k]
        # dp[i][j-1] =            dp[i-1][j-2]+dp[i-1][j-3]+...+dp[i-1][j-k]+dp[i-1][j-k-1]
        # 得到O(1)的递推公式： dp[i][j]=dp[i][j-1]+dp[i-1][j-1]-dp[i-1][j-k-1]
        for i in range(1, k + 1):
            if i > target: break
            dp[0][i] = 1
        for i in range(1, n):
            dp[i][i + 1] = 1
            for j in range(i + 2, target + 1):
                dp[i][j] = dp[i][j - 1] \
                         + dp[i - 1][j - 1] \
                         - (dp[i - 1][j - k - 1] if j - k - 1 >= 0 else 0)
                dp[i][j] %= MOD

        return dp[-1][-1]



so = Solution()
print(so.numRollsToTarget(n = 2, k = 6, target = 7))
print(so.numRollsToTarget(n = 1, k = 6, target = 3))
print(so.numRollsToTarget(n = 30, k = 30, target = 500))




