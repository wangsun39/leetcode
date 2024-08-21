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
        h = (n + 1) // 2  # 长度一半
        dp = [[-1] * k for _ in range(h)]  # 从中间开始向左侧的距离为i，模k值为j的字符为dp[i][j]
        for i in range(10):
            v = i * 10 ** (h - 1) % k
            if n & 1:
                dp[0][v] = i
            else:
                dp[0][v] = dp[0][v] * 10 % k

        for i in range(1, h):
            if i == h - 1:
                mn = 1
            else:
                mn = 0
            for j in range(mn, 10):
                if n & 1:
                    # 10|0100000...
                    left = j * 10 ** (h + i - 1) % k
                    right = j * 10 ** (h - i - 1) % k
                else:
                    # 10[0]010000...
                    left = j * 10 ** (h + i - 1) % k
                    right = j * 10 ** (h - i - 2) % k
                v = (left + right) % k
                for t in range(k):
                    if dp[i - 1][t] != -1:
                        dp[i][(t + v) % k] = v
        dp = dp[::-1]
        res = [str(dp[0][0])]
        v = dp[0][0]
        for i in range(1, h):
            v = k - v
            res.append(str(dp[i][v]))

        if n & 1:
            res += res[:-1][::-1]
        else:
            res += res[::-1]
        return ''.join(res)





so = Solution()
print(so.largestPalindrome(n = 3, k = 5))
print(so.largestPalindrome(4, 7))




