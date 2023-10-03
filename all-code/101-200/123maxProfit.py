# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#  
#
# 示例 1:
#
# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 示例 2：
#
# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3：
#
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
# 示例 4：
#
# 输入：prices = [1]
# 输出：0
#  
#
# 提示：
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 105



from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        N = len(prices)
        x1, x2, x3, x4 = -prices[0], 0, -prices[0], 0
        for i in range(1, N):
            x1 = max(x1, -prices[i]) # 前i天，买一次后的最大利润
            x2 = max(x2, prices[i] + x1)  # 前i天买卖一次的最大利润， 其中：prices[i] + x1 # 第i天卖是第一次卖时，最大利润
            x3 = max(x3, x2 - prices[i]) # 前i天，买2次后的最大利润， 其中：x2 - prices[i] # 第i天买是第二次买时，最大利润
            x4 = max(x4, prices[i] + x3)  # 前i天买卖2次的最大利润， 其中：prices[i] + x3 # 第i天卖是第二次卖时，最大利润

        return max(x2, x4)

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mi = prices[0]
        dp1 = [0] * n   # dp1[i] 表示前i天，包括i，单次最大利润
        for i, x in enumerate(prices[1:], 1):
            dp1[i] = max(dp1[i - 1], x - mi)
            mi = min(mi, x)
        mx = prices[-1]
        dp2 = [0] * n   # dp2[i] 表示从第i天开始向后，单次最大利润
        for i in range(n - 2, -1, -1):
            dp2[i] = max(dp2[i + 1], mx - prices[i])
            mx = max(mx, prices[i])
        ans = dp2[0]
        for i in range(n - 1):
            ans = max(ans, dp1[i] + dp2[i + 1])
        return ans



so = Solution()
print(so.maxProfit([1,2,3,4,5]))
print(so.maxProfit([2,1,4,5,2,9,7]))
print(so.maxProfit([1,4,2]))
print(so.maxProfit([3,3,5,0,0,3,1,4]))
print(so.maxProfit([7, 6, 4, 3, 1]))

