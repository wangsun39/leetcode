# 给你一个字符串 s ，如果可以将它分割成三个 非空 回文子字符串，那么返回 true ，否则返回 false 。
#
# 当一个字符串正着读和反着读是一模一样的，就称其为 回文字符串 。
#
#
#
# 示例 1：
#
# 输入：s = "abcbdd"
# 输出：true
# 解释："abcbdd" = "a" + "bcb" + "dd"，三个子字符串都是回文的。
# 示例 2：
#
# 输入：s = "bcbddxy"
# 输出：false
# 解释：s 没办法被分割成 3 个回文子字符串。
#
#
# 提示：
#
# 3 <= s.length <= 2000
# s 只包含小写英文字母。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        d = [[0] * n for _ in range(n)]
        for i in range(n):
            d[i][i] = 1
            flg = True
            for j in range(n):
                if i - j < 0 or i + j >= n: break
                if flg and s[i - j] == s[i + j]:
                    d[i - j][i + j] = 1
                else:
                    flg = False
            if i == n - 1: break
            flg = True
            for j in range(n):
                if i - j < 0 or i + 1 + j >= n: break
                if flg and s[i - j] == s[i + 1 + j]:
                    d[i - j][i + 1 + j] = 1
                else:
                    flg = 0

        @cache
        def dfs(start, num):
            if start >= n: return num == 0
            if num == 1:
                return d[start][n - 1]
            for j in range(start, n):
                if d[start][j] and dfs(j + 1, num - 1):
                    return True
            return False
        return dfs(0, 3)


so = Solution()
print(so.checkPartitioning(s = "abcbdd"))
print(so.checkPartitioning(s = "bcbddxy"))
