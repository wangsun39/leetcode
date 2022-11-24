# 给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。
#
# 生成的测试用例保证结果符合 32-bit 整数范围。
#
#
#
# 示例 1：
#
# 输入：nums = [2,1,4,3], left = 2, right = 3
# 输出：3
# 解释：满足条件的三个子数组：[2], [2, 1], [3]
# 示例 2：
#
# 输入：nums = [2,9,2,5,6], left = 2, right = 8
# 输出：7
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= left <= right <= 109


from typing import List
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        l, r = [-1] * n, [n] * n
        stack = []
        for i, e in enumerate(nums):
            while len(stack) and nums[stack[-1]] < e:
                stack.pop()
            if len(stack):
                l[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if len(stack):
                r[i] = stack[-1]
            stack.append(i)
        ans = 0
        print(l, r)
        for i, e in enumerate(nums):
            if e < left or e > right:
                continue
            ans += (i - l[i]) * (r[i] - i)
        return ans


so = Solution()
print(so.numSubarrayBoundedMax(nums = [34,46,51,92,50,61,49,82,4,4], left = 18, right = 84))  # 24
print(so.numSubarrayBoundedMax(nums = [2,1,4,3], left = 2, right = 3))  # 3
print(so.numSubarrayBoundedMax(nums = [2,9,2,5,6], left = 2, right = 8))  # 7

