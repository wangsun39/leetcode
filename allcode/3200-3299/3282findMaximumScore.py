# 给你一个长度为 n 的整数数组 nums 。
#
# 你的目标是从下标 0 出发，到达下标 n - 1 处。每次你只能移动到 更大 的下标处。
#
# 从下标 i 跳到下标 j 的得分为 (j - i) * nums[i] 。
#
# 请你返回你到达最后一个下标处能得到的 最大总得分 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,1,5]
#
# 输出：7
#
# 解释：
#
# 一开始跳到下标 1 处，然后跳到最后一个下标处。总得分为 1 * 1 + 2 * 3 = 7 。
#
# 示例 2：
#
# 输入：nums = [4,3,1,3,2]
#
# 输出：16
#
# 解释：
#
# 直接跳到最后一个下标处。总得分为 4 * 4 = 16 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        # 需要推出的结论，只能往值更大的地方跳，否则就跳到末尾
        n = len(nums)
        if n == 1: return 0
        stack = []  # [nums[i], 从i到n-1的最大得分, i]
        for i in range(n - 2, -1, -1):
            x = nums[i]
            while stack and stack[-1][0] < x:
                stack.pop()
            if stack:
                v = stack[-1][1] + (stack[-1][2] - i) * x
            else:
                v = (n - 1 - i) * x
            stack.append([x, v, i])
        return stack[-1][1]




so = Solution()
print(so.findMaximumScore(nums = [1,3,1,5]))  # 7
print(so.findMaximumScore(nums = [2,4,3]))  # 6
print(so.findMaximumScore(nums = [1,6,6]))  # 7
print(so.findMaximumScore(nums = [3,1,8,10]))  # 14
print(so.findMaximumScore(nums = [4,3,1,3,2]))  # 16




