# 爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：
#
# 爱丽丝以 0 分开始，并在她的得分少于 k 分时抽取数字。 抽取时，她从 [1, maxPts] 的范围中随机获得一个整数作为分数进行累计，其中 maxPts 是一个整数。 每次抽取都是独立的，其结果具有相同的概率。
#
# 当爱丽丝获得 k 分 或更多分 时，她就停止抽取数字。
#
# 爱丽丝的分数不超过 n 的概率是多少？
#
# 与实际答案误差不超过 10-5 的答案将被视为正确答案。
#
#
# 示例 1：
#
# 输入：n = 10, k = 1, maxPts = 10
# 输出：1.00000
# 解释：爱丽丝得到一张牌，然后停止。
# 示例 2：
#
# 输入：n = 6, k = 1, maxPts = 10
# 输出：0.60000
# 解释：爱丽丝得到一张牌，然后停止。 在 10 种可能性中的 6 种情况下，她的得分不超过 6 分。
# 示例 3：
#
# 输入：n = 21, k = 17, maxPts = 10
# 输出：0.73278
#
#
# 提示：
#
# 0 <= k <= n <= 104
# 1 <= maxPts <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        @cache
        def dfs(x):  # 从 x 开始的概率
            res = 0
            if x > n: return 0
            if x >= k: return 1

            # 以下注释掉的代码也是对的，只是性能不够
            # for i in range(1, maxPts + 1):
            #     res += dfs(x + i)
            # return res / maxPts

            # 由此启发得：dfs(x) = (dfs(x+1)+dfs(x+2)+...+dfs(x+maxPts)) / maxPts，
            # maxPts * dfs(x) = maxPts*dfs(x+1)-dfs(x + 1 + maxPts)+dfs(x+1)
            # dfs(x)=(maxPts + 1) / maxPts * dfs(x + 1) - dfs(x + 1 + maxPts) / maxPts
            if x + 1 == k:
                for i in range(1, maxPts + 1):
                    res += dfs(x + i)
                return res / maxPts
            return (maxPts + 1) / maxPts * dfs(x + 1) - dfs(x + 1 + maxPts) / maxPts

        return dfs(0)



so = Solution()
print(so.new21Game(n = 2, k = 2, maxPts = 3))  # 0.444
print(so.new21Game(n = 10, k = 1, maxPts = 10))
print(so.new21Game(n = 6, k = 1, maxPts = 10))
print(so.new21Game(n = 21, k = 17, maxPts = 10))  # 0.73278

