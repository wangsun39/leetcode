# 给你两个长度为 n 的字符串 s1 和 s2 ，以及一个字符串 evil 。请你返回 好字符串 的数目。
#
# 好字符串 的定义为：它的长度为 n ，字典序大于等于 s1 ，字典序小于等于 s2 ，且不包含 evil 为子字符串。
#
# 由于答案可能很大，请你返回答案对 10^9 + 7 取余的结果。
#
#
#
# 示例 1：
#
# 输入：n = 2, s1 = "aa", s2 = "da", evil = "b"
# 输出：51
# 解释：总共有 25 个以 'a' 开头的好字符串："aa"，"ac"，"ad"，...，"az"。还有 25 个以 'c' 开头的好字符串："ca"，"cc"，"cd"，...，"cz"。最后，还有一个以 'd' 开头的好字符串："da"。
# 示例 2：
#
# 输入：n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
# 输出：0
# 解释：所有字典序大于等于 s1 且小于等于 s2 的字符串都以 evil 字符串 "leet" 开头。所以没有好字符串。
# 示例 3：
#
# 输入：n = 2, s1 = "gx", s2 = "gz", evil = "x"
# 输出：2
#
#
# 提示：
#
# s1.length == n
# s2.length == n
# s1 <= s2
# 1 <= n <= 500
# 1 <= evil.length <= 50
# 所有字符串都只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        MOD = 10 ** 9 + 7
        m = len(evil)
        pi = [0] * m  # 前缀子串 s[:i + 1] 的真前缀和真后缀的最长匹配
        cnt = 0
        for i in range(1, m):
            b = evil[i]
            while cnt and evil[cnt] != b:
                cnt = pi[cnt - 1]
            if evil[cnt] == b:
                cnt += 1
            pi[i] = cnt

        evil0 = [int(c2i[x]) for x in list(evil)]

        print(pi)

        def f(nums):
            @cache
            def helper(i: int, is_limit: bool, match: int) -> int:
                if match == m: return 0
                if i == n:
                    return 1
                ans = 0
                upper = nums[i] if is_limit else 25  # 判断当前位是否受约束
                lower = 0
                for j in range(lower, upper + 1):
                    if j == evil0[match]:
                        ans += helper(i + 1, is_limit and j == upper, match + 1)
                    else:
                        match2 = match
                        while match2 and j != evil0[match2]:
                            match2 = pi[match2 - 1]   # 利用kmp的pi数组
                        if j != evil0[match2]:
                            ans += helper(i + 1, is_limit and j == upper, 0)
                        else:
                            ans += helper(i + 1, is_limit and j == upper, match2 + 1)
                    ans %= MOD
                return ans
            res = helper(0, True, 0)
            print(res)
            return res

        ns1 = [int(c2i[x]) for x in list(s1)]
        ns2 = [int(c2i[x]) for x in list(s2)]
        ans = f(ns2) - f(ns1) + MOD
        if evil in s1:
            return ans % MOD
        return (ans + 1) % MOD


so = Solution()
print(so.findGoodStrings(n = 3, s1 = "aca", s2 = "acz", evil = "ac"))  # 0
print(so.findGoodStrings(n = 2, s1 = "aa", s2 = "da", evil = "b"))  # 51


