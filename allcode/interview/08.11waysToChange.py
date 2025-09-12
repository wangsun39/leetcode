# 硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
#
# 示例 1：
#
#  输入：n = 5
#  输出：2
#  解释：有两种方式可以凑成总金额:
# 5=5
# 5=1+1+1+1+1
# 示例 2：
#
#  输入：n = 10
#  输出：4
#  解释：有四种方式可以凑成总金额:
# 10=10
# 10=5+5
# 10=5+1+1+1+1+1
# 10=1+1+1+1+1+1+1+1+1+1
# 说明：
#
# 注意:
#
# 你可以假设：
#
# 0 <= n (总金额) <= 1000000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def waysToChange(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        coin = [1,5,10,25]

        @cache
        def dfs(x, idx):
            if x == 0: return 1
            if x < 0: return 0
            res = dfs(x - coin[idx], idx)
            if idx:
                res += dfs(x, idx - 1)
            return res % MOD

        return dfs(n, 3)



so = Solution()
print(so.waysToChange(5))




