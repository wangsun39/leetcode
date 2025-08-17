# 给你一个整数数组 nums 和一个整数 threshold 。
#
# 找到长度为 k 的 nums 子数组，满足数组中 每个 元素都 大于 threshold / k 。
#
# 请你返回满足要求的 任意 子数组的 大小 。如果没有这样的子数组，返回 -1 。
#
# 子数组 是数组中一段连续非空的元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,4,3,1], threshold = 6
# 输出：3
# 解释：子数组 [3,4,3] 大小为 3 ，每个元素都大于 6 / 3 = 2 。
# 注意这是唯一合法的子数组。
# 示例 2：
#
# 输入：nums = [6,5,6,5,8], threshold = 7
# 输出：1
# 解释：子数组 [8] 大小为 1 ，且 8 > 7 / 1 = 7 。所以返回 1 。
# 注意子数组 [6,5] 大小为 2 ，每个元素都大于 7 / 2 = 3.5 。
# 类似的，子数组 [6,5,6] ，[6,5,6,5] ，[6,5,6,5,8] 都是符合条件的子数组。
# 所以返回 2, 3, 4 和 5 都可以。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i], threshold <= 109


from leetcode.allcode.competition.mypackage import *

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        min_k = [threshold // x + 1 for x in nums]
        stack = []
        left = [-1] * n
        right = [n] * n
        for i, x in enumerate(min_k):
            while stack and min_k[stack[-1]] <= x:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            x = min_k[i]
            while stack and min_k[stack[-1]] <= x:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        for i in range(n):
            if right[i] - left[i] - 1 >= min_k[i]:
                return min_k[i]
        return -1

so = Solution()
print(so.validSubarraySize(nums = [1,3,4,3,1], threshold = 6))

