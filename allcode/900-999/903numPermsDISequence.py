# 给定一个长度为 n 的字符串 s ，其中 s[i] 是:
#
# “D” 意味着减少，或者
# “I” 意味着增加
# 有效排列 是对有 n + 1 个在 [0, n]  范围内的整数的一个排列 perm ，使得对所有的 i：
#
# 如果 s[i] == 'D'，那么 perm[i] > perm[i+1]，以及；
# 如果 s[i] == 'I'，那么 perm[i] < perm[i+1]。
# 返回 有效排列  perm的数量 。因为答案可能很大，所以请返回你的答案对 109 + 7 取余。
#
#
#
# 示例 1：
#
# 输入：s = "DID"
# 输出：5
# 解释：
# (0, 1, 2, 3) 的五个有效排列是：
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
# 示例 2:
#
# 输入: s = "D"
# 输出: 1
#
#
# 提示:
#
# n == s.length
# 1 <= n <= 200
# s[i] 不是 'I' 就是 'D'


from leetcode.allcode.competition.mypackage import *

class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]  # dp[i][j] 前i个数字，其中第i位之后恰有j的数字大于第i位的数字的所以组合数
        dp[0] = [1] * (n + 1)
        for i in range(1, n + 1):
            for j in range(n - i + 1):  # 需要满足这个条件 i + j <= n
                if s[i - 1] == 'I':  # nums[i-1]<nums[i]  当i时，比nums[i]的j个数都比nums[i-1]大，加上nums[i],至少j+1的比nums[i]的情况
                    # 每种情况，都对应唯一的一种选nums[i]的方式
                    dp[i][j] = sum(dp[i - 1][t] for t in range(j + 1, n + 1)) % MOD
                else:
                    dp[i][j] = sum(dp[i - 1][t] for t in range(j + 1)) % MOD
        return sum(dp[-1]) % MOD

so = Solution()
print(so.numPermsDISequence("DID"))