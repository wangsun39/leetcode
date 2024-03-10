

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp1 = [[-inf] * k for _ in range(n)]
        dp2 = [[0] * k for _ in range(n)]
        dp1[0][0] = dp2[0][0] = nums[0]
        for i in range(1, n):
            for j in range(min(i + 1, k)):
                dp1[i][j] = dp1[i - 1][j]
                dp2[i][j] = dp2[i - 1][j]
                if j == 0 and dp1[i][j] < 0 and dp1[i][j] < nums[i]:
                    dp2[i][j] = dp1[i][j] = nums[i]
                    continue
                if j == 0 and dp1[i][j] < nums[i]:
                    dp2[i][j] = dp1[i][j] = nums[i]

                if j & 1 == 0:
                    if dp1[i][j] < dp1[i - 1][j] + nums[i]:
                        dp1[i][j] = dp1[i - 1][j] + nums[i]
                        dp2[i][j] = dp2[i - 1][j] + nums[i]
                    if j > 0 and dp1[i][j] < dp1[i - 1][j - 1] + dp2[i - 1][j - 1] + nums[i]:
                        dp1[i][j] = dp1[i - 1][j - 1] + dp2[i - 1][j - 1] + nums[i]
                        dp2[i][j] = dp2[i - 1][j - 1] + nums[i]
                else:
                    if dp1[i][j] < dp1[i - 1][j] - nums[i]:
                        dp1[i][j] = dp1[i - 1][j] - nums[i]
                        dp2[i][j] = dp2[i - 1][j] - nums[i]
                    if j > 0 and dp1[i][j] < dp1[i - 1][j - 1] + dp2[i - 1][j - 1] - nums[i]:
                        dp1[i][j] = dp1[i - 1][j - 1] + dp2[i - 1][j - 1] - nums[i]
                        dp2[i][j] = dp2[i - 1][j - 1] - nums[i]
        # print(dp1)
        # print(dp2)
        return dp1[-1][-1]




so = Solution()
print(so.maximumStrength([-50,-24], 1))
print(so.maximumStrength([-50,-24], 1))
print(so.maximumStrength([-1,-2,-3],
1))
print(so.maximumStrength([-99,85], 1))
print(so.maximumStrength(nums = [-1,-2,-3], k = 1))
print(so.maximumStrength(nums = [1,2,3,-1,2], k = 3))
print(so.maximumStrength(nums = [12,-2,-2,-2,-2], k = 5))




