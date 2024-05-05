# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。
#
# 示例:
#
# 输入: 2
# 输出: 91
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。




from leetcode.allcode.competition.mypackage import *

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        counts = [0] * 11
        counts[0], counts[1] = 1, 10
        k = 9
        for i in range(2, n + 1):
            k *= (11 - i)  # 长度为 i 的数字，首位不能是0，因此有 9 * 9 * 8 * ... * (11 - i) 种可能
            counts[i] = k + counts[i - 1]  # 再加上长度小于i的所有数字
        print(counts)
        return counts[n]



so = Solution()
print(so.countNumbersWithUniqueDigits(10))



