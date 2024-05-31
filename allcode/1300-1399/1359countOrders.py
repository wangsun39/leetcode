# 给你 n 笔订单，每笔订单都需要快递服务。
#
# 计算所有有效的 取货 / 交付 可能的顺序，使 delivery(i) 总是在 pickup(i) 之后。
#
# 由于答案可能很大，请返回答案对 10^9 + 7 取余的结果。
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：1
# 解释：只有一种序列 (P1, D1)，物品 1 的配送服务（D1）在物品 1 的收件服务（P1）后。
# 示例 2：
#
# 输入：n = 2
# 输出：6
# 解释：所有可能的序列包括：
# (P1,P2,D1,D2)，(P1,P2,D2,D1)，(P1,D1,P2,D2)，(P2,P1,D1,D2)，(P2,P1,D2,D1) 和 (P2,D2,P1,D1)。
# (P1,D2,P2,D1) 是一个无效的序列，因为物品 2 的收件服务（P2）不应在物品 2 的配送服务（D2）之后。
# 示例 3：
#
# 输入：n = 3
# 输出：90
#
#
# 提示：
#
# 1 <= n <= 500

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countOrders1(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(pick, deli):
            if pick == 0 and deli == 0: return 1
            res = 0
            if pick > 0:
                res += dfs(pick - 1, deli) * pick
                res %= MOD
            if deli > pick:
                res += dfs(pick, deli - 1) * (deli - pick)
                res %= MOD
            return res
        return dfs(n, n)

    def countOrders(self, n: int) -> int:
        # 2024/5/30 排列组合
        # C(2n,2)*C(2n-2,2)*C(2n-4,2)*...
        MOD = 10 ** 9 + 7
        ans = 1
        for i in range(n, 0, -1):
            ans *= i * (i * 2 - 1)
            ans %= MOD
        return ans

so = Solution()
print(so.countOrders(2))
print(so.countOrders(1))
print(so.countOrders(3))




