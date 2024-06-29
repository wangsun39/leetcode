# 一个魔法师有许多不同的咒语。
#
# 给你一个数组 power ，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。
#
# 已知魔法师使用伤害值为 power[i] 的咒语时，他们就 不能 使用伤害为 power[i] - 2 ，power[i] - 1 ，power[i] + 1 或者 power[i] + 2 的咒语。
#
# 每个咒语最多只能被使用 一次 。
#
# 请你返回这个魔法师可以达到的伤害值之和的 最大值 。
#
#
#
# 示例 1：
#
# 输入：power = [1,1,3,4]
#
# 输出：6
#
# 解释：
#
# 可以使用咒语 0，1，3，伤害值分别为 1，1，4，总伤害值为 6 。
#
# 示例 2：
#
# 输入：power = [7,1,6,6]
#
# 输出：13
#
# 解释：
#
# 可以使用咒语 1，2，3，伤害值分别为 1，6，6，总伤害值为 13 。
#
#
#
# 提示：
#
# 1 <= power.length <= 105
# 1 <= power[i] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        counter = Counter(power)
        power = sorted(counter.items())
        n = len(power)
        dp = [0] * n  # 使用 power[i] 能达到的最大值
        mx = [power[0][0] * power[0][1]]  # 前i个power的最大值
        for i, [k, v] in enumerate(power):
            if i > 1:
                mx.append(max(mx[i - 2], dp[i - 1]))
            if i > 0 and power[i - 1][0] < k - 2:
                dp[i] = mx[i - 1]
            elif i > 1 and power[i - 2][0] < k - 2:
                dp[i] = max(dp[i], mx[i - 2])
            elif i > 2:
                dp[i] = max(dp[i], mx[i - 3])
            dp[i] += k * v
        return max(dp)




so = Solution()
print(so.maximumTotalDamage([6,9,2,3,5,4,1,4,5]))  # 21
print(so.maximumTotalDamage([2,1,4,3,1,1,1,5]))  # 9
print(so.maximumTotalDamage([1,1,3,4]))
print(so.maximumTotalDamage([5,9,2,10,2,7,10,9,3,8]))
print(so.maximumTotalDamage(power = [7,1,6,6]))




