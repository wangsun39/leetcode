# 一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。
#
# 比方说，数组 [3,2,5] （最小值是 2）的最小乘积为 2 * (3+2+5) = 2 * 10 = 20 。
# 给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。由于答案可能很大，请你返回答案对  109 + 7 取余 的结果。
#
# 请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。
#
# 子数组 定义为一个数组的 连续 部分。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,2]
# 输出：14
# 解释：最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
# 2 * (2+3+2) = 2 * 7 = 14 。
# 示例 2：
#
# 输入：nums = [2,3,3,1,2]
# 输出：18
# 解释：最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
# 3 * (3+3) = 3 * 6 = 18 。
# 示例 3：
#
# 输入：nums = [3,1,5,6,4,2]
# 输出：60
# 解释：最小乘积的最大值由子数组 [5,6,4] （最小值是 4）得到。
# 4 * (5+6+4) = 4 * 15 = 60 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 107

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        s = list(accumulate(nums, initial=0))  # 前缀和
        n = len(nums)
        left = [-1] * n  # 左边第一个小于自己的下标
        right = [-1] * n  # 右边第一个小于自己的下标
        stack = []  # 单调栈
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] > x:
                j = stack.pop()
                right[j] = i
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                left[j] = i
            stack.append(i)
        ans = 0
        for i, x in enumerate(nums):
            l, r = left[i] + 1 if left[i] != -1 else 0, right[i] - 1 if right[i] != -1 else n - 1
            cur = x * (s[r + 1] - s[l])
            ans = max(ans, cur)
        return ans % MOD

so = Solution()
print(so.maxSumMinProduct([1,2,3,2]))
print(so.maxSumMinProduct([2,3,3,1,2]))
print(so.maxSumMinProduct([3,1,5,6,4,2]))




