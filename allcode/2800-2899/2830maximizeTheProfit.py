# 给你一个整数 n 表示数轴上的房屋数量，编号从 0 到 n - 1 。
#
# 另给你一个二维整数数组 offers ，其中 offers[i] = [starti, endi, goldi] 表示第 i 个买家想要以 goldi 枚金币的价格购买从 starti 到 endi 的所有房屋。
#
# 作为一名销售，你需要有策略地选择并销售房屋使自己的收入最大化。
#
# 返回你可以赚取的金币的最大数目。
#
# 注意 同一所房屋不能卖给不同的买家，并且允许保留一些房屋不进行出售。
#
#
#
# 示例 1：
#
# 输入：n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]
# 输出：3
# 解释：
# 有 5 所房屋，编号从 0 到 4 ，共有 3 个购买要约。
# 将位于 [0,0] 范围内的房屋以 1 金币的价格出售给第 1 位买家，并将位于 [1,3] 范围内的房屋以 2 金币的价格出售给第 3 位买家。
# 可以证明我们最多只能获得 3 枚金币。
# 示例 2：
#
# 输入：n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]
# 输出：10
# 解释：有 5 所房屋，编号从 0 到 4 ，共有 3 个购买要约。
# 将位于 [0,2] 范围内的房屋以 10 金币的价格出售给第 2 位买家。
# 可以证明我们最多只能获得 10 枚金币。
#
#
# 提示：
#
# 1 <= n <= 105
# 1 <= offers.length <= 105
# offers[i].length == 3
# 0 <= starti <= endi <= n - 1
# 1 <= goldi <= 103

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * n  # 前 i 个房屋的最大总售价
        offers.sort(key=lambda x: x[1])
        idx = 0
        ans = 0
        for i in range(n):
            if i > 0:
                dp[i] = dp[i - 1]
            while idx < len(offers) and offers[idx][1] <= i:
                if offers[idx][0] > 0:
                    dp[i] = max(dp[i], dp[offers[idx][0] - 1] + offers[idx][2])
                else:
                    dp[i] = max(dp[i], offers[idx][2])
                idx += 1
            ans = max(ans, dp[i])
            if idx > len(offers):
                break
        # print(dp)
        return ans


so = Solution()
print(so.maximizeTheProfit(8, [[0,6,5],[6,7,1],[0,0,10]]))
print(so.maximizeTheProfit(10, [[0,6,5],[2,9,4],[0,9,2],[3,9,3],[1,6,10],[0,1,3],[3,8,9],[4,8,3],[2,6,5],[0,4,6]]))
print(so.maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]))
print(so.maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]))




