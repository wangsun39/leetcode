# 给你 3 个正整数 zero ，one 和 limit 。
#
# 一个
# 二进制数组
#  arr 如果满足以下条件，那么我们称它是 稳定的 ：
#
# 0 在 arr 中出现次数 恰好 为 zero 。
# 1 在 arr 中出现次数 恰好 为 one 。
# arr 中每个长度超过 limit 的
# 子数组
#  都 同时 包含 0 和 1 。
# 请你返回 稳定 二进制数组的 总 数目。
#
# 由于答案可能很大，将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：zero = 1, one = 1, limit = 2
#
# 输出：2
#
# 解释：
#
# 两个稳定的二进制数组为 [1,0] 和 [0,1] ，两个数组都有一个 0 和一个 1 ，且没有子数组长度大于 2 。
#
# 示例 2：
#
# 输入：zero = 1, one = 2, limit = 1
#
# 输出：1
#
# 解释：
#
# 唯一稳定的二进制数组是 [1,0,1] 。
#
# 二进制数组 [1,1,0] 和 [0,1,1] 都有长度为 2 且元素全都相同的子数组，所以它们不稳定。
#
# 示例 3：
#
# 输入：zero = 3, one = 3, limit = 2
#
# 输出：14
#
# 解释：
#
# 所有稳定的二进制数组包括 [0,0,1,0,1,1] ，[0,0,1,1,0,1] ，[0,1,0,0,1,1] ，[0,1,0,1,0,1] ，[0,1,0,1,1,0] ，[0,1,1,0,0,1] ，[0,1,1,0,1,0] ，[1,0,0,1,0,1] ，[1,0,0,1,1,0] ，[1,0,1,0,0,1] ，[1,0,1,0,1,0] ，[1,0,1,1,0,0] ，[1,1,0,0,1,0] 和 [1,1,0,1,0,0] 。
#
#
#
# 提示：
#
# 1 <= zero, one, limit <= 200

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        n = zero + one
        dp0 = [[0] * (zero + 1) for _ in range(n + 1)]  # dp[i][j] 表示长度为i的数字，有j个0且最后一位是0的总数
        dp1 = [[0] * (one + 1) for _ in range(n + 1)]  # dp[i][j] 表示长度为i的数字，有j个1且最后一位是1的总数
        dp0[1][1], dp1[1][1] = 1, 1
        for i in range(2, n + 1):
            # 1 <= j <= zero and 0 <= i - j <= one
            for j in range(max(1, i - one), min(i, zero) + 1):
                if i == j <= limit:
                    dp0[i][j] = 1
                    continue
                if i - j >= one + 1: continue
                # 1 <= k <= limit and i - k >= i - k
                for k in range(1, min(limit, j) + 1):
                    dp0[i][j] += dp1[i - k][i - j]
                    dp0[i][j] %= MOD
            for j in range(max(1, i - zero), min(i, one) + 1):
                if i == j <= limit:
                    dp1[i][j] = 1
                    continue
                if i - j >= zero + 1: continue
                for k in range(1, min(limit, j) + 1):
                    dp1[i][j] += dp0[i - k][i - j]
                    dp1[i][j] %= MOD

        # print(dp0)
        # print(dp1)
        return (dp1[-1][-1] + dp0[-1][-1]) % MOD


so = Solution()
print(so.numberOfStableArrays(zero = 1, one = 3, limit = 3))  # 4
print(so.numberOfStableArrays(zero = 1, one = 2, limit = 2))  # 3
print(so.numberOfStableArrays(zero = 1, one = 2, limit = 1))
print(so.numberOfStableArrays(zero = 3, one = 3, limit = 2))
print(so.numberOfStableArrays(zero = 1, one = 1, limit = 2))




