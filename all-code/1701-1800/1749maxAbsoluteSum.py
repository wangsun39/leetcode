# 给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。
#
# 请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。
#
# abs(x) 定义如下：
#
# 如果 x 是负整数，那么 abs(x) = -x 。
# 如果 x 是非负整数，那么 abs(x) = x 。
#
#
# 示例 1：
#
# 输入：nums = [1,-3,2,3,-4]
# 输出：5
# 解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。
# 示例 2：
#
# 输入：nums = [2,-5,1,-4,3,-2]
# 输出：8
# 解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
from itertools import accumulate
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        mn = mx = 0
        for i in range(1, n + 1):
            ans = max(ans, abs(s[i] - mn), abs(s[i] - mx))
            mn = min(mn, s[i])
            mx = max(mx, s[i])
        return ans


so = Solution()

print(so.maxAbsoluteSum([-3,-5,-3,-2,-6,3,10,-10,-8,-3,0,10,3,-5,8,7,-9,-9,5,-8]))
print(so.maxAbsoluteSum([1,-3,2,3,-4]))
print(so.maxAbsoluteSum([2,-5,1,-4,3,-2]))




