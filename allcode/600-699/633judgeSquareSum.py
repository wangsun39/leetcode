# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
#
#
#
# 示例 1：
#
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
# 示例 2：
#
# 输入：c = 3
# 输出：false
#
#
# 提示：
#
# 0 <= c <= 231 - 1

from leetcode.allcode.competition.mypackage import *

sq = set()
cur = 1
while cur * cur < 2 ** 31:
    sq.add(cur * cur)
    cur += 1

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for x in sq:
            if c - x in sq:
                return True
        return False

so = Solution()
print(so.judgeSquareSum(5))





