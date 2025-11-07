# 在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。例如，在数组{5, 8, 4, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。
#
# 示例：
#
# 输入：[5, 3, 1, 2, 3]
# 输出：[5, 1, 3, 2, 3]
# 提示：
#
# nums.length <= 10000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 3: return nums
        arr = sorted(nums, reverse=True)
        for i in range((n + 1) // 2):
            nums[i * 2] = arr[i]
            nums[i * 2 + 1] = arr[i + (n + 1) // 2]


so = Solution()
print(so.wiggleSort([5, 3, 1, 2, 3]))




