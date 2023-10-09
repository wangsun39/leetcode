# 给定一个字符串
# s，计算
# s
# 的
# 不同非空子序列
# 的个数。因为结果可能很大，所以返回答案需要对
# 10 ^ 9 + 7
# 取余 。
#
# 字符串的
# 子序列
# 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。
#
# 例如，"ace"
# 是
# "abcde"
# 的一个子序列，但
# "aec"
# 不是。
#
#
# 示例
# 1：
#
# 输入：s = "abc"
# 输出：7
# 解释：7
# 个不同的子序列分别是
# "a", "b", "c", "ab", "ac", "bc", 以及
# "abc"。
# 示例
# 2：
#
# 输入：s = "aba"
# 输出：6
# 解释：6
# 个不同的子序列分别是
# "a", "b", "ab", "ba", "aa"
# 以及
# "aba"。
# 示例
# 3：
#
# 输入：s = "aaa"
# 输出：3
# 解释：3
# 个不同的子序列分别是
# "a", "aa"
# 以及
# "aaa"。
#
#
# 提示：
#
# 1 <= s.length <= 2000
# s
# 仅由小写英文字母组成


import copy
from typing import List
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = int(1e9 + 7)
        n = len(s)
        dp = [0] * (n + 1)
        used = [set() for _ in range(n + 1)]
        dp[0] = 1 # dp[0] 表示空串，不计入ans
        ans = 0
        for i in range(1, n + 1):
            for j in range(i):
                if s[i - 1] not in used[j]:
                    dp[i] += dp[j]
                    used[j].add(s[i - 1])
                dp[i] %= MOD
            ans += dp[i]
            ans %= MOD
        print(dp)
        return ans

    def distinctSubseqII2(self, s: str) -> int:  # 其他解法
        f = [[0] * 26 for _ in range(len(s) + 1)]
        for i, c in enumerate(s, 1):
            c = ord(c) - ord('a')
            f[i] = f[i - 1].copy()
            f[i][c] = (1 + sum(f[i - 1])) % MOD
        return sum(f[-1]) % MOD


so = Solution()
print(so.distinctSubseqII("abc"))
print(so.distinctSubseqII("aba"))
