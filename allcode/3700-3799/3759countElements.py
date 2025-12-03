# 给你一个长度为 n 的整数数组 nums 和一个整数 k。
#
# 如果数组 nums 中的某个元素满足以下条件，则称其为 合格元素：存在 至少 k 个元素 严格大于 它。
#
# 返回一个整数，表示数组 nums 中合格元素的总数。
#
#
#
# 示例 1：
#
# 输入： nums = [3,1,2], k = 1
#
# 输出： 2
#
# 解释：
#
# 元素 1 和 2 均有至少 k = 1 个元素大于它们。
# 没有元素比 3 更大。因此答案是 2。
#
# 示例 2：
#
# 输入： nums = [5,5,5], k = 2
#
# 输出： 0
#
# 解释：
#
# 由于所有元素都等于 5，没有任何元素比其他元素大。因此答案是 0。
#
#
#
# 提示：
#
# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= k < n

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        x = nums[n - k]
        p = bisect_left(nums, x)
        return p


so = Solution()
print(so.countElements(nums = [3,1,2], k = 1))
print(so.countElements(nums = [3,3,3], k = 1))




