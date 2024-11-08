# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
#
# 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
# 每个元音 'a' 后面都只能跟着 'e'
# 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
# 每个元音 'i' 后面 不能 再跟着另一个 'i'
# 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
# 每个元音 'u' 后面只能跟着 'a'
# 由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。
#
#
#
# 示例 1：
#
# 输入：n = 1
# 输出：5
# 解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
# 示例 2：
#
# 输入：n = 2
# 输出：10
# 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
# 示例 3：
#
# 输入：n = 5
# 输出：68
#
#
# 提示：
#
# 1 <= n <= 2 * 10^4

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp1 = [1] * 5
        for i in range(1, n):
            dp2 = [0] * 5
            dp2[0] = dp1[1] + dp1[2] + dp1[4]
            dp2[1] = dp1[0] + dp1[2]
            dp2[2] = dp1[1] + dp1[3]
            dp2[3] = dp1[2]
            dp2[4] = dp1[2] + dp1[3]
            dp1 = dp2[:]
        return sum(dp1) % MOD


so = Solution()
print(so.countVowelPermutation(1))




