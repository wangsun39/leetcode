# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
#
#
#
# 示例 1：
#
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 示例 2：
#
# 输入：n = 0
# 输出：0
# 示例 3：
#
# 输入：n = 1
# 输出：0
#
#
# 提示：
#
# 0 <= n <= 5 * 106

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        def check(s, t):
            d = {}
            for i, x in enumerate(s):
                if x in d and d[x] != t[i]: return False
                d[x] = t[i]
            return True
        return check(s, t) and check(t, s)

so = Solution()
print(so.isIsomorphic(s = "egg", t = "add"))

