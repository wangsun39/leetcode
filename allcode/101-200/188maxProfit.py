# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#  
#
# 示例 1：
#
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 示例 2：
#
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
#  
#
# 提示：
#
# 0 <= k <= 100
# 0 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
from cmath import inf
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)
        if 0 == N or 0 == k:
            return 0
        x = [0 for _ in range(k * 2)]
        for i in range(0, k * 2, 2):
            x[i] = -prices[0]

        for i in range(1, N):
            x[0] = max(x[0], -prices[i])
            for j in range(1, k * 2):
                if j % 2 == 1:
                    x[j] = max(x[j], x[j - 1] + prices[i])
                else:
                    x[j] = max(x[j], x[j-1] - prices[i])

        return max(x)

    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 2023/10/4  DP
        n = len(prices)
        dp1 = [[-inf] * k for _ in range(n)]  # 前 <=i 天买 j + 1 次的最大收益
        dp2 = [[0] * k for _ in range(n)]  # 前 <=i 天卖 j + 1 次的最大收益
        dp1[0][0] = -prices[0]
        for i in range(1, n):
            for j in range(k):
                if i < j:
                    continue
                if j == 0:
                    dp1[i][j] = max(dp1[i - 1][j], dp1[i][j], -prices[i])
                else:
                    dp1[i][j] = max(dp1[i - 1][j], dp2[i - 1][j - 1] - prices[i])
                dp2[i][j] = max(dp2[i - 1][j], dp1[i - 1][j] + prices[i])
        # print(dp1, dp2)
        return max(dp2[-1])


so = Solution()

print(so.maxProfit(2, []))
print(so.maxProfit(2, [2,4,1]))
print(so.maxProfit(7, [3,2,6,5,0,3]))
print(so.maxProfit(2, [2,4,1]))
