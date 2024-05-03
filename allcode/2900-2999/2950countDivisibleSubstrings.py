# 每个英文字母都被映射到一个数字，如下所示。
#
#
#
# 如果字符串的字符的映射值的总和可以被字符串的长度整除，则该字符串是 可整除 的。
#
# 给定一个字符串 s，请返回 s 的 可整除子串 的数量。
#
# 子串 是字符串内的一个连续的非空字符序列。
#
#
#
# 示例 1：
#
# Substring	Mapped	Sum	Length	Divisible?
# a	1	1	1	Yes
# s	7	7	1	Yes
# d	2	2	1	Yes
# f	3	3	1	Yes
# as	1, 7	8	2	Yes
# sd	7, 2	9	2	No
# df	2, 3	5	2	No
# asd	1, 7, 2	10	3	No
# sdf	7, 2, 3	12	3	Yes
# asdf	1, 7, 2, 3	13	4	No
# 输入：word = "asdf"
# 输出：6
# 解释：上表包含了有关 word 中每个子串的详细信息，我们可以看到其中有 6 个是可整除的。
# 示例 2:
#
# 输入：word = "bdh"
# 输出：4
# 解释：4 个可整除的子串是："b"，"d"，"h"，"bdh"。
# 可以证明 word 中没有其他可整除的子串。
# 示例 3:
#
# 输入：word = "abcd"
# 输出：6
# 解释：6 个可整除的子串是："a"，"b"，"c"，"d"，"ab"，"cd"。
# 可以证明 word 中没有其他可整除的子串。
#
#
# 提示：
#
# 1 <= word.length <= 2000
# word 仅包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        d = {}
        for x in ascii_lowercase:
            if x <= 'b':
                d[x] = 1
            elif x <= 'e':
                d[x] = 2
            elif x <= 'h':
                d[x] = 3
            elif x <= 'k':
                d[x] = 4
            elif x <= 'n':
                d[x] = 5
            elif x <= 'q':
                d[x] = 6
            elif x <= 't':
                d[x] = 7
            elif x <= 'w':
                d[x] = 8
            elif x <= 'z':
                d[x] = 9

        s = [0]
        ans = 0
        for i, x in enumerate(word):
            s.append(s[-1] + d[x])
            for j in range(i + 1):
                if (s[i + 1] - s[j]) % (i + 1 - j) == 0:
                    ans += 1
        return ans


so = Solution()
print(so.countDivisibleSubstrings("asdf"))
print(so.countDivisibleSubstrings("bdh"))
print(so.countDivisibleSubstrings("abcd"))




