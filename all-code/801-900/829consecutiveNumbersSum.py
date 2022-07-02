# 给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。 
#
#  
#
# 示例 1:
#
# 输入: n = 5
# 输出: 2
# 解释: 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
# 示例 2:
#
# 输入: n = 9
# 输出: 3
# 解释: 9 = 4 + 5 = 2 + 3 + 4
# 示例 3:
#
# 输入: n = 15
# 输出: 4
# 解释: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
#  
#
# 提示:
#
# 1 <= n <= 109​​​​​​​


from typing import List
import math
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        lower = (int(((2 * n + 1) ** 2 + 8 * n) ** 0.5) - (2 * n + 1)) // 2
        lower = max(1, lower)
        upper = int(((1 + 8 * n) ** 0.5 - 1) // 2 + 1)
        for i in range(lower, upper):
            if (2 * n - i * i + i) % (2 * i) == 0:
                ans += 1
        return ans



so = Solution()
print(so.consecutiveNumbersSum(6))
print(so.consecutiveNumbersSum(1))
print(so.consecutiveNumbersSum(2))
print(so.consecutiveNumbersSum(5))
print(so.consecutiveNumbersSum(9))
print(so.consecutiveNumbersSum(15))

