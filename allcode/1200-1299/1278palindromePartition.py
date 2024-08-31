# 给你一个由小写字母组成的字符串 s，和一个整数 k。
#
# 请你按下面的要求分割字符串：
#
# 首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
# 接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
# 请返回以这种方式分割字符串所需修改的最少字符数。
#
#
#
# 示例 1：
#
# 输入：s = "abc", k = 2
# 输出：1
# 解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。
# 示例 2：
#
# 输入：s = "aabbc", k = 3
# 输出：0
# 解释：你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。
# 示例 3：
#
# 输入：s = "leetcode", k = 8
# 输出：0
#
#
# 提示：
#
# 1 <= k <= s.length <= 100
# s 中只含有小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        chg = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(1, min(i + 1, n - i)):
                if s[i - j] == s[i + j]:
                    chg[i - j][i + j] = chg[i - j + 1][i + j - 1]
                else:
                    chg[i - j][i + j] = chg[i - j + 1][i + j - 1] + 1
            if i == n - 1: continue
            if s[i] != s[i + 1]:
                chg[i][i + 1] = 1
            for j in range(1, min(i + 1, n - i - 1)):
                if s[i - j] == s[i + 1 + j]:
                    chg[i - j][i + 1 + j] = chg[i - j + 1][i + j]
                else:
                    chg[i - j][i + 1 + j] = chg[i - j + 1][i + j] + 1

        @cache
        def dfs(i, kk):  # 从idx开始，分割成kk个子字符串需要修改的最少次数
            if kk == 0:
                if i == n: return 0
                return inf
            if i == n - 1:
                if kk == 1: return 0
                return inf
            res = inf
            for j in range(i, n):
                res = min(res, dfs(j + 1, kk - 1) + chg[i][j])
            return res
        return dfs(0, k)



so = Solution()
print(so.palindromePartition("oiwwhqjkb", 1))
print(so.palindromePartition("tcymekt", 4))
print(so.palindromePartition(s = "abc", k = 2))
print(so.palindromePartition(s = "aabbc", k = 3))
print(so.palindromePartition(s = "leetcode", k = 8))




