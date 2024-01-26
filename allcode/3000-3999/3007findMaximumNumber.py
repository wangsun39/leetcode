# 给你一个整数 k 和一个整数 x 。
#
# 令 s 为整数 num 的下标从 1 开始的二进制表示。我们说一个整数 num 的 价值 是满足 i % x == 0 且 s[i] 是 设置位 的 i 的数目。
#
# 请你返回 最大 整数 num ，满足从 1 到 num 的所有整数的 价值 和小于等于 k 。
#
# 注意：
#
# 一个整数二进制表示下 设置位 是值为 1 的数位。
# 一个整数的二进制表示下标从右到左编号，比方说如果 s == 11100 ，那么 s[4] == 1 且 s[2] == 0 。
#
#
# 示例 1：
#
# 输入：k = 9, x = 1
# 输出：6
# 解释：数字 1 ，2 ，3 ，4 ，5 和 6 二进制表示分别为 "1" ，"10" ，"11" ，"100" ，"101" 和 "110" 。
# 由于 x 等于 1 ，每个数字的价值分别为所有设置位的数目。
# 这些数字的所有设置位数目总数是 9 ，所以前 6 个数字的价值和为 9 。
# 所以答案为 6 。
# 示例 2：
#
# 输入：k = 7, x = 2
# 输出：9
# 解释：由于 x 等于 2 ，我们检查每个数字的偶数位。
# 2 和 3 在二进制表示下的第二个数位为设置位，所以它们的价值和为 2 。
# 6 和 7 在二进制表示下的第二个数位为设置位，所以它们的价值和为 2 。
# 8 和 9 在二进制表示下的第四个数位为设置位但第二个数位不是设置位，所以它们的价值和为 2 。
# 数字 1 ，4 和 5 在二进制下偶数位都不是设置位，所以它们的价值和为 0 。
# 10 在二进制表示下的第二个数位和第四个数位都是设置位，所以它的价值为 2 。
# 前 9 个数字的价值和为 6 。
# 前 10 个数字的价值和为 8，超过了 k = 7 ，所以答案为 9 。
#
#
# 提示：
#
# 1 <= k <= 1015
# 1 <= x <= 8

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:

        def f(val):  # 返回<=n的所有数的价值和
            s = bin(val)[2:]
            n = len(s)
            res = 0

            left = 0  # x左侧的有效数位(还要考虑在s中此数位是否为1)
            for i, y in enumerate(s):
                if y == '0': continue
                right = (n - i - 1)  # x 右侧的所有数
                r = (n - i - 1) // x  # x 右侧的所有数位中有效数位个数
                # 本次循环共有 2 ** right 个数
                res += 2 ** (right - 1) * r + 2 ** right * left # 每个数都有左侧的left个价值，右侧的每个数位在一半的数中体现价值
                if (n - i) % x == 0 and y == '1':
                    left += 1
            res += left  # 加上val本身的价值
            return res

        lo, hi = 0, 10 ** 16
        # lo, hi = 0, 10
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if f(mid) <= k:
                lo = mid
            else:
                hi = mid
        return lo


so = Solution()
print(so.findMaximumNumber(k = 9, x = 1))
print(so.findMaximumNumber(k = 7, x = 2))




