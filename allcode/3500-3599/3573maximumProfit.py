# 给你一个整数数组 prices，其中 prices[i] 是第 i 天股票的价格（美元），以及一个整数 k。
#
# 你最多可以进行 k 笔交易，每笔交易可以是以下任一类型：
#
# 普通交易：在第 i 天买入，然后在之后的第 j 天卖出，其中 i < j。你的利润是 prices[j] - prices[i]。
#
# 做空交易：在第 i 天卖出，然后在之后的第 j 天买回，其中 i < j。你的利润是 prices[i] - prices[j]。
#
# 注意：你必须在开始下一笔交易之前完成当前交易。此外，你不能在已经进行买入或卖出操作的同一天再次进行买入或卖出操作。
#
# 通过进行 最多 k 笔交易，返回你可以获得的最大总利润。
#
#
#
# 示例 1:
#
# 输入: prices = [1,7,9,8,2], k = 2
#
# 输出: 14
#
# 解释:
#
# 我们可以通过 2 笔交易获得 14 美元的利润：
# 一笔普通交易：第 0 天以 1 美元买入，第 2 天以 9 美元卖出。
# 一笔做空交易：第 3 天以 8 美元卖出，第 4 天以 2 美元买回。
# 示例 2:
#
# 输入: prices = [12,16,19,19,8,1,19,13,9], k = 3
#
# 输出: 36
#
# 解释:
#
# 我们可以通过 3 笔交易获得 36 美元的利润：
# 一笔普通交易：第 0 天以 12 美元买入，第 2 天以 19 美元卖出。
# 一笔做空交易：第 3 天以 19 美元卖出，第 4 天以 8 美元买回。
# 一笔普通交易：第 5 天以 1 美元买入，第 6 天以 19 美元卖出。
#
#
# 提示:
#
# 2 <= prices.length <= 103
# 1 <= prices[i] <= 109
# 1 <= k <= prices.length / 2

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dfs(day, kk, t):  # 前day天，进行kk次交易的最大收益
            # t 表示最后一次正在进行的单个操作，1: 卖出，2: 买入，3: 无
            if kk == 0:
                return 0
            if day < 1:
                if t == 1:
                    return prices[0]
                elif t == 2:
                    return -prices[0]
                else:
                    return 0
            v1 = dfs(day - 1, kk, t)
            if t == 3:
                v2 = dfs(day - 1, kk - 1, 2) + prices[day]
                v3 = dfs(day - 1, kk - 1, 1) - prices[day]
                return max(v1, v2, v3)
            elif t == 1:
                if kk & 1:
                    v2 = dfs(day - 1, kk - 1, 3) + prices[day]
                else:
                    v2 = dfs(day - 1, kk - 1, 2) + prices[day]
                return max(v1, v2)
            else:
                if kk & 1:
                    v2 = dfs(day - 1, kk - 1, 3) - prices[day]
                else:
                    v2 = dfs(day - 1, kk - 1, 1) - prices[day]
                return max(v1, v2)

        ans = dfs(n - 1, k * 2, 3)
        dfs.cache_clear()
        return ans

so = Solution()
print(so.maximumProfit(prices = [1,7,9,8,2], k = 2))




