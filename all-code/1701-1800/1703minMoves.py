# 给你一个整数数组 nums 和一个整数 k 。 nums 仅包含 0 和 1 。每一次移动，你可以选择 相邻 两个数字并将它们交换。
#
# 请你返回使 nums 中包含 k 个 连续 1 的 最少 交换次数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,0,1,0,1], k = 2
# 输出：1
# 解释：在第一次操作时，nums 可以变成 [1,0,0,0,1,1] 得到连续两个 1 。
# 示例 2：
#
# 输入：nums = [1,0,0,0,0,0,1,1], k = 3
# 输出：5
# 解释：通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,1,1,1] 。
# 示例 3：
#
# 输入：nums = [1,1,0,1], k = 2
# 输出：0
# 解释：nums 已经有连续 2 个 1 了。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# nums[i] 要么是 0 ，要么是 1 。
# 1 <= k <= sum(nums)



# Definition for a binary tree node.
from typing import List
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        cur_sum = sum(nums[:k + 1])
        i = 0
        ans = k
        while True:
            ans = min(ans, k - cur_sum)
            if cur_sum == k:
                return 0
            if nums[i] == 1:
                cur_sum -= 1
            i += 1
            if i + k > len(nums):
                return ans
            if nums[i + k - 1] == 1:
                cur_sum += 1

so = Solution()

print(so.minMoves(nums = [1,0,0,1,0,1], k = 2))
print(so.minMoves(nums = [1,0,0,0,0,0,1,1], k = 3))
print(so.minMoves(nums = [1,1,0,1], k = 2))


