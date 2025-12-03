# 给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 0 (false)、1 (true)、& (AND)、 | (OR) 和 ^ (XOR) 符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。
#
# 示例 1：
#
# 输入：s = "1^0|0|1", result = 0
#
# 输出：2
# 解释：两种可能的括号方法是
# 1^(0|(0|1))
# 1^((0|0)|1)
# 示例 2：
#
# 输入：s = "0&0&0&1^1|0", result = 1
#
# 输出：10
# 提示：
#
# 运算符的数量不超过 19 个

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countEval(self, s: str, result: int) -> int:
        n = len(s)

        @cache
        def dfs(l, r, t):   # t: 1: 目标是1， 0: 目标是0， 2: 目标是1或0
            if l == r: return 1 if int(s[l]) == t or t == 2 else 0
            res = 0
            for i in range(l + 1, r, 2):
                if t == 1:
                    if s[i] == '&':
                        v1 = dfs(l, i - 1, 1)
                        v2 = dfs(i + 1, r, 1)
                        res += v1 * v2
                    elif s[i] == '|':
                        v1 = dfs(l, i - 1, 0)
                        v2 = dfs(l, i - 1, 2)
                        v3 = dfs(i + 1, r, 0)
                        v4 = dfs(i + 1, r, 2)
                        res += v2 * v4 - v1 * v3
                    else:
                        v1 = dfs(l, i - 1, 0)
                        v2 = dfs(l, i - 1, 1)
                        v3 = dfs(i + 1, r, 0)
                        v4 = dfs(i + 1, r, 1)
                        res += v1 * v4 + v2 * v3
                elif t == 0:
                    if s[i] == '|':
                        v1 = dfs(l, i - 1, 0)
                        v2 = dfs(i + 1, r, 0)
                        res += v1 * v2
                    elif s[i] == '&':
                        v1 = dfs(l, i - 1, 1)
                        v2 = dfs(l, i - 1, 2)
                        v3 = dfs(i + 1, r, 1)
                        v4 = dfs(i + 1, r, 2)
                        res += v2 * v4 - v1 * v3
                    else:
                        v1 = dfs(l, i - 1, 0)
                        v2 = dfs(l, i - 1, 1)
                        v3 = dfs(i + 1, r, 1)
                        v4 = dfs(i + 1, r, 0)
                        res += v1 * v4 + v2 * v3
                else:
                    v1 = dfs(l, i - 1, 2)
                    v2 = dfs(i + 1, r, 2)
                    res += v1 * v2
            return res

        return dfs(0, n - 1, result)


so = Solution()
print(so.countEval(s = "1^0|0|1", result = 0))
print(so.countEval(s = "1^0", result = 1))




