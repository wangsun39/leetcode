# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 假设你总是可以到达数组的最后一个位置。
#
# 
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#     从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。
# 示例 2:
#
# 输入: [2,3,0,1,4]
# 输出: 2
# 
#
# 提示:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 105

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        minStep = [10000] * N
        minStep[0] = 0
        curMax = 0
        for i in range(N):
            j = curMax + 1
            while j < N and j <= i + nums[i]:
                minStep[j] = minStep[i] + 1
                if j == N - 1:
                    return minStep[j]
                j += 1
            curMax = j - 1
        print(minStep)
        return minStep[-1]

    def jump1(self, nums: List[int]) -> int:  # 一个优化算法，在空间复杂度上达到O(1)
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

    def jump3(self, nums: List[int]) -> int:
        # 贪心 2023/2/23 本质上应该和上面的方法是相同的
        n = len(nums)
        ans = right = cur = 0  # right 记录当前能跳到的最远距离
        while right < n - 1:
            next = right
            while cur <= right:
                next = max(next, cur + nums[cur])
                cur += 1
            ans += 1
            right = next
        return ans

so = Solution()
print(so.jump([1,2,3]))
print(so.jump([2,3,1,1,4]))
print(so.jump([2,3,0,1,4]))
