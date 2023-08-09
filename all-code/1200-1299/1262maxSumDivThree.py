# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
#
#
#
# 示例 1：
#
# 输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
# 示例 2：
#
# 输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
# 示例 3：
#
# 输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
#
#
# 提示：
#
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4

from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        mod = [0, 0, 0]
        for x in nums:
            m = [y for y in mod]
            for i in range(3):
                idx = (mod[i] + x) % 3
                m[idx] = max(m[idx], mod[i] + x)
            mod = [y for y in m]
        return mod[0]





obj = Solution()

