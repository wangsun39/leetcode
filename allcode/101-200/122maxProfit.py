# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#  
#
# 示例 1:
#
# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:
#
# 输入: prices = [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:
#
# 输入: prices = [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
#
# 提示：
#
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104


from leetcode.allcode.competition.mypackage import *


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        curMin = prices[0]
        res = 0
        for e in prices[1:]:
            if e > curMin:
                res += (e - curMin)
            curMin = e

        return res

    def maxProfit(self, prices: List[int]) -> int:
        # 2024/4/30 DP
        dp1, dp2 = -inf, 0
        for x in prices:
            dp11 = max(dp2 - x, dp1)
            dp22 = max(dp1 + x, dp2)
            dp1, dp2 = dp11, dp22
            # print(dp1, dp2)
        return dp22


so = Solution()
print(so.maxProfit([7, 1, 5, 3, 6, 4]))
print(so.maxProfit([1,2,3,4,5]))
print(so.maxProfit([7, 6, 4, 3, 1]))

