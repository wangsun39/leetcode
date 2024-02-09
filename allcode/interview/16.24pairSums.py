# 设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
#
# 示例 1:
#
# 输入: nums = [5,6,5], target = 11
# 输出: [[5,6]]
# 示例 2:
#
# 输入: nums = [5,6,5,6], target = 11
# 输出: [[5,6],[5,6]]
# 提示：
#
# nums.length <= 100000
# -10^5 <= nums[i], target <= 10^5

from leetcode.allcode.competition.mypackage import *

class Solution:
        def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
            nums.sort()
            n = len(nums)
            i, j = 0, n - 1
            ans = []
            while i < j:
                while nums[i] + nums[j] > target:
                    j -= 1
                if nums[i] + nums[j] == target:
                    ans.append([nums[i], nums[j]])
                    j -= 1
                i += 1
            return ans



so = Solution()
print(so.pairSums(nums = [5,6,5], target = 11))
print(so.pairSums(nums = [5,6,5,6], target = 11))




