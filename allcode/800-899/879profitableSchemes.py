# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
#
# 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
#
# 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
#
# 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。
#
#
#
# 示例 1：
#
# 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。
# 示例 2：
#
# 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
#
#
# 提示：
#
# 1 <= n <= 100
# 0 <= minProfit <= 100
# 1 <= group.length <= 100
# 1 <= group[i] <= 100
# profit.length == group.length
# 0 <= profit[i] <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        m = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m)]  # dp[i][j][k]  前i个工作，参与人数为j，总利润为k的方案总数
        # 其中 dp[i][j][minProfit] 表示前i个工作，参与人数为j，总利润至少为minProfit的方案总数
        for i in range(m):
            dp[i][0][0] = 1
        if group[0] <= n:
            if profit[0] < minProfit:
                dp[0][group[0]][profit[0]] = 1
            else:
                dp[0][group[0]][minProfit] = 1
        for i in range(1, m):
            dp[i] = deepcopy(dp[i - 1])
            if group[i] > n:
                continue
            if profit[i] >= minProfit:
                for j in range(group[i], n + 1):
                    dp[i][j][minProfit] += sum(dp[i - 1][j - group[i]])
                    dp[i][j][minProfit] %= MOD
                continue
            for j in range(group[i], n + 1):
                for k in range(profit[i], minProfit):
                    dp[i][j][k] += dp[i - 1][j - group[i]][k - profit[i]]
                    dp[i][j][k] %= MOD
                for t in range(profit[i] + 1):  # dp[i][j][minProfit] 表示利润 >= minProfit
                    dp[i][j][minProfit] += dp[i - 1][j - group[i]][minProfit - profit[i] + t]
                    dp[i][j][minProfit] %= MOD
        ans = sum(dp[-1][i][minProfit] for i in range(n + 1)) % MOD
        return ans


so = Solution()
print(so.profitableSchemes(n = 5, minProfit = 1, group = [6,3,6,1], profit = [2,0,0,1]))
print(so.profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]))
print(so.profitableSchemes(n = 5, minProfit = 3, group = [2,2], profit = [2,3]))


