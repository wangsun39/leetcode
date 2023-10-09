# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
#
# 返回这三个数的和。
#
# 假定每组输入只存在恰好一个解。
#
#
#
# 示例 1：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 示例 2：
#
# 输入：nums = [0,0,0], target = 1
# 输出：0
#
#
# 提示：
#
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

from collections import Counter
from math import inf
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = inf
        for i, x in enumerate(nums):
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] == target - x: return target
                if nums[j] + nums[k] > target - x:
                    if abs(ans - target) > nums[j] + nums[k] + x - target:
                        ans = nums[j] + nums[k] + x
                    k -= 1
                else:
                    if abs(ans - target) > target - (nums[j] + nums[k] + x):
                        ans = nums[j] + nums[k] + x
                    j += 1

        return ans


so = Solution()
print(so.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(so.threeSumClosest(nums = [0,0,0], target = 1))
