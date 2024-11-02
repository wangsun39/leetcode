# 给你一个整数数组 nums 。
#
# 请你将 nums 中每一个元素都替换为它的各个数位之 和 。
#
# 请你返回替换所有元素以后 nums 中的 最小 元素。
#
#
#
# 示例 1：
#
# 输入：nums = [10,12,13,14]
#
# 输出：1
#
# 解释：
#
# nums 替换后变为 [1, 3, 4, 5] ，最小元素为 1 。
#
# 示例 2：
#
# 输入：nums = [1,2,3,4]
#
# 输出：1
#
# 解释：
#
# nums 替换后变为 [1, 2, 3, 4] ，最小元素为 1 。
#
# 示例 3：
#
# 输入：nums = [999,19,199]
#
# 输出：10
#
# 解释：
#
# nums 替换后变为 [27, 10, 19] ，最小元素为 10 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 104

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minElement(self, nums: List[int]) -> int:
        nums2 = []
        for x in nums:
            l = list(str(x))
            y = sum(int(z) for z in l)
            nums2.append(y)
        return min(nums2)


so = Solution()
print(so.minElement())



