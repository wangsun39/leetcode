# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
#
#
# 示例 1:
#
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 示例 2:
#
# 输入: nums = [0]
# 输出: [0]
#
#
# 提示:
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
#
#
# 进阶：你能尽量减少完成的操作次数吗？

from leetcode.allcode.competition.mypackage import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for i, x in enumerate(nums):
            if x != 0:
                nums[cur], nums[i] = nums[i], nums[cur]
                cur += 1
        return


so = Solution()
print(so.moveZeroes(nums = [0,1,0,3,12]))