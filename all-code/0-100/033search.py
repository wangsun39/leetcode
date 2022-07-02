# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
#  
#
# 示例 1：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
#
# 输入：nums = [1], target = 0
# 输出：-1
#  
#
# 提示：
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
#  
#
# 进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？



from collections import defaultdict
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left, right = 0, len(nums) - 1
        pos = N - 1
        if nums[left] > nums[right]:
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] > nums[left]:
                    left = mid
                else:
                    right = mid
            pos = left
            nums = nums[right:] + nums[:left + 1]
            print(nums)
        if target < nums[0] or target > nums[-1]:
            return -1
        if nums[0] == target:
            return (pos + 1) % N
        if nums[-1] == target:
            return pos
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(mid, nums[mid])
            if nums[mid] == target:
                return (mid + pos + 1) % N
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


so = Solution()
#print(so.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(so.search([4,5,6,7,0,1,2], 2))
print(so.search([1,3,5], 5))
print(so.search([3, 1], 3))


