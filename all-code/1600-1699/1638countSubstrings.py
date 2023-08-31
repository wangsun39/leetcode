# 给你两个字符串 s 和 t ，请你找出 s 中的非空子串的数目，这些子串满足替换 一个不同字符 以后，是 t 串的子串。换言之，请你找到 s 和 t 串中 恰好 只有一个字符不同的子字符串对的数目。
#
# 比方说， "computer" and "computation" 只有一个字符不同： 'e'/'a' ，所以这一对子字符串会给答案加 1 。
#
# 请你返回满足上述条件的不同子字符串对数目。
#
# 一个 子字符串 是一个字符串中连续的字符。
#
#
#
# 示例 1：
#
# 输入：s = "aba", t = "baba"
# 输出：6
# 解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# 加粗部分分别表示 s 和 t 串选出来的子字符串。
# 示例 2：
# 输入：s = "ab", t = "bb"
# 输出：3
# 解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
# ("ab", "bb")
# ("ab", "bb")
# ("ab", "bb")
# 加粗部分分别表示 s 和 t 串选出来的子字符串。
# 示例 3：
# 输入：s = "a", t = "a"
# 输出：0
# 示例 4：
#
# 输入：s = "abe", t = "bbc"
# 输出：10
#
#
# 提示：
#
# 1 <= s.length, t.length <= 100
# s 和 t 都只包含小写英文字母。





from typing import Optional,List
from collections import Counter
import heapq


# Definition for a binary tree node.
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp1 = [[0] * m for _ in range(n)]  # dp1[i][j] 表示 以 s[i] t[j] 结尾的两个串有多个相同子串
        dp2 = [[0] * m for _ in range(n)]  # dp2[i][j] 表示 以 s[i] t[j] 结尾的两个串有多个相同仅差一个元素的子串

        for i in range(n):
            if s[i] == t[0]:
                dp1[i][0] = 1
            else:
                dp2[i][0] = 1
        for i in range(m):
            if s[0] == t[i]:
                dp1[0][i] = 1
            else:
                dp2[0][i] = 1
        for i in range(1, n):
            for j in range(1, m):
                if s[i] == t[j]:
                    dp1[i][j] = dp1[i - 1][j - 1] + 1
                    dp2[i][j] = dp2[i - 1][j - 1]
                else:
                    dp2[i][j] = dp1[i - 1][j - 1] + 1
        print(dp1)
        print(dp2)
        return sum([sum(x) for x in dp2])



so = Solution()

print(so.countSubstrings(s = "ab", t = "bb"))
print(so.countSubstrings(s = "aba", t = "baba"))
print(so.countSubstrings(s = "a", t = "a"))
print(so.countSubstrings(s = "abe", t = "bbc"))




