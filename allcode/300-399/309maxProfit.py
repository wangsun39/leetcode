from cmath import inf
from typing import List
from collections import defaultdict

# 给定一个整数数组，其中第i个元素代表了第i天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#


class Solution:

    def maxProfit1(self, prices: List[int]) -> int:
        N = len(prices)
        # dp[n] = [a, b, c] 表示第n天， a 表示当前持有股票的最大收益， b表示当前不持有股票但可以购买的最大收益，c表示在冷冻期的最大收益
        dp = [[0 for _ in range(3)] for _ in range(N)]
        dp[0][0], dp[0][1], dp[0][2] = -prices[0], 0, 0
        for i in range(1, N):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0] + prices[i]
        return max(dp[-1][1], dp[-1][2])

    def maxProfit(self, prices: List[int]) -> int:
        # 2023/10/05
        n = len(prices)
        dp1 = [-inf] * (n + 1)  # 当天买
        dp2 = [-inf] * (n + 1)  # 当天卖
        dp3 = [-inf] * (n + 1)  # 空窗期
        dp4 = [-inf] * (n + 1)  # 手上有股票
        dp5 = [0] * (n + 1)     # 手上无股票
        for i in range(n):
            dp1[i + 1] = max(dp3[i] - prices[i], dp5[i] - prices[i])
            dp2[i + 1] = max(dp1[i] + prices[i], dp4[i] + prices[i])
            dp3[i + 1] = dp2[i]
            dp4[i + 1] = max(dp1[i], dp4[i])
            dp5[i + 1] = max(dp2[i], dp3[i], dp5[i])
        return max(dp1[-1], dp2[-1], dp3[-1], dp4[-1], dp5[-1])


so = Solution()
print(so.maxProfit([1,2,3,0,2]))
print(so.maxProfit([5,7,11,13,17,19,29,43,47,53]))

