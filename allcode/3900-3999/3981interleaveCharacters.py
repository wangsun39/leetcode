# 给你三个字符串 word1、word2 和 target。
#
# 你的任务是计算从 word1 和 word2 中选择字符以形成 target 的方案数，需满足以下条件：
#
# 对于 target 中的每个字符，从 word1 或 word2 中选择一个匹配的字符。
# 从 word1 中选择的下标必须是 严格 递增的。
# 从 word2 中选择的下标必须是 严格 递增的。
# 必须从 word1 和 word2 两者 中 至少 各选择一个字符。
# 如果对于 target 中的 至少 一个位置，选择的字符来自不同的字符串或不同的下标，则认为两种方案是不同的。
#
# 返回方案数。由于答案可能非常大，请返回它对 109 + 7 取余 后的结果。
#
#
#
# 示例 1：
#
# 输入： word1 = "abc", word2 = "bac", target = "abc"
#
# 输出： 5
#
# 解释：
#
# 有 5 种形成 target 的方案：
#
# word1[0] = 'a', word1[1] = 'b', word2[2] = 'c'
# word1[0] = 'a', word2[0] = 'b', word1[2] = 'c'
# word1[0] = 'a', word2[0] = 'b', word2[2] = 'c'
# word2[1] = 'a', word1[1] = 'b', word1[2] = 'c'
# word2[1] = 'a', word1[1] = 'b', word2[2] = 'c'
# 所有方案都保持了每个字符串内部递增的下标顺序，并且从每个字符串中至少选择了一个字符。
#
# 示例 2：
#
# 输入： word1 = "cd", word2 = "cd", target = "ccd"
#
# 输出： 4
#
# 解释：
#
# 有 4 种形成 target 的方案：
#
# word1[0] = 'c', word2[0] = 'c', word1[1] = 'd'
# word1[0] = 'c', word2[0] = 'c', word2[1] = 'd'
# word2[0] = 'c', word1[0] = 'c', word1[1] = 'd'
# word2[0] = 'c', word1[0] = 'c', word2[1] = 'd'
# target 中的前两个 'c' 字符必须分别来自两个字符串。最后一个 'd' 可以从任意一个字符串中选择。
#
# 示例 3：
#
# 输入： word1 = "xy", word2 = "xy", target = "xyxy"
#
# 输出： 2
#
# 解释：
#
# 有 2 种形成 target 的方案：
#
# word1[0] = 'x', word1[1] = 'y', word2[0] = 'x', word2[1] = 'y'
# word2[0] = 'x', word2[1] = 'y', word1[0] = 'x', word1[1] = 'y'
# target 中的每个 "xy" 部分完全来自同一个字符串。
#
# 示例 4：
#
# 输入： word1 = "ab", word2 = "cde", target = "ace"
#
# 输出： 1
#
# 解释：
#
# 唯一的方案是选择 word1[0] = 'a'、word2[0] = 'c' 和 word2[2] = 'e'。因此，答案为 1 。
#
#
#
# 提示：
#
# 1 <= word1.length, word2.length, target.length <= 100
# word1、word2 和 target 仅由小写英文字母组成。

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        n1, n2, nt = len(word1), len(word2), len(target)
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i, j, k, f):
            # word1前i个字母和word2的前j个字母能匹配target前k个字母的总数
            if k == -1:
                # print(i, j, k, f, 1)
                return 1  # 走到这里 对于相同的i/j, f==1orf==2各会计算一次，最后要除以2
            if i < 0 and j < 0:
                return 0
            res = 0
            if f == 1:
                if i < 0: return 0
                if word1[i] == target[k]:
                    if k == 0:
                        res += 1  # 匹配完成
                    else:
                        res += dfs(i - 1, j, k - 1, 1) + dfs(i - 1, j, k - 1, 2)
                res += dfs(i - 1, j, k, 1)
            else:
                if j < 0: return 0
                if word2[j] == target[k]:
                    if k == 0:
                        res += 1  # 匹配完成
                    else:
                        res += dfs(i, j - 1, k - 1, 1) + dfs(i, j - 1, k - 1, 2)
                res += dfs(i, j - 1, k, 2)

            res %= MOD
            # print(i, j, k, f, res)
            return res


        ans = dfs(n1 - 1, n2 - 1, nt - 1, 1) + dfs(n1 - 1, n2 - 1, nt - 1, 2)
        print(ans)

        def subs(word):
            m = len(word)

            dp = [[0] * nt for _ in range(m)]  # dp[i][j] word前i个字母匹配target前j个字符的总数
            if word[0] == target[0]:
                dp[0][0] = 1
            for i in range(1, m):
                for j in range(nt):
                    if i < j: break
                    dp[i][j] = dp[i - 1][j]
                    if word[i] == target[j]:
                        if j > 0:
                            dp[i][j] += dp[i - 1][j - 1]
                        else:
                            dp[i][j] += 1
                    dp[i][j] %= MOD
            # print(dp)
            return dp[-1][-1]

        c1 = subs(word1)
        c2 = subs(word2)
        # print(c1)
        # print(c2)

        return (ans - c1 - c2) % MOD





so = Solution()
print(so.interleaveCharacters(word1 = "a", word2 = "a", target = "a"))
print(so.interleaveCharacters(word1 = "abc", word2 = "bac", target = "abc"))
# print(so.interleaveCharacters(word1 = "aabbccc", word2 = "bac", target = "abc"))




