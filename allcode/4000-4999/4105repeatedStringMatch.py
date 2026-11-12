# 给你两个由小写英文字母组成的字符串 a 和 b，以及两个整数 x 和 y。
#
# 如果将 b 重复恰好 y 次得到的字符串 (b * y) 是将 a 重复恰好 x 次得到的字符串 (a * x) 的 子串 ，返回 true。否则，返回 false。
#
# 子串 是字符串内连续的 非空 字符序列。
#
#
# 示例 1：
#
# 输入： a = "ab", b = "abab", x = 2, y = 1
#
# 输出： true
#
# 解释：
#
# a * x = "ab" * 2 = "abab"
# b * y = "abab" * 1 = "abab"
# 它们完全相同，因此 b * y 是 a * x 的子串。所以，答案是 true。
# 示例 2：
#
# 输入： a = "abc", b = "bc", x = 2, y = 3
#
# 输出： false
#
# 解释：
#
# a * x = "abc" * 2 = "abcabc"
# b * y = "bc" * 3 = "bcbcbc"
# 答案是 false，因为 b * y = "bcbcbc" 不是 a * x = "abcabc" 的子串。
# 示例 3：
#
# 输入： a = "abcd", b = "cdab", x = 2, y = 1
#
# 输出： true
#
# 解释：
#
# a * x = "abcd" * 2 = "abcdabcd"
# b * y = "cdab" 出现在 a * x = "abcdabcd" 的下标 [2..5] 处。因此，答案是 true。
#
#
# 提示：
#
# 1 <= a.length <= 100
# 1 <= b.length <= 100
# 1 <= x <= 109
# 1 <= y <= 109
# a 和 b 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
        na, nb = len(a), len(b)
        n, m = na * x, nb * y
        if n < m: return False

        na2 = nb // na + 1  # 至少有 na2 个 a ，长度可以严格超过 nb，保证如果能覆盖b，一定在此长度之内
        if nb % na == 0:
            if a * (nb // na) == b:  # 对于完全覆盖b的情况，na2 就取恰好的长度
                na2 -= 1
        if na2 > x: return False

        a2 = a * na2
        if b not in a2:
            if na2 + 1 <= x:   # 再加个1， 对付这个场景： a = "ssp", b = "ps"
                na2 += 1
                a2 = a * na2
            if b not in a2:
                return False
        pb = a2.find(b)
        a3 = a2[pb:] + a2[:pb]
        if na2 * na % nb == 0 and b * (na2 * na // nb) == a3:  # b 是 a3 的循环节
            # a * x 有多少个 b 的循环节
            nx = na * x // nb
            if pb != 0:
                nx -= 1
            return nx >= y

        # b 不是 a2/a3 的循环节
        if x == 1:
            return b * y in a
        if m > na * 2:
            return False
        return b * y in a + a




so = Solution()
print(so.repeatedStringMatch(a = "ssp", b = "ps", x = 13, y = 1))  # True
print(so.repeatedStringMatch(a = "ab", b = "abab", x = 2, y = 1))  # True
print(so.repeatedStringMatch(a = "ba", b = "ab", x = 3, y = 2))  # True
print(so.repeatedStringMatch(a = "abab", b = "ab", x = 2, y = 3))  # True
print(so.repeatedStringMatch(a = "baba", b = "ab", x = 2, y = 3))  # True


