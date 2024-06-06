# 小扣在秋日市集购买了一个古董键盘。由于古董键盘年久失修，键盘上只有 26 个字母 a~z 可以按下，且每个字母最多仅能被按 k 次。
#
# 小扣随机按了 n 次按键，请返回小扣总共有可能按出多少种内容。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。
#
# 示例 1：
#
# 输入：k = 1, n = 1
#
# 输出：26
#
# 解释：由于只能按一次按键，所有可能的字符串为 "a", "b", ... "z"
#
# 示例 2：
#
# 输入：k = 1, n = 2
#
# 输出：650
#
# 解释：由于只能按两次按键，且每个键最多只能按一次，所有可能的字符串（按字典序排序）为 "ab", "ac", ... "zy"
#
# 提示：
#
# 1 <= k <= 5
# 1 <= n <= 26*k

from leetcode.allcode.competition.mypackage import *

class Solution:
    def keyboard(self, k: int, n: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(left, x1, x2, x3, x4, x5):  # 剩余字母个数left，xi表示剩余i个字符的字母个数
            res = 0
            if left == 0: return 1
            if x1:
                res += dfs(left - 1, x1 - 1, x2, x3, x4, x5) * x1
                res %= MOD
            if x2:
                res += dfs(left - 1, x1 + 1, x2 - 1, x3, x4, x5) * x2
                res %= MOD
            if x3:
                res += dfs(left - 1, x1, x2 + 1, x3 - 1, x4, x5) * x3
                res %= MOD
            if x4:
                res += dfs(left - 1, x1, x2, x3 + 1, x4 - 1, x5) * x4
                res %= MOD
            if x5:
                res += dfs(left - 1, x1, x2, x3, x4 + 1, x5 - 1) * x5
                res %= MOD
            # print(left, x1, x2, x3, x4, x5, res)
            return res
        if k == 5:
            return dfs(n, 0,0,0,0,26)
        elif k == 4:
            return dfs(n, 0,0,0,26,0)
        elif k == 3:
            return dfs(n, 0,0,26,0,0)
        elif k == 2:
            return dfs(n, 0,26,0,0,0)
        elif k == 1:
            return dfs(n, 26,0,0,0,0)

so = Solution()
print(so.keyboard(k = 1, n = 1))
print(so.keyboard(k = 2, n = 3))  # 17550
print(so.keyboard(k = 5, n = 130))
print(so.keyboard(k = 1, n = 2))


