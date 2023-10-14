# 给你一个下标从 0 开始、由 n 个整数组成的数组 nums 和一个整数 target 。
#
# 你的初始位置在下标 0 。在一步操作中，你可以从下标 i 跳跃到任意满足下述条件的下标 j ：
#
# 0 <= i < j < n
# -target <= nums[j] - nums[i] <= target
# 返回到达下标 n - 1 处所需的 最大跳跃次数 。
#
# 如果无法到达下标 n - 1 ，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,6,4,1,2], target = 2
# 输出：3
# 解释：要想以最大跳跃次数从下标 0 到下标 n - 1 ，可以按下述跳跃序列执行操作：
# - 从下标 0 跳跃到下标 1 。
# - 从下标 1 跳跃到下标 3 。
# - 从下标 3 跳跃到下标 5 。
# 可以证明，从 0 到 n - 1 的所有方案中，不存在比 3 步更长的跳跃序列。因此，答案是 3 。
# 示例 2：
#
# 输入：nums = [1,3,6,4,1,2], target = 3
# 输出：5
# 解释：要想以最大跳跃次数从下标 0 到下标 n - 1 ，可以按下述跳跃序列执行操作：
# - 从下标 0 跳跃到下标 1 。
# - 从下标 1 跳跃到下标 2 。
# - 从下标 2 跳跃到下标 3 。
# - 从下标 3 跳跃到下标 4 。
# - 从下标 4 跳跃到下标 5 。
# 可以证明，从 0 到 n - 1 的所有方案中，不存在比 5 步更长的跳跃序列。因此，答案是 5 。
# 示例 3：
#
# 输入：nums = [1,3,6,4,1,2], target = 0
# 输出：-1
# 解释：可以证明不存在从 0 到 n - 1 的跳跃序列。因此，答案是 -1 。
#
#
# 提示：
#
# 2 <= nums.length == n <= 1000
# -109 <= nums[i] <= 109
# 0 <= target <= 2 * 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-inf] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        if dp[-1] == -inf:
            return -1
        # print(dp)
        return dp[-1]


so = Solution()
print(so.maximumJumps(nums = [1,3,6,4,1,2], target = 2))
print(so.maximumJumps(nums = [1,3,6,4,1,2], target = 3))
print(so.maximumJumps(nums = [1,3,6,4,1,2], target = 0))




