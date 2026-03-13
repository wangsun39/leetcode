# 给你一个整数数组 nums。
#
# 返回 nums 中 严格大于 nums 中所有元素 平均值 的 最小未出现正整数。
#
# 数组的 平均值 定义为数组中所有元素的总和除以元素的数量。
#
#
# 示例 1:
#
# 输入: nums = [3,5]
#
# 输出: 6
#
# 解释:
#
# nums 的平均值是 (3 + 5) / 2 = 8 / 2 = 4 。
# 大于 4 的最小未出现正整数是 6。
# 示例 2:
#
# 输入: nums = [-1,1,2]
#
# 输出: 3
#
# 解释:
#
# nums 的平均值是 (-1 + 1 + 2) / 3 = 2 / 3 = 0.667 。
# 大于 0.667 的最小未出现正整数是 3 。
# 示例 3:
#
# 输入: nums = [4,-1]
#
# 输出: 2
#
# 解释:
#
# nums 的平均值是 (4 + (-1)) / 2 = 3 / 2 = 1.50。
# 大于 1.50 的最小未出现正整数是 2。
#
#
# 提示:
#
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        s = set(nums)
        ss = sum(nums)
        v = ss // len(nums)
        x = max(v + 1, 1)
        while x in s:
            x += 1
        return x


so = Solution()


