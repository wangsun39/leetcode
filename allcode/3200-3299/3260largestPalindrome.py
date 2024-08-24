# 给你两个 正整数 n 和 k。
#
# 如果整数 x 满足以下全部条件，则该整数是一个 k 回文数：
#
# x 是一个
# 回文数
# 。
# x 可以被 k 整除。
# 以字符串形式返回 最大的  n 位 k 回文数。
#
# 注意，该整数 不 含前导零。
#
#
#
# 示例 1：
#
# 输入： n = 3, k = 5
#
# 输出： "595"
#
# 解释：
#
# 595 是最大的 3 位 k 回文数。
#
# 示例 2：
#
# 输入： n = 1, k = 4
#
# 输出： "8"
#
# 解释：
#
# 1 位 k 回文数只有 4 和 8。
#
# 示例 3：
#
# 输入： n = 5, k = 6
#
# 输出： "89898"
#
#
#
# 提示：
#
# 1 <= n <= 105
# 1 <= k <= 9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        pow10 = [1] * n
        for i in range(1, n):
            pow10[i] = pow10[i - 1] * 10 % k

        h = (n + 1) // 2  # 长度一半
        # 只考虑前一半
        dp = [[[None] * 2 for _ in range(k)] for _ in range(h)]
        # 从中间开始向右侧的距离为 i，dp[i][j] = [a, b]，
        # 其中a为从位置i向左到达对称点的数中，模k余数为j的最大数在i处填的值，b为取到a时，i+1位需要的模k余数值
        for i in range(10):
            v = (i * pow10[h - 1]) % k
            if n & 1:
                dp[0][v] = [i, None]
            else:
                dp[0][(v * 11) % k] = [i, None]

        for i in range(1, h):
            for j in range(10):  # 第i个位置要填的数字
                if n & 1:
                    # v = j00.mid.00j000.. % k
                    v = (pow10[h + i - 1] + pow10[h - i - 1]) * j % k
                else:
                    # v = j00.mid|mid.00j000.. % k
                    v = (pow10[h + i] + pow10[h - i - 1]) * j % k
                for t in range(k):
                    if dp[i - 1][t][0]:
                        u = (v + t) % k
                        dp[i][u] = [j, t]

        # print(dp)
        ch, nxt = dp[-1][0]
        ans = [str(ch)]
        for i in range(h - 2, -1, -1):
            ch, nxt = dp[i][nxt]
            ans.append(str(ch))
        if n & 1:
            ans = ans + ans[:-1][::-1]
        else:
            ans = ans + ans[::-1]
        # print(ans)
        return ''.join(ans)



so = Solution()
print(so.largestPalindrome(4, 7))
print(so.largestPalindrome(n = 3, k = 5))




