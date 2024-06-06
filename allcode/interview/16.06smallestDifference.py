# 给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差
#
#
#
# 示例：
#
# 输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
# 输出：3，即数值对(11, 8)
#
#
# 提示：
#
# 1 <= a.length, b.length <= 100000
# -2147483648 <= a[i], b[i] <= 2147483647
# 正确结果在区间 [0, 2147483647] 内

from leetcode.allcode.competition.mypackage import *

class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        b.sort()
        n = len(b)
        ans = inf
        for x in a:
            p = bisect_left(b, x)
            if p == n:
                ans = min(ans, x - b[-1])
            else:
                ans = min(ans, b[p] - x)
                if p > 0:
                    ans = min(ans, x - b[p - 1])
        return ans




so = Solution()
print(so.smallestDifference(3))
print(so.trailingZeroes(5))





