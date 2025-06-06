# 某个程序本来应该输出一个整数数组。但是这个程序忘记输出空格了以致输出了一个数字字符串，我们所知道的信息只有：数组中所有整数都在 [1, k] 之间，且数组中的数字都没有前导 0 。
#
# 给你字符串 s 和整数 k 。可能会有多种不同的数组恢复结果。
#
# 按照上述程序，请你返回所有可能输出字符串 s 的数组方案数。
#
# 由于数组方案数可能会很大，请你返回它对 10^9 + 7 取余 后的结果。
#
#
#
# 示例 1：
#
# 输入：s = "1000", k = 10000
# 输出：1
# 解释：唯一一种可能的数组方案是 [1000]
# 示例 2：
#
# 输入：s = "1000", k = 10
# 输出：0
# 解释：不存在任何数组方案满足所有整数都 >= 1 且 <= 10 同时输出结果为 s 。
# 示例 3：
#
# 输入：s = "1317", k = 2000
# 输出：8
# 解释：可行的数组方案为 [1317]，[131,7]，[13,17]，[1,317]，[13,1,7]，[1,31,7]，[1,3,17]，[1,3,1,7]
# 示例 4：
#
# 输入：s = "2020", k = 30
# 输出：1
# 解释：唯一可能的数组方案是 [20,20] 。 [2020] 不是可行的数组方案，原因是 2020 > 30 。 [2,020] 也不是可行的数组方案，因为 020 含有前导 0 。
# 示例 5：
#
# 输入：s = "1234567890", k = 90
# 输出：34
#
#
# 提示：
#
# 1 <= s.length <= 10^5.
# s 只包含数字且不包含前导 0 。
# 1 <= k <= 10^9.

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        m = len(str(k))
        dp = [[0] * m for _ in range(n)]  # dp[i][j] 表示以第i个字母结尾，最后一段长度为j+1的可能性有多少种
        pre = [0] * n   # sum(dp[i])
        if int(s[0]) > k: return 0
        dp[0][0] = pre[0] = 1
        for i, ch in enumerate(s[1:], 1):
            if int(ch) > k: return 0
            s1 = 0  # 以 s[i] 结尾的和
            for j in range(m):
                if j > i: break
                s1 += (10 ** j) * int(s[i - j])
                if i == j:
                    if s1 <= k:
                        dp[i][j] = 1
                elif s[i - j] != '0' and s1 <= k:
                    dp[i][j] = pre[i - j - 1]

            pre[i] = sum(dp[i]) % MOD

        return pre[-1]


so = Solution()
print(so.numberOfArrays(s = "5", k = 4))
print(so.numberOfArrays(s = "1000", k = 10000))




