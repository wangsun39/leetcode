# 给你一个整数 num ，请你返回三个连续的整数，它们的 和 为 num 。如果 num 无法被表示成三个连续整数的和，请你返回一个 空 数组。
#
#
#
# 示例 1：
#
# 输入：num = 33
# 输出：[10,11,12]
# 解释：33 可以表示为 10 + 11 + 12 = 33 。
# 10, 11, 12 是 3 个连续整数，所以返回 [10, 11, 12] 。
# 示例 2：
#
# 输入：num = 4
# 输出：[]
# 解释：没有办法将 4 表示成 3 个连续整数的和。
#
#
# 提示：
#
# 0 <= num <= 1015

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            return [num // 3 - 1, num // 3, num // 3 + 1]
        return []


so = Solution()
print(so.sumOfThree())




