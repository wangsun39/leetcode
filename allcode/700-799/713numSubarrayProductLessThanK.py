# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
#
#
# 示例 1：
#
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
# 示例 2：
#
# 输入：nums = [1,2,3], k = 0
# 输出：0
#
#
# 提示:
#
# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106




from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j, product = 0, 0, 1
        ans = 0
        for j, num in enumerate(nums):
            while i <= j:
                if product * num < k:
                    ans += (j - i + 1)
                    product *= num
                    break
                else:
                    if nums[i] < k:
                        product //= nums[i]
                    i += 1
        return ans



so = Solution()
print(so.numSubarrayProductLessThanK([57,44,92,28,66,60,37,33,52,38,29,76,8,75,22], k = 18))
print(so.numSubarrayProductLessThanK([10,5,2,6], k = 100))
print(so.numSubarrayProductLessThanK([1,2,3], k = 0))


