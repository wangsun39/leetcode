# 给你数字字符串 s ，请你返回 s 中长度为 5 的 回文子序列 数目。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。
#
# 提示：
#
# 如果一个字符串从前往后和从后往前读相同，那么它是 回文字符串 。
# 子序列是一个字符串中删除若干个字符后，不改变字符顺序，剩余字符构成的字符串。
#
#
# 示例 1：
#
# 输入：s = "103301"
# 输出：2
# 解释：
# 总共有 6 长度为 5 的子序列："10330" ，"10331" ，"10301" ，"10301" ，"13301" ，"03301" 。
# 它们中有两个（都是 "10301"）是回文的。
# 示例 2：
#
# 输入：s = "0000000"
# 输出：21
# 解释：所有 21 个长度为 5 的子序列都是 "00000" ，都是回文的。
# 示例 3：
#
# 输入：s = "9999900000"
# 输出：2
# 解释：仅有的两个回文子序列是 "99999" 和 "00000" 。
#
#
# 提示：
#
# 1 <= s.length <= 104
# s 只包含数字字符。
from leetcode.allcode.competition.mypackage import *

class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        c1, c2 = [[0] * 10 for _ in range(n)], [[0] * 10 for _ in range(n)]  # i 左右(包括i)分别有多少个 0 - 9
        c3, c4 = [[0] * 100 for _ in range(n)], [[0] * 100 for _ in range(n)]  # i 左右(包括i)分别有多少个 00 - 99
        for i in range(n):
            num = int(s[i])
            if i > 0:
                c1[i] = [e for e in c1[i - 1]]
                c3[i] = [e for e in c3[i - 1]]
            c1[i][num] += 1
            if i > 0:
                for j in range(10):
                    idx = j * 10 + num
                    c3[i][idx] += c1[i - 1][j]

        for i in range(n - 1, -1, -1):
            num = int(s[i])
            if i < n - 1:
                c2[i] = [e for e in c2[i + 1]]
                c4[i] = [e for e in c4[i + 1]]
            c2[i][num] += 1
            if i < n - 1:
                for j in range(10):
                    idx = num * 10 + j
                    c4[i][idx] += c2[i + 1][j]
        # print(c1)
        # print(c2)
        # print(c3)
        # print(c4)
        ans = 0
        for i in range(2, n - 2):
            for j in range(100):
                left = c3[i - 1][j]
                right = c4[i + 1][(j%10)*10 + j // 10]
                ans += (left * right)
                ans %= MOD
        return ans

so = Solution()
print(so.countPalindromes("00000"))
print(so.countPalindromes("103301"))
print(so.countPalindromes("0000000"))
print(so.countPalindromes("9999900000"))




