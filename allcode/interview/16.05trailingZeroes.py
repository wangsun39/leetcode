from leetcode.allcode.competition.mypackage import *


# 设计一个算法，算出 n 阶乘有多少个尾随零。
#
# 示例 1:
#
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
# 示例 2:
#
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 说明: 你算法的时间复杂度应为 O(log n) 。


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n > 0:
            n //= 5
            ans += n
        return ans




so = Solution()
print(so.trailingZeroes(3))
print(so.trailingZeroes(5))





