# 对于一个整数数组 nums，逆序对是一对满足 0 <= i < j < nums.length 且 nums[i] > nums[j]的整数对 [i, j] 。
#
# 给你两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个 逆序对 的不同的数组的个数。由于答案可能很大，只需要返回对 109 + 7 取余的结果。
#
#
#
# 示例 1：
#
# 输入：n = 3, k = 0
# 输出：1
# 解释：
# 只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
# 示例 2：
#
# 输入：n = 3, k = 1
# 输出：2
# 解释：
# 数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
#
#
# 提示：
#
# 1 <= n <= 1000
# 0 <= k <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def kInversePairs1(self, n: int, k: int) -> int:
        # 这个方法简洁，容易理解，但性能不够
        MOD = 10 ** 9 + 7

        @cache
        def dfs(left, target):  # 剩下的left个数，构成target个逆序对，能有多少种组合
            if target == 0: return 1
            res = 0
            for i in range(left):
                if target < i: break
                res += dfs(left - 1, target - i)
                res %= MOD
            return res

        return dfs(n, k)

    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n)]  # dp[i][j] 表示前i项（从0开始），逆序对数为j的数组个数
        for i in range(n): dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, k + 1):
                if j <= i:
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD
                else:
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - i - 1]) % MOD
        return dp[-1][-1]



obj = Solution()
print(obj.kInversePairs(n = 3, k = 0))

