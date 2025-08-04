# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#
#
# 提示：
#
# 1 <= n <= 8

from leetcode.allcode.competition.mypackage import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @cache
        def dfs(l, r):
            if l == n == r:
                return ['']
            res = []
            if l < n:
                res1 = dfs(l + 1, r)
                for x in res1:
                    res.append('(' + x)
            if r < n and l > r:
                res1 = dfs(l, r + 1)
                for x in res1:
                    res.append(')' + x)
            return res

        return dfs(0, 0)




