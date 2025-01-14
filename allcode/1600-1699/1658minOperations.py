# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
#
# 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
# 示例 2：
#
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
# 示例 3：
#
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109
import math
from leetcode.allcode.competition.mypackage import *
import itertools
from bisect import *


# Definition for a binary tree node.
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        # 左右前缀和
        left = [0] + list(itertools.accumulate(nums))
        right = [0] + list(itertools.accumulate(nums[::-1]))
        print(left, right)
        if left[-1] < x: return -1
        l = 0
        r = bisect_left(right, x - l)
        ans = math.inf if r < n + 1 and left[l] + right[r] != x else l + r
        while l < n + 1:
            while r >= 0 and left[l] + right[r] > x:
                r -= 1
            if r >= 0 and left[l] + right[r] == x:
                ans = min(ans, l + r)
            l += 1
        return ans if ans != math.inf else -1


so = Solution()
#
print(so.minOperations(nums = [1,1], x = 3))  # -1
print(so.minOperations(nums = [1,1,4,2,3], x = 5))  # 2
print(so.minOperations(nums = [5,6,7,8,9], x = 4))  # -1
print(so.minOperations(nums = [3,2,20,1,1,3], x = 10))  # 5




