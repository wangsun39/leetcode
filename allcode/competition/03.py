

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




