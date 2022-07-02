# 给你一个整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
#
# 输入：nums = [1], target = 1
# 输出：1
#  
#
# 提示：
#
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000



from typing import List
import bisect
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        upper = sum(nums[:-1])  # 剩余数的上界
        dp1 = {target: 1}
        dp2 = {}
        for i in range(N - 1, 0, -1):
            for key in dp1:
                if abs(key - nums[i]) <= upper:
                    if key - nums[i] in dp2:
                        dp2[key - nums[i]] += dp1[key]
                    else:
                        dp2[key - nums[i]] = dp1[key]
                if abs(key + nums[i]) <= upper:
                    if key + nums[i] in dp2:
                        dp2[key + nums[i]] += dp1[key]
                    else:
                        dp2[key + nums[i]] = dp1[key]
            upper -= nums[i - 1]
            dp1, dp2 = dp2, {}
            print(dp1)

        res = 0
        if nums[0] in dp1:
            res = dp1[nums[0]]
        if -nums[0] in dp1:
            res += dp1[-nums[0]]
        return res

so = Solution()
print(so.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))   # 256
print(so.findTargetSumWays([1,1,1,1,1], 3))   # 5
print(so.findTargetSumWays([1], 1))  # 1

