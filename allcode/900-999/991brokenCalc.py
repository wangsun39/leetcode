# 在显示着数字 startValue 的坏计算器上，我们可以执行以下两种操作：
#
# 双倍（Double）：将显示屏上的数字乘 2；
# 递减（Decrement）：将显示屏上的数字减 1 。
# 给定两个整数 startValue 和 target 。返回显示数字 target 所需的最小操作数。
#
#
#
# 示例 1：
#
# 输入：startValue = 2, target = 3
# 输出：2
# 解释：先进行双倍运算，然后再进行递减运算 {2 -> 4 -> 3}.
# 示例 2：
#
# 输入：startValue = 5, target = 8
# 输出：2
# 解释：先递减，再双倍 {5 -> 4 -> 8}.
# 示例 3：
#
# 输入：startValue = 3, target = 10
# 输出：3
# 解释：先双倍，然后递减，再双倍 {3 -> 6 -> 5 -> 10}.
#
#
# 提示：
#
# 1 <= startValue, target <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        dis = {target: 0}
        while target != 1:
            if target & 1:
                dis[target + 1] = dis[target] + 1
                target += 1
            else:
                dis[target >> 1] = dis[target] + 1
                target >>= 1
        ans = inf
        for x in dis.keys():
            if x <= startValue:
                ans = min(ans, dis[x] + startValue - x)
        return ans


so = Solution()
print(so.brokenCalc(startValue = 3, target = 10))
print(so.brokenCalc(startValue = 2, target = 3))
print(so.brokenCalc(startValue = 5, target = 8))



