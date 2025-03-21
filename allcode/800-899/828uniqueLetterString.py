# 我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。
#
# 例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，因为它们只出现一次，所以 countUniqueChars(s) = 5 。
#
# 本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。输入用例保证返回值为32 位整数。
#
# 注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 s 的所有子字符串中的唯一字符）。
#
#
#
# 示例 1：
#
# 输入: s = "ABC"
# 输出: 10
# 解释: 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
#      其中，每一个子串都由独特字符构成。
#      所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
# 示例 2：
#
# 输入: s = "ABA"
# 输出: 8
# 解释: 除了 countUniqueChars("ABA") = 1 之外，其余与示例 1 相同。
# 示例 3：
#
# 输入：s = "LEETCODE"
# 输出：92
#
#
# 提示：
#
# 1 <= s.length <= 10^5
# s 只包含大写英文字符


from leetcode.allcode.competition.mypackage import *
class Solution:
    def uniqueLetterString1(self, s: str) -> int:
        dp1, dp2 = defaultdict(int), defaultdict(int)
        dp3, dp4 = defaultdict(int), defaultdict(int)
        n = len(s)
        ans = 0
        for i in range(n):
            ch = s[i]
            for j in range(ord('A'), ord('Z') + 1):
                cch = chr(j)
                if cch == ch:
                    dp3[cch] = dp2[cch] + 1
                    dp4[cch] = 0
                else:
                    dp3[cch] = dp1[cch]
                    dp4[cch] = dp2[cch] + 1
                ans += dp3[cch]
            dp1, dp2 = dp3, dp4
        return ans

    def uniqueLetterString(self, s: str) -> int:
        # 2023/11/26 考虑某一个数字前一次出现的位置p1，和前前一次出现的位置p2
        # dp[i] = dp[i - 1] + (i - p1) - (p1 - p2)
        pre = [-1] * 26
        ppre = [-1] * 26
        n = len(s)
        dp = [0] * n  # 以第i个字符结尾的字符串的countUniqueChars总和
        dp[0] = 1
        pre[ord(s[0]) - ord('A')] = 0
        for i, x in enumerate(s[1:], 1):
            dp[i] = dp[i - 1]
            p1 = pre[ord(x) - ord('A')]
            p2 = ppre[ord(x) - ord('A')]
            dp[i] += (i - p1) - (p1 - p2)
            if p1 == -1:
                pre[ord(x) - ord('A')] = i
            else:
                ppre[ord(x) - ord('A')] = p1
                pre[ord(x) - ord('A')] = i

        return sum(dp)


so = Solution()
print(so.uniqueLetterString("LEETCODE"))
print(so.uniqueLetterString("ABC"))

