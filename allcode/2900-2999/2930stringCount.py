# 给你一个整数 n 。
#
# 如果一个字符串 s 只包含小写英文字母，且 将 s 的字符重新排列后，新字符串包含 子字符串 "leet" ，那么我们称字符串 s 是一个 好 字符串。
#
# 比方说：
#
# 字符串 "lteer" 是好字符串，因为重新排列后可以得到 "leetr" 。
# "letl" 不是好字符串，因为无法重新排列并得到子字符串 "leet" 。
# 请你返回长度为 n 的好字符串 总 数目。
#
# 由于答案可能很大，将答案对 109 + 7 取余 后返回。
#
# 子字符串 是一个字符串中一段连续的字符序列。
#
#
# 示例 1：
#
# 输入：n = 4
# 输出：12
# 解释：总共有 12 个字符串重新排列后包含子字符串 "leet" ："eelt" ，"eetl" ，"elet" ，"elte" ，"etel" ，"etle" ，"leet" ，"lete" ，"ltee" ，"teel" ，"tele" 和 "tlee" 。
# 示例 2：
#
# 输入：n = 10
# 输出：83943898
# 解释：长度为 10 的字符串重新排列后包含子字符串 "leet" 的方案数为 526083947580 。所以答案为 526083947580 % (109 + 7) = 83943898 。
#
#
# 提示：
#
# 1 <= n <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 4: return 0
        dp2 = [0] * 12  # 枚举12种可能。递推
        dp1 = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 23]
        for i in range(1, n):
            dp2[11] = dp1[11] * 23   #  不包含任何l/e/t
            dp2[0] = dp1[0] * 24 + dp1[11]  # 仅包含 'l' 至少1个
            dp2[1] = dp1[1] * 23 + dp1[11]  # 仅包含 'e' 1个
            dp2[2] = dp1[2] * 24 + dp1[11]  # 仅包含 't' 至少1个
            dp2[3] = dp1[0] + dp1[1] + dp1[3] * 24  # 仅包含 'le'
            dp2[4] = dp1[1] + dp1[2] + dp1[4] * 24  # 仅包含 'te'
            dp2[5] = dp1[1] + dp1[5] * 24  # 仅包含 'e' 至少2个
            dp2[6] = dp1[0] + dp1[2] + dp1[6] * 25  # 仅包含 'lt'
            dp2[7] = dp1[3] + dp1[4] + dp1[6] + dp1[7] * 25  # 仅包含 'let'
            dp2[8] = dp1[3] + dp1[5] + dp1[8] * 25  # 仅包含 'lee'
            dp2[9] = dp1[4] + dp1[5] + dp1[9] * 25  # 仅包含 'tee'
            dp2[10] = dp1[7] + dp1[8] + dp1[9] + dp1[10] * 26  # 包含 'leet'
            for j in range(12):
                dp2[j] %= MOD
            dp1, dp2 = dp2, [0] * 12
        return dp1[-2]




so = Solution()
print(so.stringCount(5))
print(so.stringCount(4))
print(so.stringCount(10))




