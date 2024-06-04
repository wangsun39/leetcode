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
        def dfs(mask, nn):  # 从 idx 个字母开始，剩下 nn 个数时，总数是多少
            if (26 - mask.bit_count()) * k < nn: return 0
            if mask.bit_count() == 26 or nn == 0: return 1
            res = 0
            for i in range(26):
                if (1 << i) & mask == 0:
                    for j in range(1, k + 1):
                        if j > nn: break
                        res += dfs(mask | (1 << i), nn - j)
                        res %= MOD
            return res
        return dfs(0, n)

so = Solution()
print(so.keyboard(k = 5, n = 130))
print(so.keyboard(k = 1, n = 1))
print(so.keyboard(k = 1, n = 2))


