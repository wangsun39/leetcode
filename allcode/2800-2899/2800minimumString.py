# 给你三个字符串 a ，b 和 c ， 你的任务是找到长度 最短 的字符串，且这三个字符串都是它的 子字符串 。
# 如果有多个这样的字符串，请你返回 字典序最小 的一个。
#
# 请你返回满足题目要求的字符串。
#
# 注意：
#
# 两个长度相同的字符串 a 和 b ，如果在第一个不相同的字符处，a 的字母在字母表中比 b 的字母 靠前 ，那么字符串 a 比字符串 b 字典序小 。
# 子字符串 是一个字符串中一段连续的字符序列。
#
#
# 示例 1：
#
# 输入：a = "abc", b = "bca", c = "aaa"
# 输出："aaabca"
# 解释：字符串 "aaabca" 包含所有三个字符串：a = ans[2...4] ，b = ans[3..5] ，c = ans[0..2] 。结果字符串的长度至少为 6 ，且"aaabca" 是字典序最小的一个。
# 示例 2：
#
# 输入：a = "ab", b = "ba", c = "aba"
# 输出："aba"
# 解释：字符串 "aba" 包含所有三个字符串：a = ans[0..1] ，b = ans[1..2] ，c = ans[0..2] 。由于 c 的长度为 3 ，结果字符串的长度至少为 3 。"aba" 是字典序最小的一个。
#
#
# 提示：
#
# 1 <= a.length, b.length, c.length <= 100
# a ，b ，c 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        a, b, c = sorted([a, b, c], key=lambda x:len(x))
        if a in b or a in c:
            a = ''
        if b in c:
            b = ''
        def cat1(u: str, v: str):
            nu, nv = len(u), len(v)
            for i in range(nu):
                if v.startswith(u[i:]):
                    return u + v[nu - i:]
            return u + v
        def cat2(x: str, y: str, z: str):
            t = cat1(x, y)
            return cat1(t, z)

        l = [cat2(a, b, c), cat2(a, c, b), cat2(b, a, c), cat2(b, c, a), cat2(c, b, a), cat2(c, a, b)]
        mn = min(len(x) for x in l)
        l = [x for x in l if len(x) == mn]
        return min(l)


so = Solution()
print(so.minimumString(a = "cab", b = "a", c = "b"))
print(so.minimumString(a = "ca", b = "a", c = "a"))
print(so.minimumString(a = "abc", b = "bca", c = "aaa"))
print(so.minimumString(a = "ab", b = "ba", c = "aba"))




