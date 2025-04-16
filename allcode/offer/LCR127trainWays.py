# 今天的有氧运动训练内容是在一个长条形的平台上跳跃。平台有 num 个小格子，每次可以选择跳 一个格子 或者 两个格子。请返回在训练过程中，学员们共有多少种不同的跳跃方式。
#
# 结果可能过大，因此结果需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 示例 1：
#
# 输入：n = 2
# 输出：2
# 示例 2：
#
# 输入：n = 5
# 输出：8
#
#
# 提示：
#
# 0 <= n <= 100
# 注意：本题与主站 70 题相同： https://leetcode-cn.com/problems/climbing-stairs/

from leetcode.allcode.competition.mypackage import *

class Solution:
    def trainWays(self, num: int) -> int:
        MOD = 10 ** 9 + 7
        if num == 0: return 1
        @cache
        def dfs(n):
            if n <= 2:
                return n
            return (dfs(n - 1) + dfs(n - 2)) % MOD
        return dfs(num)


so = Solution()




