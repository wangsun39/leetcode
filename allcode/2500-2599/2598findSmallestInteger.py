# 给你一个下标从 0 开始的整数数组 nums 和一个整数 value 。
#
# 在一步操作中，你可以对 nums 中的任一元素加上或减去 value 。
#
# 例如，如果 nums = [1,2,3] 且 value = 2 ，你可以选择 nums[0] 减去 value ，得到 nums = [-1,2,3] 。
# 数组的 MEX (minimum excluded) 是指其中数组中缺失的最小非负整数。
#
# 例如，[-1,2,3] 的 MEX 是 0 ，而 [1,0,3] 的 MEX 是 2 。
# 返回在执行上述操作 任意次 后，nums 的最大 MEX 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,-10,7,13,6,8], value = 5
# 输出：4
# 解释：执行下述操作可以得到这一结果：
# - nums[1] 加上 value 两次，nums = [1,0,7,13,6,8]
# - nums[2] 减去 value 一次，nums = [1,0,2,13,6,8]
# - nums[3] 减去 value 两次，nums = [1,0,2,3,6,8]
# nums 的 MEX 是 4 。可以证明 4 是可以取到的最大 MEX 。
# 示例 2：
#
# 输入：nums = [1,-10,7,13,6,8], value = 7
# 输出：2
# 解释：执行下述操作可以得到这一结果：
# - nums[2] 减去 value 一次，nums = [1,-10,0,13,6,8]
# nums 的 MEX 是 2 。可以证明 2 是可以取到的最大 MEX 。
#
#
# 提示：
#
# 1 <= nums.length, value <= 105
# -109 <= nums[i] <= 109

from leetcode.allcode.competition.mypackage import *


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        s = Counter()
        for i, x in enumerate(nums):
            s[nums[i] % value] += 1

        for i in range(n):
            j = i % value
            if s[j] > 0:
                s[j] -= 1
            else:
                return i
        return n



so = Solution()
print(so.findSmallestInteger([1,2,3,4,0], 4))
print(so.findSmallestInteger([3,0,3,2,4,2,1,1,0,4], 5))
print(so.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7))
print(so.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5))




