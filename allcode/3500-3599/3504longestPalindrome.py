# 给你两个字符串 s 和 t。
#
# 你可以从 s 中选择一个子串（可以为空）以及从 t 中选择一个子串（可以为空），然后将它们 按顺序 连接，得到一个新的字符串。
#
# 返回可以由上述方法构造出的 最长 回文串的长度。
#
# 回文串 是指正着读和反着读都相同的字符串。
#
# 子字符串 是指字符串中的一个连续字符序列。
#
#
#
# 示例 1：
#
# 输入： s = "a", t = "a"
#
# 输出： 2
#
# 解释：
#
# 从 s 中选择 "a"，从 t 中选择 "a"，拼接得到 "aa"，这是一个长度为 2 的回文串。
#
# 示例 2：
#
# 输入： s = "abc", t = "def"
#
# 输出： 1
#
# 解释：
#
# 由于两个字符串的所有字符都不同，最长的回文串只能是任意一个单独的字符，因此答案是 1。
#
# 示例 3：
#
# 输入： s = "b", t = "aaaa"
#
# 输出： 4
#
# 解释：
#
# 可以选择 "aaaa" 作为回文串，其长度为 4。
#
# 示例 4：
#
# 输入： s = "abcde", t = "ecdba"
#
# 输出： 5
#
# 解释：
#
# 从 s 中选择 "abc"，从 t 中选择 "ba"，拼接得到 "abcba"，这是一个长度为 5 的回文串。
#
#
#
# 提示：
#
# 1 <= s.length, t.length <= 1000
# s 和 t 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        def calc(s1, s2):
            n1, n2 = len(s1), len(s2)
            res = 0
            ss2 = set()
            for i in range(n2):
                for j in range(i, n2):
                    ss2.add(s2[i: j + 1][::-1])
            for i in range(n1):
                # 单中心
                m1 = 0
                for j in range(1, n1):
                    if i - j < 0 or i + j >= n1: break
                    if s1[i - j] != s1[i + j]:
                        break
                    m1 = j
                res = max(res, m1 * 2 + 1)
                m2 = m1 + 1
                while i - m2 >= 0:
                    if s1[i - m2: i - m1] not in ss2:
                        break
                    m2 += 1
                res = max(res, (m2 - 1) * 2 + 1)
                # 双中心
                m1 = -1
                for j in range(n1):
                    if i - j < 0 or i + 1 + j >= n1: break
                    if s1[i - j] != s1[i + 1 + j]: break
                    m1 = j
                if m1 > -1:
                    res = max(res, (m1 + 1) * 2)
                m2 = m1 + 1
                while i - m2 >= 0:
                    if s1[i - m2: i - m1] not in ss2:
                        break
                    m2 += 1
                res = max(res, m2 * 2)
            return res
        ans1 = calc(s, t)
        ans2 = calc(t[::-1], s[::-1])
        return max(ans1, ans2)



so = Solution()
print(so.longestPalindrome(s = "b", t = "aaaa"))
print(so.longestPalindrome(s = "abcde", t = "ecbbba"))
print(so.longestPalindrome(s = "abcde", t = "ecdba"))
print(so.longestPalindrome(s = "a", t = "a"))




