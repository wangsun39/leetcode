# 给你一个字符串 s 和一个整数 k ，请你将 s 分成 k 个 子字符串 ，使得每个 子字符串 变成 半回文串 需要修改的字符数目最少。
#
# 请你返回一个整数，表示需要修改的 最少 字符数目。
#
# 注意：
#
# 如果一个字符串从左往右和从右往左读是一样的，那么它是一个 回文串 。
# 如果长度为 len 的字符串存在一个满足 1 <= d < len 的正整数 d ，len % d == 0 成立且所有对 d 做除法余数相同的下标对应的字符连起来得到的字符串都是 回文串 ，那么我们说这个字符串是 半回文串 。比方说 "aa" ，"aba" ，"adbgad" 和 "abab" 都是 半回文串 ，而 "a" ，"ab" 和 "abca" 不是。
# 子字符串 指的是一个字符串中一段连续的字符序列。
#
#
# 示例 1：
#
# 输入：s = "abcac", k = 2
# 输出：1
# 解释：我们可以将 s 分成子字符串 "ab" 和 "cac" 。子字符串 "cac" 已经是半回文串。如果我们将 "ab" 变成 "aa" ，它也会变成一个 d = 1 的半回文串。
# 该方案是将 s 分成 2 个子字符串的前提下，得到 2 个半回文子字符串需要的最少修改次数。所以答案为 1 。
# 示例 2:
#
# 输入：s = "abcdef", k = 2
# 输出：2
# 解释：我们可以将 s 分成子字符串 "abc" 和 "def" 。子字符串 "abc" 和 "def" 都需要修改一个字符得到半回文串，所以我们总共需要 2 次字符修改使所有子字符串变成半回文串。
# 该方案是将 s 分成 2 个子字符串的前提下，得到 2 个半回文子字符串需要的最少修改次数。所以答案为 2 。
# 示例 3：
#
# 输入：s = "aabbaa", k = 3
# 输出：0
# 解释：我们可以将 s 分成子字符串 "aa" ，"bb" 和 "aa" 。
# 字符串 "aa" 和 "bb" 都已经是半回文串了。所以答案为 0 。
#
#
# 提示：
#
# 2 <= s.length <= 200
# 1 <= k <= s.length / 2
# s 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
# max = lambda a, b: b if b > a else a

MX = 201
divisors = [[] for _ in range(MX)]  # divisors[i] 表示 i 的所有因子
for i in range(1, MX):  # 预处理每个数的所有因子，时间复杂度 O(MlogM)，M=1e5
    for j in range(i, MX, i):
        divisors[j].append(i)
# print(divisors)

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        def min_chg(ss):
            m = len(ss)
            if m == 1: return inf
            res = inf
            for d in divisors[m][:-1]:
                u = m // d  # mod d 为的数的个数
                diff = 0
                for i in range(m):
                    # 找i的对称点 ，按d个一组，i在 j组，第t个
                    j = i // d
                    t = i % d
                    # 目标在 v 组
                    v = u - 1 - j
                    if j >= v: break
                    i2 = v * d + t
                    if ss[i] != ss[i2]:
                        diff += 1
                res = min(res, diff)
            return res

        chg = [[0] * n for _ in range(n)]  # 子串s[i:j]变成半回文的最小修改次数
        for i in range(n):
            for j in range(i, n):
                chg[i][j] = min_chg(s[i: j + 1])

        dp = [[inf] * k for _ in range(n)]  # dp[i][j] 前i个数分成j段，最小的改动次数
        for i in range(1, n):
            dp[i][0] = chg[0][i]
            for j in range(1, k):
                if (i + 1) < (j + 1) * 2: continue
                for t in range(i - 1):
                    dp[i][j] = min(dp[t][j - 1] + chg[t + 1][i], dp[i][j])

        return dp[-1][-1]


so = Solution()
print(so.minimumChanges(s = "abcc", k = 1))
print(so.minimumChanges(s = "abcac", k = 2))


